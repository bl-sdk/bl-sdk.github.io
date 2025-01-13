---
nav_order: 2
---

# Frequently Asked Questions
{:.no_toc}

### Table of Contents
{:.no_toc}
- toc
{:toc}

## Can I use this on Steam Deck/Linux/Mac
Yes, through a compatibility layer. The SDK only works on a Windows executable, but you can just run
that version on Linux/Mac instead. Since there's no official Linux release for either game, and no
official Mac release for WL, you're likely already doing this already.

**Steam Deck/Linux**

In Steam, set the game's launch options to:

```
WINEDLLOVERRIDES="dsound=n,b" %command%
```

Once you get in game, open console by pressing tilde twice, and double check there's no proton
errors detected. Once that's set up you can continue following all other instructions.

**Mac**

While we believe it's possible, we don't properly understand the process for running the Windows
executable on a Mac. If you do, let us know, and we can fill this section in properly.

## Can I use this alongside hotfix or pak mods?
Yup, they're all fully compatible - though as always, *specific mods* may have issues when used
together.

## Tilde isn't opening the console / I want to use a different console key
Tilde isn't quite a standardised key, so on some keyboard layouts a different character sends the
same signal to the game. [You can check this site for a reference](https://kbdlayout.info/features/virtualkeys/VK_OEM_3).

To rebind the console key, create a new file
`<game>\OakGame\Binaries\Win64\Plugins\unrealsdk.user.toml`, and open it in notepad. Add the
following content, substituting the key as appropriate:

```toml
[unrealsdk]
console_key = "F1"
```

## My game is crashing...
### When I open one of the entries in the BL3 Mod Menu
Update the sdk, this was fixed in version 1.3. The BL3 update on 2024-08-08 caused older versions of
the BL3 Mod Menu to crash when creating a slider or keybind option.

## How do I use this with the plugin loader for OpenHotfixLoader/BL3HM/other dll mods?
For convenience, the SDK zip comes with a plugin loader pre-packaged, the sdk itself is a plugin
just like everything else. You can just throw these other mods into the `Plugins` folder, and
everything should keep working as before.

## How do I use this with dxvk/other programs hooking `d3d11.dll`?
If you've previously installed mods, they probably came with a `d3d11.dll` plugin loader, which
would cause conflicts. The sdk ships with a different plugin loader precisely for this, if you still
have a `d3d11.dll`, you can simply overwrite it with dxvk.

## I still have an old plugin loader, is this a problem?
Generally, no. Having multiple plugin loaders is not a problem, since once a plugin is loaded, other
pluginloaders won't do anything to it.

There are some niche known issues with using specific dlls as pluginloaders. The SDK has changed
dlls a few times to try avoid them:

- `d3d11.dll`

  The oldest version of this does not allow the SDK to load it's dependencies correctly, so the SDK
  itself will completely fail to load. The SDK never shipped with this version, but if you installed
  older modding tools you might still have one. SDK version 1.0 shipped with a version which
  addressed this.

  When using this plugin loader, your steam overlay (and perhaps other overlay programs) stops
  functioning.

  If you want to install dxvk, it will also need to override this same dll.

- `xinput1_3.dll`

  This shipped with SDK version 1.1.

  When playing under Proton, you had to use `WINEDLLOVERRIDES="xinput1_3=n,b"`. Setting this
  variable breaks all controller input, even without any mods, and in multiple other games.

- `dsound.dll`

  This has shipped since SDK version 1.2.

  No known issues \o/
