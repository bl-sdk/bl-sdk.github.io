---
pyproject_url: https://raw.githubusercontent.com/Last1SiN/TrueFastball/refs/heads/main/pyproject.toml
---

TrueFastball is a Borderlands 2-style Fastball overhaul for Borderlands 3. It increases Fastball damage with a configurable multiplier and accelerates the tested throw animation, while deliberately leaving Borderlands 3's native Fastball projectile speed and trajectory unchanged.

## Features

- Applies only to equipped Fastball throws and the actual Fastball projectile delivery.
- Default Fastball Damage Multiplier: 2.56.
- Multiplies the already-computed runtime GrenadeDamage, preserving native level and Mayhem scaling.
- Default Throw Animation RateScale: 2.0.
- Restores temporary throw-animation changes when the owning grenade action ends.
- Does not modify Fastball projectile speed, gravity, upward velocity, or trajectory.
- Exposes both release settings through the in-game Mod Menu.
- Validates manually edited or otherwise invalid saved settings before use.

## Requirements

- Borderlands 3.
- [BL3 PythonSDK / Oak Mod Manager v1.11+ — latest stable release](https://github.com/bl-sdk/oak-mod-manager/releases/latest).
- [Official BL3 SDK installation guide](https://bl-sdk.github.io/oak-mod-db/).

Oak Mod Manager v1.11 already bundles the required Mods Base 1.12, BL3 Mod Menu 1.8, pyunrealsdk 1.10.0, and unrealsdk 3.2.0 components; they do not need to be downloaded separately when using that release or a newer compatible Oak release.

## Installation

1. Fully close Borderlands 3.
2. If BL3 PythonSDK / Oak is not installed or needs updating, open the [latest stable Oak Mod Manager release](https://github.com/bl-sdk/oak-mod-manager/releases/latest), download `bl3-sdk.zip` from **Assets**, and extract it directly into the Borderlands 3 game folder, allowing folders/files to merge. See the [official BL3 SDK installation guide](https://bl-sdk.github.io/oak-mod-db/) for the complete procedure and Proton/Linux notes.
3. Start the game once after installing/updating the SDK and verify that the **MODS** entry appears on the main menu.
4. Download the latest TrueFastball from [GitHub Releases](https://github.com/Last1SiN/TrueFastball/releases/latest).
5. Fully close the game and copy `TrueFastball.sdkmod` **without extracting it** to `Borderlands 3\sdk_mods\`.
6. Remove older Fastball test/probe builds so only one Fastball runtime mod can load.
7. Start/restart the game, open **MODS -> TrueFastball**, enable it, and use **Options** to configure the two values.

To update the mod, replace the existing `TrueFastball.sdkmod` with the newer file and restart the game.

## Compatibility

- Fastball damage modification is gated to the actual Fastball projectile delivery.
- Borderlands 3 Fastball projectile speed and trajectory are intentionally unchanged.
- Co-op support: **ClientSide**.

## Credits

- **Development:** Sol / GPT-5.6 Sol
- **Design, testing & QA:** Last1SiN
- **BL3 PythonSDK / Oak Mod Manager:** created by [apple1417](https://github.com/apple1417), with contributions from the [BL-SDK](https://github.com/bl-sdk) project and contributors.
