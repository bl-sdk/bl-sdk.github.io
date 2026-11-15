---
pyproject_url: https://raw.githubusercontent.com/Kakuyamii/bl1-sliding-mod/main/Sliding/pyproject.toml
mod_categories: gameplay
---

# Sliding

Adds Borderlands 3-style sliding to Borderlands 1. 
Crouch while sprinting to drop into a slide.
Jump while sliding to keep the momentum.
Slide into enemies to deal melee damage; works with skills.

## Settings

- **Slide mechanic**: configurable slide speed and deceleration, so you can
  make slides long and fast or short and snappy.
- **Slope physics**: slide faster downhill and slower uphill, with an
  adjustable influence slider (0-300%).
- **Slide melee**: melee hits while sliding deal adjustable damage, from 0% to
  500% of normal.
- **Camera effects**: FOV boost and camera tilt while sliding, which can be
  switched off.
- **Visible legs**: your legs appear in first person while sliding (Lilith, Roland, mordecai and
  Brick are all supported).
- **Slide sound**: terrain-aware slide audio with volume and pitch-variation
  sliders.
- **Particles**: slide particle effects with adjustable density and size.
- **Debug tool**: optional on-screen slide info, logging and diagnostic dumps
  for bug reports.

## Notes

- Borderlands 1 only. Not tested in Borderlands 1 Enhanced.
- The mod bundles a `.upk` for the leg meshes and extracts it to a
  `Sliding_assets` folder next to your SDK settings. The optional debug tool
  writes to `Sliding_diagnostics`.
- Multiplayer was not tested yet. If issues arise, report them.
- Credits: Movement Speed Changer by eeriegoesd (GPL-3.0-or-later).
- Source code and bug reports:
  [GitHub](https://github.com/Kakuyamii/bl1-sliding-mod)
