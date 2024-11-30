---
author: Siggles
coop_support: Unknown
dependencies:
- UserFeedback>=1.6
download: https://github.com/Siggless/bl-sdk-mods/raw/main/AmbientSpawns/AmbientSpawns.zip
legacy: true
license:
  name: GNU GPLv3
  url: https://choosealicense.com/licenses/gpl-3.0
supported_games:
- BL2
title: Ambient Spawns
urls:
  Issues: https://github.com/Siggless/bl-sdk-mods/issues
  Source Code: https://github.com/Siggless/bl-sdk-mods/tree/main/AmbientSpawns
version: 1.1.0
---
Periodically spawns random groups of enemies.
The idea is to make the game more unpredictable.

It matches spawn points to enemies with spawn animations, so it doesn't look too janky.
Options for spawn frequency and distance to the player, and which enemies to use:
- Den		- Only spawns enemies that usually spawn from a chosen point.
- Level	- Only spawns enemies loaded in the current level.
- DLC*	- May spawn any custom enemy groups from the current DLC (or base game).
- Game*	- May spawn any custom enemy groups from the entire game.
*These options require all available enemies to be loaded upon reaching the start menu.
*This causes a few textures to break, and possibly crashes.