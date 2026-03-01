---
nav_order: 1
---

# Developing SDK Mods
{:.no_toc}

Work in progress

### Table of Contents
{:.no_toc}
- toc
{:toc}

## Setting up your Workspace
1. Create a new folder to develop your mods within. The mod manager supports loading from multiple
   mods folders, so you can keep the mods you're developing separate.

2. Create a new file `unrealsdk.user.toml` in the game's `Plugins` folder, and add the following
   content:

   ```toml
   [unrealsdk]
   console_log_level = "DWRN"

   [pyunrealsdk]
   # pyexec_root = "C:\\path\\to\\new\\mod\\folder"

   [mod_manager]
   extra_folders = [
      "C:\\path\\to\\new\\mod\\folder"
   ]
   ```

   - `unrealsdk.console_log_level`

     This sets the default log level. Setting it to `DWRN`, developer warning, will print some extra
     log messages to console, which are relevant for developers, but which we don't want normal
     users to worry over.

   - `pyunrealsdk.pyexec_root`

     Changes the root directory used when running `pyexec` commands. You may want to redirect this
     to your new folder, so you can run files within it directly.

   - `mod_manager.extra_folders`

     This is a list of extra mod folders, which lets you keep your development folder separate from
     other mods.

3. Extract the default `.sdkmod`s, so you can see all the raw python source files (and so your IDE
   can parse them).

   Mods are generally released as a single `.sdkmod` file, since this helps prevent a lot of
   mistakes casual users might make while installing, but this is unsuitable for development.

   `.sdkmod` files are all just renamed zips, open them in any archive program and extract the inner
   folders back into the mods folder - go from `sdk_mods/my_mod.sdkmod/my_mod/*` to just
   `sdk_mods/my_mod/*`.

   Note that if you have both an extracted folder and a `.sdkmod` with the same name, the folder
   takes priority.

4. Point your IDE at the other mods folders, so it can follow imports. This should be the base
   `sdk_mods` folder, and the `sdk_mods/.stubs` folder for the native modules.

   - In vscode, add to the `python.analysis.extraPaths` option.
   - For pyright, add to the `tool.pyright.extraPaths` array.

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
set in `pyunrealsdk.pyexec_root` previously. Note that this is *not* running a python script in the
traditional sense, it's instead more similar to something like `eval(open(file).read())`. The
interpreter is not restarted, and there's no way to accept arguments into `sys.argv`.

## Better Debugging Tools

{: .note }
The following features aren't yet fully available across all games.

The mod manager has integrations with a few third party tools, which give a better debugging
experience than just using console and print statements.

The recommended way to get started is to
[create a virtual environment](https://docs.python.org/3/library/venv.html), ideally using the exact
same Python version, and architecture (32 vs 64-bit) as the SDK. Then add the path to it's
`site-packages` folder to your `unrealsdk.user.toml`:

```toml
[mod_manager]
extra_sys_path = [
   "C:\\path\\to\\.venv\\Lib\\site-packages",
]
```

This may not work if using Proton on Linux, if the specific tool relies on Windows libraries.
Everything should still work if you manually download Windows packages, as long as you put them
somewhere importable from inside the game's Python instance.

### debugpy
[debugpy](https://github.com/microsoft/debugpy) is a generic python debugger - it's what gives you
breakpoints. It implements the standard Debug Adaptor Protocol, so should work with most IDEs.

1. Install it inside your venv using `pip install debugpy`. As long as it's importable, the sdk will
   automatically start a server on launch.

2. Add the following to your `unrealsdk.user.toml`:

   ```toml
   [pyunrealsdk]
   debugpy = true
   ```

   This enables debugpy compatibility in `pyunrealsdk` itself - without this breakpoints won't
   always trigger.

3. Configure your debugger for remote debugging, attaching to `localhost:5678`.

   - In vscode, use the `Python: Remote Attach` template.

4. Restart the game, add some breakpoints, and confirm you can hit them.

   If you cannot hit breakpoints, try call the `breakpoint()` function. If this works, then you have
   a source mapping issue.

### IPython / Jupyter
[IPython](https://ipython.org/) is a better interactive Python console, which spawned the Jupyter
project. Even if you don't care about notebooks, the IPython console is a much more friendly
replacement for `py`/`pyexec` commands. The mod manager can launch an IPython kernel, which you
should be able to attach to from any Jupyter client.

1. Install it inside your venv using `pip install ipykernel`. Note this also installs debugpy as a
   dependency.

   If you don't already have another preferred jupyter client, also run `pip install jupyter`.

2. Restart the game. On launch, it should print something like the following to console:
   ```
   Started ipykernel server
   To connect another client to this kernel, use:
       --existing kernel-19212.json
   ```

3. Connect to the existing kernel in your preferred client.

   For example, using the basic console client, run:
   ```sh
   jupyter console --existing kernel-19212.json
   ```

   You are able to connect multiple clients to the same game instance.

When closing a client, make sure to use `exit(keep_kernel=True)` or `quit(keep_kernel=True)`.
Forgetting this means it will also close the kernel, and prevent re-connecting until you restart the
game.

Stdout/stderr can behave oddly at times, since both `ipykernel` and `pyunrealsdk` try redirect it.
In your mods, if you want to write to console, it's best practice to use the `unrealsdk.logging.*`
functions, which write directly to console/the log file without going through stdout.

## Adding to the Mod DB
The DB primarily sources info from your mod's `pyproject.toml`. With a well configured pyproject,
all you need to do is point the DB at it, and everything will be extracted automatically.

To add your mod, you'll need to add a markdown file to one of the `_*_mods` folders in
[this site's repo](https://github.com/bl-sdk/bl-sdk.github.io).

### Simplest Configuration
The simplest possible file is the following. Make sure the url points at an auto-updating link,
instead of a specific commit.

```md
---
pyproject_url: https://raw.githubusercontent.com/apple1417/oak-sdk-mods/master/abcd/pyproject.toml
---
```

### More Detailed Customization
Now the simplest config copies everything straight from the `pyproject.toml`. You may want to
customize it further - e.g. you may want a more detailed description, adding images and/or videos.

You can overwrite your mod's description simply by adding extra markdown to the end of the page.

```md
---
pyproject_url: https://raw.githubusercontent.com/apple1417/oak-sdk-mods/master/abcd/pyproject.toml
---

# My cool mod
Look at this image:
![alt text](/assets/mods/oak/abcd/some_image.png)
```

Jekyll uses [kramdown](https://kramdown.gettalong.org/syntax.html), which may support some extra
syntax than what you're used to.

In addition to those, there are two bits of the templating system you should probably know about:

- When linking to something that's part of the site, whether an image or another page, prefer using
  {% raw %}`{{ "/path/to/file.txt" | relative_url }}`{% endraw %}. This ensures the link will get
  updated correctly if hosted under another url.

- If you want to embed a youtube video, prefer using
  {% raw %}`{% youtube https://www.youtube.com/watch?v=dQw4w9WgXcQ %}`{% endraw %}.

Now the above lets you customize the description, but there's still all the other info above it.
You can overwrite these by setting front matter variables. If you're not familiar with Jekyll, the
"front matter" is a block of YAML configuration inbetween triple dashes at the top - you used it
previously to set the `pyproject_url`.

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
Redirects<sup>8</sup>       | `redirect_from`   | Not supported

<sup>1</sup> Multiple authors are concatenated in the order given.    
<sup>2</sup> An array of strings. If not given, defaults to all games for the category you're in.    
<sup>3</sup> One of `Unknown`, `Incompatible`, `RequiresAllPlayers`, or `ClientSide`. Defaults to
             unknown.    
<sup>4</sup> A table with keys `name` and `url`. Prefer linking to a summary site, rather than
             direct to your `LICENSE`.    
<sup>5</sup> Used as the name, with no url.    
<sup>6</sup> A dict where keys are the names and values are the urls.    
<sup>7</sup> HTML tags are stripped, rather than just being escaped.    
<sup>8</sup> An array of relative urls to redirect to this page - i.e. if you moved your mod, it's
             old urls. See also
             [`jekyll-redirect-from`](https://github.com/jekyll/jekyll-redirect-from#usage).    
{: .fs-2 }

### Updating Info
While this site is statically generated, every time a mod page is loaded it fetches the pyproject
and updates the page with any changes, the values fetched when the site is generated are only used
as defaults (note that front matter overrides still take priority). This means you generally don't
need to touch the db again, changes will be picked up automatically.

There are a few exceptions to this, which are not automatically updated:
- The title used in the sidebar and tab title (the header on the mod page does get updated).

- `project.name`, which is used for matching dependencies to their mod page.

- The dependencies displayed on the missing requirements page.

- The data powering the searchbar.

- The fields which are always displayed (e.g. Title, Author) will not be set to unknown if you
  completely delete their section in your pyproject, the old data is preferred.
  
  Requirements and Misc URLs are already hidden when not in use, so the updates *will* delete them.

If you make significant changes to your pyproject, it may be worth kicking off another build to
update the static versions of these. Do note that this data is updated anytime the site is
generated, someone else adding an unrealated mod will update yours.

## Handling Missing Requirements
It's recommended to put dependency version checks right at the top of your main `__init__.py`, to
make sure your mod only loads if everything is present, and to give users more helpful error
messages.

One simple way of doing this is using asserts and `__import__`:
```py
if True:  # avoids E402
    assert __import__("mods_base").__version_info__ >= (1, 4), "Please update the SDK"
    assert __import__("pyunrealsdk").__version_info__ >= (1, 3, 0), "Please update the SDK"
    assert __import__("unrealsdk").__version_info__ >= (1, 3, 0), "Please update the SDK"
    assert __import__("ui_utils").__version_info__ >= (1, 0), "Please update the SDK"

    from mods_base import Game

    assert Game.get_current() == Game.BL3, "The Hunt Tracker only works in BL3"
```

It's easiest to set your required versions to be >= the version you're currently developing with,
rather than searching through history to find the oldest possible compatible one.

Now asserts make for nice and simple code, but not all users check console before going out and
complaining. As an alternative, you can open a page in their browser instead - this site provides
two for that purpose.

- [{{ "oak-mod-db/requirements?mod=my_mod" | absolute_url }}]({{ "oak-mod-db/requirements?mod=my_mod" | absolute_url }})
- [{{ "oak2-mod-db/requirements?mod=my_mod" | absolute_url }}]({{ "oak2-mod-db/requirements?mod=my_mod" | absolute_url }})
- [{{ "willow1-mod-db/requirements?mod=my_mod" | absolute_url }}]({{ "willow1-mod-db/requirements?mod=my_mod" | absolute_url }})
- [{{ "willow2-mod-db/requirements?mod=my_mod" | absolute_url }}]({{ "willow2-mod-db/requirements?mod=my_mod" | absolute_url }})

```py
try:
    assert __import__("mods_base").__version_info__ >= (1, 5), "Please update the SDK"
except (AssertionError, ImportError) as ex:
    import webbrowser
    webbrowser.open("{{ "willow2-mod-db/requirements?mod=my_mod" | absolute_url }}")
    raise ex
```

The `?mod=` query parameter should be set to your mod's `project.name`.

As mentioned above, anything in `project.dependencies` is shown as a requirement on the mod page. If
you want to require a particular version of the sdk, you can add a dependency on `oak_mod_manager`,
`oak2_mod_manager`, `willow1_mod_manager`, or `willow2_mod_manager` (as appropriate).

```toml
[project]
dependencies = [
  'oak_mod_manager >= 1.2',
]
```
Since requiring the sdk is somewhat implicit, it remains to be seen if the possible future package
manager will need this.
