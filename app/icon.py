"""Genera el icono pixel art de la app (dado de hueso con 5 pips y brillo de cripta).

Escribe los mipmaps de Android y store/icon-512.png para Google Play.
Uso: python icon.py
"""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(ROOT, 'android', 'app', 'src', 'main', 'res')
STORE = os.path.join(ROOT, 'store')

N = 54  # 108dp adaptive canvas -> 2 px per dp cell at mdpi, integer at every density
BG = (11, 10, 18, 255)
OUT = (20, 14, 24, 255)
BONE = [(122, 104, 84, 255), (184, 166, 136, 255), (226, 214, 188, 255), (248, 242, 226, 255)]
PIP = [(70, 14, 28, 255), (150, 30, 50, 255)]
GLOW = [(30, 22, 48, 255), (52, 34, 82, 255), (84, 52, 120, 255)]
GOLD = [(232, 176, 74, 255), (255, 226, 140, 255)]
BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


def foreground():
    im = Image.new('RGBA', (N, N), (0, 0, 0, 0))
    px = im.load()
    c = (N - 1) / 2
    # dithered purple glow behind the die
    for y in range(N):
        for x in range(N):
            d = ((x - c) ** 2 + (y - c) ** 2) ** .5
            t = 1 - d / 22
            if t <= 0:
                continue
            lvl = t * 3 + BAYER[y % 4][x % 4] / 16 - .5
            if lvl >= 0:
                px[x, y] = GLOW[min(2, int(lvl))]
    # die body 24x24, rounded corners, outline + bevel
    s, o = 24, (N - 24) // 2
    def inside(x, y, r=3):
        cx = min(max(x, r), s - 1 - r)
        cy = min(max(y, r), s - 1 - r)
        return (x - cx) ** 2 + (y - cy) ** 2 <= r * r + .5
    for y in range(s):
        for x in range(s):
            if not inside(x, y):
                continue
            edge = not (inside(x - 1, y) and inside(x + 1, y) and inside(x, y - 1) and inside(x, y + 1))
            if edge:
                col = OUT
            elif x >= s - 3 or y >= s - 3:
                col = BONE[0] if (x >= s - 2 or y >= s - 2) else BONE[1]
            elif x <= 2 or y <= 2:
                col = BONE[3]
            else:
                col = BONE[2]
            px[o + x, o + y] = col
    # pips (5), 4x4 with a lit corner
    for gx, gy in [(5, 5), (15, 5), (10, 10), (5, 15), (15, 15)]:
        for y in range(4):
            for x in range(4):
                if (x in (0, 3)) and (y in (0, 3)):
                    continue
                px[o + gx + x, o + gy + y] = PIP[1] if (x + y) <= 2 else PIP[0]
    # chipped corner and a crack, so it reads as old bone
    for x, y in [(19, 3), (20, 4), (20, 5), (21, 6)]:
        px[o + x, o + y] = BONE[1]
    # gold embers
    for x, y, k in [(10, 12, 1), (11, 13, 0), (43, 15, 1), (42, 16, 0), (40, 41, 1), (13, 39, 0), (45, 33, 0)]:
        px[x, y] = GOLD[k]
    return im


def full(fg):
    im = Image.new('RGBA', (N, N), BG)
    im.alpha_composite(fg)
    return im


def up(im, size):
    big = im.resize((im.width * 16, im.height * 16), Image.NEAREST)
    return big if big.width == size else big.resize((size, size), Image.LANCZOS)


def circle(im):
    m = Image.new('L', (im.width * 4, im.height * 4), 0)
    from PIL import ImageDraw
    ImageDraw.Draw(m).ellipse((0, 0, m.width - 1, m.height - 1), fill=255)
    m = m.resize(im.size, Image.LANCZOS)
    out = Image.new('RGBA', im.size, (0, 0, 0, 0))
    out.paste(im, (0, 0), m)
    return out


fg = foreground()
whole = full(fg)
legacy = whole.crop((9, 9, N - 9, N - 9))  # legacy icons show the central 72dp
for dens, k in {'mdpi': 1, 'hdpi': 1.5, 'xhdpi': 2, 'xxhdpi': 3, 'xxxhdpi': 4}.items():
    d = os.path.join(RES, f'mipmap-{dens}')
    os.makedirs(d, exist_ok=True)
    fg.resize((int(108 * k),) * 2, Image.NEAREST).save(os.path.join(d, 'ic_launcher_foreground.png'))
    up(legacy, int(48 * k)).save(os.path.join(d, 'ic_launcher.png'))
    circle(up(legacy, int(48 * k))).save(os.path.join(d, 'ic_launcher_round.png'))
os.makedirs(STORE, exist_ok=True)
up(legacy, 512).convert('RGB').save(os.path.join(STORE, 'icon-512.png'))
print('iconos generados')
