---
nav_order: 1
---

# Installation Instructions

## Video Guide

{% youtube https://youtu.be/Xm1TLydB5Qo %}

## Text Guide

1. Download the latest release from github.

   ![Github download page](/assets/images/installation/00-download.png)

   Make sure to download the right release for your game, and not either of the source code links.

2. Locate your game files.

   The default locations are:    
   Steam: `C:\Program Files (x86)\Steam\steamapps\common\<game>`    
   Epic: `C:\Program Files\Epic Games\<game>`    

   In Steam, you can also find this via RMB -> Manage -> Browse Local Files.
   ![Steam browse local files option](/assets/images/installation/01-steam-local.png)

3. Open up the zip you downloaded, and extract it's contents directly into the game folder, such
   that they merge.

   ![Extracting the zip into the game folder](/assets/images/installation/02-extract-files.png)

   If you're asked to overwrite existing files, accept.

4. \[PROTON ONLY\] When playing on Linux via Proton, you need to add the following launch arg:
   ```
   WINEDLLOVERRIDES="dsound=n,b" %command%
   ```

5. The SDK should be installed now. You should see a new `MODS` option on the main menu. You can
   click this to start configuring your mods.

   ![The mods menu](https://bl-sdk.github.io/assets/images/posts/mod-install1.5.png)

6. To install SDK mods, navigate back to the `sdk_mods` folder you extracted during step 3. SDK mods
   come in two forms:
   - `.sdkmod` files can be dropped directly into this folder.

     ![Installing a dot sdkmod](/assets/images/installation/05-dot-sdkmod.png)

   - `.zip` files contain an inner folder you need to extract, in a similar manner to how you
     extracted the sdk.

     ![Installing a dot zip](/assets/images/installation/06-dot-zip.png)

     Make sure that when you extract you don't accidentally create two nested folders, this will not
     work.

     ![Comparing normal vs nested mod folders](/assets/images/installation/07-nested.png)

7. After installing SDK mods, you need to restart the game for them to get loaded.
