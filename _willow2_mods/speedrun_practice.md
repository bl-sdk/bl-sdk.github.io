---
pyproject_url: https://raw.githubusercontent.com/Justin99x/willow2-sdk-mods/refs/heads/main/speedrun_practice/pyproject.toml
---

Borderlands 2 mod with various utilities to help in practicing speedruns. All speedruns are currently supported on
some level, although many runs (e.g. current patch) don't need much help other than an easy way to make practice saves.

Co-op is now supported!

## Installation

1. Make sure the new BL2 Python SDK is installed according to https://bl-sdk.github.io/willow2-mod-db/
2. This mod has the following dependencies:
    1. Borderlands Commander v2.5: https://bl-sdk.github.io/mods/BorderlandsCommander/
3. Copy speedrun_practice.sdkmod into your sdk_mods folder.
4. Launch the game, select "Mods" from the main menu, then enable SpeedrunPractice

## Features

### Block achievements

Accidental presses of the Achievements menu option no longer open Steam/Epic

### Disable travel portal

There's an option in the menu to disable the blue tunnel on entering a level at a fast travel station. Helpful for
faster practice when level reloads are needed.

### Move save to top

Keybind to use `touch` command to set the modified time of your save file to current time, which effectively brings it
to the top of the list when choosing saves in the character menu.

### Save checkpoints and game state

A keybind can be set up to save checkpoints to allow for easy replay of the same segments. When the keybind is pressed,
the following actions occur:

- The user is asked for the name of the new file.
- A new save file is created with the current state of the game and set to read only.
- Non-savable game states are stored in the actual save file using some unused player stat values. Whenever using this
  save in the future, a second key bind can be used to load those game states, allowing for continuation
  of game play with the same number of stacks and merges applied. Useful for practicing the same late game segments.
  - Anarchy stacks
  - Buck Up stacks
  - Free Shots
  - Smasher/SMASH stacks
  - Active weapon
  - Current ammo in clips
  - Weapon merges
  - Map position 
  - NEW: Expertise stacks
  - NEW: Crit/accuracy bonuses from mass duping in co-op
- All items are now co-op compatible! Both users need to be running the mod.

It's best to leave the checkpoint files as read only. The player stats are not rewritten when saving regularly, only
when using the checkpoint feature.

### Stacks and skills keybinds

Using an in game keybind and input window, can set the following to desired values. Note that you must be using a game
patch that allows these for the keybinds to be enabled. For example, weapon merging is not available on patches 1.8.5
and later.

- Anarchy stacks (Gaige only)
- Buck up stacks (Gaige only)
- New: Expertise stacks (Axton only)
- Free shot stacks (from Vladof launcher)
- Evil Smasher chance stacks
- Evil Smasher SMASH stacks
- Merge all equipped weapons

### Jakobs shotgun auto-fire

Menu option that makes all Jakobs shotguns auto fire. This is intended to mimic the functionality of the in-game
free scroll macro created by Apple. SDK mods and that macro cannot be installed simultaneously, so I added this option
for practice. Just turn this option on and rebind fire to whatever key you plan to use for the free scroll macro.

### Randomize gear (Any% Gaige only)

A keybind can be set that randomizes your shotgun and shield based on your current story
progress and the vendors you would have checked at that point. When the keybind is pressed, all jakobs shotguns and amp
and turtle shields are dropped in front of you, and new gear from the vendor item pools are equipped or put into your
inventory.

The purpose of this is to be able to practice sections of the game with a wide variety of RNG based gear that you would
likely encounter during normal runs.

Specifically, each of the following items are rolled:

- Frostburn - always get a white Turtle shield
- Sanctuary level 8-10 - always get a Jakobs shotgun with a Jakobs, Bandit, or Torgue barrel
- Fridge level 13-14 - always get an amp shield with at least 100 damage
- Overlook level 14-16 - always get a Jakobs shotgun with a Jakobs, Bandit, or Torgue barrel
- Hyperion Bridge - one attempt to get an amp shield with at least 25 more damage than existing amp
- Wildlife - one attempt to get an amp shield with at least 25 more damage than existing amp
- Thousand Cuts - one attempt to get an amp shield with at least 25 more damage than existing amp

If at any point an amp shield with damage >= 175 is obtained, no more shield vendors are checked.

### Reset gunzerk (Geared Sal)

Keybind to end gunzerk and reset cooldown. Also fills your rocket ammo and drop swaps all weapons to get them back to
the optimal drop order needed for drop reloading. This works only if you have your damage weapons in slots 1 and 2, with
Badabooms in slots 3 and 4.

### Reset gunzerk, teleport, and trigger skills (Geared Sal)

A separate keybind to do the same thing as reset gunzerk, plus teleport you to the currently active Commander position
with 0 velocity, and trigger skills of your choosing. The skills triggered by this keybind are configurable in the
options menu:

- Incite
- Locked and Loaded
- All kill skills

## Changelog

### Version 2.1
- Added co-op support. Off-host players can now use keybinds and save game states. Additionally added support for two important co-op run items:
  - Expertise stacks (saving and keybind)
  - Crit and accuracy bonuses from mass duping (saving only)

### Version 2.0

- Updated to work with new Python SDK (and moved to new repo).
- New SDK works on older patches, which removes the need for all older patch simulation functionality. Users are now
  expected to practice on the game version they plan on using for the run.
- Automatically get save file directories - no need to set config file value.

### Version 1.6

- Added option to disable travel portal (blue tunnel) for faster practice.
- When resetting to commander position as Geared Sal, velocity is now set to 0.

### Version 1.5

- Added Geared Sal functionality.
- Options and keybinds update automatically based on loaded character and speedrun category selection.
- Block achievements from tabbing out your game.
- Add "touch" functionality to move current save to top of list.

### Version 1.4.1

- Fixed issue where travel and Jakobs auto fire were not resetting back to normal state when disabling the mod.

### Version 1.4

- Save states are now stored in the save file itself.
- Added Evil Smasher stacking so that the mod can be used for All Quests.
- Changed keybinds for adding/removing stacks to a single "set" keybind for each.
- Changed internal logic of infinite ammo stacking to exactly mimic the old patches.
- Changed internal logic of weapon merging to exactly mimic the old patches.
- Removed dependency on Commander.

### Version 1.3

- Added gear randomizer keybind.

### Version 1.2

- Fixed issue where save names with letters broke the system - now correctly treats save file numbers as hexadecimal.
- Changed save behavior to keep the current save active and keep the save filename constant, only the newly created save
  increments.
- Pickup radius changed to 200 to mimic version 1.1 functionality.

### Version 1.1

- Removed DLC expansions from the FT menu
- Auto enable Three Horns Divide FT without going to station
- Added keybind to show current stats - buckup, free shots, and crit bonus
- Ability to save checkpoints complete with game state (anarchy, buck up, merged weapons, and map position)
- Games loaded from checkpoint files will load with same weapon as previously active
- Option to make Jakobs shotguns auto-fire