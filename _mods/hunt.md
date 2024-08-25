---
pyproject_url: https://raw.githubusercontent.com/apple1417/oak-sdk-mods/master/hunt/pyproject.toml
---

The official Borderlands 3 Hunt Tracker.

Automatically keeps track of which unique items you've collected.

<video width="100%"
    muted autoplay loop playsinline
    disablepictureinpicture disableremoteplayback
    poster="{{ "/assets/mods/hunt/00-drops.jpeg" | relative_url }}"
    src="{{ "/assets/mods/hunt/00-drops.webm" | relative_url }}"
></video>

Calculates a number of interesting stats about your run, and lets you display them in game.

<video width="100%"
    muted autoplay loop playsinline
    disablepictureinpicture disableremoteplayback
    poster="{{ "/assets/mods/hunt/01-stats.jpeg" | relative_url }}"
    src="{{ "/assets/mods/hunt/01-stats.webm" | relative_url }}"
></video>

Or, lets you export them to a text file for even more advanced customization in OBS.

![OBS text source settings pulling from the text file]({{ "/assets/mods/hunt/02-obs.jpeg" | relative_url }})
{:style="display: block; margin: 0 auto; width: 50%"}

Also contains a full encyclopedia of every unique drop in the game (or at least the Hunt-viable
ones), including the specific maps and enemies which drop them, as well as any other restrictions
the source may have.

<video width="100%"
    muted autoplay loop playsinline
    disablepictureinpicture disableremoteplayback
    poster="{{ "/assets/mods/hunt/03-info.jpeg" | relative_url }}"
    src="{{ "/assets/mods/hunt/03-info.webm" | relative_url }}"
></video>


And of course, there's a single massive list of everything, which you can use in case you're not
sure of the exact map, or if you just want to have some fun scrolling.

<video width="100%"
    muted autoplay loop playsinline
    disablepictureinpicture disableremoteplayback
    poster="{{ "/assets/mods/hunt/04-everything.jpeg" | relative_url }}"
    src="{{ "/assets/mods/hunt/04-everything.webm" | relative_url }}"
></video>

## Coop Support

<video width="100%"
    muted autoplay loop playsinline
    disablepictureinpicture disableremoteplayback
    poster="{{ "/assets/mods/hunt/05-coop.jpeg" | relative_url }}"
    src="{{ "/assets/mods/hunt/05-coop.webm" | relative_url }}"
></video>

As long as all players are running it, the tracker also fully supports coop. This is done by
transmitting some information using the item's loot beam, hence the blinking. Coop support can be
disabled if you find the blinking distracting.

There a few slight caveats to playing in coop:

- In Coopetition mode, each player must individually look at the item to redeem it for themselves,
  one player can't just unlock it for everyone.

- If any player picks the item up, it no longer counts as a valid drop for the others. Make sure
  everyone's redeemed it before doing so.

- If players split up, sometimes clients won't get notified of a drop if they're too far away from
  it. If they then travel back to it, they'll be unable to redeem it.

If you have a particularly bad connection (primarily concerning packet loss), you may also need to up
the blink duration in settings to consistently transmit information to clients.
