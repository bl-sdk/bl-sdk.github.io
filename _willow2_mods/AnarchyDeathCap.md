---
pyproject_url: https://raw.githubusercontent.com/renard162/borderlands_sdk_mods/refs/heads/master/AnarchyDeathCap/pyproject.toml
---
Limits Anarchy stack loss on death for the Mechromancer, allowing players to maintain Anarchy-focused builds without interfering with normal gameplay flow.

Anarchy stacks are also preserved when quitting the game, preventing unintended losses outside of combat.

By default, the stack loss limitation requires points in Rational Anarchist, keeping the behavior tied to skill investment. This requirement can be disabled through the mod options.

When the player has points in Rational Anarchist and respawns with fewer than 25 Anarchy stacks, stacks are reset to 0, since rebuilding Anarchy is faster and more consistent from zero than from low values.

Mod options dynamically update the Rational Anarchist skill description, ensuring that the in-game text always reflects the current configuration.

All behaviors provided by this mod can be fully configured through the in-game mod options menu.
