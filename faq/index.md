---
nav_order: 2
---

# Frequently Asked Questions
{:.no_toc}

### Table of Contents
{:.no_toc}
- toc
{:toc}

## Can I use this alongside hotfix or pak mods?
Yup, they're all fully compatible - though as always, *specific mods* may have issues when used
together.

## How do I use this with the plugin loader for OpenHotfixLoader/BL3HM/other dll mods?
For convenience, the SDK zip comes with a plugin loader pre-packaged, the sdk itself is a plugin
just like everything else. You can just throw these other mods into the `Plugins` folder, and
everything should keep working as before.

Note that the SDK relies on some updated features from the plugin loader it ships with, replacing it
with an older version may stop the SDK from loading, with the error `The specified module could not
 be found`.

## How do I use this with dxvk/other programs hooking `d3d11.dll`?
If you've previously installed mods, they probably came with a `d3d11.dll` plugin loader, which
would cause conflicts. However, since version 1.1, the SDK comes with a `xinput1_3.dll` plugin
loader instead. This means you can simply overwrite the older one with dxvk - they both do the same
thing.

## Tilde isn't opening the console / I want to use a different console key
Tilde isn't quite a standardised key, so on some keyboard layouts a different character sends the
same signal to the game. [You can check this site for a reference](https://kbdlayout.info/features/virtualkeys/VK_OEM_3).

To rebind the console key, open `<game>\OakGame\Binaries\Win64\Plugins\unrealsdk.env` in notepad.
Add a new line, substituting the key as appropriate:
```
UNREALSDK_CONSOLE_KEY=F1
```
Note that this file is bundled with the SDK, so updating will overwrite it.
