---
nav_order: 1
redirect_from:
  - /about/
  - /mods/
  - /types/Content/
  - /types/Gameplay/
  - /types/Library/
  - /types/Utility/
---

# Installation Instructions

## Video Guide

{% youtube https://youtu.be/cCkNCjx3xDM %}

## Text Guide
1. Install the latest
   [Microsoft Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x86.exe).

   ![VC Redist Installer](/assets/images/willow2-installation/vcredist.png)
   
   If you're running under Proton, you can do this by installing `vcrun2022` using
   [protontricks](https://github.com/Matoking/protontricks).

2. Download the latest release from github.

   ![Github download page](/assets/images/willow2-installation/00-download.png)

   Make sure not to download one of the the source code links.

3. Locate your game files.

   The default locations are:    
   Steam: `C:\Program Files (x86)\Steam\steamapps\common\<game>`    
   Epic: `C:\Program Files\Epic Games\<game>`    

   In Steam, you can also find this via RMB -> Manage -> Browse Local Files.
   ![Steam browse local files option](/assets/images/willow2-installation/01-steam-local.png)

4. Open up the zip you downloaded, and extract it's contents directly into the game folder, such
   that they merge.

   ![Extracting the zip into the game folder](/assets/images/willow2-installation/02-extract-files.png)

   If you're asked to overwrite existing files, accept.

5. \[PROTON ONLY\] When playing on Linux via Proton, you need to add the following launch arg:
   ```
   WINEDLLOVERRIDES="ddraw=n,b" %command%
   ```

   [See the faq for more]({{ "/willow2-mod-db/faq/#can-i-use-this-on-steam-decklinuxmac" | relative_url }}).

6. The SDK should be installed now. You should see a new `MODS` option on the main menu. You can
   click this to start configuring your mods.

   ![The main menu, with a 'MODS' entry](/assets/images/willow2-installation/03-bl2-menu-outer.png)    
   ![The mods menu](/assets/images/willow2-installation/04-bl2-menu-inner.png)

7. To install SDK mods, navigate back to the `sdk_mods` folder you extracted during step 4. SDK mods
   come in two forms:
   - `.sdkmod` files can be dropped directly into this folder.

     ![Installing a dot sdkmod](/assets/images/willow2-installation/05-dot-sdkmod.png)

   - `.zip` files contain an inner folder you need to extract, in a similar manner to how you
     extracted the sdk.

     ![Installing a dot zip](/assets/images/willow2-installation/06-dot-zip.png)

     Make sure that when you extract you don't accidentally create two nested folders, this will not
     work.

     ![Comparing normal vs nested mod folders](/assets/images/willow2-installation/07-nested.png)

8. After installing SDK mods, you need to restart the game for them to get loaded.
