---
pyproject_url: https://raw.githubusercontent.com/tunnelweb/coop-save-quit/refs/heads/main/CoopSaveQuit/pyproject.toml
---

Save quitting is how you farm, and it kicks everyone else out of your game. This does the same job
without ending the session.

Press F6. Chests come back unopened, vendors restock, enemies respawn, and nobody gets kicked out.

## Host only, with one exception

Only the host presses the key, and only the host needs it for the reload. Travel is server side so
your friend gets pulled along, and everyone lands back where they were stood instead of at the fast
travel point.

Read only is the exception. Saving happens on whoever owns the character, on their own machine, in
their own copy of the game, so nothing the host does can hold a partners progress back. If they
want their quest rewards farmable too they need this mod installed as well, with Save Before
Reloading turned off. Then when you reload the map under them, their game rolls its own missions
back the same way yours does.

## Options

**Respawn Chests & Vendors** (on) - vendors count as population too, so their item of the day
rerolls every time you reload.

**Respawn Enemies** (on) - separate switch, because enemies sit on a different population class to
everything else. Turn it off if respawning mission NPCs gets in the way.

**Restore Position** (on) - off means you come back at the station instead. Theres no window to
tune any more, the mod holds you in place until the position actually sticks and lets go the
moment you start walking.

**Save Before Reloading** (on) - commit your game before reloading, the way a real save quit does.
Turning it off IS read only mode, the game stops saving entirely and every reload rolls your
missions back to the last save. Flick it off before you turn a quest in, not after, the turn in
autosaves on the spot and theres nothing left to roll back to.

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

## The frozen load fix

Sometimes a map load, any map load, not just this mods reloads, wedges the game at about one
frame a second and never comes back. The cause turned out to be a leak in the engine itself. To
load a map it first has to garbage collect the one its leaving, and occasionally an object thats
marked never collect is still holding the old maps levels through cross level references, so
collection can never succeed. The engine retries the full sweep every second or so forever, and
that sweep is the freeze.

The mod fights it on two fronts. First it tries to stop the leak mattering at all, a little
while after every load, once the game is visibly calm, it asks the engine for one ordinary
cleanup collect. Thats the same call the game makes at its own transitions, nothing unusual
happens, but it gives the engine a clean chance to let go of the old maps leftovers while
nothing is being loaded. If that lands, the next load has nothing to wedge on and theres no
freeze to fix.

Second, the rescue. When a load freezes outright for ten seconds and then sits under five fps,
the mod cuts the leaked cross level references, takes the never collect mark off the leaked
holder, and asks the engine to run the collect right then. If the ask lands recovery is quick,
if the engine ignores it its own schedule still gets there inside a couple of minutes. Either
way dont quit out, the screen tells you when its working on it.

Only a stuck load gets touched. The never collect mark turns out to be load bearing on a healthy
game, some of what wears it is held through plain native pointers the collector cant see, so
nothing gets stripped from a game thats fine. A healthy load just gets one line written to the
log, a note of whats rooted, so a future wedge can be traced.

Both players want the mod installed for this one, a wedge can happen on either machine and each
copy can only unstick its own game.

## Known quirks

It travels to whatever station your save last recorded, not necessarily one in the map youre stood
in. Nearly every map has a New-U or a level transition and those count, so youll probably never
hit it. If your last save was somewhere else though, thats where youll end up.

On some machines the reload still freezes the screen for about half a minute, thats the engine
leak from the frozen load section above. The rescue handles it by itself every time, so if the
loading screen sits there frozen just wait it out, dont quit. Getting the freeze to not happen at
all is still being worked on.
