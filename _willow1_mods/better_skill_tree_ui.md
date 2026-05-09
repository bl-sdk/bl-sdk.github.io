---
pyproject_url: https://raw.githubusercontent.com/Ry0511/my_bl1_sdk_mods/refs/heads/master/src/py/skill_tree_tweaks/pyproject.toml
download: https://github.com/Ry0511/my_bl1_sdk_mods/raw/refs/heads/master/packaged/skill_tree_tweaks-1.0.zip
---

> ***INFO*** - This is an SDK and UPK mod you need to install both components for the mod to function correctly. (see:
> Installation for more information)

Improves the skill tree UI by highlighting skills affected by class mods and clearly displaying
their adjusted values.

## Changes

The skill tree information panel now contains colour-coded text to indicate the current and next state of the skill.
Below is a table of the possible colour codings.

| Indicator                                                   | Description                                                                             |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <span style="color: #F4D35E;">Current Grade (Yellow)</span> | The skill is partially invested into                                                    |
| <span style="color: #23CE6B;">Current Grade (Green)</span>  | The skill is fully invested into                                                        |
| <span style="color: #EF3054;">Current Grade (Red)</span>    | Skill is augmented but has not been invested into; warns you that the skill is inactive |
| <span style="color: #0ACDFF;">Next Grade (Blue/Cyan)</span> | Next grade text, only visible if the skill is not fully invested into                   |

> Augmented skills should have a Cyan icon similar to other games - however depending on what mods you have installed
> this icon might not be visible. The above text based changes are agnostic of the ui changes and should always be there.

## Credits

Big thanks to sleepmaster for his awesome work on the flash file changes!

## Installation

1. Download the mod via the 'Download' button on this page
2. Extract the downloaded zip file into your `sdk_mods` directory
3. Extract the `skill_tree_tweaks/custom_ui_full.zip` to your games base directory i.e., `...\Borderlands` (the
   directory containing the WillowGame folder)
4. If you don't get a 'Replace Files' prompt, you installed it incorrectly.