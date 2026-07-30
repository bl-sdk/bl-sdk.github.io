---
pyproject_url: https://raw.githubusercontent.com/RedxYeti/bl2-willow2-sdkmods/refs/heads/main/VHRandomizer/pyproject.toml
---
Requires corourtines https://bl-sdk.github.io/willow2-mod-db/mods/coroutines/


Randomly pick a vault hunter with timed auto swap options or a hotkey.


Keeps your gear/levels/skill tree/missions etc.

Options:

  Swap type:
  
    Full Random will pick a random character every time
    
    Half Random will go through every character randomly before repeating in a new random order
    
    Linear will go through each character in a specific order

  Character:
  
    Share shield, grenade, artifact, weapons decide whether your characters share those items or theyre seperate per character
    
    Interrupt action skills will decide if you can randomize while using an action skill
    
    Silly ragdoll will ragdoll your last character

  Auto Swap:
  
    Min swap time is the lowest time in seconds the mod will randomize
    
    Max swap time is the max time between randomization, set this 1 higher than the min if you want to swap a specific interval
    
    Start/Stop buttons will start or stop the randomization, you can also use the hotkey

  Hotkeys:
  
    Swap Character will randomize your character as long as you meet the requirements (not in a car, cutscene etc)
    
    Toggle swapping will turn on or off the swapping
    
    Mark all items will mark items that are equipped on all characters, very useful if share gear is off
    

TPS and AoDK are supported but largely untested.

Suggested mods to use:

Anarchy Saver https://bl-sdk.github.io/willow2-mod-db/mods/anarchysaver/

Backpack Manager https://bl-sdk.github.io/willow2-mod-db/mods/backpackmanager/


Extra Notes:

Back up your saves if you care about them!

No coop support

Dont use premade saves from places like nexus, this mod relies on item serials and those saves usually have a bunch of spawned items with the same serial.

Loot Lemon codes may have the same issue.

Certain actions are blocked mid randomization, you might not encounter this

Inputs get eaten during swaps, no way around this.

Expect softlocks or even hardlocks

Expect a few crashes
