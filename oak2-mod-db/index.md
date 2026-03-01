---
nav_order: 1
---

# Installation Instructions

WORK IN PROGRESS

## Video Guide

{% youtube https://youtu.be/Xm1TLydB5Qo %}

## Text Guide

1. Download the latest release from github.

   ![Github download page](/assets/images/oak-installation/00-download.png)

   Make sure to download the right release for your game, and not either of the source code links.

2. Locate your game files.

   The default locations are:    
   Steam: `C:\Program Files (x86)\Steam\steamapps\common\<game>`    
   Epic: `C:\Program Files\Epic Games\<game>`    

   In Steam, you can also find this via RMB -> Manage -> Browse Local Files.
   ![Steam browse local files option](/assets/images/oak-installation/01-steam-local.png)

   The Gamepass version is not currently supported.

3. Open up the zip you downloaded, and extract it's contents directly into the game folder, such
   that they merge.

   ![Extracting the zip into the game folder](/assets/images/oak-installation/02-extract-files.png)

   If you're asked to overwrite existing files, accept.

4. \[PROTON ONLY\] When playing on Linux via Proton, you need to add the following launch arg:
   ```
   WINEDLLOVERRIDES="dsound=n,b" %command%
   ```

   [See the faq for more]({{ "/oak-mod-db/faq/#can-i-use-this-on-steam-decklinuxmac" | relative_url }}).

5. The SDK should be installed now. To verify:
   - In BL3, you should see a new `MODS` option on the main menu. You can click this to start
     configuring your mods.

     ![The BL3 mods menu](/assets/images/oak-installation/03-bl3-menu.png)

   - In WL, hit tilde (`` `/~ ``) twice to open console, and you should see a message saying the
     console mod menu has been loaded. Type `mods` and press enter to start configuring your mods.

     ![The console-based WL mods menu](/assets/images/oak-installation/04-wl-menu.png)

6. To install SDK mods, navigate back to the `sdk_mods` folder you extracted during step 3. SDK mods
   come in two forms:
   - `.sdkmod` files can be dropped directly into this folder.

     ![Installing a dot sdkmod](/assets/images/oak-installation/05-dot-sdkmod.png)

   - `.zip` files contain an inner folder you need to extract, in a similar manner to how you
     extracted the sdk.

     ![Installing a dot zip](/assets/images/oak-installation/06-dot-zip.png)

     Make sure that when you extract you don't accidentally create two nested folders, this will not
     work.

     ![Comparing normal vs nested mod folders](/assets/images/oak-installation/07-nested.png)

7. After installing SDK mods, you need to restart the game for them to get loaded.
