---
nav_order: 2
---

# Frequently Asked Questions

## Can I use this alongside hotfix or pak mods?
Yup, they're all fully compatible - though as always, *specific mods* may have issues when used
together.

## How do I use this with the plugin loader for OpenHotfixLoader/BL3HM/other dll mods?
For convienience, the SDK zip comes with a plugin loader pre-packaged, the sdk itself is a plugin
just like everything else. You can just throw these other mods into the `Plugins` folder, and
everything should keep working as before.

Note that the SDK relies on some updated features from the plugin loader it ships with, replacing it
with an older version may stop the SDK from loading, with the error `The specified module could not
 be found`.
