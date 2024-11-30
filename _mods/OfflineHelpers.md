---
author: apple1417
coop_support: Unknown
dependencies: []
download: https://github.com/apple1417/bl-sdk-mods/raw/master/OfflineHelpers/OfflineHelpers.zip
legacy: true
license:
  name: GNU GPLv3
  url: https://choosealicense.com/licenses/gpl-3.0
supported_games:
- BL2
- TPS
- AoDK
title: Offline Helpers
urls:
  Source Code: https://github.com/apple1417/bl-sdk-mods/
version: '1.3'
---
Adds several small features useful when playing offline.
- Fixes a crash when trying to chat while not connected to SHiFT.
- Adds an option to force your game to never connect to SHiFT.
- Adds an option to automatically hide the offline warning.

Note that using 'Force Offline Mode' will cause issues when running offline mod files - you need to manually open your mod file in a text editor, search for `GearboxAccountData_1` and change the `1` to a `0`. You will need to do this every time you re-save the file in BLCMM.