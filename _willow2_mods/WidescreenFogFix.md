---
pyproject_url: https://raw.githubusercontent.com/lumi-fiona/bl2-widescreen-fog-fix/main/widescreen_fog_fix/pyproject.toml
---

# Widescreen Fog Fix

Keeps the fog, haze and atmosphere at any field of view on ultrawide and super ultrawide screens.

On a screen wider than 16:9, Borderlands 2 stops drawing a map's height fog on the ground once the
FOV gets high enough, and the game suddenly looks crisp and flat. The sprint zoom (and vehicle boost)
widens the view too, so the fog pops in and out while you run. This is the "sky darkens / fog
disappears when sprinting on 21:9" bug, and the usual advice was to lower the FOV to 108.

| Screen | Fog disappears above (FOV slider) |
|---|---|
| 32:9 (3840×1080, 5120×1440) | 107.4 |
| 21:9 (2560×1080, 3440×1440) | about 125.5 |
| 16:9 | about 136, which the menu doesn't reach |

With this mod enabled the fog stays at any FOV the game or an FOV mod can reach.

### How it works

The engine draws height fog as one full-screen quad at the view depth
`max(30, FogMinStartDistance) × Ratio`, where `Ratio = 1 / sqrt(1 + tanH² + tanV²)`. Once that depth
drops below the 10-unit near clip plane, the whole quad is clipped and no geometry gets fog. That
happens when the corner of the view is more than 3 times farther away than its centre. The mod points
the single instruction that loads the `30.0` at the game's own `100.0` constant instead. That moves
the cut-off far beyond any usable FOV, and fog only starts a metre or two in front of the camera,
where it's zero anyway.

Only the game's memory changes while it runs. The exe on disk is never touched, and disabling the mod
puts the game's value back straight away. It's client-side rendering only, so it's fine in co-op. It
targets the current Steam build and does nothing, with a log message, on any other build.

More detail, including a hex edit for people without the SDK, is in the
[README](https://github.com/lumi-fiona/bl2-widescreen-fog-fix#readme).
