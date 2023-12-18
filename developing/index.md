# Developing SDK Mods
Work in progress

## Setting up your Workspace
The first thing to do when getting started is setting up your workspace so you can see all the raw
python source files (and so your IDE can parse them). Mods are generally released as a single
`.sdkmod` file, since this helps prevent a lot of mistakes casual users might make while installing,
but this is unsuitable for development. `.sdkmod` files are all just renamed zips, open them in any
archive program and extract the inner folders into your `sdk_mods` dir - go from
`sdk_mods/my_mod.sdkmod/my_mod/*` to just `sdk_mods/my_mod/*`. Note that if you have both an
extracted folder and a `.sdkmod`, the folder takes priority.

The next thing to setup is the stub files for the sdk's embedded modules - your IDE obviously won't
be able to find any source files. Point your IDE at the the `.stubs` folder:
- In vscode, add to the `python.analysis.extraPaths` option.

After finishing setting up, try take a quick read through the base sdk mod files and the stubs. They
are all filled with all sorts of type hints and docstrings, which should help explain a lot about
how the SDK works.

## Debugging
Print debugging's fun and all, but for proper dev work you need to get a real debugger set up. The
SDK comes with some integration with [debugpy](https://github.com/microsoft/debugpy).

1. Downloading the latest version of debugpy, and extract it into the `sdk_mods` folder such that
   it's importable. The initialization script will attempt to import it and start a listener
   automatically.

2. Define the environment variable `PYUNREALSDK_DEBUGPY`. This is easiest done by appending to the
   `unrealsdk.env` file in the plugins folder. You will still be able to attach without doing this,
   however breakpoints won't work across threads, only explicit `breakpoint()` calls.

3. Launch the game, then you can attach to a remote debugging session on `localhost:5678`:
   - In vscode, use the `Python: Remote Attach` template.

If you need to debug something during startup, add a `debugpy.wait_for_client()` call. Note that the
SDK initialization runs in it's own thread, the game will still start normally, this only blocks the
SDK.

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
License<sup>3</sup>         | `license`         | `tool.sdkmod.license`, `project.license.text`<sup>4</sup>
Requirements                | `dependencies`    | `project.dependencies`
Misc URLs<sup>5</sup>       | `urls`            | `project.urls`
Download Link               | `download`        | `tool.sdkmod.download`
Description                 | The page contents | `project.description`<sup>6</sup>

<sup>1</sup> Multiple authors are concatenated in the order given.    
<sup>2</sup> An array of strings, with valid values of `BL3` and `WL` (case insensitive). If not
             given, defaults to all games.    
<sup>3</sup> A table with keys `name` and `url`. Prefer linking to a summary site, rather than
             direct to your `LICENSE`.    
<sup>4</sup> Used as the name, with no url.    
<sup>5</sup> A dict where keys are the names and values are the urls.    
<sup>6</sup> HTML tags are stripped, rather than just being escaped.    
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
