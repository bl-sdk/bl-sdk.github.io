---
pyproject_url: https://raw.githubusercontent.com/Last1SiN/SnappyMovement/refs/heads/main/pyproject.toml
---

SnappyMovement makes Borderlands 3 ground movement more responsive by reducing acceleration and stopping inertia without increasing the game's normal movement speed. It changes only the local player's MaxAcceleration and BrakingDecelerationWalking, while leaving MaxWalkSpeed, MaxSprintSpeed, and GroundFriction untouched.

## Features

- Three selectable response profiles: Soft, Near Instant, and Instant.
- Custom mode with separate sliders for MaxAcceleration and BrakingDecelerationWalking.
- The default Near Instant profile uses 30000 / 40000.
- Selecting a preset updates both sliders automatically.
- Moving either slider manually switches the profile to Custom.
- Option changes apply immediately while the mod is enabled.
- Settings are reapplied to the local player's new pawn after respawn or map transitions.
- Values captured before SnappyMovement changed them are restored when the mod is disabled.
- Does not modify maximum walk speed, maximum sprint speed, GroundFriction, jump settings, air control, or slide speed.

## Requirements

- Borderlands 3.
- [BL3 PythonSDK / Oak Mod Manager v1.11+ — latest stable release](https://github.com/bl-sdk/oak-mod-manager/releases/latest).
- [Official BL3 SDK installation guide](https://bl-sdk.github.io/oak-mod-db/).

Oak Mod Manager v1.11 already bundles the required Mods Base 1.12, BL3 Mod Menu 1.8, pyunrealsdk 1.10.0, and unrealsdk 3.2.0 components; they do not need to be downloaded separately when using that release or a newer compatible Oak release.

## Installation

1. Fully close Borderlands 3.
2. If BL3 PythonSDK / Oak is not installed or needs updating, open the [latest stable Oak Mod Manager release](https://github.com/bl-sdk/oak-mod-manager/releases/latest), download bl3-sdk.zip from Assets, and extract it directly into the Borderlands 3 game folder, allowing folders and files to merge. See the [official BL3 SDK installation guide](https://bl-sdk.github.io/oak-mod-db/) for the complete procedure and Proton/Linux notes.
3. Start the game once after installing or updating the SDK and verify that the MODS entry appears on the main menu.
4. Download the latest SnappyMovement from [GitHub Releases](https://github.com/Last1SiN/SnappyMovement/releases/latest).
5. Fully close the game and copy SnappyMovement.sdkmod without extracting it to the Borderlands 3 sdk_mods folder.
6. Remove older No Movement Inertia hotfix builds so they cannot apply the same movement properties at the same time.
7. Start or restart the game, open MODS -> SnappyMovement, enable it, and use Options to select a profile or tune the sliders.

To update the mod, replace the existing SnappyMovement.sdkmod with the newer file and restart the game.

## Compatibility

- Applies to the local player's runtime movement component.
- Co-op support: Unknown — not formally validated for this release.
- Does not intentionally modify maximum movement speed, GroundFriction, jump settings, air control, or slide speed.

## Credits

- **Mod creator / code:** Sol (ChatGPT, GPT-5.6 Sol)
- **QA / maintainer:** [Last1SiN](https://github.com/Last1SiN)
- **BL3 PythonSDK / Oak Mod Manager:** created by [apple1417](https://github.com/apple1417), with contributions from the [BL-SDK](https://github.com/bl-sdk) project and contributors.
