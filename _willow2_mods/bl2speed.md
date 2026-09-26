---
pyproject_url: https://raw.githubusercontent.com/NKAYE0/BL2speed/main/bl2speed/pyproject.toml
---

Makes sprinting faster, leaving normal walking speed untouched.

Adds a single option, **Sprint Speed**, with choices from `1x` up to `10x`. The
number is how fast you sprint compared to a normal sprint, so `2x` means you
cover ground twice as quickly as vanilla sprinting does. `1x` is the game's own
speed, so the mod can be left enabled with no effect. The default is `1.5x`.

The multipliers are true multiples of vanilla sprint speed rather than raw
internal values — the mod reads the game's own sprint definition at runtime and
solves for the value that produces the requested speed, so `2x` really is twice
as fast.

### Notes

- Walking, crouching and vehicle speeds are unchanged. Only sprinting is
  affected, and disabling the mod restores the game's own value exactly.
- **Coop is untested.** The mod only edits your own game's sprint definition
  and touches no networking code, so it shouldn't affect anyone else — but BL2
  corrects player movement against the host, and I haven't tested whether a
  faster sprint gets corrected. Expect the possibility of rubber-banding,
  especially at high multipliers. Reports welcome.
- Air control is deliberately untouched, so momentum behaves exactly as vanilla
  once you leave the ground. At `3x` and above you will overshoot ledges and
  jumps you're used to.
