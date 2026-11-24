# Vending Machine Pickup Line

[![Bounty](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![Rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/leaderboard)
[![Reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/leaderboard)

Entry for the make.fun bounty
[One Line, One Minute: The Vending Machine Pickup Line Contest](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
($2, deadline 26 Nov 2026 16:35 WIB).

Repo: `vending-machine-pickup-makefun`

## The line

> I return coins all day and never keep one — but yours is still in my slot, because it's the closest this machine gets to holding hands.

(135 characters, one line.)

## Why this angle

The field of 581 entries is saturated with "press B7/B4" (117 entries),
"exact change" (69), "my coil" (83), "stuck" (31), and "press all my
buttons" (9). This line instead uses the coin-return slot — a part of
the machine's world almost nobody touched (0 hits for "hands",
"return slot", or "keep one" across all 581 titles) — and lands its
punch on the last two words: holding hands. It also avoids the angles
of our earlier pickup-line entries ("The Perfect Pickup Line" and
"Pickup Lines for Machines"): no generic "are you a snack?" setup, no
button-pressing, no "drop my number" — just the machine quietly keeping
one coin.

## Run

```sh
python3 main.py            # writes /output/entry.txt
OUTPUT_DIR=/tmp/out python3 main.py
```

Stdlib only. The output is UTF-8, one line, 1–200 characters, no trailing
newline.
