---
pyproject_url: https://raw.githubusercontent.com/Ry0511/my_bl1_sdk_mods/refs/heads/master/src/py/skill_tree_tweaks/pyproject.toml
---

Improves the skill tree UI by highlighting skills affected by class mods and clearly displaying
their adjusted values.

## Changes

> NOTE: Installation no longer requires the manual `.upk` file changes - you can install the same as any other `.sdkmod`

The skill tree information panel now contains colour-coded text to indicate the current and next state of the skill.
Below is a table of the possible colour codings.

| Indicator                                                   | Description                                                                             |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <span style="color: #F4D35E;">Current Grade (Yellow)</span> | The skill is partially invested into                                                    |
| <span style="color: #23CE6B;">Current Grade (Green)</span>  | The skill is fully invested into                                                        |
| <span style="color: #EF3054;">Current Grade (Red)</span>    | Skill is augmented but has not been invested into; warns you that the skill is inactive |
| <span style="color: #0ACDFF;">Next Grade (Blue/Cyan)</span> | Next grade text, only visible if the skill is not fully invested into                   |

> Augmented skills should have a Cyan icon similar to other games - however depending on what mods you have installed
> this icon might not be visible. The above text based changes are agnostic of the ui changes and should always be
> there.

## Credits

Big thanks to sleepmaster for his awesome work on the flash file changes!
