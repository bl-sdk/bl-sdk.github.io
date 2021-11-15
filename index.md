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
![yt](https://youtu.be/hsnqPZIc_L8)

But if you're more of a text guide style person:

1. Download the [latest release](https://github.com/bl-sdk/PythonSDK/releases/latest) on Github.
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

## Development

Using the Unreal Engine console, you can use a few extra console commands added in by the PythonSDK:
- `py <PYTHON STATEMENT>`, using this will run arbitrary python code.
- `pyexec <PYTHON FILE>`, execute an arbitrary python file.

The PythonSDK itself passes a ton of functions over to the Python interface.
All of these are included in the `unrealsdk` module which you can import from a python script.

### Writing SDK Mods
The best set of advice is to look at other mods (see this DB for mods :P)
The SDK's mod "API" (in Python) comes with a ton of doc strings which you should read through in order to get an understanding of how to write a mod.

If you've got questions, you can always ask in our [Discord](https://discord.gg/VJXtHvh).
There's plenty of tutorials online helping you to get proficient in Python (or coding in general),
you should atleast understand / be proficient in object orientated programming or atleast be willing to learn these things.

One of the more helpful things with writing SDK mods is looking at the game's decompiled UnrealScript code, allowing you to understand what functions do what actions:
1. Download Gildor's [Unreal Package Decompressor](https://www.gildor.org/downloads) and [UE Explorer](https://eliotvu.com/portfolio/view/21/ue-explorer).
2. Open up `WillowGame/CookedPCConsole` and then run the decompressor on the relevant UPKs there. `WillowGame` and `Engine` are the most useful, and you may occasionally find `GameFramework` and `GearboxFramework` handy, pretty much everything else can be ignored.
3. Once you've decompressed the UPKs, look at them in UE Explorer, switch to object view, and then scroll/search around for whatever class.
   
   You can also export the decompiled scripts to your disk if you want to use a different text/code editor.    
   ![Tools -> Exporting -> Export Scripts](/assets/images/posts/mod-dev1.png)

### Adding to the Database
In order to add your mods to this database, you need to create a JSON file and host it somewhere, following the format like:
```json
{
  "mods": [
    {
      "name": "[Mod Name]",
      "authors": "[Mod Author]",
      "description": "[Description, can include HTML/Markdown]",
      "tagline": "[Optional: A short description of the mod, if not available will pull from `description`]",
      "types": ["[Mod Types]"],
      "supports": ["[Supported Games ie `[\"BL2\", \"TPS\", \"AoDK\"]`]"],
      "issues": "[Optional] A link to your issues report page",
      "source": "[Optional] Link to the source code",
      "latest": "[LATEST VERSION]",
      "versions": {
        "[Latest Version]": "[Version Link]",
        "[Old Version]": "[Old Version Link]"
      },
      "[Optional] requirements": {
        "[Requirement]": "(>=, ==, <=)[VERSION]"
      },
      "license": "[Optional] See: https://github.com/bl-sdk/bl-sdk.github.io/blob/main/scripts/GenerateModDocs.py#L12 for available options",
      "date": "[Optional] An ISO8601 formatted date time string"
    }
  ],
  "[Optional] defaults": {
    "authors": "[Mod Author]",
    "source": "[Mod Source]",
    "supports":  ["[Supported Games ie `[\"BL2\", \"TPS\"]`]"],
    "license": "See: https://github.com/bl-sdk/bl-sdk.github.io/blob/main/scripts/GenerateModDocs.py#L12 for available options",
    "types": ["[Mod Types]"],
  }
}
```
If you want to add more mods to be displayed in the database, add to the `mods` array following the same format.
If you're tired of constantly typing in your mods `"authors": "MY NAME"`, you can add/create the `defaults` object and define your author name, etc there instead and remove it from the mod objects.
Mod object properties take priority over the defaults so if you have `"authors": "test1234"` in a mod object but your default is `"authors": "this is my name"`, the mod's author will be `test1234`.

If you're wanting to link to a different mod on the database without making it a requirement or something, you'll want to remove all non-alphanumeric characters.
For example: `mod-name: "Sanity Saver"` gets saved as `SanitySaver.md` so when linking to it from another page, you'll want to do `[Sanity Saver](/mods/SanitySaver)`

You can also implement other licenses that aren't supported by declaring it as a list: 
`"license": ["User Friendly Name", "Full URL Link"]`

Then you can make a [Pull Request](https://github.com/bl-sdk/bl-sdk.github.io/pulls) and edit `https://github.com/bl-sdk/bl-sdk.github.io/blob/master/scripts/RepoInfo.json` to include the **direct** link to your hosted JSON file.

### Missing Requirements Notifications
If a user doesn't install all the requirements your mod needs, it probably can't load. Rather than just having your mod fail to load with no proper indication, this database provides a page you can open to explain what's missing.

[https://bl-sdk.github.io/requirements/](/requirements)

As you can see, this page doesn't work out of the box, you need to use query parameters to fill in some information.

| Field         | Usage                                                                                        |
|:--------------|:---------------------------------------------------------------------------------------------|
| `m`/`mod`     | Holds the name of your mod.                                                                  |
| `u`/`update`  | If it exists, changes the page to talk about outdated requirements rather than missing ones. |
| `a`/`all`     | If it exists, also pulls in all requirements defined in your mod info file.                  |
| Anything Else | The name of a requirement mod to list, optionally holding the required version.              |

Only the first instance of the predefined fields are used, so if you really need to define a requirement called `update` you can simply add it as a parameter twice.

Once you have your url, to open the page you can use the `webbrowser` module.
```py
try:
  from Mods import AsyncUtil
except ImportError as ex:
  import webbrowser
  webbrowser.open("https://bl-sdk.github.io/requirements/?mod=Alt%20Use%20Vendors&AsyncUtil")
  raise ex
```
You can add more complex logic to build up the url based on exactly which mods are installed and what their versions are.
If you want to pass in the version (i.e. `Mod >= 3.1`), you do it like so: `UserFeedback=>=3.1` or `UserFeedback===3.1`.
The requirements page will pull the latest version of the requirements.
