---
pyproject_url: https://raw.githubusercontent.com/Last1SiN/FasterLongbow/refs/heads/main/pyproject.toml
---

Configurable Longbow grenade throw and pre-teleport timing for Borderlands 3. Speeds up equipped Longbow delivery without changing other grenade delivery types, exposes the tested timing values through the Mod Menu, and enforces a safe minimum for Longbow teleport timing.

## Features
- Faster Longbow grenade throw animation.
- Shorter Longbow pre-teleport delay.
- Separate configurable timing for Divider Longbow grenades.
- All timing values can be changed from the in-game mod settings.
- Invalid or unsafe manually edited settings are validated before use.
- Longbow Teleport Delay is hard-limited to 0.11 seconds minimum because lower tested values can break the teleport.
- Temporary runtime timing changes are restored after the owning grenade action ends.
- Uses the actual grenade animation RateScale instead of moving the SpawnAndThrowGrenade notify.

## Credits

- **Development:** Sol / GPT-5.6 Sol
- **Design, testing & QA:** Last1SiN
- **BL3 PythonSDK / Oak Mod Manager:** created by [apple1417](https://github.com/apple1417), with contributions from the [BL-SDK](https://github.com/bl-sdk) project and contributors.
