---
author: Milo
coop_support: Unknown
dependencies: []
download: https://github.com/ncalvin1/Milo-BL2-SDK-Mods/raw/refs/heads/main/PlayerRandomizer/PlayerRandomizer_v0.2.zip
legacy: true
license:
  name: GNU GPLv3
  url: https://choosealicense.com/licenses/gpl-3.0
supported_games:
- BL2
- TPS
- AoDK
title: Player Randomizer
urls:
  Source Code: https://github.com/ncalvin1/Milo-BL2-SDK-Mods
version: '0.2'
---
Fills a player's trees with random skills, and
updates class mods to boost skills from the new set.

Idea stolen from Abahbob's Cross Class Skill Randomizer.

# Usage:
From the main menu, under Mods, enable 'Player
Randomizer (New Seed)'.  Bring up Options-&gt;Mods-&gt;Player
Randomizer to control how you want to randomize your
character.
  - **Skill Sources** sets which characters to pull skills
from.
  - **Additional Skills** lets you include skills that
should work despite referencing the wrong Action Skill,
as well as skills that may be nonfunctional or badly
broken.
  - **Action Skill** determines which character's action
skill to assign to yours; note that graphics may be
wrong for some character/skill combinations, but the
effects should still work correctly.
  - **Skill Density** selects how much to fill in the skill
tree - for reference, BL2 character trees are about 60%
full, while TPS trees average 65% full.
  - **Randomizing Tier Points** changes how many skill
points it takes to unlock the next skill tier.
  - **Randomize COMs** enables modifying the player's
classmods to contain skills from the new random tree.

Once you've made your choices, load your character and
start the session as usual.  The next time you launch
the game, the Mods menu will show a new enabled entry,
'Effect Randomizer (#)', where the number is the
newly-generated effect seed.  Remember that seed - if
the game crashes, you'll need to re-enable that entry.