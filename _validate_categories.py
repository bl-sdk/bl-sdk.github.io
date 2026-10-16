#!/usr/bin/env python
# /// script
# requires-python = ">=3.13"
# dependencies = [
#   "pyyaml",
# ]
# ///

from __future__ import annotations

import re
import sys
from difflib import get_close_matches
from pathlib import Path
from typing import TYPE_CHECKING, Any

import yaml

if TYPE_CHECKING:
    from collections.abc import Collection

CATEGORIES_FILE = Path(__file__).parent / "_data" / "categories.yml"


PER_TREE_CATEGORIES: dict[str, tuple[str, ...]] = {
    # Map from the category key to the mod folders it's allowed in
    # BL1
    "brick": ("_willow1_mods",),
    "lilith": ("_willow1_mods",),
    "mordecai": ("_willow1_mods",),
    "roland": ("_willow1_mods",),
    # BL2
    "axton": ("_willow2_mods",),
    "gaige": ("_willow2_mods",),
    "krieg": ("_willow2_mods",),
    "maya": ("_willow2_mods",),
    "salvador": ("_willow2_mods",),
    "zer0": ("_willow2_mods",),
    # TPS
    "athena": ("_willow2_mods",),
    "aurelia": ("_willow2_mods",),
    "claptrap": ("_willow2_mods",),
    "jack": ("_willow2_mods",),
    "nisha": ("_willow2_mods",),
    "wilhelm": ("_willow2_mods",),
    # BL3
    "amara": ("_oak_mods",),
    "fl4k": ("_oak_mods",),
    "moze": ("_oak_mods",),
    "zane": ("_oak_mods",),
    # WL
    "blightcaller": ("_oak_mods",),
    "brrzerker": ("_oak_mods",),
    "clawbringer": ("_oak_mods",),
    "graveborn": ("_oak_mods",),
    "spellshot": ("_oak_mods",),
    "spore-warden": ("_oak_mods",),
    "stabbomancer": ("_oak_mods",),
    # BL4
    "amon": ("_oak2_mods",),
    "c4sh": ("_oak2_mods",),
    "harlowe": ("_oak2_mods",),
    "loveless": ("_oak2_mods",),
    "rafa": ("_oak2_mods",),
    "vex": ("_oak2_mods",),
}


def get_all_categories() -> Collection[str]:
    """
    Gets a list of all valid categories.

    Returns:
        The list of categories.
    """
    with CATEGORIES_FILE.open() as file:
        data = yaml.safe_load(file)
        return data.keys()


VALID_CATEGORY_NAME_RE = re.compile("^[a-z0-9-]+$")


def validate_category_name(categories: Collection[str]) -> int:
    """
    Makes sure all category names are correctly formatted.

    Args:
        categories: The list of categories to validate.
    Returns:
        The amount of errors - 0 on success.
    """
    errors = 0
    for cat in categories:
        if not VALID_CATEGORY_NAME_RE.match(cat):
            sys.stderr.write(f"Invalid category name '{cat}'!\n")
            errors += 1
    return errors


def parse_front_matter(path: Path) -> tuple[Collection[str], int]:
    """
    Parses jekyll front matter, extracting the mod categories.

    Args:
        path: Path to the file to parse.
    Returns:
        A (categories, num_errors) tuple.
    """
    categories: set[str] = set()

    try:
        with path.open() as file:
            data = next(yaml.safe_load_all(file))
            assert isinstance(data, dict)
            front_matter: dict[str, Any] = data  # type: ignore
    except Exception:  # noqa: BLE001
        sys.stderr.write(f"Couldn't parse front matter from {path}\n")
        return (), 1

    if "mod_categories" not in front_matter:
        for key in ("mod_Categories", "mod_category", "category", "categories", "tag", "tags"):
            if key in front_matter:
                sys.stderr.write(
                    f"wrong key for categories, use 'mod_categories', not '{key}', from {path}\n",
                )
                return (), 1
        return (), 0

    mod_categories = front_matter["mod_categories"]
    if not isinstance(mod_categories, str):
        sys.stderr.write(f"'mod_categories' has invalid type {type(categories)}, from {path}\n")
        return (), 1

    split_categories = mod_categories.split()
    if len(set(split_categories)) != len(split_categories):
        sys.stderr.write(f"duplicate mod categories in {path}\n")
        return split_categories, 1

    return split_categories, 0


def validate_mod_file(
    all_categories: Collection[str],
    path: Path,
) -> int:
    """
    Validates the categories stored in a mod file.

    Args:
        all_categories: A list of valid categories.
        path: Path to the mod file to validate.
    """
    mod_categories, errors = parse_front_matter(file)

    tree = path.parent.name  # e.g. "_oak_mods"

    for category in mod_categories:
        if category not in all_categories:
            suggestion = get_close_matches(category, all_categories, n=1)
            if suggestion:
                sys.stderr.write(
                    f"invalid category '{category}', did you mean '{suggestion[0]}'? from {path}\n",
                )
            else:
                sys.stderr.write(f"invalid category '{category}', from {path}\n")
            errors += 1
            continue
        if (
            (allowed_trees := PER_TREE_CATEGORIES.get(category)) is not None  # formatting
            and tree not in allowed_trees
        ):
            sys.stderr.write(
                f"'{category}' is not a valid category for mod files in '{tree}', from {path}\n",
            )
            errors += 1
            continue

    return errors


if __name__ == "__main__":
    errors = 0

    all_categories = get_all_categories()
    errors += validate_category_name(all_categories)

    for file in Path(__file__).resolve().parent.glob("_*_mods/*"):
        errors += validate_mod_file(all_categories, file)

    if errors:
        sys.stderr.write(f"{errors} total errors\n")
        sys.exit(1)
    else:
        sys.stdout.write("No errors\n")
