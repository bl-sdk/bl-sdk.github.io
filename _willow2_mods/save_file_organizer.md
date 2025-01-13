---
pyproject_url: https://raw.githubusercontent.com/Justin99x/willow2-sdk-mods/refs/heads/main/save_file_organizer/pyproject.toml
---

Users can name their BL2/TPS files anything they want that ends in the .sav extension. In addition,
several utility features are included.

## Features

### Rename all saves to a standard format

In the options menu there is a button to rename all saves in your save folder to follow the format:
`Save#### - <UICharacterName>.sav.`

So a save that was `Save1234.sav` with a character name of Bandit Krieg will now be `Save1234.sav - Bandit Krieg.sav`

### Auto rename saves

Automatically renames all saves each time you enter the main menu to the format specified above. Useful if you make a
lot of new characters or rename characters often.

### Restore saves

This button restores all saves to the game's standard format.

### Defrag saves

This button renames all saves in the above format, except it also changes your save IDs such that they start from
Save0000 and move up sequentially. Hex characters are skipped so that only digits 0-9 are used.

WARNING: The defrag button loads and resaves your save files. If the save has unloaded items, such as from a mod
overhaul, you may lose those items.