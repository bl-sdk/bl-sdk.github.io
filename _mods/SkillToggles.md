---
author: Relentless and Chronophylos
coop_support: Unknown
dependencies:
- EridiumLib>=0.4.2
download: https://github.com/DAmNRelentless/bl2-skilltoggles/releases/tag/v1.3.2
legacy: true
license:
  name: GNU GPLv3
  url: https://choosealicense.com/licenses/gpl-3.0
supported_games:
- BL2
- TPS
title: Skill Toggles
urls:
  Issues: https://github.com/DAmNRelentless/bl2-skilltoggles/issues
  Source Code: https://github.com/DAmNRelentless/bl2-skilltoggles
version: 1.3.2
---
Lets you deactivate Action Skills by holding a configurable hotkey.

Features:
- deactivate the Action Skills for each character
- configurable hotkey
- options to enable deactivation for class individually

Notes:
- since this is often not the case with SDK mods: yes, this has multiplayer support if all players have it installed
- deactivating Action Skills won't give you a cooldown bonus
  - there are some exceptions in Borderlands TPS where it works
- in a multiplayer environment, only the host settings of the mod are taken into account
  - that means only the host can define which Action Skills are deactivatable
  - you can still use your own hotkey
- the default toggle key is `F` which also is the default Action Skill hotkey
  - you need to *hold* they key, not just press it to avoid accidental deactivation
  - you can change it to anything in the modded keybinds but you can't change it back to `F` because it's already taken by the Action Skill
  - if you want to use the `F` key again, you need to delete the settings.json file in the mod directory, restart the game and reenable the mod
  - if you are using another hotkey for the Action Skill, you can also directly edit the modded hotkey in the `settings.json` file while the game is closed

Everything related to versions and their release notes can be found in the [changelog](https://github.com/DAmNRelentless/bl2-skilltoggles/blob/main/CHANGELOG.md).
If you found a bug or you have a feature request, please use our issue tracker linked below.