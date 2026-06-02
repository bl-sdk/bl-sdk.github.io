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

## Is it safe to install the SDK?
Depends on what you mean by safe.

Note all the following answers relate to normal, "well behaved" mods. While we've never had an
incident, a malicious mod could break all the rules.

### Will the SDK delete/corrupt my saves?
In general, no. Some specific mods may be more risky.

Mods which add new items/characters generally require a starting new character. Loading an unmodded
character with these, or a modded one without them, could possibly cause issues. If you ever make
this mistake, the `disconnect` console command will quit without saving.

### Will I get banned for using the SDK?
No.

The 2K Terms of Service state that, if you use mods to grief/hack their servers, they reserve the
right to ban you (from SHiFT, not the game). They also say they'll ban you if you grief/hack by
other means - using mods isn't the relevant part. In practice, most people recommend staying away
from matchmaking because this is essentially never enforced, even in cases it clearly should be.

### Will the SDK prevent me getting achievements/give me achievements I haven't earned?
No. The SDK does not interact with achievements in any way. Specific mods may make getting
achievements easier/harder.

### Will the SDK give me a virus?
The SDK itself will not - it does occasionally get caught in a scan. To be safe make sure you only
ever download it from the official github, linked in the sidebar.

While we've never had an incident, it is theoretically possible for SDK mods to contain a virus. SDK
mods are not sandboxed, they can run arbitrary code on your system, and we do not actively review
their contents. Treat them like installing any other program on your system.

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
