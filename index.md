---
layout: main
---

**Page Contents**
* TOC
{:toc}

This is the main page for the PythonSDK Mod Database.
The [PythonSDK](https://github.com/bl-sdk/PythonSDK) is an Unreal Engine plugin allowing you to write plugins in Python to interact directly with UE objects.
This opens up many new avenues for modding, from simply allowing modifying dynamically generated objects to letting modders run arbitrary game functions whenever they please.

Currently it supports:
- Borderlands 2
- Borderlands: The Pre-Sequel
- Tiny Tina's Assault on Dragon Keep: A Wonderlands One-shot Adventure
<p></p>

## SDK Installation

If you're a video guide type person, [apple1417](https://github.com/apple1417) made a video guide:
![yt](https://youtu.be/57WxvASCX70)

But if you're more of a text guide style person:

1. Download the [latest release](https://github.com/bl-sdk/bl2-mod-manager/releases/latest) on Github.
![PythonSDK Download Page](/assets/images/posts/installation1.png)
2. Open `PythonSDK.zip`. It should contain a single `Binaries` folder:
![PythonSDK.zip Contents](/assets/images/posts/installation2.png)
1. Locate your game's files.
  
   In Steam, this can be done by right-clicking on the game in your library, selecting "Properties," then in the "Local Files" section, clicking "Browse":    
   ![Steam Contextual Menu](/assets/images/posts/installation3.png) ![Steam Local Files Properties](/assets/images/posts/installation4.png)

   The default locations are:    
   Steam: `C:\Program Files (x86)\Steam\steamapps\common\<game>`    
   Epic: `C:\Program Files\Epic Games\<game>`    
2. Copy the `Binaries` folder from `PythonSDK.zip` **exactly as it is** over your game folder, so it merges with the one there.
![Win32 Folder Contents](/assets/images/posts/installation5.png)
5. If you had previously installed an older version of the SDK, delete any old files that weren't overwritten by the ones in the latest `PythonSDK.zip`. The release notes will tell you which ones.
6. You are done, and may launch the game (if it is running, relaunch it now). You should see a "Mods" menu in the main menu!
7. If the SDK fails to run with the files correctly in place as described above, you may need to [download and install Microsoft Visual C++ Redistributable](https://aka.ms/vs/16/release/vc_redist.x86.exe).

## Installing on Linux
PythonSDK does not yet work natively on Linux, but it seems to work well under SteamPlay/Proton and Wine. To load properly, though, Wine needs to be told to allow `ddraw.dll` overrides. Simply set the game's launch options (via `Properties -> General`) to:

```
WINEDLLOVERRIDES="ddraw=n,b" %command%
```

Additionally, the latest SDK releases want the main executable name to be `Borderlands2.exe` (or one of the other games as relevant), so doing a symlink/copy for `Launcher.exe` won't work. If you want or need to bypass the launcher you can add `-NoLauncher` to the launch options after `%command%`:

```
WINEDLLOVERRIDES="ddraw=n,b" %command% -NoLauncher -NoStartupMovies
```

## Mod Installation
Installing mods is even simpler than installing the SDK itself.

In order to install SDK mods, all you need to do is:

1. Download the mod itself, usually this will be a zip file.
![Mod Download Link](/assets/images/posts/mod-install1.png)
2. With the "General" mod selected, press `O` to open the Mods folder.    
   ![Open Mods Folder Key](/assets/images/posts/mod-install1.5.png)
3. Then you can extract the folder from the mod zip file into this Mods folder.    
   ![Extracted Mod Folder](/assets/images/posts/mod-install2.png)
   In the root of this new mod folder, there should be an `__init__.py` file. Depending on the mod, there might be other files too, in the mod folder, but the `__init__.py` should always be there.
   ![`__init__.py`](/assets/images/posts/mod-install3.png)
4. Restart your game, and the mod will get loaded.
5. Certain mods may have requirements, you can see them by looking at the `Requirements` header. Follow the exact same steps to install these.
6. More advanced mods could have some extra steps needed to install them, you should always read through the `Description` section of the mod page to make sure that you've installed the mod properly!

## Further Support
If you need further help, join the [Borderlands Modding Support Discord](https://discord.gg/bXeqV8Ef9R) to read through FAQs or ask your own questions.
