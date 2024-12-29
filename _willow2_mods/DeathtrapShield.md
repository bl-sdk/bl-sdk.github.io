---
author: Relentless
coop_support: Unknown
dependencies:
- EridiumLib>=0.4.2
download: https://github.com/DAmNRelentless/bl2-deathtrapshield/releases/tag/v1.1.1
legacy: true
license:
  name: GNU GPLv3
  url: https://choosealicense.com/licenses/gpl-3.0
redirect_from:
- /mods/DeathtrapShield/
supported_games:
- BL2
title: Deathtrap Shield
urls:
  Issues: https://github.com/DAmNRelentless/bl2-deathtrapshield/issues
  Source Code: https://github.com/DAmNRelentless/bl2-deathtrapshield
version: 1.1.1
---
Gives Deathtrap its own configurable shield from the inventory of Gaige.

Features:
- Deathtrap can use its own shield and no longer shares the shield with Gaige
- you can define which shield to use in the inventory
- configurable hotkey

Notes:
- since this is often not the case with SDK mods: yes, this has multiplayer support
- the default behaviour of the skill applies and the shield of Gaige will be shared when:
  - you don't set a Deathtrap shield
  - you equip the Deathtrap shield to Gaige
- the Deathtrap shield will lose its status when:
  - you set a new Deathtrap shield while already having one
  - you equip the Deathtrap shield to Gaige
  - you throw the Deathtrap shield on the ground
  - another character that is not a Mechromancer puts it in their inventory
- other useful information:
  - this only works if you unlocked the `Sharing is Caring` skill
  - you can only set one Deathtrap shield at a time
  - you can't set a Deathtrap shield as trash or favorite (unset it first)
  - the Deathtrap shield will have another color
- the hotkey to set the Deathtrap shield can be modified in the modded keybinds
- if you have a Deathtrap shield set, you won't be able to edit your save game in the SaveGame Editor unless you rejoin the game and remove the shield status, this can't be fixed

Everything related to versions and their release notes can be found in the [changelog](https://github.com/DAmNRelentless/bl2-deathtrapshield/blob/main/CHANGELOG.md).
If you found a bug or you have a feature request, please use our issue tracker linked below.