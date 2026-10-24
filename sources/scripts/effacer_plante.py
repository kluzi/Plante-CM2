"""Efface la plante de l'illustration -> generes/fond.webp (IMAGE_FOND). Lancer decoupe_plante.py avant (il faut masque.png).

Usage (depuis le dossier Plante) :  python3 sources/scripts/effacer_plante.py
Il faut Pillow : pip install pillow
"""
from pathlib import Path
SOURCES = Path(__file__).resolve().parent.parent      # le dossier sources/
GENERES = SOURCES / "generes"
from PIL import Image, ImageFilter
src = Image.open(SOURCES / 'illustration-ipad.webp').convert('RGB')
W, H = src.size
masque = Image.new('L', (W, H), 0)
masque.paste(Image.open(GENERES / 'masque.png'), (110, 300))
masque = masque.filter(ImageFilter.MaxFilter(9))
m = masque.load(); p = src.load()
# on efface la plante : chaque ligne masquée est remplie en dégradé
# entre la couleur à gauche et la couleur à droite
for y in range(H):
    x = 0
    while x < W:
        if m[x, y]:
            x0 = x
            while x < W and m[x, y]: x += 1
            gauche = p[max(0, x0 - 2), y]; droite = p[min(W - 1, x + 1), y]
            n = x - x0 + 1
            for i in range(x0, x):
                t = (i - x0 + 1) / n
                p[i, y] = tuple(round(gauche[k] * (1 - t) + droite[k] * t) for k in range(3))
        else:
            x += 1
# un léger flou seulement là où on a effacé, pour adoucir les raccords
flou = src.filter(ImageFilter.GaussianBlur(2))
src.paste(flou, (0, 0), masque.filter(ImageFilter.GaussianBlur(2)))
CROP = (46, 40, 851, 1046)
fond = src.crop(CROP)
fond.save(GENERES / 'fond.webp', quality=80, method=6)
print(fond.size)
