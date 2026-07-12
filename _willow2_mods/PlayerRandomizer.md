---
pyproject_url: https://raw.githubusercontent.com/ncalvin1/Milo-BL2-SDK-Mods/refs/heads/main/PlayerRandomizer/PlayerRandomizer/pyproject.toml
redirect_from:
- /mods/PlayerRandomizer/
---
# Character Randomizer
An overengineered redesign and expansion of Abahbob's elegant Cross-Class Skill
Randomizer, this mod scrambles a player character's skills and class mods.

## Features
  - Change or randomize the action skill.
  - Choose which characters you want to borrow skills from.
  - Select how densely you want the skill trees populated.
  - Update class mods to augment the character's new skills.

## Notes
  - This does not work in multiplayer.
  - Action skill graphics and user interfaces are not updated.  Characters using
      Gunzerk will notice the offhand weapon is not visible, but it still fires
      projectiles.  Characters using Decepti0n will miss part of Zer0's HUD,
      and Zer0 characters using another action skill may notice his HUD behaving
      strangely.  Characters whose original action skills can't normally be
      terminated early will notice that they can't pull back turrets, Deathtrap,
      the Aspis shield, or Digi-Jacks early to reduce cooldown.  (And, yes,
      Gaige breathing like Salvador when she's gunzerking is one of the more
      disturbing things I've encountered in a game.)
  - The mod does not work with custom characters as anything other than the
      main character.  It may work with custom characters as the main character,
      but there are no guarantees.  In particular, skills that have been
      cannibalized to make other skills work (such as Maya's Cloud Kill in the
      Lilith mod) will probably malfunction or even crash the game.  Back up
      your game save, try 'em, and see!
    - Custom character text mods must have the Offline checkbox selected in
        BLCMM, or COM randomization will tend to crash.
    - Verify that the Player Randomizer has noted the custom character by
       opening the Options -> Mods -> Skill Sources menu and checking that the
       custom character's name is in the list.  If not, try disabling and
       re-enabling the Player Randomizer, then re-selecting the target player
       character.
    - Known successes:
      - Roland works unchanged.  Axton's extra turret skills appear to stack
          on Roland's turret without issue.
      - Lilith works, but only if Blight Phoenix is added as a cheat.  Otherwise
          the game hangs as soon as one opens her skill trees.

## Usage
  - From the main menu, under Mods, enable 'Player Randomizer'.
  - Return to the main menu and select the character you want to have randomized
      skills.
  - Bring up Options->Mods->Player Randomizer to control how you want to
      randomize your character.
    - **Skill Sources** sets which characters to pull skills from.
    - **Additional Skills** lets you include skills that should work despite
       referencing the wrong Action Skill, as well as skills that may be
       nonfunctional or badly broken.
    - **Action Skill** determines which character's action skill to assign to
       yours; note that graphics may be wrong for some character/skill
       combinations, but the effects should still work correctly.
    - **Skill Density** selects how much to fill in the skill tree - for
       reference, BL2 character trees are about 60% full, while TPS trees
       average 65% full.
    - **Randomizing Tier Points** changes how many skill points it takes to
       unlock the next skill tier.
    - **Randomize COMs** enables modifying the player character's classmods to
       contain skills from the new random tree.
    - **Cheats** let you specify skills you want to appear in the player
       character's skill tree and one random classmod.
    - **Reroll** chooses a new set of random skills.
  - Start your game as usual.

## Known Issues
  - Disable the PlayerRandomizer when starting a new character, and only
      re-enable it after saving the new character at least once.  Otherwise the
      game may hang.
  - Changes made through the in-game menu do not take effect until quitting
      to the main menu and re-entering the game.
  - Krieg's Buzzaxe Rampage does not work for other characters.
  - Gunzerking works only partially in AoDK.  The offhand gun contributes
      modifiers such as Moxxi healing, and makes firing noises, but does not
      fire projectiles.
