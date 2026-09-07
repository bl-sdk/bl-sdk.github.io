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

## Compatibility

- The damage multiplier applies only to Fastball grenades.
- Borderlands 3 Fastball projectile speed and trajectory are intentionally unchanged.

## Credits

- **Development:** Sol / GPT-5.6 Sol
- **Design, testing & QA:** Last1SiN
- **BL3 PythonSDK / Oak Mod Manager:** created by [apple1417](https://github.com/apple1417), with contributions from the [BL-SDK](https://github.com/bl-sdk) project and contributors.
