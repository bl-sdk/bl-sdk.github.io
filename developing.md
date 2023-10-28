# Developing SDK Mods
Coming soon

## Adding to the Mod DB
The DB primarily sources info from your mod's `pyproject.toml`. With a well configured pyproject,
all you need to do is point the DB at it, and everything will be extracted automatically. To do
this, add a file for your mod to the `_mods/` dir of this repo, and add the front matter variable
`pyproject_url`, pointing at an auto updating link.

```md
---
pyproject_url: https://raw.githubusercontent.com/apple1417/oak-sdk-mods/master/abcd/pyproject.toml
---
```

You can overwrite your mod's description simply by adding some extra content to the page. You can
use this to embed images or videos, which wouldn't be suitable for the in-game mod description.

You can overwrite some of the other info on the page by setting various front matter variables.

Field                       | Front matter      | `pyproject.toml`
----------------------------|-------------------|-------------
Title                       | `title`           | `tool.sdkmod.name`, `project.name`
Author(s)                   | `author`          | `project.authors[n].name`<sup>1</sup>
Latest Version              | `version`         | `tool.sdkmod.version`, `project.version`
Supported Games<sup>2</sup> | `supported_games` | `tool.sdkmod.supported_games`
License<sup>3</sup>         | `license`         | `tool.sdkmod.license`, `project.license.text`<sup>4</sup>
Requirements                | `dependencies`    | `project.dependencies`
Misc URLs<sup>5</sup>       | `urls`            | `project.urls`
Download Link               | `download`        | `tool.sdkmod.download`
Description                 | The page contents | `project.description`

<sup>1</sup> Multiple authors are concatenated in the order given.    
<sup>2</sup> An array of strings, with valid values of `BL3` and `WL` (case insensitive). If not
             given, defaults to all games.    
<sup>3</sup> A table with keys `name` and `url`. Prefer linking to a summary site, rather than
             direct to your `LICENSE`.    
<sup>4</sup> Used as the name, with no url.    
<sup>5</sup> A dict where keys are the names and values are the urls.
{: .fs-2 }

### Updating Info
While this site is statically generated, every time a mod page is loaded it fetches the pyproject
and updates the page with any changes, the values fetched when the site is generated are only used
as defaults (note that front matter overrides still take priority). This means you generally don't
need to touch the db again, changes will be picked up automatically.

There are two main exceptions to this: the title, and the search data. While the title will get
updated on the mod page itself, the sidebar won't get updated, and the data powering the searchbar
is never updated live. If you make significant changes to your pyproject, it may be worth kicking
off another build to update the static versions of these.
