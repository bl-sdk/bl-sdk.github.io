---
pyproject_url: https://raw.githubusercontent.com/Squ1ggs/Bl4SDKmods/refs/heads/main/bl4_character_swapper/pyproject.toml
mod_categories: gameplay ui
---

# BL4 Character Swapper

Swap your character's appearance to native BL4 hunters, NPCs, enemies and bosses.
Search the catalog, preview a character, apply it and restore your original body.
This is a standalone SDK mod: Squ1ggs Boosting Tools is not required.

**BLImGui is strongly recommended.** Press **F10** for the searchable picker,
character groups, target selection and preview/apply/restore controls. The
swapper supports both official BLImGui windows and compatible customised tab
menus. Without BLImGui, use the SDK console and type `asw_help`.

- [Recommended official BLImGui 1.1 download](https://github.com/juso40/blimgui/raw/ff5be35f41d69f28056befdd1bfb8caddae5892b/blimgui.zip)
- [Official BL4 BLImGui installation instructions]({{ "/oak2-mod-db/mods/blimgui/" | relative_url }})
- [Author's repository](https://github.com/Squ1ggs/Bl4SDKmods)

Extract BLImGui into `sdk_mods/blimgui`, preserving its supplied `dist64`
dependencies. Do not create a second nested `blimgui` folder. A separate system
Python or `pip` installation is not required.

Place `bl4_character_swapper.sdkmod` directly in `sdk_mods`, then enable
**BL4 Character Swapper**. Do not enable both an archive and a loose copy.

**Already using Squ1ggs Boosting Tools?** Character swapping is included in its
**Appearance** tab. Desktop users do not need this standalone package or BLImGui.

Host authority is required for previews and selected-player changes. Characters
must be available in the installed game content. Vehicle swaps and foreign-game
characters are excluded. Catalog inclusion is not a tested-model claim. Live
preview/apply/restore, respawn/travel behavior and multiplayer visibility are
not verified for every catalog entry.
