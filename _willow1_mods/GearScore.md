---
pyproject_url: https://raw.githubusercontent.com/EerieGoesD/borderlands-1-goty-mods/refs/heads/main/GearScore/pyproject.toml
mod_categories: gear ui
---

Rates every weapon by DPS and shield by Shield Power according to in-game formula, on item cards wherever you see it (character skills not counted).

The number shows on item cards in your backpack, in vending machines, on mission rewards
and on loot lying on the ground. Page Up and Page Down in the backpack shows a DPS page,
listing your guns best first.

Weapons: `shots x damage x pellets / (shots x fire interval + reload)`, where shots is
the magazine divided by the ammo each shot costs. A gun whose bullets swing on their
way, such as the Madjack, is scaled down by how much of the flight the bullet spends
inside a human-sized body, when Disregard Zig-Zag Bullets is on. Shields:
`capacity + recharge rate x (breather - recharge delay)`, with the recharge part never
more than the capacity. Every number comes off the item itself, unrounded, so it can
differ slightly from the card.

## Settings

- **Disregard Accuracy**: Assumes every bullet hits. Turn it off and the DPS is scaled by the gun's accuracy.
- **Disregard Critical**: Ignores critical hits. Turn it off and the DPS is multiplied by the gun's own critical bonus, as if every shot were a critical.
- **Disregard Elements**: Ignores burn, shock and corrosion. Turn it off and the extra damage an elemental gun throws is added, scaled by its x1 to x4 rating.
- **Disregard Zig-Zag Bullets**: Scores guns whose bullets swing on their way, such as the Madjack, by how often those bullets can hit, which puts them near the bottom. Turn it off and they score as if every shot lands.
- **Compare vs current gear**: Off by default. Adds indicators under the score comparing the gun vs the guns you carry, equipped and in your backpack: your best overall (All), of the same weapon type (Type), of the same element (Element, or No Elem for guns without one), and of both (Both). + is your best, - is worse than your best, = is the same as your best.
- **Score font size**: How big the number is printed on the card.
- **Score Shields**: Shows Shield Power on shield cards. Turn it off and shields get no score, and Clean Up leaves them alone.
- **Breather Seconds**: How many seconds you expect to be out of fire between bursts in a fight. Shield Power is the shield's capacity plus whatever it recharges in that time, after its recharge delay, and never more than one full bar. At 0 shields are rated by capacity alone.
- **Clean Up Inventory**: Drops every shield but the one with the highest Shield Power, every class mod but the most expensive one, and every gun that is not your best of its type, its element, or both. Equipped items count too. Class mods for other characters are dropped. Anything your level is too low for is neither counted nor dropped. Grenade mods are left alone.
