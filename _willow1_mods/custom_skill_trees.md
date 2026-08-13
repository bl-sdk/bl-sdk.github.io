---
pyproject_url: https://raw.githubusercontent.com/Ry0511/my_bl1_sdk_mods/refs/heads/master/src/py/custom_skill_trees/pyproject.toml
---

- supports `Skill Randomizer`
- supports `Skilltree UI Fix` `>= v1.3`

# For Users

You can customise the skill tree using the spinner options, though this is slow and error-prone. The better solution is
to use a preset file which is a list of skills in a `.txt` file. These files should be placed into  
`Borderlands\sdk_mods\settings\custom_skill_trees\presets` whenever you run the mod it will create an `example.txt` file
which shows the structure of the file.

> Backup your saves if you do not want to risk anything getting broken!

> Live edits to the player skill tree are naturally volatile - prefer doing it in the main menu to avoid issues.

# For Modders

This provides an interface for interacting with the skill tree letting you embed custom flash content without needing to
touch the main flash file. Biggest benefit here is that the edits are hot reloaded live so do not require a game restart
or anything on your end other than modifying your custom `.swf` file.

## Example

Minimal usage example for registering a skill definition to a custom flash file - note the module path + flash file is
because both directory and .sdkmod archives are supported.

```py
from custom_skill_trees import FlashContent, add_custom_skill
add_custom_skill(
    skill_path="path.to.skill.definition",
    flash=FlashContent("your_mod.assets", "your_flash.swf"),
    is_kill_skill=False,
)
```

A more comprehensive example can be found
in: [Metal Storm 2.0 Mod](https://github.com/Ry0511/my_bl1_sdk_mods/tree/539f7cb4d2e66045e967e136597f0d6a3e217914/src/py/example_skill_tree)