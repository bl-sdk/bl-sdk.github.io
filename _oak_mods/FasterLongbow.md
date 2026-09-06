---
pyproject_url: https://raw.githubusercontent.com/Last1SiN/FasterLongbow/refs/heads/main/pyproject.toml
---

Configurable Longbow grenade throw and pre-teleport timing for Borderlands 3. Speeds up equipped Longbow delivery without changing other grenade delivery types, exposes the tested timing values through the Mod Menu, and enforces a safe minimum for Longbow teleport timing. Client-side co-op compatible.

## Requirements

- Borderlands 3.
- [BL3 PythonSDK / Oak Mod Manager v1.11+ — latest stable release](https://github.com/bl-sdk/oak-mod-manager/releases/latest).
- [Official BL3 SDK installation guide](https://bl-sdk.github.io/oak-mod-db/).

Oak Mod Manager v1.11 already bundles the required Mods Base 1.12, BL3 Mod Menu 1.8, pyunrealsdk 1.10.0, and unrealsdk 3.2.0 components; they do not need to be downloaded separately when using that release or a newer compatible Oak release.

## Installation

1. Fully close Borderlands 3.
2. If BL3 PythonSDK / Oak is not installed or needs updating, open the [latest stable Oak Mod Manager release](https://github.com/bl-sdk/oak-mod-manager/releases/latest), download `bl3-sdk.zip` from **Assets**, and extract it directly into the Borderlands 3 game folder, allowing folders/files to merge. See the [official BL3 SDK installation guide](https://bl-sdk.github.io/oak-mod-db/) for the complete procedure and Proton/Linux notes.
3. Start the game once after installing/updating the SDK and verify that the **MODS** entry appears on the main menu.
4. Download the latest FasterLongbow from [GitHub Releases](https://github.com/Last1SiN/FasterLongbow/releases/latest).
5. Fully close the game and copy `FasterLongbow.sdkmod` **without extracting it** to `Borderlands 3\sdk_mods\`.
6. Start/restart the game, open **MODS -> FasterLongbow**, enable it, and use **Options** to configure the timing values.

To update the mod, replace the existing `.sdkmod` with the newer file and restart the game. Remove older FasterLongbow test/probe builds or extracted copies before installing the release.

## Credits

- **Mod creator / code:** Sol (ChatGPT, GPT-5.6 Sol)
- **QA / maintainer:** [Last1SiN](https://github.com/Last1SiN)
- **BL3 PythonSDK / Oak Mod Manager:** created by [apple1417](https://github.com/apple1417), with contributions from the [BL-SDK](https://github.com/bl-sdk) project and contributors.
