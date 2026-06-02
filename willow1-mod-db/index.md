---
nav_order: 1
---

# Installation Instructions

![Enhanced is not supported](/assets/images/willow1-installation/no-enhanced.png)
{: style="margin-bottom:-1.5em;"}

## Video Guide

{% youtube https://youtu.be/jqE43fNbTGM %}

## Text Guide
1. Install the latest
   [Microsoft Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x86.exe).

   ![VC Redist Installer](/assets/images/willow1-installation/vcredist.png)
   
   If you're running under Proton, you can do this by installing `vcrun2022` using
   [protontricks](https://github.com/Matoking/protontricks).

2. Download the latest release from github.

   ![Github download page](/assets/images/willow1-installation/download.png)

   Make sure not to download one of the the source code links.

3. Locate your game files.

   The default locations is `C:\Program Files (x86)\Steam\steamapps\common\Borderlands`.

   You can also find this via RMB -> Manage -> Browse Local Files.

   ![Steam browse local files option](/assets/images/willow1-installation/steam-local.png)

4. Open up the zip you downloaded, and extract it's contents directly into the game folder, such
   that they merge.

   ![Extracting the zip into the game folder](/assets/images/willow1-installation/extract-files.png)

   If you're asked to overwrite existing files, accept.

5. \[PROTON ONLY\] When playing on Linux via Proton, you need to add the following launch arg:
   ```
   WINEDLLOVERRIDES="dsound=n,b" %command%
   ```

   [See the faq for more]({{ "/willow1-mod-db/faq/#can-i-use-this-on-steam-decklinuxmac" | relative_url }}).

6. The SDK should be installed now. You should see a new `MODS` option on the main menu. You can
   click this to start configuring your mods.

   ![The main menu, with a 'MODS' entry](/assets/images/willow1-installation/menu-outer.png)    
   ![The mods menu](/assets/images/willow1-installation/menu-inner.png)

7. To install SDK mods, navigate back to the `sdk_mods` folder you extracted during step 4. SDK mods
   come in three forms:
   - `.sdkmod` files can be dropped directly into this folder.

     ![Installing a dot sdkmod](/assets/images/willow1-installation/dot-sdkmod.png)

   - `.zip` files which contain only a single folder need to be extracted into `sdk_mods`. Drag the
     inner folder in a similar manner to how you extracted the SDK.

     ![Installing a dot zip](/assets/images/willow1-installation/dot-zip.png)

     Make sure that when you extract you don't accidentally create two nested folders, this will not
     work.

     ![Comparing normal vs nested mod folders](/assets/images/willow1-installation/nested.png)

   - `.zip` files which have both an `sdk_mods` folder and some other folder (usually `WillowGame`)
     need to be extracted back into the base game folder, in the exact same way as the SDK.

     ![Installing a hybrid dot zip](/assets/images/willow1-installation/dot-zip-hybrid.png)

     These are hybrid mods, they need all the files in the zip, not just the `.sdkmod`.

8. After installing SDK mods, you need to restart the game for them to get loaded.
