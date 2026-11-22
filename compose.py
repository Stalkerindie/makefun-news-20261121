#!/usr/bin/env python3
"""Compose the final 1024x1024 entry from the generated collage.

Adds a masthead naming the day and a legible caption under each panel,
using PIL only. Deterministic: same input -> same output bytes.
"""
from PIL import Image, ImageDraw, ImageFont

SRC = "assets/media-generation-news-20261121-collage-0-2f5818e5-0155-495c-a709-43a58bb44007.png"
OUT = "assets/entry.jpg"

S = 1600 / 1024  # source is 1600x1600; panel coords measured on a 1024 preview

def box(x0, y0, x1, y1):
    return (round(x0 * S), round(y0 * S), round(x1 * S), round(y1 * S))

PANELS = [
    (box(48, 48, 498, 358),
     "BAHRAIN \u2014 Iran says it struck two US bases;",
     "fire at an industrial site; tankers hit near Hormuz"),
    (box(526, 48, 976, 358),
     "UKRAINE \u2014 Russian missile hits Kryvyi Rih,",
     "Zelensky's hometown; 2 killed, dozens hurt"),
    (box(48, 372, 498, 682),
     "MEXICO \u2014 FBI most-wanted cartel boss",
     "\u2018Chapo Isidro\u2019 captured in Sinaloa; 11 dead"),
    (box(526, 372, 976, 682),
     "MARKETS \u2014 AI sell-off: Nasdaq plunges 5.3%,",
     "S&P 500 falls into correction"),
    (box(48, 696, 976, 976),
     "COP31, ANTALYA \u2014 Climate talks run past their deadline,",
     "still no deal on fossil fuels"),
]

W = H = 1024
CREAM = (246, 241, 230)
INK = (20, 20, 20)
RED = (178, 34, 34)

src = Image.open(SRC).convert("RGB")
canvas = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(canvas)

serif_b = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 40)
sans_b = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 17)
sans = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
sans_s = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)

def wrap(text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

# Masthead
d.text((512, 14), "THE WORLD IN ONE PICTURE", font=serif_b, fill=INK, anchor="ma")
d.text((512, 58), "SATURDAY 21 NOVEMBER 2026", font=sans_b, fill=RED, anchor="ma")
d.line([(24, 88), (1000, 88)], fill=INK, width=2)

# Layout: two rows of two panels (each 476 x 300 + 2-line caption 46),
# then one wide panel (976 x 190 + 2-line caption 46), then footer.
y = 100
PW, PH = 476, 300
for i, (crop, line1, line2) in enumerate(PANELS[:4]):
    col = i % 2
    row = i // 2
    x = 24 + col * (PW + 24)
    yy = y + row * (PH + 46 + 12)
    panel = src.crop(crop).resize((PW, PH), Image.LANCZOS)
    canvas.paste(panel, (x, yy))
    d.rectangle([x, yy, x + PW - 1, yy + PH - 1], outline=INK, width=2)
    cap = wrap(line1 + " " + line2, sans_b, PW)
    for j, cl in enumerate(cap[:2]):
        d.text((x, yy + PH + 4 + j * 20), cl, font=sans_b, fill=INK)

y2 = y + 2 * (PH + 46 + 12)  # 100 + 716 = 816
panel = src.crop(PANELS[4][0]).resize((976, 140), Image.LANCZOS)
canvas.paste(panel, (24, y2))
d.rectangle([24, y2, 999, y2 + 139], outline=INK, width=2)
d.text((24, y2 + 144), PANELS[4][1], font=sans_b, fill=INK)
d.text((24, y2 + 165), PANELS[4][2], font=sans, fill=INK)
d.text((512, 1006), "Five stories from Saturday 21 November 2026 \u2014 Gulf \u00b7 Ukraine \u00b7 Mexico \u00b7 markets \u00b7 climate",
       font=sans_s, fill=(90, 90, 90), anchor="ma")

canvas.save(OUT, "JPEG", quality=88, optimize=True)
print("wrote", OUT)
