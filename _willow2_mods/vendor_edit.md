---
pyproject_url: https://raw.githubusercontent.com/apple1417/willow2-sdk-mods/master/vendor_edit/pyproject.toml
---

Lets you edit all your gear while in game. Get started by looking at it in your inventory.

<video width="100%"
    muted autoplay loop playsinline
    disablepictureinpicture disableremoteplayback
    poster="{{ "/assets/mods/willow2/vendor_edit/demo.jpeg" | relative_url }}"
    src="{{ "/assets/mods/willow2/vendor_edit/demo.webm" | relative_url }}"
></video>

Has full mod support, including introducing a way to share modded item codes.

For example, try this one when running [BL2 Exodus]({{ "/willow2-mod-db/mods/bl2exodus/" | relative_url }}):
```
BL2MODDED[hwAAAABZMgCA5v//A6HVxmIIxPD/HwGDIQYIDBMY/v///0/D8A==|AHj5icHRieNCzOrj6U9AO7g+/kEuDMSoR2RH7FqIanfisg/PXCtYAwA8ijzJ]
```

### Why does the game freeze when I open the menu?
The very first time you open the edit menu, the mod has to load some assets. If they're not already
loaded, this will lead to a short freeze as it fetches them from another map.

### Can you make editing items have a cost?
Pick what you think an appropriate cost is and throw it away.

### Can you add an option to use any part on any item?
No. There are 1800 vanilla weapon parts in BL2 - how are you going to find the specific one you
want? This works with modded parts too, which makes the problem even worse - and means no predefined
list of categories is ever going to be complete. Then on top of all that, the menus themselves start
breaking when an inventory gets too many items, even your base inventory, not just this modded one.
