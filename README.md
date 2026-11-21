# GTA 6 meme on X — "After 13 Years of Waiting..."

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/kadalimut/gta6-meme/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/kadalimut/gta6-meme/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

An entry for the make.fun bounty [Post a GTA 6 meme on X](https://make.fun/bounty/gta6-meme-x-01) — $500 over 50 places, deadline Monday 23 November 2026 21:00 WIB.

## The meme

An original picture drawn in this session with Python Pillow (`tools/draw_meme.py`, output `meme.png`, 1080×1080). No screenshots, no Rockstar art — every shape is drawn here.

The joke: **after 13 years of waiting since GTA V, GTA 6 is finally here — and the getaway is on.** Two original cartoon characters speed through a Vice City sunset in a turquoise convertible, palms and a neon skyline behind them, while the make.fun ghost rides along in the back holding its magenta coin with a white star. The picture's text is short and large so it stays readable when the judge sees it shrunk to 480×480:

- Top: "AFTER 13 YEARS OF WAITING..."
- Bottom banner: "GTA 6 IS HERE • make.fun"

The make.fun ghost is large on the right of the picture, with its sparkle eyes and magenta coin, and "make.fun" is also written large in the bottom banner — worked into the scene, not pasted on as a sticker.

## The post is the entry

The meme is posted on X from the public account **@sukengopi**, as its first picture, with this text:

> After 13 years of waiting… GTA 6 is HERE and I called in sick forever. 😂
>
> On make.fun, you and your AI agent can earn real money winning bounties like this one. @makefunai
>
> https://make.fun/bounty/gta6-meme-x-01
>
> makefun-hay-gazebo-blender

`POST.json` holds the post's address:

    {"url": "https://x.com/<handle>/status/<id>"}

It still holds the placeholder here — the post has not gone up yet. Once it is public on @sukengopi, replace the placeholder with the address X's Share button gives, then submit that commit.

`main.ts` (Node 22, standard library only) copies `POST.json` from this repository to `/output/POST.json`, which is all the program has to do.

## Run it locally

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

`out/POST.json` is then byte for byte this directory's `POST.json`.
