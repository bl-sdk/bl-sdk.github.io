---
pyproject_url: https://raw.githubusercontent.com/PANIC-Studios/classic-minimap-bl1/refs/heads/main/classic_minimap/pyproject.toml
mod_categories: ui utility
urls:
  Source and releases: https://github.com/PANIC-Studios/classic-minimap-bl1
---

Classic Minimap adds an on-screen minimap for the original Borderlands 1. It displays vector map detail, hostile markers, vendors and other nearby places, and mission and turn-in cues. Settings include map placement, size, opacity, labels, compass orientation and entity density.

## Navigation and known limitations

Foot and vehicle guidance uses the game's authored navigation graph. **Objective routing is incomplete:** a displayed path can stop before the mission marker when graph connections are missing. A path or bearing is advisory and does not establish physical traversability. Collision-query suitability and vehicle traversal are unqualified.

High entity density is the default and allows more enemy candidates and map-line drawing operations. Select **Map > Entity density > Standard** to reduce the drawing budget. Both settings have finite budgets and may omit items in crowded scenes. High density can increase HUD cost.

The 0.8.1 build was verified offline. In-game startup, callback latency and frame time for this build have not been measured; previous callback measurements exceeded the project's performance targets. Enhanced edition and co-op compatibility are unverified.

## Installation

Install the [BL1 Python SDK]({{ "/willow1-mod-db/" | relative_url }}), close the game, then place `classic_minimap.sdkmod` in the game's `sdk_mods` folder. Restart the game and enable the mod from the Mods menu. Back up any existing minimap archive before replacing it.

## Images

![Historical in-game screenshot of the minimap showing a Medical vendor and area exit]({{ "/assets/mods/willow1/classic_minimap/historical-ingame-dev45.png" | relative_url }})

*In-game screenshot from the earlier 0.8.0.dev45 build; it is not a native screenshot of 0.8.1.*

![Offline rendering of minimap layouts, labels and guidance in several scenes]({{ "/assets/mods/willow1/classic_minimap/offline-hud-preview-081.png" | relative_url }})

*0.8.1 offline rendering harness with synthetic places and approximate fonts; not an in-game screenshot.*
