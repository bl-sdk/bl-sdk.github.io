---
pyproject_url: https://raw.githubusercontent.com/EerieGoesD/borderlands-1-goty-mods/refs/heads/main/GearScore/pyproject.toml
---

Rates every weapon by DPS and shield by Shield Power according to in-game formula, on item cards wherever you see it (character skills not counted).

The number shows on item cards in your backpack, in vending machines, on mission rewards
and on loot lying on the ground. Page Up and Page Down in the backpack shows a DPS page,
listing everything you carry best first.

Weapons: `shots x damage x pellets / (shots x fire interval + reload)`, where shots is
the magazine divided by the ammo each shot costs. Shields:
`capacity + recharge rate x (60 - recharge delay)`. Every number comes off the item
itself, unrounded, so it can differ slightly from the card.

## Settings

- **Disregard Accuracy**: Assumes every bullet hits. Turn it off and the DPS is scaled by the gun's accuracy.
- **Disregard Critical**: Ignores critical hits. Turn it off and the DPS is multiplied by the gun's own critical bonus, as if every shot were a critical.
- **Disregard Elements**: Ignores burn, shock and corrosion. Turn it off and the extra damage an elemental gun throws is added, scaled by its x1 to x4 rating.
- **Score font size**: How big the number is printed on the card.

For full information about this mod and to report bugs, please visit
[eeriegoesd.com/gaming/mods](https://eeriegoesd.com/gaming/mods/).
