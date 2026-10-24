"""Découpe la plante de l'illustration -> generes/plante.webp (IMAGE_PLANTE) et generes/masque.png.

Usage (depuis le dossier Plante) :  python3 sources/scripts/decoupe_plante.py
Il faut Pillow : pip install pillow
"""
from pathlib import Path
SOURCES = Path(__file__).resolve().parent.parent      # le dossier sources/
GENERES = SOURCES / "generes"
from collections import deque
from PIL import Image, ImageFilter
src = Image.open(SOURCES / 'illustration-ipad.webp').convert('RGB')
X0, Y0, X1, Y1 = 110, 300, 826, 582
im = src.crop((X0, Y0, X1, Y1))
W, H = im.size
rgb = im.load()
hsv = im.convert('HSV').load()

vert = Image.new('L', (W, H), 0); v = vert.load()
for y in range(H):
    for x in range(W):
        h, s, val = hsv[x, y]
        if 30 <= h <= 115 and s > 60 and val > 45:
            v[x, y] = 255
proche = vert.filter(ImageFilter.MaxFilter(9)).load()

masque = Image.new('L', (W, H), 0); m = masque.load()
SX0, SX1, SY0 = 485 - X0, 590 - X0, 455 - Y0      # zone des bâtonnets
for y in range(H):
    for x in range(W):
        r, g, b = rgb[x, y]
        h, s, val = hsv[x, y]
        bas = y > 557 - Y0
        baton = SX0 <= x <= SX1 and y >= SY0 and r > 190 and g > 150 and r - b > 35 and r > g
        sombre = val < 115 and proche[x, y] and not bas and ((25 <= h <= 130 and s > 50) or val < 45)
        if v[x, y] or baton or sombre:
            m[x, y] = 255

# bâtonnets : on ajoute aussi leur contour sombre
bat = Image.new('L', (W, H), 0); bp = bat.load()
for y in range(SY0, H):
    for x in range(SX0, SX1 + 1):
        r, g, b = rgb[x, y]
        if r > 190 and g > 150 and r - b > 35 and r > g: bp[x, y] = 255
bproche = bat.filter(ImageFilter.MaxFilter(7)).load()
for y in range(SY0, H):
    for x in range(SX0, SX1 + 1):
        if bproche[x, y] and hsv[x, y][2] < 115 and y <= 572 - Y0: m[x, y] = 255

# on garde le plus gros morceau (la plante + bâtonnets), on enlève les petites taches
def composantes(test):
    vu = bytearray(W * H); res = []
    for y0 in range(H):
        for x0 in range(W):
            i = y0 * W + x0
            if vu[i] or not test(x0, y0): continue
            q = deque([(x0, y0)]); vu[i] = 1; pts = []
            while q:
                x, y = q.popleft(); pts.append((x, y))
                for nx, ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                    if 0 <= nx < W and 0 <= ny < H:
                        j = ny * W + nx
                        if not vu[j] and test(nx, ny): vu[j] = 1; q.append((nx, ny))
            res.append(pts)
    return res
morceaux = composantes(lambda x, y: m[x, y] > 0)
morceaux.sort(key=len, reverse=True)
garde = set()
for p in morceaux:
    if len(p) > 1500: garde.update(p)
for y in range(H):
    for x in range(W):
        m[x, y] = 255 if (x, y) in garde else 0
# boucher les petits trous (pas les grands espaces entre les feuilles)
for p in composantes(lambda x, y: m[x, y] == 0):
    bord = any(x in (0, W-1) or y in (0, H-1) for x, y in p)
    if not bord and len(p) < 500:
        for x, y in p: m[x, y] = 255

masque.save(GENERES / 'masque.png')
alpha = masque.filter(ImageFilter.GaussianBlur(0.6))
out = im.convert('RGBA'); out.putalpha(alpha)
out.save(GENERES / 'plante.webp', quality=88, method=6)
print(W, H, [len(p) for p in morceaux[:6]])
