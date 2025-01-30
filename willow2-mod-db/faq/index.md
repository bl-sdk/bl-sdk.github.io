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
that version on Linux/Mac instead.

The official Linux/Mac releases are rather outdated, they don't include all the latest updates, and
you can't even coop with Windows players due to the version mismatch, so it's generally recommended
to do this anyway.

**Steam Deck/Linux**

In Steam, force a specific proton version under the game's *Properties* 🡒 *Compatibility* tab. Then
on the *General* tab, set the launch options to:

```
WINEDLLOVERRIDES="ddraw=n,b" %command%
```

Once you get in game, open console by pressing tilde twice, and double check there's no proton
errors detected. You may have to switch proton builds a few times, the exact builds that work seems
to vary between people for reasons we haven't worked out. Generally though, recent builds of
[Proton GE](https://github.com/GloriousEggroll/proton-ge-custom) seem to have better results - and
you may find it easier to install them via [ProtonUp-Qt](https://github.com/DavidoTek/ProtonUp-Qt).

Once you manage to load in without any proton errors, you're all set up, you can continue following
all other instructions.

**Mac**

While we believe it's possible, we don't properly understand the process for running the Windows
executable on a Mac. If you do, let us know, and we can fill this section in properly.

## Can I use this alongside text/blcm mods?
Yup, they're fully compatible - though as always, *specific mods* may have issues when used
together.

## Tilde isn't opening the console / I want to use a different console key
Tilde isn't quite a standardised key, so on some keyboard layouts a different character sends the
same signal to the game. [You can check this site for a reference](https://kbdlayout.info/features/virtualkeys/VK_OEM_3).

[OpenBLCMM](https://github.com/BLCM/OpenBLCMM/) provides a helpful menu to rebind the console key,
under Tools -> INI Tweaks.

Alternatively, you can manually rebind the key. Open the file
`<my documents>/My games/Borderlands 2/WillowGame/Config/WillowInput.ini` in notepad. Search for
`ConsoleKey=`, and replace the key as appropriate.

## How do I unbind a Keybind?
Set it to the same thing it was already bound to.

## My game is crashing...
### Immediately on starting / After hitting play in the launcher.
Try install the latest [Microsoft Visual C++ Redistrubutable](https://aka.ms/vs/17/release/vc_redist.x86.exe).

## What does it mean if a mod's a legacy mod?
SDK version 3.0 went through a major rewrite, which significantly changed the best way to write
mods. Legacy mods are simply all mods created before this version. Since these were written with
an older version in mind, some of their behaviour might now feel a bit off. There might also be a
few issues if used in scenarios enabled by the new sdk - for example, in older versions of the SDK
you could only enable mods while on the main menu, so some legacy mods might have issues if enabled
while in game.

The legacy mod compatibility layer will be removed at some point in the future.

## I tried extracting a mod zip, but it's not appearing in the mod menu
Firstly, check console for any errors. Most often, you're missing one of the mod's requirements. The
requirements should always be listed on the mod page. To fix this, just install/update the
requirements.

If there are no error messages, but it's still not appearing, that's usually caused by accidentally
extracting to a nested folder. If you open the folder you extracted, `sdk_mods/<Mod Name>`, and just
see another folder `sdk_mods/<Mod Name>/<Mod Name>`, you've run into this.

![Comparing normal vs nested mod folders](/assets/images/willow2-installation/07-nested.png)

To fix this, simply copy the inner folder and move it up a level. To avoid running into it in
future, always drag the folder directly out of the zip file.

## Why do some SDK mods disable when I restart the game, when others stay enabled?
In legacy mods, the mod author had to explicitly turn on auto-enabling. It may simply never have been
updated to turn it on.

In modern mods, auto-enabling is on by default, so if a mod doesn't auto-enable, the author must
have deliberately disabled it.
