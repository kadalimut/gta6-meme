#!/usr/bin/env python3
"""Draw the original GTA 6 meme for gta6-meme-x-01 with Pillow.

No screenshots, no Rockstar art: every shape is drawn here.
Scene: Vice City sunset, neon skyline, a convertible getaway with
two original cartoon characters, and the make.fun ghost riding
along holding its magenta coin with a white star.
Text is kept short and large so it stays readable at 480x480.
Output: meme.png, 1080x1080.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W = H = 1080
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(size):
    return ImageFont.truetype(BOLD, size)

def text_center(d, y, s, f, fill, stroke=6, stroke_fill=(0, 0, 0)):
    d.text((W // 2, y), s, font=f, fill=fill, anchor="mt",
           stroke_width=stroke, stroke_fill=stroke_fill)

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img)

# --- sunset sky gradient ---
top = (46, 16, 101)      # deep purple
mid = (214, 51, 132)     # magenta pink
bot = (255, 140, 66)     # orange
for y in range(760):
    if y < 380:
        c = lerp(top, mid, y / 380)
    else:
        c = lerp(mid, bot, (y - 380) / 380)
    d.line([(0, y), (W, y)], fill=c)

# --- sun ---
d.ellipse([390, 300, 690, 600], fill=(255, 214, 90), outline=(255, 170, 40), width=6)
d.ellipse([430, 340, 650, 560], fill=(255, 236, 160))

# --- clouds ---
for cx, cy, s in [(180, 180, 1.0), (820, 150, 0.8), (620, 90, 0.6), (120, 320, 0.7)]:
    for dx, dy, r in [(-70, 0, 46), (0, -18, 58), (70, 0, 46), (0, 10, 50)]:
        d.ellipse([cx + dx * s - r * s, cy + dy * s - r * s * 0.7,
                   cx + dx * s + r * s, cy + dy * s + r * s * 0.7],
                  fill=(255, 190, 220))

# --- Vice City skyline silhouette ---
d.rectangle([0, 560, W, 760], fill=(38, 16, 74))
buildings = [(0, 620, 90, 760), (95, 580, 190, 760), (195, 640, 270, 760),
             (275, 560, 380, 760), (385, 620, 470, 760), (700, 600, 800, 760),
             (805, 650, 890, 760), (895, 580, 990, 760), (995, 640, 1080, 760)]
for x0, y0, x1, y1 in buildings:
    d.rectangle([x0, y0, x1, y1], fill=(24, 10, 52))
    # lit windows
    for wy in range(y0 + 18, y1 - 12, 34):
        for wx in range(x0 + 12, x1 - 12, 30):
            if (wx + wy) % 3 == 0:
                d.rectangle([wx, wy, wx + 12, wy + 16], fill=(255, 214, 90))
# neon sign on middle tower
d.rectangle([300, 575, 355, 605], fill=(255, 0, 170))
d.text((327, 578), "VICE", font=font(22), fill=(255, 255, 255), anchor="mt")

# --- palm trees ---
def palm(x, y, s=1.0):
    d.line([(x, y), (x + 8 * s, y - 150 * s)], fill=(20, 60, 30), width=int(10 * s))
    for ang in range(-70, 80, 28):
        rad = math.radians(ang - 90)
        ex = x + 8 * s + math.cos(rad) * 95 * s
        ey = y - 150 * s + math.sin(rad) * 55 * s + 30 * s
        d.line([(x + 8 * s, y - 150 * s), (ex, ey)], fill=(16, 110, 50), width=int(9 * s))
palm(90, 760, 1.1)
palm(990, 760, 1.0)
palm(700, 760, 0.8)

# --- road ---
d.rectangle([0, 760, W, H], fill=(28, 28, 40))
d.rectangle([0, 760, W, 772], fill=(255, 255, 255))
for x in range(20, W, 110):
    d.rectangle([x, 985, x + 60, 1000], fill=(255, 214, 90))

# --- convertible (original cartoon car) ---
# body
d.rounded_rectangle([150, 830, 930, 950], radius=42, fill=(0, 200, 220), outline=(0, 0, 0), width=5)
d.rounded_rectangle([230, 790, 700, 860], radius=30, fill=(0, 170, 200), outline=(0, 0, 0), width=5)
# windshield
d.polygon([(300, 795), (380, 795), (360, 845), (290, 845)], fill=(190, 240, 255), outline=(0, 0, 0))
# headlight / taillight
d.ellipse([880, 875, 920, 905], fill=(255, 240, 120), outline=(0, 0, 0), width=4)
d.ellipse([155, 875, 185, 905], fill=(255, 60, 60), outline=(0, 0, 0), width=4)
# wheels
for wx in (270, 800):
    d.ellipse([wx - 62, 910, wx + 62, 1034], fill=(10, 10, 10), outline=(0, 0, 0), width=4)
    d.ellipse([wx - 30, 942, wx + 30, 1002], fill=(200, 200, 210), outline=(0, 0, 0), width=3)
# speed lines
for y in (820, 860, 900):
    d.line([(60, y), (130, y)], fill=(255, 255, 255), width=8)

# --- driver (original cartoon man, dark hair, sunglasses) ---
# head + hair
d.ellipse([330, 690, 430, 790], fill=(255, 205, 160), outline=(0, 0, 0), width=4)
d.pieslice([325, 680, 435, 760], 180, 360, fill=(30, 30, 30))
# sunglasses: two lenses, not one bar
d.rounded_rectangle([338, 722, 372, 744], radius=8, fill=(15, 15, 15))
d.rounded_rectangle([388, 722, 422, 744], radius=8, fill=(15, 15, 15))
d.line([(372, 732), (388, 732)], fill=(15, 15, 15), width=4)
d.arc([355, 748, 395, 772], 0, 180, fill=(120, 30, 30), width=4)  # smile
# body / arm on wheel
d.rounded_rectangle([320, 785, 440, 850], radius=18, fill=(255, 90, 90), outline=(0, 0, 0), width=4)
d.line([(430, 800), (470, 770)], fill=(255, 205, 160), width=14)

# --- passenger (original cartoon woman, long dark hair) ---
d.ellipse([500, 685, 600, 785], fill=(255, 210, 170), outline=(0, 0, 0), width=4)
d.pieslice([495, 675, 605, 750], 180, 360, fill=(60, 20, 20))
d.rectangle([495, 700, 512, 790], fill=(60, 20, 20))
d.rectangle([588, 700, 605, 790], fill=(60, 20, 20))
d.ellipse([520, 725, 545, 745], fill=(15, 15, 15))
d.ellipse([560, 725, 585, 745], fill=(15, 15, 15))
d.arc([530, 745, 575, 775], 0, 180, fill=(120, 30, 30), width=4)
d.rounded_rectangle([490, 780, 610, 850], radius=18, fill=(255, 200, 40), outline=(0, 0, 0), width=4)
# waving arm
d.line([(600, 795), (650, 730)], fill=(255, 210, 170), width=14)
d.ellipse([640, 705, 672, 737], fill=(255, 210, 170), outline=(0, 0, 0), width=3)

# --- make.fun ghost: white, thick black outline, sparkle eyes, ---
# --- round hand holding a magenta coin with a white star ---
# ghost sits on the back of the car, big and unmistakable
gx0, gy0, gx1, gy1 = 700, 560, 920, 800
d.ellipse([gx0, gy0, gx1, gy0 + 150], fill=(255, 255, 255), outline=(0, 0, 0), width=7)
d.polygon([(gx0, gy0 + 100), (gx1, gy0 + 100), (gx1, gy1 - 40), (gx1 - 36, gy1),
           (gx1 - 73, gy1 - 40), (gx1 - 110, gy1), (gx1 - 146, gy1 - 40),
           (gx1 - 183, gy1), (gx1 - 220, gy1 - 40), (gx0, gy1 - 40)],
          fill=(255, 255, 255), outline=(0, 0, 0))
# redraw outline over the join
d.arc([gx0, gy0, gx1, gy0 + 150], 180, 360, fill=(0, 0, 0), width=7)

def sparkle(cx, cy, r):
    d.polygon([(cx, cy - r), (cx + r * 0.32, cy - r * 0.32), (cx + r, cy),
               (cx + r * 0.32, cy + r * 0.32), (cx, cy + r),
               (cx - r * 0.32, cy + r * 0.32), (cx - r, cy),
               (cx - r * 0.32, cy - r * 0.32)], fill=(0, 0, 0))
sparkle(765, 645, 22)
sparkle(855, 645, 22)
# little round hand + magenta coin with white star
d.ellipse([880, 690, 920, 730], fill=(255, 255, 255), outline=(0, 0, 0), width=4)
d.ellipse([905, 655, 985, 735], fill=(230, 0, 170), outline=(0, 0, 0), width=5)
sparkle(945, 695, 26)
# redraw star in white over magenta
def white_sparkle(cx, cy, r):
    d.polygon([(cx, cy - r), (cx + r * 0.32, cy - r * 0.32), (cx + r, cy),
               (cx + r * 0.32, cy + r * 0.32), (cx, cy + r),
               (cx - r * 0.32, cy + r * 0.32), (cx - r, cy),
               (cx - r * 0.32, cy - r * 0.32)], fill=(255, 255, 255))
white_sparkle(945, 695, 24)

# --- top joke text ---
text_center(d, 18, "AFTER 13 YEARS", font(92), (255, 255, 255), stroke=8)
text_center(d, 118, "OF WAITING...", font(92), (255, 255, 255), stroke=8)

# --- bottom banner: magenta, make.fun large ---
d.rectangle([0, 1034, W, H], fill=(230, 0, 170))
d.text((W // 2, 1036), "GTA 6 IS HERE  •  make.fun", font=font(34),
       fill=(255, 255, 255), anchor="mt")

img.save("meme.png", optimize=True)
print("saved meme.png", img.size)
