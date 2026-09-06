---
pyproject_url: https://raw.githubusercontent.com/Last1SiN/BL4-SuperDash/refs/heads/main/pyproject.toml
---

Multi-directional Super Dash for Borderlands 4 with one rebindable key or controller button. Follows your current movement direction, including keyboard diagonals and continuous analog stick angles on gamepad, with forward fallback from a standstill. Preserves sprint after landing when started from sprint. Uses native Dash/Jump calls without external macro software. Client-side co-op compatible.

## Requirements

- Borderlands 4.
- [BL4 PythonSDK / Oak2 Mod Manager v0.3+ — latest stable release](https://github.com/bl-sdk/oak2-mod-manager/releases/latest).
- [Official BL4 SDK installation guide](https://bl-sdk.github.io/oak2-mod-db/).

Oak2 Mod Manager v0.3 already bundles the required Mods Base 1.12, Console Mod Menu 1.6, and Keybinds 1.1 components; they do not need to be downloaded separately when using that release or a newer compatible Oak2 release.

## Installation

1. Fully close Borderlands 4.
2. If BL4 PythonSDK / Oak2 is not installed or needs updating, download the [latest stable Oak2 Mod Manager release](https://github.com/bl-sdk/oak2-mod-manager/releases/latest) and extract it directly into the Borderlands 4 game folder (the folder containing `OakGame`), allowing folders/files to merge. See the [official SDK guide](https://bl-sdk.github.io/oak2-mod-db/) for the complete procedure and Proton/Linux notes.
3. Start the game once after installing/updating the SDK. Press `~` twice, type `mods`, and verify that the Mod Menu opens.
4. Download the latest BL4 Super Dash from [GitHub Releases](https://github.com/Last1SiN/BL4-SuperDash/releases/latest) or [Nexus Mods](https://www.nexusmods.com/borderlands4/mods/289).
5. Fully close the game and copy `BL4_SuperDash.sdkmod` **without extracting it** to `Borderlands 4\sdk_mods\`.
6. Start/restart the game, press `~` twice, type `mods`, open **BL4 Super Dash**, enable it, and bind **Super Dash** to the desired keyboard, mouse, or gamepad button.

To update the mod, replace the existing `.sdkmod` with the newer file and restart the game.

## Credits

- **Mod creator / code:** Sol (ChatGPT, GPT-5.6 Sol)
- **QA / maintainer:** [Last1SiN](https://github.com/Last1SiN)
- **BL4 PythonSDK / Oak2 Mod Manager:** created by [apple1417](https://github.com/apple1417), with contributions from the [BL-SDK](https://github.com/bl-sdk) project and contributors.
