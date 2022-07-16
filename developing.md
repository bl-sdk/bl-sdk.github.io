---
layout: main
---

**Page Contents**
* TOC
{:toc}

# Developing Mods

Using the Unreal Engine console, you can use a few extra console commands added in by the PythonSDK:
- `py <PYTHON STATEMENT>`, using this will run arbitrary python code.
- `pyexec <PYTHON FILE>`, execute an arbitrary python file.

The PythonSDK itself passes a ton of functions over to the Python interface.
All of these are included in the `unrealsdk` module which you can import from a python script.

## Writing SDK Mods
The best set of advice is to look at other mods (see this DB for mods :P)
The SDK's mod "API" (in Python) comes with a ton of doc strings which you should read through in order to get an understanding of how to write a mod.

If you've got questions, you can always ask in the [Developer Discord](https://discord.gg/VJXtHvh).
There's plenty of tutorials online helping you to get proficient in Python (or coding in general),
you should atleast understand / be proficient in object orientated programming or atleast be willing to learn these things.

## Viewing UnrealScript code
One of the more helpful things with writing SDK mods is looking at the game's decompiled UnrealScript code, allowing you to understand what functions do what actions:
1. Download Gildor's [Unreal Package Decompressor](https://www.gildor.org/downloads) and [UE Explorer](https://eliotvu.com/portfolio/view/21/ue-explorer).
2. Open up `WillowGame/CookedPCConsole` and then run the decompressor on the relevant UPKs there. `WillowGame` and `Engine` are the most useful, and you may occasionally find `GameFramework` and `GearboxFramework` handy, pretty much everything else can be ignored.
3. Once you've decompressed the UPKs, look at them in UE Explorer, switch to object view, and then scroll/search around for whatever class.
   
   You can also export the decompiled scripts to your disk if you want to use a different text/code editor.    
   ![Tools -> Exporting -> Export Scripts](/assets/images/posts/mod-dev1.png)

## Adding to the Database
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

## Missing Requirements Notifications
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

<hr>

# Developer FAQ

## How do I create a new mod?
1. Create a new folder in the Mods folder
2. Create an `__init__.py` within it with the following basic template:
```python
   import unrealsdk
   from Mods import ModMenu
   
   class MyMod(ModMenu.SDKMod):
       Name: str = "My Mod Name"
       Author: str = "My Name"
       Description: str = "My Mod Description"
       Version: str = "1.0.0"
       SupportedGames: ModMenu.Game = ModMenu.Game.BL2 | ModMenu.Game.TPS  # Either BL2 or TPS; bitwise OR'd together
       Types: ModMenu.ModTypes = ModMenu.ModTypes.Utility  # One of Utility, Content, Gameplay, Library; bitwise OR'd together
       
   instance = MyMod()
   
   ModMenu.RegisterMod(instance)
```
3. Launch the game. Your mod should now appear in the mod manager. If it doesn't, console output / contents of `python-sdk.log` (which can be found in your `Win32` folder, one folder up from the Mods folder) should give a clue as to why.

## How to reload my mod without having to restart the game?
Add the following to your `__init__.py` **before** RegisterMod is called:
```python
if __name__ == "__main__":
    unrealsdk.Log(f"[{instance.Name}] Manually loaded")
    for mod in ModMenu.Mods:
        if mod.Name == instance.Name:
            if mod.IsEnabled:
                mod.Disable()
            ModMenu.Mods.remove(mod)
            unrealsdk.Log(f"[{instance.Name}] Removed last instance")

            # Fixes inspect.getfile()
            instance.__class__.__module__ = mod.__class__.__module__
            break
```
Now you should be able to reload your mod by running `pyexec ModFolderName/__init__.py` (change ModFolderName to the name of the folder your mod is in).

Note that this code snippet is a workaround more than anything, and could break in certain situations. Restarting your mod like this is not the same as restarting the game, as it does not restart game state, so it will not be a clean slate and your mod could potentially behave differently than if you were to restart.

## How to make my mod do things when it's enabled?
Override the `Enable` instance method, for example:
```python
class MyMod(ModMenu.SDKMod):
    ...
    def Enable(self) -> None:
        super().Enable()
        unrealsdk.Log("I ARISE!")
```
`super().Enable()` calls the base class `Enable` method, which registers any hooks or network methods, so you should call that first.

`Log` will log a message to the console. Now when you launch the game and enable your mod you should see "I ARISE!" in the console output. Replace that with whatever you want to do upon enable.

Cleanup functionality can go in the `Disable` instance method:
```python
    def Disable(self) -> None:
        unrealsdk.Log("I sleep.")
        super().Disable()
```
`super().Disable()` calls the base class `Disable` method, which removes any hooks or network methods.

Now when you disable your mod you should see "I sleep." in the console output. Replace that with whatever you want to do upon disable.

A good practice is to restore anything you've changed back to what it was in the `Disable` method.

For other functions you can override, check the `SDKMod` base class, defined in `ModMenu/ModObjects.py` in the Mods folder.

## How to save enabled state?
`SaveEnabledState` allows you to indicate whether your mod should be automatically enabled on subsequent runs if the user enabled it.

Values it can be set to:
* `NotSaved`: The enabled state is not saved.
* `LoadWithSettings`: The enabled state is saved, and the mod is enabled when the mod settings are loaded.
* `LoadOnMainMenu`: The enabled state is saved, and the mod is enabled upon reaching the main menu - after hotfixes are all setup and all the normal packages are loaded.

For example, to set it to `LoadWithSettings` add the following class variable to your mod class:
```python
SaveEnabledState: ModMenu.EnabledSaveType = ModMenu.EnabledSaveType.LoadWithSettings
```
This will save your mod's enabled state in settings.json, and the mod will be enabled when the mod settings are loaded.

## How to add options to the options menu?
Instantiate your options and add them to the `Options` instance variable of your mod class.

See `ModMenu/Options.py` for available option classes you can use.

Here is an example for adding a `Boolean` option:
```python
class MyMod(ModMenu.SDKMod):
    def __init__(self) -> None:
        self.MyBoolean = ModMenu.Options.Boolean(
            Caption="Set My Boolean",
            Description="Whether My Boolean should be on.",
            StartingValue=True,
            Choices=["No", "Yes"]  # False, True
        )
        
        self.Options = [
            self.MyBoolean,
        ]
```

This `Boolean` should now appear in the options menu, under the name of your mod (provided the mod is enabled). You can get the value from it by accessing `self.MyBoolean.CurrentValue`, which, since it's a boolean, will be True or False.

To handle changes to this value in real time, you can override the method `ModOptionChanged`. For example:

```python
    def ModOptionChanged(self, option: ModMenu.Options.Base, new_value) -> None:
        if option == self.MyBoolean:
            if new_value:
                unrealsdk.Log("You turned on My Boolean")
            else:
                unrealsdk.Log("You turned off My Boolean")
```

Note that this function is called before the change to CurrentValue occurred, so we check `new_value` and not `self.MyBoolean.CurrentValue`.

Also note that for backwards-compatibility reasons, upon enable of your mod this function will be called for every option that is not in a `Nested`. Do not rely on this functionality, as it may be removed in future. Logic addressing settings values on startup should be placed in the `Enable` method instead.

You can change the values of options programmatically, but make sure to call `ModMenu.SaveModSettings(mod: ModObjects.SDKMod)` afterwards (passing an instance of your mod, or `self` if called from within your mod class) or the new values will not be updated in the mod's `settings.json`.

## How to add game keybinds?
See `ModMenu/KeybindManager.py`.

Instantiate your keybinds and add them to the `Keybinds` instance variable of your mod class.

Here is an example:

```python
...
def sayHi() -> None:
    unrealsdk.Log("hi")

class MyMod(ModMenu.SDKMod):
    ...
    Keybinds = [
        ModMenu.Keybind("Say hi", "F3", OnPress=sayHi),
    ]
```

Now "hi" will be outputted to the console whenever F3 is pressed while ingame.

Any bindings can be customised by the user in Options > Keyboard / Mouse > Modded Key Bindings.

If the function you give `OnPress` takes an argument, it will be passed a `ModMenu.InputEvent` enum with the input event type, which can be `Pressed` (0), `Released` (1), `Repeat` (2), `DoubleClick` (3), or `Axis` (4). This allows you to perform different actions depending on the input type, which you can use, for instance, to do something while a button is held by watching for `Pressed` and `Released`.

Alternatively, there is also the `ModMenu.SDKMod` method `GameInputPressed(self, bind: ModMenu.Keybind, event: ModMenu.InputEvent)` which you can override. It will be called when any key event is performed on one of the mod's `Keybinds`. Instead of passing an `OnPress` method when you define the `Keybind`, you can perform the associated action in this method instead.

```python
...
class MyMod(ModMenu.SDKMod):
    ...

    HiBind = ModMenu.Keybind("Say hi", "F3")

    Keybinds = [
        HiBind,
    ]

    def GameInputPressed(self, bind: ModMenu.Keybind, event: ModMenu.InputEvent) -> None:
        if bind == self.HiBind and event == ModMenu.InputEvent.Pressed:
            unrealsdk.Log("hi")
```

## How to add mod manager keybinds?
You can have bindings the mod performs when a key is pressed in the mods menu, just like the default `Enable` by pressing `Enter`, by modifying `SettingsInput` instance variable of your mod class. This is a dictionary mapping `key`: `action`, where both are `str`. Handle the different actions by overriding `SettingsInputPressed`. See the `SDKMod` base class in `ModMenu/ModObjects.py`.

Here is an example:

```python
def sayHi() -> None:
    unrealsdk.Log("hi")

class MyMod(ModMenu.SDKMod):
    ...
    SettingsInputs = ModMenu.SDKMod.SettingsInputs.copy()
    SettingsInputs["H"] = "Say hi"
    
    def SettingsInputPressed(self, action: str) -> None:
        if action == "Say hi":
            sayHi()
        else:
            super().SettingsInputPressed(action)
```

Now "hi" will be outputted to the console whenever H is pressed while the mod is selected in the mod manager.

## How to hook into game functions?
You can use the `@Hook` decorator. PythonSDK will handle the registering and removing of hooks itself, so long as you remember to call the base class Enable/Disable if you override those methods.

The function you hook must have the signature:
`([self,] caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct)`

Example:

```python
class MyMod(ModMenu.SDKMod):
    ...
    @ModMenu.Hook("WillowGame.WillowPlayerController.SpawningProcessComplete")
    def onSpawn(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
        unrealsdk.Log("onSpawn called")
        return True
```

If you do not return True the function you hooked into will not continue executing as normal, which is sometimes desired, but if you do not want that remember to return True. If I forget return True in this case, I spawn in a weird place, don't have any money, eridium, or anything in my inventory, among other things, because we diverted the logic ordinarily handling all that.

Alternatively, it is also possible to register hooks manually with `unrealsdk.RunHook(funcName: str, hookName: str, funcHook: object)`, where
* `funcName`: a string of the game function to hook, 
* `hookName`: a name it can be referenced by when you remove it, 
* `funcHook`: the function you want to have called,

*or* `unrealsdk.RegisterHook(..)` (same arguments), 

and remove them with `unrealsdk.RemoveHook(funcName: str, hookName: str)`.

It is preferrable to use `RunHook` over `RegisterHook`, since the former ensures the hook is not registered twice.

## How to know what game objects to modify?
* Look through decompiled UPKs, as explained in the [Writing SDK Mods](#writing-sdk-mods) section.
* Look through objects in BLCMM Object Explorer, and other tools described in the [BLCMods Wiki](https://github.com/BLCM/BLCMods/wiki). There is a guide [here](https://github.com/BLCM/BLCMods/wiki/Tutorial%3A-Getting-Started-Making-Mods#setting-up-blcmm) on how to get object data for Object Explorer, and basic usage.
* Look at the source of existing [PythonSDK Mods]({{ site.baseurl }}{% link mods.md %}).
* Even source of text mods can help, as they can tell you what objects you can modify.

You can discuss what you're trying to do on the [Discord](https://discord.gg/VJXtHvh), and people will probably chime in to help you out!

## How to publish my mod?
Upload your mod(s) to a public repository, then to add it to this site follow the steps on [Adding to the Database](#adding-to-the-database) in the main page.

Note that you should not commit `settings.json` file nor `__pycache__`, as they are automatically generated.
