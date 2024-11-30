---
author: plu5
coop_support: Unknown
dependencies:
- UserFeedback>=1.5
download: https://github.com/plu5/p-borderlands/releases/latest
legacy: true
license: {}
supported_games:
- BL2
title: Saves Backuper
urls:
  Issues: https://github.com/plu5/p-borderlands/issues
  Source Code: https://github.com/plu5/p-borderlands/blob/main/SavesBackuper
version: 1.0.0 2021-04-21
---
Back up the contents of your saves folder each time you launch the game.
- You can set the number of backups that will be kept, to keep them below a certain threshold.
- You can set which folder to back up and where to back up to.


UserFeedback is required, make sure you remember to install that too.

Usage:
- On first enable, the paths configuration panel will pop up. There are some guesses made on where your SaveData folder might be. Status will tell you whether they are valid. Verify they are the paths you want or modify them as you see fit.
- On subsequent launches, the mod will be enabled automatically and save a backup, and no action is required. The panel will not pop up again unless there is a problem with the paths. You can open it manually by pressing C in the mod manager.
- By default, the number of backups to keep is set to 5. After this number is exceeded, the oldest one will be deleted. You can customise this behaviour in Options -&gt; Mods.

There is pretty good logging in this mod. You can check what’s going on by looking at the console or log (in `/Binaries/Win32/python-sdk.log`).

More information is available on the [README](https://github.com/plu5/p-borderlands/tree/main/SavesBackuper).