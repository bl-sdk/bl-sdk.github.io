---
has_children: true
---

# Developing SDK Mods
Work in progress

## Setting up your Workspace
1. Create a new folder to develop your mods within. The mod manager supports loading from multiple
   mods folders, so you can keep the mods you're developing separate.

2. Open up `OakGame\Binaries\Win64\Plugins\unrealsdk.env`, and add the following lines:
   - ```ini
     MOD_MANAGER_EXTRA_FOLDERS=["C:\\path\\to\\new\\mod\\folder"]
     ```
     This is a json list of paths to extra mod folders, you can append more - though note it must
     stay on a single line.
   
   - ```ini
     UNREALSDK_LOG_LEVEL=DWRN
     ```
     This sets the default log level to developer warning. This will print some extra log messages
     to console, which are relevant for developers, but which we don't want normal users to worry
     over.
   
   - ```ini
     PYUNREALSDK_DEBUGPY=1
     ```
     This enables [debugpy](https://github.com/microsoft/debugpy) support, which will let you
     properly attach a debugger.
   
   You may also want to modify `PYUNREALSDK_PYEXEC_ROOT` to point at your mod folder. This will let
   you run `C:\path\to\new\mod\folder\test.py` using simply `pyexec test.py`.
   
   Note that the mod manager download contains this file, so when updating you need to be careful
   not to overwrite it/to restore it afterwards.

3. Download the latest version of debugpy, and extract to one of your mods folders such that it's
   importable. The mod manager initialization script will automatically import it and start a
   listener.

4. Extract the default `.sdkmod`s, so you can see all the raw python source files (and so your IDE
   can parse them).
   
   Mods are generally released as a single `.sdkmod` file, since this helps prevent a lot of
   mistakes casual users might make while installing, but this is unsuitable for development.
   
   `.sdkmod` files are all just renamed zips, open them in any archive program and extract the inner
   folders back into the mods folder - go from `sdk_mods/my_mod.sdkmod/my_mod/*` to just
   `sdk_mods/my_mod/*`.
   
   Note that if you have both an extracted folder and a `.sdkmod` with the same name, the folder
   takes priority.

5. Point your IDE at the other mods folders, so it can follow imports. This should be the base
   `sdk_mods` folder, and the `sdk_mods/.stubs` folder for the native modules.

   - In vscode, add to the `python.analysis.extraPaths` option.

6. Configure your debugger for remote debugging, attaching to `localhost:5678`.

   - In vscode, use the `Python: Remote Attach` template.

   After doing this, launch the game and make sure you can attach.

After finishing setting up, try take a quick read through the base sdk mod files and the stubs. They
are all filled with all sorts of type hints and docstrings, which should help explain a lot about
how the SDK works.

## Experimenting Using the Console
When you start experimenting with a concept, it's easier to work in console than it is to write a
full mod. The SDK registers two custom console commands:

`py` lets you run small snippets of python. By default, it executes one line at a time, stripping
any leading whitespace.
```py
py from mods_base import get_pc
py pc = get_pc()
py print(pc)
```

You can also use heredoc-like syntax to execute multiline queries. This happens if the first two
non-whitespace characters are `<<` (which is invalid python syntax for a single line).
```py
py << EOF
is_hostile = get_pc().GetTeamComponent().IsHostile
for pawn in unrealsdk.find_all("OakCharacter", exact=False):
    if not is_hostile(pawn):
        print(pawn)
EOF
```

`pyexec` is useful for more complex scripts - it executes an entire file, relative to the location
set in `PYUNREALSDK_PYEXEC_ROOT` previously. Note that this is *not* running a python script in the
traditional sense, it's instead more similar to something like `eval(open(file).read())`. The
interpreter is not restarted, and there's no way to accept arguments into `sys.argv`.

## Adding to the Mod DB
The DB primarily sources info from your mod's `pyproject.toml`. With a well configured pyproject,
all you need to do is point the DB at it, and everything will be extracted automatically. To do
this, add a file for your mod to the `_mods/` dir of this repo, and add the front matter variable
`pyproject_url`, pointing at an auto updating link.

```md
---
pyproject_url: https://raw.githubusercontent.com/apple1417/oak-sdk-mods/master/abcd/pyproject.toml
---
```

You can overwrite your mod's description simply by adding some extra content to the page. You can
use this to embed images or videos, which wouldn't be suitable for the in-game mod description.

You can overwrite some of the other info on the page by setting various front matter variables.

Field                       | Front matter      | `pyproject.toml`
----------------------------|-------------------|-------------
Title                       | `title`           | `tool.sdkmod.name`, `project.name`
Author(s)                   | `author`          | `project.authors[n].name`<sup>1</sup>
Latest Version              | `version`         | `tool.sdkmod.version`, `project.version`
Supported Games<sup>2</sup> | `supported_games` | `tool.sdkmod.supported_games`
Coop Support                | `coop_support`    | `tool.sdkmod.coop_support`
License<sup>4</sup>         | `license`         | `tool.sdkmod.license`, `project.license.text`<sup>5</sup>
Requirements                | `dependencies`    | `project.dependencies`
Misc URLs<sup>6</sup>       | `urls`            | `project.urls`
Download Link               | `download`        | `tool.sdkmod.download`
Description                 | The page contents | `project.description`<sup>7</sup>

<sup>1</sup> Multiple authors are concatenated in the order given.    
<sup>2</sup> An array of strings, with valid values of `BL3` and `WL` (case insensitive). If not
             given, defaults to all games.    
<sup>3</sup> One of `Unknown`, `Incompatible`, `RequiresAllPlayers`, or `ClientSide`. Defaults to
             unknown.    
<sup>4</sup> A table with keys `name` and `url`. Prefer linking to a summary site, rather than
             direct to your `LICENSE`.    
<sup>5</sup> Used as the name, with no url.    
<sup>6</sup> A dict where keys are the names and values are the urls.    
<sup>7</sup> HTML tags are stripped, rather than just being escaped.    
{: .fs-2 }

### Updating Info
While this site is statically generated, every time a mod page is loaded it fetches the pyproject
and updates the page with any changes, the values fetched when the site is generated are only used
as defaults (note that front matter overrides still take priority). This means you generally don't
need to touch the db again, changes will be picked up automatically.

There are a few exceptions to this, which are not automatically updated:
- The title used in the sidebar and tab title (the header on the mod page does get updated).
- `project.name`, which is used for matching dependencies to their mod page.
- The data powering the searchbar.
- The fields which are always displayed will not be set to unknown if you completely delete their
  section in your pyproject, the old data is preferred. Requirements and Misc URLs are already
  hidden when not in use, so the updates *will* delete them.

If you make significant changes to your pyproject, it may be worth kicking off another build to
update the static versions of these. Do note that this data is updated anytime the site is
generated, someone else adding an unrealated mod will update yours.
