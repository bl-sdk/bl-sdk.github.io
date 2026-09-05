#!/usr/bin/env python
# /// script
# requires-python = ">=3.13"
# dependencies = [
#   "pyyaml",
#   "requests",
#   "validate-pyproject[all]",
# ]
# ///

import logging
import re
import subprocess
import sys
import tomllib
import zipfile
from functools import cache
from io import BytesIO
from pathlib import Path
from typing import TYPE_CHECKING, Any, NewType, NoReturn, TypedDict
from urllib.parse import unquote, urlparse

import requests
import yaml
from validate_pyproject.api import Validator
from validate_pyproject.errors import ValidationError
from validate_pyproject.plugins import PluginWrapper

if TYPE_CHECKING:
    from validate_pyproject.types import Schema

    Url = NewType("Url", str)

log = logging.getLogger(__name__)

SCHEMA: Schema = {  # type: ignore
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "https://github.com/bl-sdk/bl-sdk.github.io/blob/master/_validate_pyproject.py",
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "version": {"type": "string"},
        "mod_type": {
            "enum": ["Standard", "Library"],
        },
        "supported_games": {
            "type": "array",
            "items": {
                "enum": ["BL1", "BL1E", "BL2", "TPS", "AoDK", "BL3", "WL", "BL4"],
            },
        },
        "coop_support": {
            "enum": ["Unknown", "Incompatible", "RequiresAllPlayers", "ClientSide", "HostOnly"],
        },
        "license": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "url": {"type": "string", "format": "url"},
            },
            "required": ["name", "url"],
            "additionalProperties": False,
        },
        "download": {"type": "string", "format": "url"},
        "auto_enable": {"type": "boolean"},
        "uses_native_modules": {"type": "boolean"},
    },
    "required": ["download"],
    "additionalProperties": False,
}


if TYPE_CHECKING:

    class FrontMatterSettings(TypedDict, total=False):
        pyproject_url: Url
        download: Url
        legacy: bool
        uses_native_modules: bool


def parse_front_matter(path: Path) -> FrontMatterSettings:
    """
    Parses jekyll front matter, extracting the pyproject url and possibly an explicit download url.

    Args:
        path: Path to the file to parse:
    Returns:
        The parsed front matter settings.
    """
    settings: FrontMatterSettings = {}
    try:
        with path.open() as file:
            data = next(yaml.safe_load_all(file))
            assert isinstance(data, dict)
            front_matter: dict[str, Any] = data  # type: ignore
    except Exception:  # noqa: BLE001
        log.warning("Couldn't find pyproject url for file: %s", path)
        return settings

    for key, value_type in {
        "pyproject_url": str,
        "download": str,
        "legacy": bool,
        "uses_native_modules": bool,
    }.items():
        if key not in front_matter:
            continue
        if not isinstance(value := front_matter[key], value_type):
            continue
        settings[key] = value  # type: ignore

    return settings


BAD_GITHUB_URL = re.compile(r"github.com/.+?/.+?/raw/")


def pyproject_from_url(url: Url) -> dict[str, Any] | None:
    """
    Downloads and parses a pyproject.toml hosted at a url.

    Args:
        url: The url to download from.
    Returns:
        The parsed contents, or None on error.
    """
    try:
        resp = requests.get(url, allow_redirects=False, timeout=1)
    except requests.Timeout:
        log.error("Timeout trying to download pyproject_url: %s", url)
        return None

    if resp.headers.get("Access-Control-Allow-Origin") != "*":
        log.error("CORS failure on pyproject_url: %s", url)
        if BAD_GITHUB_URL.search(url):
            log.error(
                "  github.com/.../raw/ links do not work in the pyproject_url in mod markdown"
                " files, use the raw.githubusercontent.com version",
            )
        return None

    if 300 <= resp.status_code < 400:  # noqa: PLR2004
        # If it's a redirect which passed CORS, just try follow it fully?
        try:
            resp = requests.get(url, allow_redirects=True, timeout=1)
        except requests.Timeout:
            log.error("Timeout trying to download pyproject_url: %s", url)
            return None

    if resp.status_code != requests.codes.ok:
        log.error("Got a %d % from pyproject_url: %s", resp.status_code, resp.reason, url)
        return None

    try:
        return tomllib.loads(resp.text)
    except tomllib.TOMLDecodeError:
        log.error("Invalid toml at pyproject_url:%s", url)
        return None


def pyproject_from_file(path: Path) -> dict[str, Any] | None:
    """
    Parses a pyproject.toml from a local file.

    Args:
        path: The path to parse.
    Returns:
        The parsed contents, or None on error.
    """
    try:
        with path.open("rb") as file:
            return tomllib.load(file)
    except FileNotFoundError:
        log.error("Couldn't find file %s", path)
        return None
    except tomllib.TOMLDecodeError:
        log.error("Invalid toml at path %s", path)
        return None


@cache
def _make_validator() -> Validator:
    return Validator(extra_plugins=[PluginWrapper("sdkmod", lambda _: SCHEMA)])


MOD_MANAGER_PYPROJECT = re.compile(
    r"^https://raw\.githubusercontent\.com/bl-sdk/\w+-mod-manager/master/manager_pyproject\.toml$",
)
MOD_MANAGER_DOWNLOAD = re.compile(r"^https://github\.com/bl-sdk/\w+-mod-manager/releases/latest$")


def validate_pyproject(
    pyproject: dict[str, Any],
    front_matter: FrontMatterSettings,
    *,
    location: Path | Url,
) -> bool:
    """
    Validate a parsed pyproject is correctly formatted.

    Args:
        pyproject: The parsed pyproject to validate.
        front_matter: Any custom front matter settings.
        location: Where the pyproject was obtained from.
    Returns:
        True if the pyproject is correctly formatted, false on any errors.
    """
    log.info("Checking %s", location)

    validator = _make_validator()
    try:
        validator(pyproject)
    except ValidationError as ex:
        log.error("  %s", ex.message)  # type: ignore
        if "pep508-identifier" in ex.message:
            log.error(
                "  see: https://packaging.python.org/en/latest/specifications/name-normalization/#name-format",
            )
        log.error("  This may not be the only issue!")
        return False

    # We know tools either does not exist, or is a dict, because it already passed above validation
    # Make sure our tool.sdkmod table is present, since it doesn't check that
    if "sdkmod" not in pyproject.get("tool", {}):
        # Emulate a regular error
        log.error("  `tool` must contain `sdkmod` properties")
        return False

    download_url: Url = (
        front_matter["download"]
        if "download" in front_matter
        else pyproject["tool"]["sdkmod"]["download"]
    )

    # Try check if this is pointing to one of the mod manager pages
    # We want to validate it's pyproject, but the download will always be different, so skip it
    if isinstance(location, str):
        if MOD_MANAGER_PYPROJECT.match(location):
            return True
    elif location.name.endswith("_mod_manager.md") and MOD_MANAGER_DOWNLOAD.match(download_url):
        return True

    uses_native_modules: bool = (
        front_matter["uses_native_modules"]
        if "uses_native_modules" in front_matter
        else pyproject["tool"]["sdkmod"].get("uses_native_modules", False)
    )

    return validate_download_url(download_url, uses_native_modules)


def validate_download_url(url: Url, expects_native_modules: bool) -> bool:  # noqa: C901
    """
    Validate a mod's download is correctly formatted.

    Args:
        url: The url to download.
        expects_native_modules: True if we expect this mod to contain native modules.
    Returns:
        True if the pyproject is correctly formatted, false on any errors.
    """
    filename = Path(unquote(urlparse(url).path))

    is_sdkmod = filename.suffix == ".sdkmod"
    if not is_sdkmod and filename.suffix != ".zip":
        log.error("  `tool.sdkmod.download` must be a `.zip` or `.sdkmod` file")
        return False

    try:
        resp = requests.get(url, timeout=2)
    except requests.Timeout:
        log.error("Timeout trying to download mod at url %s", url)
        return False

    try:
        zip_path = zipfile.Path(BytesIO(resp.content))
        zip_iter = zip_path.iterdir()
    except zipfile.BadZipFile:
        log.error("  `tool.sdkmod.download` does not point at a valid zip file")
        log.error("  Is it a direct download link?")
        return False

    if (zip_entry := next(zip_iter, None)) is None:
        log.error("  `tool.sdkmod.download` points to an empty zip file")
        return False

    contains_native_modules = any(zip_path.glob("**/*.pyd")) or any(zip_path.glob("**/*.dll"))
    if contains_native_modules != expects_native_modules:
        log.error(
            "  The zip %s native modules, but the mod %s tagged with use_native_modules",
            "contains" if contains_native_modules else "does not contain",
            "isn't" if contains_native_modules else "is",
        )
        return False

    if zip_entry.name == filename.stem and next(zip_iter, None) is None:
        # There's only one top level entry, which has the same name as the file
        # i.e. passes the .sdkmod or .zip formats
        return True
    # Either a hybrid mod, or invalid

    if is_sdkmod:
        # .sdkmods cannot be hybrid mods
        log.error(
            "  .sdkmod files may only contain a single root folder, which must be named the same as"
            " the zip (excluding suffix).",
        )
        return False

    sdk_mods = zip_path / "sdk_mods"
    if not sdk_mods.exists():
        log.error("  .zip file is not one of the allowed layouts. Options are:")
        log.error("  - single root folder, named the same as the zip (i.e. same layout as .sdkmod)")
        log.error(
            "  - root folder contains an sdk_mods folder, holding either a single folder or a"
            " .sdkmod",
        )
        return False

    zip_iter = sdk_mods.iterdir()
    if (zip_entry := next(zip_iter, None)) is None:
        log.error("  .zip file has empty sdk_mods folder")
        return False

    if zip_entry.is_file() and not zip_entry.name.endswith(".sdkmod"):
        log.error("  .zip file %s is not a .sdkmod", zip_entry.name)
        return False

    if next(zip_iter, None) is not None:
        log.error("  .zip file sdk_mods folder contains multiple entries")
        return False

    return True


def get_git_changed_files(ref: str | None = None) -> list[Path]:
    """
    Gets all files in the current git repository which have changed since origin/master.

    Returns:
        A list of changed files.
    """
    root = Path(
        subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            check=True,
            encoding="utf8",
            capture_output=True,
        ).stdout.strip(),
    )

    command = ["git", "diff", "--name-only"]
    if ref is None:
        command += ["--merge-base", "origin/master"]
    else:
        command.append(ref)

    changes = subprocess.run(
        command,
        check=True,
        encoding="utf8",
        capture_output=True,
    ).stdout
    return [(root / x.strip()).resolve() for x in changes.splitlines()]


if __name__ == "__main__":
    import argparse

    all_mod_pages = list(Path(__file__).resolve().parent.glob("_*_mods/*"))

    parser = argparse.ArgumentParser(
        description="Validates sdk mod 'pyproject.toml's are correctly formatted.",
    )
    subparsers = parser.add_subparsers()
    parser.set_defaults(action="all")

    # Assume this is being used outside of the bl-sdk.github.io repo if we couldn't find any mods
    if all_mod_pages:
        all_parser = subparsers.add_parser(
            "all",
            help="Validates all sdk mod pages in the repository. Default if no args are given.",
        )
        all_parser.set_defaults(action="all")

        git_changed_parser = subparsers.add_parser(
            "git_changed",
            help="Validates all sdk mod pages which have been modified in git.",
        )
        git_changed_parser.set_defaults(action="git_changed")
        git_changed_parser.add_argument(
            "ref",
            nargs="?",
            help="The ref to compare against, defaulting to the merge base with origin/master.",
        )

    front_matter_parser = subparsers.add_parser(
        "front_matter",
        help="Validates pyproject files linked in a page's front matter.",
    )
    front_matter_parser.add_argument("files", type=Path, nargs="+", help="The files to validate.")
    front_matter_parser.set_defaults(action="front_matter")

    url_parser = subparsers.add_parser(
        "url",
        help="Validates pyproject files hosted at the given urls.",
    )
    url_parser.set_defaults(action="url")
    url_parser.add_argument("urls", nargs="+", help="The urls to validate.")

    file_parser = subparsers.add_parser(
        "file",
        help="Validates local pyproject files.",
    )
    file_parser.set_defaults(action="file")
    file_parser.add_argument("files", type=Path, nargs="+", help="The files to validate.")

    args = parser.parse_args()

    class ColourFormatter(logging.Formatter):
        def format(self, record: logging.LogRecord) -> str:
            message = super().format(record)
            if record.levelno == logging.WARNING:
                return f"\x1b[33m{message}\x1b[0m"
            if record.levelno == logging.ERROR:
                return f"\x1b[31m{message}\x1b[0m"
            if record.levelno == logging.CRITICAL:
                return f"\x1b[31;1m{message}\x1b[0m"
            return message

    logging.basicConfig(level=logging.INFO)
    logging.getLogger().handlers[0].setFormatter(ColourFormatter("%(levelname)-8s| %(message)s"))
    logging.getLogger("validate_pyproject.api").setLevel(logging.WARNING)

    def print_summary_and_exit(total_files: int, num_ok: int) -> NoReturn:
        logger = log.info if total_files == num_ok else log.warning
        logger(
            "%d/%d file%s passed validation",
            num_ok,
            total_files,
            "s" if total_files > 1 else "",
        )
        sys.exit(0 if num_ok == total_files else 1)

    front_matter_files: list[Path] = []
    urls: list[tuple[Url, FrontMatterSettings]] = []
    match args.action:
        case "all" if all_mod_pages:
            front_matter_files = all_mod_pages
        case "git_changed" if all_mod_pages:
            changed_files = get_git_changed_files(args.ref)
            front_matter_files = [x for x in all_mod_pages if x in changed_files]
            if not front_matter_files:
                log.warning("Couldn't find any modified mod files!")
                sys.exit(0)

        case "front_matter":
            front_matter_files = args.files
        case "url":
            urls = [(u, {}) for u in args.urls]

        case "file":
            total_files = len(args.files)  # type: ignore
            num_ok = 0
            for path in args.files:
                pyproject = pyproject_from_file(path)
                front_matter = parse_front_matter(path)
                if pyproject is not None and validate_pyproject(
                    pyproject,
                    front_matter,
                    location=path,
                ):
                    num_ok += 1
            print_summary_and_exit(total_files, num_ok)
        case _:
            log.error("command got invalid action '%s'", args.action)
            sys.exit(1)

    total_files = len(front_matter_files) + len(urls)
    num_ok = 0

    for path in front_matter_files:
        front_matter = parse_front_matter(path)
        if front_matter.get("legacy", False):
            # This was a legacy mod, don't include it in the count
            log.info("Skipping legacy mod %s", path)
            total_files -= 1
            continue
        if (url := front_matter.get("pyproject_url")) is None:
            continue
        urls.append((url, front_matter))

    for url, front_matter in urls:
        pyproject = pyproject_from_url(url)
        if pyproject is None:
            continue

        if validate_pyproject(pyproject, front_matter, location=url):
            num_ok += 1

    print_summary_and_exit(total_files, num_ok)
