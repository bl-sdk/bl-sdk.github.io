#!/usr/bin/env python
import argparse
import json
import platform
import shutil
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Literal

ALL_CONFIGS: tuple[str, ...] = ("dev", "oak", "willow2")

BASE_CONFIG = "dev"
EXTRA_CONFIGS: tuple[str, ...] = ("oak", "willow2")

EXTRA_STYLESHEETS_TO_DELETE: tuple[str, ...] = (
    "just-the-docs-dark.css",
    "just-the-docs-default.css",
    "just-the-docs-light.css",
)

SITE_DIR = Path(__file__).parent / "_site"
MERGED_SITE_DIR = Path(__file__).parent / "_merged_site"


def build_or_serve(
    action: Literal["build", "serve"],
    config: str,
    *args: str,
) -> None:
    """
    Runs a Jekyll build or serve process.

    Args:
        action: Which action to run.
        config: Which site configuration to use.
        *args: Extra args to pass to the Jekyll process.
    """
    subprocess.run(
        [
            "bundle",
            "exec",
            "jekyll",
            action,
            "--config",
            ("_config.yml" if config == BASE_CONFIG else f"_config.yml,_config_{config}.yml"),
            *args,
        ],
        check=True,
        # On Windows bundle is actually bundle.bat, but thanks to PATHEXT you can call it as just
        # "bundle". Need to treat it as a shell command to get the same behaviour.
        shell=platform.system() == "Windows",
    )


def merge() -> None:
    """Builds and merges all site configurations."""
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    if MERGED_SITE_DIR.exists():
        shutil.rmtree(MERGED_SITE_DIR)
    SITE_DIR.mkdir(exist_ok=True)

    for config in (BASE_CONFIG, *EXTRA_CONFIGS):
        build_or_serve("build", config, "-d", str(SITE_DIR / config))

    replace_default_css()
    merge_sitemaps()
    merge_search_data()
    move_redirects()

    for config in EXTRA_CONFIGS:
        shutil.move(
            SITE_DIR / config / f"{config}-mod-db",
            SITE_DIR / BASE_CONFIG / f"{config}-mod-db",
        )

    shutil.move(SITE_DIR / BASE_CONFIG, MERGED_SITE_DIR)
    shutil.rmtree(SITE_DIR)


def replace_default_css() -> None:
    """Replaces the "just-the-docs-default.css" stylesheet with each config's specific one."""
    for config in (BASE_CONFIG, *EXTRA_CONFIGS):
        for path in (SITE_DIR / config).glob("**/*.html"):
            path.write_text(
                path.read_text(encoding="utf8").replace(
                    "/assets/css/just-the-docs-default.css",
                    f"/assets/css/just-the-docs-{config}.css",
                ),
                encoding="utf8",
            )

    for stylesheet in EXTRA_STYLESHEETS_TO_DELETE:
        (SITE_DIR / BASE_CONFIG / "assets" / "css" / stylesheet).unlink(missing_ok=True)


def merge_sitemaps() -> None:
    """Merges the `sitemap.xml`s across all configurations."""
    base_sitemap = SITE_DIR / BASE_CONFIG / "sitemap.xml"
    tree = ET.parse(base_sitemap)  # noqa: S314
    root = tree.getroot()

    for config in EXTRA_CONFIGS:
        root.extend(ET.parse(SITE_DIR / config / "sitemap.xml").getroot())  # noqa: S314

    tree.write(
        base_sitemap,
        encoding="UTF-8",
        xml_declaration=True,
        default_namespace="http://www.sitemaps.org/schemas/sitemap/0.9",
    )


def merge_search_data() -> None:
    """Merges the `search-data.json`s, and updates the javascript to pull from the relevant one."""
    for config in (BASE_CONFIG, *EXTRA_CONFIGS):
        shutil.move(
            SITE_DIR / config / "assets" / "js" / "search-data.json",
            SITE_DIR / BASE_CONFIG / "assets" / "js" / f"search-data-{config}.json",
        )

    main_js = SITE_DIR / BASE_CONFIG / "assets" / "js" / "just-the-docs.js"
    main_js.write_text(
        main_js.read_text(encoding="utf8").replace(
            "'/assets/js/search-data.json'",
            (
                "`/assets/js/search-data-${"
                'window.location.pathname.match(/^\\/(willow2|oak)-mod-db/)?.[1] ?? "dev"'
                "}.json`"
            ),
        ),
        encoding="utf8",
    )


def move_redirects() -> None:
    """Moves any redirects from the extra site configs back into the base folder."""
    for config in EXTRA_CONFIGS:
        redirects_json = SITE_DIR / config / "redirects.json"
        if not redirects_json.exists():
            continue
        with redirects_json.open() as file:
            data: dict[str, str] = json.load(file)
            for redirect_path in data:
                filename = (
                    redirect_path[1:] + ("index" if redirect_path[-1] == "/" else "") + ".html"
                )
                dest = SITE_DIR / BASE_CONFIG / filename
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(SITE_DIR / config / filename, dest)

    (SITE_DIR / BASE_CONFIG / "redirects.json").unlink(missing_ok=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="helper to run jekyll with the right settings")
    subparsers = parser.add_subparsers(required=True)

    # As far as we're concerned, these are basically aliases for each other - only difference being
    # we need to use whichever action the user specified. Seems easiest by just adding two parsers.
    for name in ("build", "serve"):
        build_or_serve_parser = subparsers.add_parser(name, help=f"runs a jekyll {name}")
        build_or_serve_parser.set_defaults(action=name)

        build_or_serve_parser.add_argument(
            "config",
            choices=(BASE_CONFIG, *EXTRA_CONFIGS),
            help="which site configuration to use",
        )
        build_or_serve_parser.add_argument(
            "extra_args",
            nargs=argparse.REMAINDER,
            metavar="...",
            help="remaining args are passed directly to jekyll",
        )

    merge_parser = subparsers.add_parser("merge", help="builds and merges the full site")
    merge_parser.set_defaults(action="merge")

    args = parser.parse_args()
    action: Literal["build", "serve", "merge"] = args.action

    match action:
        case "build" | "serve":
            build_or_serve(args.action, args.config, *args.extra_args)
        case "merge":
            merge()
