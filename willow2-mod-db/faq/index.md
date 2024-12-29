---
nav_order: 2
---

# Frequently Asked Questions
{:.no_toc}

### Table of Contents
{:.no_toc}
- toc
{:toc}

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

## What do the different "Coop" fields on the mod pages mean?

| Category             | Meaning                                                                                                                             |
|:---------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| Incompatible         | The mod is fundamentally incompatible with coop, it can only be played solo.                                                        |
| Requires All Players | The mod needs all players to have it installed in order to work best. There may still be aspects which don't work as well off host. |
| Client Side          | The mod is entirely client side, and can be used in coop regardless of what other players are running.                              |

These categories are manually set by the mod's developer, a mod which is still left on unknown may
simply never have been tested.

## What does it mean if a mod's a legacy mod?
SDK version 3.0 went through a major rewrite, which significantly changed the best way to write
mods. Legacy mods are simply all mods created before this version. Since these were written with
an older version in mind, some of their behaviour might now feel a bit off. There might also be a
few issues if used in scenarios enabled by the new sdk - for example, in older versions of the SDK
you could only enable mods while on the main menu, so some legacy mods might have issues if enabled
while in game.

The legacy mod compatibility layer will be removed at some point in the future.

## I tried extracting a mod zip, but it's not appearing in the mod menu
This is usually caused by accidentally extracting to a nested folder. If you open the folder you
extracted, `sdk_mods/<Mod Name>`, and just see another folder `sdk_mods/<Mod Name>/<Mod Name>`,
you've run into this.

![Comparing normal vs nested mod folders](/assets/images/willow2-installation/06-nested.png)

To fix this, simply copy the inner folder and move it up a level. To avoid running into it in
future, always drag the folder directly out of the zip file.

## Why do some SDK mods disable when I restart the game, when others stay enabled?
In legacy mods, the mod author had to explictly turn on auto-enabling. It may simply never have been
updated to turn it on.

In modern mods, auto-enabling is on by default, so if a mod doesn't auto-enable, the author must
have deliberately disabled it.
