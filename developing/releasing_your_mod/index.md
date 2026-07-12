---
nav_order: 4
---
# Releasing Your Mod
{:.no_toc}

### Table of Contents
{:.no_toc}
- toc
{:toc}

## Packaging Your Mod
While working on your mod, you'll just have a bunch of lose files in a folder. When it comes time to
release, we need to package it up more nicely. There are three formats we accept.

You might consider writing a script to package mods automatically. Several contributors have done
so; we don't have a general purpose script since they all have customizations to suit each persons'
needs.

### `.sdkmod` file
The standard format is as a single `.sdkmod` file, which users just drop directly in their mods
folder.

`.sdkmod` files are really just `.zip`s with a renamed extension. We renammed it mostly to avoid the
default Windows file association, which helps prevent users getting confused (extracting files wrong
is a very common source of installation issues). The root folder must only contain a single folder,
which must be named the same thing as the `.sdkmod`, and your `__init__.py` goes inside that inner
folder.

<details markdown="1">
<summary>Expand for Examples</summary>

**Ok**
```
my_mod.sdkmod
- my_mod/
  - __init__.py
  - other_file.py
```

**Not ok, missing inner folder**
```
my_mod.sdkmod
- __init__.py
```

**Not ok, too far nested**
```
my_mod.sdkmod
- my_mod/
  - my_mod/
    - __init__.py
```

**Not ok, `.sdkmod` and folder have different names**
```
My Mod.sdkmod
- my_mod/
  - __init__.py
```

**Not ok, multiple files in root**
```
my_mod.sdkmod
- my_mod/
  - __init__.py
- LICENSE
```

**Not ok, multiple folders in root**
```
my_mod.sdkmod
- my_mod/
  - __init__.py
- dependency_mod/
  - __init__.py
```

</details>

This format is also validated during SDK's initialization, an incorrectly formatted `.sdkmod` will
not be imported.

### Mod Folder Zip
Python is perfectly happy to import files from inside a zip, that's how `.sdkmod`s work. But very
occasionally there are reasons you need the user to properly extract your folder. The only known
things that require this are:
- You're shipping a native Python module (a `.pyd`) which you need to import.
- (Willow 2) You're shipping a text mod alongside your mod, which you want to `exec <path>` in
  console.

For these cases, the next acceptable format is actually the exact same as a `.sdkmod`, except you
keep the extension as `.zip`. Our guides all tell users to extract zips.

As some extra advice, these are some common use cases which cause people to *think* they need this
format, but which *do not*, and can work perfectly fine as a `.sdkmod`:
- You have some assert file which you need to read from at runtime. Use `mods_base.open_in_mod_dir`,
  or in more advanced cases maybe `importlib.resources`.

- You're writing some data to a file, and a `HiddenOption` won't cut it for some reason (e.g. you're
  using sqlite). Pick a folder under `SETTINGS_DIR`, and put all your files under it - making sure
  to create the folder if needed. Also set your `settings_file` to be in this folder in
  `build_mod(...)`.

### Hybrid Zip
The last format is for hybrid mods, which need both an SDK mod and a upk/pak/some other file in the
game folder. These should be a zip file, called `.zip`, containing all your files arranged relative
to the base game folder. Users should be able to install these just by merging all files into their
game folder, in the same way you install the SDK.

What we specifically look for in this case is that the root folder inside the zip contains an
`sdk_mods` folder, which itself contains either a single `.sdkmod`, or a single folder.

<details markdown="1">
<summary>Expand for Examples</summary>

**Ok**
```
my_mod.zip
- sdk_mods/
  - my_mod.sdkmod
- WillowGame/
  - CookedPC/
    - MyMod.upk
- Readme.md       # though maybe don't use a generic name, likely to be overridden
```
```
my_mod.zip
- OakGame/
  - Binaries/
    - Win64/
      - Plugins/
        - ohl-mods/
          - my_mod.bl3hotfix
- sdk_mods/
  - my_mod/
    - __init__.py
```

**Not ok, multiple files/folders in `sdk_mods`**
```
my_mod.zip
- sdk_mods/
  - my_mod.sdkmod
  - Readme.md
```
```
my_mod.zip
- sdk_mods/
  - my_mod.sdkmod
  - other_mod.sdkmod
```
```
my_mod.zip
- sdk_mods/
  - my_mod/
    - __init__.py
  - other_mod.sdkmod
```

**Not ok, missing `sdk_mods` folder/not laid out like the game folder**
```
my_mod.zip
- my_mod.sdkmod
- my_mod.pak
```

</details>

## Adding to the Mod DB
Both `mods_base` and the mods db are built around the idea of your mod's `pyproject.toml` being a
single source of truth. In the past it wasn't uncommon to update your mod but forget to update the
db, or vice versa, which this concept helps avoid. With a well configured pyproject, all your mod
details will be extracted automatically.

To add your mod, you'll need to add a markdown file to one of the `_*_mods` folders in
[this site's repo](https://github.com/bl-sdk/bl-sdk.github.io).

### Simplest Configuration
The simplest configuration is the following.

```md
---
pyproject_url: https://raw.githubusercontent.com/apple1417/oak-sdk-mods/master/abcd/pyproject.toml
---

# My cool mod
Does some cool things.
```

Make sure the url points at an auto-updating link, instead of a specific commit. If you're using
github, also make sure to use the `raw.githubusercontent.com` link - *not* the `github.com/.../raw/`
links, which don't work.

Please write a detailed description - more so than what you might put in the mod's in-game
description. Historically a lot of mods have had very basic descriptions, which makes it hard for
users to find the right thing. If your mod adds a god mode cheat, the words "god mode" should
probably be on the page somewhere, so that the searchbar can find it.

### More Advanced Markdown
If you want to include images/other assets, add them to a `assets/mods/<tree>/<mod_name>` folder.

```md
---
pyproject_url: https://raw.githubusercontent.com/apple1417/oak-sdk-mods/master/abcd/pyproject.toml
---

# My cool mod
Look at this image:
![alt text](/assets/mods/oak/abcd/some_image.png)
```

Jekyll uses [kramdown](https://kramdown.gettalong.org/syntax.html) to render markdown, which
probably supports some extra syntax than what you're used to.

There's also two bits of the templating system you should probably know about:

- When linking to something that's part of the site, whether an image or another page, prefer using
  {% raw %}`{{ "/path/to/file.txt" | relative_url }}`{% endraw %}. This ensures the link will get
  updated correctly if hosted under another url.

  The above example image should really have been:
  ```md
  ![alt text]({% raw %}{{ "/assets/mods/oak/abcd/some_image.png" | relative_url }}{% endraw %})
  ```

- If you want to embed a youtube video, prefer using
  {% raw %}`{% youtube https://www.youtube.com/watch?v=dQw4w9WgXcQ %}`{% endraw %}.

If you're using some of these more advanced features, you may want to build the site locally to make
sure they display as you expect.

### Changing Mod Details
Now you can easily customize the mod description by just writing markdown, but there's still all the
other info above it. You can overwrite these by setting front matter variables. If you're not
familiar with Jekyll, the "front matter" is a block of YAML configuration inbetween triple dashes at
the top - you used it previously to set the `pyproject_url`.

Field                       | Front matter      | `pyproject.toml`
----------------------------|-------------------|-------------
Title                       | `title`           | `tool.sdkmod.name`, `project.name`
Author(s)                   | `author`          | `project.authors[n].name`<sup>1</sup>
Latest Version              | `version`         | `tool.sdkmod.version`, `project.version`
Supported Games<sup>2</sup> | `supported_games` | `tool.sdkmod.supported_games`
Coop Support                | `coop_support`    | `tool.sdkmod.coop_support`
License<sup>4</sup>         | `license`         | `tool.sdkmod.license`, `project.license.text`<sup>5</sup>
Requirements                | `dependencies`    | `project.dependencies`
Misc URLs<sup>6</sup>       | `urls`            | `project.urls`
Download Link               | `download`        | `tool.sdkmod.download`
Description                 | The page contents | `project.description`<sup>7</sup>
Redirects<sup>8</sup>       | `redirect_from`   | Not supported

<sup>1</sup> Multiple authors are concatenated in the order given.    
<sup>2</sup> An array of strings. If not given, defaults to all games for the category you're in.    
<sup>3</sup> One of `Unknown`, `Incompatible`, `RequiresAllPlayers`, or `ClientSide`. Defaults to
             unknown.    
<sup>4</sup> A table with keys `name` and `url`. Prefer linking to a summary site, rather than
             direct to your `LICENSE`.    
<sup>5</sup> Used as the name, with no url.    
<sup>6</sup> A dict where keys are the names and values are the urls.    
<sup>7</sup> HTML tags are stripped, rather than just being escaped.    
<sup>8</sup> An array of relative urls to redirect to this page - i.e. if you moved your mod, it's
             old urls. See also
             [`jekyll-redirect-from`](https://github.com/jekyll/jekyll-redirect-from#usage).    
{: .fs-2 }

Again, if you're using any of these, you may want to build the site locally to make sure they
display as you expect.

### Updating Mod Details
While this site is statically generated, every time a mod page is loaded it fetches the pyproject
and updates the page with any changes, the values fetched when the site is generated are only used
as defaults (note that front matter overrides still take priority). This means you generally don't
need to touch the db again, changes will be picked up automatically.

There are a few exceptions to this, which are not automatically updated:
- The title used in the sidebar and tab title (the header on the mod page does get updated).

- `project.name`, which is used for matching dependencies to their mod page.

- The dependencies displayed on the missing requirements page.

- The data powering the searchbar.

- The fields which are always displayed (e.g. Title, Author) will not be set to unknown if you
  completely delete their section in your pyproject, the old data is preferred.
  
  Requirements and Misc URLs are already hidden when not in use, so the updates *will* delete them.

If you make significant changes to your pyproject, it may be worth kicking off another build to
update the static versions of these. Do note that this data is updated anytime the site is
generated, someone else adding an unrealated mod will update yours.

## Handling Missing Requirements
It's recommended to put dependency version checks right at the top of your main `__init__.py`, to
make sure your mod only loads if everything is present, and to give users more helpful error
messages.

One simple way of doing this is using asserts and `__import__`:
```py
if True:  # avoids E402
    assert __import__("mods_base").__version_info__ >= (1, 4), "Please update the SDK"
    assert __import__("pyunrealsdk").__version_info__ >= (1, 3, 0), "Please update the SDK"
    assert __import__("unrealsdk").__version_info__ >= (1, 3, 0), "Please update the SDK"
    assert __import__("ui_utils").__version_info__ >= (1, 0), "Please update the SDK"

    from mods_base import Game

    assert Game.get_current() == Game.BL3, "The Hunt Tracker only works in BL3"
```

It's easiest to set your required versions to be >= the version you're currently developing with,
rather than searching through history to find the oldest possible compatible one.

Now asserts make for nice and simple code, but not all users check console before going out and
complaining. As an alternative, you can open a page in their browser instead - this site provides
several for that purpose.

- [{{ "oak-mod-db/requirements?mod=my_mod" | absolute_url }}]({{ "oak-mod-db/requirements?mod=my_mod" | absolute_url }})
- [{{ "oak2-mod-db/requirements?mod=my_mod" | absolute_url }}]({{ "oak2-mod-db/requirements?mod=my_mod" | absolute_url }})
- [{{ "willow1-mod-db/requirements?mod=my_mod" | absolute_url }}]({{ "willow1-mod-db/requirements?mod=my_mod" | absolute_url }})
- [{{ "willow2-mod-db/requirements?mod=my_mod" | absolute_url }}]({{ "willow2-mod-db/requirements?mod=my_mod" | absolute_url }})

```py
try:
    assert __import__("mods_base").__version_info__ >= (1, 5), "Please update the SDK"
except (AssertionError, ImportError) as ex:
    import webbrowser
    webbrowser.open("{{ "willow2-mod-db/requirements?mod=my_mod" | absolute_url }}")
    raise ex
```

The `?mod=` query parameter should be set to your mod's `project.name`.

As mentioned above, anything in `project.dependencies` is shown as a requirement on the mod page. If
you want to require a particular version of the SDK, you can add a dependency on `oak_mod_manager`,
`oak2_mod_manager`, `willow1_mod_manager`, or `willow2_mod_manager` (as appropriate).

```toml
[project]
dependencies = [
  'oak_mod_manager >= 1.2',
]
```
Since requiring the SDK is somewhat implicit, it remains to be seen if the possible future package
manager will need this.

## Why not use Nexus?
This question comes up from time to time.

Most importantly, Nexus Mods is not run by the community, we have absolutely no influence into what
they do. We have a number of additional greviences:
- They require an account to download.
- They've historically hosted stolen mods, and refused to take them down despite our reports.
- They explicitly let you to submit mods "on behalf of" someone else, and give you rewards for doing
  so, which leads to the above stolen mods.
- They claim Vortex support, but it's completely broken in every single game. But when this is
  pointed out they also say it's community made, and to take it up with them - despite none of the
  plugins having been made by anyone involved in the community.
- The few times someone from Nexus has tried talking to us, it's all PR talk and they refuse to see
  the problem in any of the above.

And in general, all the behaviour we're seen from Nexus is incredibly profit seeking, which is at
complete odds with how we want to work.

In contrast, there's a number of advantages to posting on our Mod DB.
- Full HTML customization (if you want to use it, not required).
- Automatically updates whenever you push to your repo.
- Makes sure your mods are properly formatted.
- No comments from confused users.
- Future plans for an automated mod installer will be based on it - if you're on the Mod DB, won't
  need to update anything.

Additionally, in the rare cases the SDK needs to make a breaking change, we use the DB to find what
mods it would impact, and work out a migration - or flipping that the other way, if you're not on
the Mod DB, we won't be aware and may break your mod without warning.
