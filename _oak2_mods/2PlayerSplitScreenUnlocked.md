---
pyproject_url: https://raw.githubusercontent.com/TitanNav/bl4-2player-splitscreen/main/mod/bl4ss/pyproject.toml
title: 2-Player Split-Screen Unlocked
---

![2-Player Split-Screen Unlocked]({{ "/assets/mods/oak2/bl4ss/banner.png" | relative_url }})

**Two-player local split-screen for Borderlands 4 on PC — one keyboard/mouse or controller for Player 1, a second
controller for Player 2, one screen.**

> **This is a BETA.** It has only been tested in the first open area after the prologue. Cutscenes, story events,
> vehicles, fast travel, bosses and plenty of other things I haven't reached yet may break it. I'm publishing early
> to gather feedback while I work through a full two-player playthrough, which is going to take a while.
> **Back up your saves before using it** (`Documents\My Games\Borderlands 4\Saved`).

---

## What it does

Borderlands 4 already contains couch co-op: the split-screen layout, Player 2's own menus, a "Swap Player" button,
separate saves for Player 2. On PC that path is never finished. A second player can't be added, a new Player 2
character can't get past character creation, and even when Player 2 exists, they never actually arrive in the
world. This mod closes those gaps so the game's own split-screen works:

- Player 2 joins on the main menu (automatically, or with one button).
- Player 2 loads any of their characters, or creates a new one, from the game's own couch co-op menus.
- Both players travel into the world together and play in split-screen.
- A handful of split-screen bugs are fixed along the way (blurred screen, lost mouse look, invisible menu cursor).

Player 2's characters are saved separately from Player 1's, under
`Saved\SaveGames\Profiles\client_0_user_1\`.

---

## Requirements and dependencies

- **Borderlands 4 on Steam.** Tested on the current Steam build (in-game version `1.10.1`, Steam build 25234898).
  Not tested on other stores.
- **The Oak2 Mod Manager (Python SDK) — required.** This mod is a Python SDK mod and does nothing without it. Get it
  from the SDK's official site: https://bl-sdk.github.io/oak2-mod-db/. It brings everything the mod depends on:
  - the SDK itself (`unrealsdk`, `pyunrealsdk`) and its own embedded Python, so no separate Python install is needed
  - `mods_base` (the mod framework: options, hooks, console commands)
  - `keybinds` (the F7/F8 hotkeys)
  - `console_mod_menu` (the `mods` console menu used to configure this mod)

  Tested with unrealsdk 3.2.0, pyunrealsdk 1.10.0 and mod manager 0.3.
- **Two controllers, both connected before you launch the game.** This is a hard requirement:
  - Player 1 uses keyboard/mouse **and/or** the first controller; Player 2 uses the second controller.
  - During Player 2's character creation the mouse cursor can disappear, and the first controller is the only
    reliable way through those screens (see "Creating a new Player 2 character").
  - **Only tested with two wired Xbox One controllers so far.** Other controllers may work; reports welcome.

## Installation

**Step 1: install the Oak2 Mod Manager (skip if you already use SDK mods).**

1. Download the mod manager from https://bl-sdk.github.io/oak2-mod-db/ and follow the install guide there for the
   current version.
2. It installs into the game folder (Steam → right-click Borderlands 4 → Manage → Browse local files). Once it's
   installed you should have:
   - `OakGame\Binaries\Win64\dsound.dll` (the SDK's loader)
   - an `OakGame\Binaries\Win64\Plugins\` folder (the SDK and its Python)
   - an `sdk_mods\` folder next to `Borderlands4.exe`, containing `mods_base.sdkmod`, `console_mod_menu.sdkmod` and
     `keybinds`
3. Launch the game once and open the console with `~`. You should see "Console Mod Menu loaded. Type 'mods' to get
   started." If you don't, fix the SDK install before continuing.

**Step 2: install BL4 2-Player Split-Screen Unlocked.**

1. Download **`bl4ss.sdkmod`** from the [latest release](https://github.com/TitanNav/bl4-2player-splitscreen/releases/latest).
2. Copy it **as-is** (don't unzip it) into the `sdk_mods\` folder from step 1, next to `mods_base.sdkmod`.
   The file must be named exactly **`bl4ss.sdkmod`**. The SDK ignores a renamed file, for example
   `bl4ss (1).sdkmod` from a repeated download, and prints an error in the console.
3. **Back up** `Documents\My Games\Borderlands 4\Saved`.
4. Connect **both** controllers, then launch the game.
5. The mod enables itself. To check, open the console (`~`) and type `mods`: **BL4 2-Player Split-Screen Unlocked** should be listed.
   You should also see a `[BL4SS] ready setter located by signature` line in the console.

**Updating:** quit the game and replace `sdk_mods\bl4ss.sdkmod` with the file from the latest release. Your
settings are kept.

**Uninstalling:** quit the game and delete `sdk_mods\bl4ss.sdkmod`. Player 2's characters stay in
`Saved\SaveGames\Profiles\client_0_user_1\`. Without the mod they can't be used, but they aren't deleted.

---

## Quick start (existing Player 2 character)

1. Launch with both controllers connected. On the main menu, **Player 2 is added automatically**. You'll see a
   second entry in the Party panel and a second character on the menu stage.
   If not, open the console (`~`) and type `bl4ss_p2`, or use the button in the mod menu (see "The mod menu").
2. Player 2 comes in with their **most recently played character**. To pick a different one: on controller 2
   press **A** on Player 2's party entry → **Swap Player** (this brings up Player 2's own menu) → **Load Vault
   Hunter**.
3. Player 1 selects **Continue**. Both players load into the world in split-screen.

To end split-screen: quit to the main menu and type `bl4ss_p2` (or use the mod menu button). A Player 2 removed by
hand isn't re-added automatically until you relaunch the game.

## Creating a new Player 2 character (one-time setup)

**Fair warning: this part is awkward, and I know it.** The game's Shared Progression screen only accepts input
from the "signed-in" player, which on PC is always Player 1. So for a moment, Player 1's controls have to drive
Player 2's menu. You only do this once per new Player 2 character; after that, Player 2 just loads it.

1. On the main menu with Player 2 added, controller 2 presses **A** on Player 2's party entry → **Swap Player**.
2. In Player 2's menu choose **Create Vault Hunter** (or **Load Vault Hunter → X Create New**) → **Yes** → pick a
   difficulty.
3. On the **Shared Progression** screen, **swap control**: open the console (`~`) and type `bl4ss_swap`, or use the
   **Swap control for P2 character creation** button in the mod menu. (The F8 hotkey does the same, but hotkeys
   often don't register on the main menu.)
4. Now **use controller 1** to choose Shared Progression On/Off and **pick Player 2's class**. The mouse cursor may
   be hidden while control is swapped, which is why the first controller is needed here.
5. **Control swaps back by itself** the moment the class is picked. (If you swapped by mistake, run `bl4ss_swap`
   again before picking a class to cancel.)
6. Controller 2 presses **B** to back out to Player 2's menu, then Player 1 selects **Continue**.
7. The new character is saved once you're in the world.

### Player 2 starts at level 1, without an action skill

A new Player 2 character starts at **level 1 with no action skill** and has to **level up to unlock it**, like a
character that hasn't played the prologue. **There is no "skip prologue" for Player 2.** I tried triggering the
game's skip-prologue rewards for Player 2 directly, and it had no effect. Expect first-time tutorial pop-ups for
Player 2 as well.

---

## The mod menu

Open the console with `~` and type `mods`, then pick **BL4 2-Player Split-Screen Unlocked**. Type the number or letter shown next to
an entry and press Enter; `q` leaves the menu. (Leave the mod menu before typing other console commands, or they're
read as menu choices.)

| Entry | What it does |
|---|---|
| **Enable / Disable** | Turns the whole mod on or off. It is enabled by default. |
| **Auto-join Player 2** (On/Off, default On) | When On, Player 2 is added whenever the main menu opens with one player and a second controller connected. Turn it Off if you want to add Player 2 yourself. |
| **Add / Remove Player 2** (button) | Main menu only. Adds Player 2 if there isn't one, removes Player 2 if there is. Same as console `bl4ss_p2` and hotkey F7. |
| **Swap control for P2 character creation** (button) | Main menu only, with Player 2 present. Gives Player 1's keyboard/mouse and controller 1 control of Player 2's menu until a class is picked; press again to cancel. Same as console `bl4ss_swap` and hotkey F8. |
| **Keybinds: Add / Remove Player 2 (F7), Swap control (F8)** | Rebind the two hotkeys. Note: hotkeys often don't register on the main menu itself; the console commands and buttons always work. |

Console commands (type in the `~` console, outside the mod menu):

- `bl4ss_p2`: add or remove Player 2 (main menu).
- `bl4ss_swap`: swap control for Player 2's character creation, or cancel the swap.

---

## Features, and how each one works

Every fix below is listed with the method it uses, so you can judge it for yourself. "Engine function" means a
normal Unreal Engine or game function called by name through the SDK, the same way any SDK mod works.

| Problem on PC | What the mod does | Method |
|---|---|---|
| **No way to add a second local player.** | Adds Player 2 on the main menu, automatically when a second controller is detected, or on demand. | Engine function `GameplayStatics.CreatePlayer`. Controller detection reads the engine's input-device list (`InputDeviceLibrary`): a connected device assigned to a second platform user. |
| **Player 2 can't get past Shared Progression when creating a character** (the screen only listens to the signed-in player). | Temporarily swaps which player each set of controls drives, until the class is picked. | Engine function `GameplayStatics.SetPlayerPlatformUserId` for both players; a hook on the game's travel notice ends the swap when the class pick moves Player 2 to the menu stage. |
| **Player 2 never arrives in the world** — stuck in the loading tunnel forever. The game waits for Player 2 to be "client ready", but that check needs an online ID, which a local guest never has, so it retries forever. | Marks Player 2 ready when they travel, which completes the arrival through the game's own code path. | **One direct call to the game's internal "client ready" function** for Player 2 (see "Is it safe?"). Located in memory by a code signature. |
| **Opening a menu blurs the other player's half** (a full-screen menu drops the game's global render scale to 10%, and in split-screen that setting is shared). | Keeps the render scale where you set it. | Re-issues the console setting `r.ScreenPercentage` once, at its current value, via the engine's console-command function. Console-set values outrank the menu's change. Your Upscaling Quality option still works. |
| **Player 1 loses mouse look after one click while Player 2's menu is open** (Player 2's menu switches the shared game window into menu input mode). | Puts Player 1 back into game input mode whenever Player 2 opens a menu, unless Player 1's own menu is open. | Engine function `WidgetBlueprintLibrary.SetInputMode_GameOnly` for Player 1, when the menu opens and again ~20 frames later. |
| **Player 2's controller cursor is invisible in menus** (menus still follow an invisible pointer, with lag). The cursor only switches on after Player 2's menu has received real mouse movement, and on PC the mouse belongs to Player 1. | The first time Player 2 opens a menu in the world, gives Player 2 the mouse for **one frame** and moves it a few pixels there and back. | Engine function `SetPlayerPlatformUserId` (swap and swap back), plus the Windows functions `mouse_event` (a ±12-pixel relative move) and, only if Player 1's menu is open at that moment, `SetCursorPos` to briefly place the pointer over Player 2's half and put it back. Once per Player 2. |

---

## Is it safe? An honest breakdown

I'd rather you know exactly what this does than find it in a decompiler, so here's everything that could look
unusual.

**What the mod is:** plain Python source running inside the Oak2 SDK. A `.sdkmod` file is a zip. Rename it to
`.zip` and read every line. Nothing is compiled or obfuscated.

**What it does *not* do:**
- No network access, no downloads, no telemetry.
- No DLLs or executables of its own. (The SDK itself hooks into the game; that's how every SDK mod works.)
- It never patches the game's code and never writes into the game's memory directly.
- It doesn't edit save files. The only file it writes is its own settings file, through the SDK's normal settings
  system.

**Things that deserve an explanation:**

1. **It reads the game's code in memory and calls one internal game function.** This is the only low-level part
   of the mod. Player 2's arrival in the world depends on an internal "client ready" function that the game runs
   for Player 1 but never for a local guest, because the step before it waits for an online ID that Player 2
   doesn't have. The function isn't exposed to mods by name, so the mod finds it by scanning the game's code for a
   known byte pattern. That's a read-only scan of the game's own process. It then calls it once for Player 2 per
   trip into the world. The function itself sets a single "ready" flag, exactly as it does for Player 1.
   - **Guard rails:** the pattern must match exactly one place, and a second, independent function that reads the
     same flag must match too. Only on the exact tested game build (checked by the executable's timestamp and
     size) is a known address used as a fallback, and only after checking the bytes there. **On anything else,
     the mod refuses and logs why.** Player 2 can still join on the menu but won't arrive in the world, rather
     than the mod calling something it isn't sure about.
   - **Alternatives I looked at:**
     - **Doing it purely through named engine functions:** there isn't one that does this.
     - **Patching the game's retry logic so the check passes for guests:** that would modify game code, which is
       more invasive and more fragile.
     - **Giving Player 2 a fake online identity:** unknown side effects on saves, party and entitlements.
     - **Calling the one function the game already calls for Player 1:** the smallest change that works, so
       that's what the mod does.

2. **It generates a tiny mouse movement and can move your pointer.** This is how Player 2's menu cursor is made
   visible (see the features table). I tried every cleaner route I could find first, and none worked:
   - toggling cursor flags
   - resetting input focus
   - changing Player 2's input type
   - swapping players without mouse movement
   - moving the pointer over Player 2's half without a swap

   What the mod does is a Windows `mouse_event` of 12 pixels there and back, once per Player 2, lasting one frame.
   `SetCursorPos` is used only when Player 1's menu is open, to place the pointer over Player 2's half for that
   frame and put it back. It only moves your own pointer, on your own PC, while the game is focused. You may see
   a barely visible flicker.

3. **It briefly swaps which player your controls drive:** during Player 2's character creation until the class
   pick, and for one frame on Player 2's first menu. This uses the engine's own function for assigning controls to
   players.

4. **It sets a console variable** (`r.ScreenPercentage`) to the value it already has, the same as typing it into
   the console yourself.

**Saves:** Player 2's characters live in their own profile folder (`Saved\SaveGames\Profiles\client_0_user_1\`),
separate from your Steam profile's saves, so they may not be covered by Steam Cloud. Back that folder up yourself.
I haven't seen any save corruption in testing, but this is a beta.

**Online play:** the mod is marked host-only and is meant for local split-screen. I haven't tested it in online
sessions with other players.

---

## Game updates: will it keep working?

- **Most of the mod should survive updates.** Adding Player 2, the control swap, the render-scale fix, the
  mouse-look fix and the cursor fix all use engine and game functions **by name**. Updates normally keep those
  names. They break only if the developers rename or rework those systems.
- **The arrival fix is the part most likely to break.** It finds the internal "client ready" function by its code
  pattern rather than a fixed address, so ordinary recompiles that just move code around are handled. If an update
  changes that function or its neighbour enough that the pattern no longer matches, **the mod refuses safely**: it
  logs "could not locate the ready setter safely", Player 2 can still join on the menu, but gets stuck on the way
  into the world.
- **How I'd patch it after an update:**
  1. Confirm the refusal message in the console.
  2. Re-find the function on the new build using the same research method: follow the "client ready" flag from the
     code that reads it.
  3. Update the byte pattern and the build check.
  4. Retest a full join → arrival → play session before publishing.

  This depends on my free time (see "Bug reports and support").

---

## Known issues

- **Player 2 spawns inside Player 1** when arriving in the world. Not a functional problem, just strange-looking;
  walk apart.
- **Player 2 starts at level 1 without an action skill** (see above). No skip-prologue for Player 2.
- **Leave Split Screen** in Player 2's pause menu does nothing. Quit to the main menu and use `bl4ss_p2` instead.
- **Hotkeys (F7/F8) often don't register on the main menu.** Use the console commands or the mod menu buttons.
- **Auto-join has occasionally not fired** even with both controllers connected. Add Player 2 by hand.
- **Controller cursor invisible:** see Troubleshooting. Player 2's is handled automatically; Player 1's has once
  needed a mouse movement first.
- **Player 2's first menu in the world** swaps controls for a single frame (you shouldn't notice it). If Player 1's
  menu is open at that moment, the mouse pointer may flicker.
- **During Player 2's character creation**, the mouse cursor may be hidden while control is swapped. Use
  controller 1.
- **Everything beyond the first area after the prologue is untested.**

## Troubleshooting

- **Player 2 isn't added on the main menu:** make sure both controllers were connected before launch, then add
  Player 2 by hand: console `bl4ss_p2`, or the mod menu button. Check that **Auto-join Player 2** is On if you
  expected it to happen automatically.
- **A controller cursor is invisible in a menu** (the highlight still follows the stick, with a slight lag): move
  the **mouse** inside that menu once, then use the stick again; the cursor shows and stays visible. Player 2's
  cursor is fixed automatically the first time Player 2 opens a menu. If Player 2's cursor stays invisible, please
  report it.
- **Player 2 is stuck in the loading tunnel / never appears in the world:** open the console (`~`) and look for a
  `[BL4SS]` line saying the ready setter couldn't be located. That means a game update changed the code the mod
  needs (see "Game updates"). Please report it with your game version.
- **Player 1 lost mouse look while Player 2's menu is open:** this should be fixed. If it happens, opening and
  closing the console (`~` twice) restores it. Please report it.
- **Controls feel swapped** (controller 1 drives Player 2): if you used `bl4ss_swap`, run it again to cancel, or
  pick a class to end it. Quitting to the main menu also clears it.
- **An action seems to do nothing:** open the console (`~`). The mod's messages start with `[BL4SS]`, and errors
  show there (they may not appear in the SDK's log file). Include those lines in bug reports.
- **"DLL load failed while importing keybinds" at startup:** that message comes from the SDK itself before any mod
  loads; relaunching the game has fixed it.
- **Something went wrong with Player 2's saves:** restore your backup of `Saved\SaveGames\Profiles\client_0_user_1\`.

---

## Bug reports and support

All bug reports are welcome, on the [issues page](https://github.com/TitanNav/bl4-2player-splitscreen/issues). Please include your game version, your controllers, what you were doing, and any
`[BL4SS]` lines or errors from the console (`~`).

That said, this is very much a hobby project, so **I can't promise quick updates**. I've really enjoyed working on
it, so I expect to keep supporting it, and I'll fix any game-breaking bugs I run into during my own playthrough.
Bugs reported by others may or may not get addressed, depending on whether I can reproduce them on my setup. No
promises, but I'll read everything.

## Credits

Built on the Oak2 Python SDK and its mod manager. Thanks to the SDK developers for making Borderlands 4 moddable.
