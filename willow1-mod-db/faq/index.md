---
nav_order: 2
---

# FAQ / Troubleshooting
{:.no_toc}

### Table of Contents
{:.no_toc}
- toc
{:toc}

## Can I use this on Steam Deck/Linux/Mac?
Yes, through a compatibility layer. The SDK only works on a Windows executable, but you can just run
that version on Linux/Mac instead. Since there are no official Linux/Mac releases, you're likely
already doing this anyway.

**Steam Deck/Linux**

In Steam, set the game's launch options to:

```
WINEDLLOVERRIDES="dsound=n,b" %command%
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
executable on a Mac. If you do, let us know, and we can fill this section in properly

## Can I use this alongside upk mods?
Yup, they're fully compatible - though as always, *specific mods* may have issues when used
together.

## My game is crashing immediately on starting / after hitting play in the launcher.
Try install the latest
[Microsoft Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x86.exe).

If you're running under Proton, you can do this by installing `vcrun2022` using
[protontricks](https://github.com/Matoking/protontricks).

## Tilde isn't opening the console / I want to use a different console key
Tilde isn't quite a standardised key, so on some keyboard layouts a different character sends the
same signal to the game. [You can check this site for a reference](https://kbdlayout.info/features/virtualkeys/VK_OEM_3).

You can manually rebind the key by opening the the file
`<my documents>/My Games/Borderlands/WillowGame/Config/WillowInput.ini` in notepad, searching for
`ConsoleKey=`, and replacing the key as appropriate.

## How do I unbind a Keybind?
Set it to the same thing it was already bound to.
