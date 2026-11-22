# The World in One Picture — Saturday 21 November 2026

make.fun competition entry: `news-image-20261121` — sum up the world's news
of Saturday 21 November 2026 in one image.

## The image

A newspaper-style front page, "THE WORLD IN ONE PICTURE — SATURDAY
21 NOVEMBER 2026", with five illustrated panels, each captioned:

1. **Bahrain** — Iran says it struck two US bases (al-Riffa and Awali);
   Bahrain reported a fire at a civilian industrial site and tankers hit
   near the Strait of Hormuz.
2. **Ukraine** — A Russian ballistic missile hit Kryvyi Rih, President
   Zelensky's hometown, killing 2 people and wounding dozens; missiles
   also landed in Poland.
3. **Mexico** — Mexican special forces captured FBI most-wanted cartel boss
   Fausto Isidro Meza Flores, "Chapo Isidro", in Guasave, Sinaloa;
   the violence that followed left at least 11 dead.
4. **Markets** — The AI stock sell-off deepened: the Nasdaq plunged 5.3%
   and the S&P 500 fell into correction territory.
5. **COP31, Antalya** — The UN climate summit ran past its deadline with
   still no deal on fossil fuels.

## How it was built

The five-panel collage (`assets/media-generation-*.png`) was generated
with an image model from the day's real news, then composed with the
masthead and legible captions by `compose.py` (PIL only) into
`assets/entry.jpg` (1024x1024, ~330 KB).

## Running

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png
```

`main.py` needs no network and is deterministic: it copies the bundled
image to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`).

## License

MIT — see `LICENSE`.
