---
nav_order: 2
---
# Getting Started

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

