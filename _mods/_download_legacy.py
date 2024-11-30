#!/usr/bin/env python
import re
from pathlib import Path
from typing import Any

import requests
import yaml

MOD_FOLDER = Path(__file__).parent
LEGACY_MODS_JSON_URL = "https://bl-sdk.github.io/mods.json"
YT_TAG_REGEX = re.compile(r"!\[yt\]\((.+?)\)", flags=re.I)


def arr_to_sentence(arr: list[str], joiner: str = "and") -> str:
    match len(arr):
        case 0:
            return ""
        case 1:
            return arr[0]
        case 2:
            return f" {joiner} ".join(arr)
        case _:
            return ", ".join(arr[:-1]) + f", {joiner} " + arr[-1]


def replace_yt_tags(data: str) -> str:
    return YT_TAG_REGEX.sub(lambda match: f"\n\n{{% youtube {match.group(1)} %}}", data)


def convert_mod_data(mod: dict[str, Any]) -> None:
    converted_data = {
        "legacy": True,
        "title": mod["name"],
        "author": arr_to_sentence(mod["authors"]),
        "version": mod["latest"],
        "supported_games": mod["supports"],
        "coop_support": "Unknown",
        "license": (
            {
                "name": mod["license"][0],
                "url": mod["license"][1],
            }
            if len(mod["license"]) > 0
            else {"name": "Unknown", "url": ""}
        ),
        "dependencies": [
            name + version for name, version in mod["requirements"].items()
        ],
        "urls": {
            k: v
            for k, v in {
                "Source Code": mod["source"],
                "Issues": mod["issues"],
            }.items()
            if v
        },
        "download": mod["versions"][mod["latest"]],
    }
    return (
        "---\n"
        + yaml.dump(converted_data)
        + "---\n"
        + replace_yt_tags(mod["description"])
    )


if __name__ == "__main__":
    for mod in requests.get(LEGACY_MODS_JSON_URL).json():
        mod_file = MOD_FOLDER / (Path(mod["url"]).stem + ".md")
        with mod_file.open("w") as file:
            file.write(convert_mod_data(mod))
