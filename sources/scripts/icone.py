"""Fabrique l'icône de l'écran d'accueil de l'iPad -> generes/icone.png (180 x 180).

Usage (depuis le dossier Plante) :  python3 sources/scripts/icone.py
Il faut Pillow : pip install pillow
"""
from pathlib import Path
SOURCES = Path(__file__).resolve().parent.parent      # le dossier sources/
GENERES = SOURCES / "generes"
from PIL import Image

src = Image.open(SOURCES / "illustration-ipad.webp").convert("RGB")
# un carré centré sur le pot et la plante
carre = src.crop((92, 296, 844, 1046)).resize((720, 720), Image.LANCZOS)
carre.resize((180, 180), Image.LANCZOS).save(GENERES / "icone.png", optimize=True)
