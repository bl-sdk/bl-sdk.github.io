---
pyproject_url: https://raw.githubusercontent.com/tunnelweb/coop-save-quit/refs/heads/main/CoopSaveQuit/pyproject.toml
---

Save quitting is how you farm, and it kicks everyone else out of your game. This does the same job
without ending the session.

Press F6. Chests come back unopened, vendors restock, enemies respawn, and nobody gets kicked out.

## Host only

Only the host needs it. Travel is server side so your friend gets pulled along, and everyone lands
back where they were stood instead of at the fast travel point.

## Options

**Respawn Chests & Vendors** (on) - vendors count as population too, so their item of the day
rerolls every time you reload.

**Respawn Enemies** (on) - separate switch, because enemies sit on a different population class to
everything else. Turn it off if respawning mission NPCs gets in the way.

**Restore Position** (on) - off means you come back at the station instead.

**Save Before Reloading** (on) - leave this alone unless you know why you want it off.

**Position Restore Window** (150) - how long the mod holds you in place after the load. Raise it
if you still end up at the station.

## How it works

quickload and Commander both call `ReturnToTitleScreen`, which is the save quit menu option, so
they kick your partner too. This travels to a station instead, down the same code path the game
uses for fast travel, and the session survives that.

The travel on its own isnt enough though. Loading a map doesnt reset chests, which is why fast
travelling somewhere and coming back has never worked for farming. Chests get handed out by the
population system, and theres one flag on it, `bTotalResetOnLevelLoad`, that decides whether a
spawner forgets what it already gave you. It ships off, so the mod flips it on and then travels.

Respawning Loot has been doing that with one `set` command for years, all credit there. This just
does the same thing from python so its all one mod, and splits chests and enemies apart since they
live on different classes.

Dice chests are left out on purpose. They stack their loot instead of rerolling it, which makes
them a pain to loot.

## Known quirks

It travels to whatever station your save last recorded, not necessarily one in the map youre stood
in. Nearly every map has a New-U or a level transition and those count, so youll probably never
hit it. If your last save was somewhere else though, thats where youll end up.
