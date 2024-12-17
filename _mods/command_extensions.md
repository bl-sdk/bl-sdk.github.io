---
pyproject_url: https://raw.githubusercontent.com/apple1417/willow2-sdk-mods/master/command_extensions/pyproject.toml
---
# Command Extensions
Adds a few new console commands, and provides functionality for other mods to do the same. All these
commands are fully compatible with blcmm files, you can just put them in your mod and have users
merge it with other files and enable/disable various categories and it all just keeps working fine.

[See here for info on the builtin commands and how to write mods using them.](https://github.com/apple1417/willow2-sdk-mods/blob/master/command_extensions/Writing-Mods.md)

### Coop Support
Coop support largely depends on the exact mod making use of this. Command Extensions itself runs
completely client slide, but specific mods may have more in depth requirements. Some commands are
simply incompatible with multiplayer, so anything relying on them too much will not work. Like
always, it's best practice to make sure all players run the exact same set of mods.

### Why does it take longer to `exec` my mods now?
This mod has to look through your mod file to handle the extra commands. This has to be done before
the game looks through it, which just takes some extra, unavoidable, time. You can speed it up by
making your mod file smaller - enable structural edits then delete any categories you don't have
enabled (and won't suddenly re-enable soon).
