---
pyproject_url: https://raw.githubusercontent.com/Last1SiN/SnappyMovement/refs/heads/main/pyproject.toml
---

SnappyMovement makes Borderlands 3 ground movement more responsive by reducing acceleration ramp-up time and stopping inertia without increasing the game's normal movement speed. It changes only the local player's MaxAcceleration and BrakingDecelerationWalking, while leaving MaxWalkSpeed, MaxSprintSpeed, and GroundFriction untouched.

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

## Compatibility

- Applies to the local player's runtime movement component.
- Does not intentionally modify maximum movement speed, GroundFriction, jump settings, air control, or slide speed.

## Credits

- **Development:** Sol / GPT-5.6 Sol
- **Design, testing & QA:** Last1SiN
- **BL3 PythonSDK / Oak Mod Manager:** created by [apple1417](https://github.com/apple1417), with contributions from the [BL-SDK](https://github.com/bl-sdk) project and contributors.
