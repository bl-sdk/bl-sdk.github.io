---
pyproject_url: https://raw.githubusercontent.com/tunnelweb/coop-save-quit/refs/heads/main/CoopSaveQuit/pyproject.toml
---

press f5 to reload the map. chests, vendors and enemies reset the same as a save quit would, but
nobody gets kicked out of your game.
only the host presses the key. everyone gets pulled along and lands back where they were stood, not
at the fast travel point.

**read only mode** (f6) is farming mode. the game stops saving and every reload puts your missions
back to where they stood when you turned it on, so quest rewards stay farmable. everything else you
do goes with them, levels and loot included. your partner needs the mod for this one since saving
happens on their machine, and toggling it as host toggles theirs. **f7** saves on the spot if you
want to commit before switching it on. **restore position** can be turned off in settings if youd
rather come back at the station.

works fine solo too. you get a save quit without the trip through the title screen, and with
read only on, f7 makes saving something you choose rather than something the game does behind
you.

respawning loot did the chest half of this with one `set` command for years, all credit there.

## known quirks

it travels to whatever station your save last recorded, which isnt always in the map youre stood
in. most maps have a new-u or a level transition and those count, so youll probably never hit it.

map loads in bl2 sometimes wedge at about one frame a second. thats an engine leak, not this mod,
but reloading gives you more loads to hit it on, so theres a fix for it in here. both players want
the mod installed, each copy can only unstick its own game. if a loading screen sits there frozen,
wait it out, dont quit.

## ai training

not for training ai. dont scrape it, dont dataset it, dont feed it to a model. no.
