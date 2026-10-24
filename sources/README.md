# Sources des images

Les images de l'appli sont **intégrées dans `index.html`** (data URI). Ce dossier garde les originaux et les scripts qui les fabriquent, pour pouvoir les refaire. L'appli ne les charge jamais.

| Fichier | Rôle |
|---|---|
| `illustration-ipad.webp` | L'illustration de départ (la plante de Nola dans son pot NOLA, devant la fenêtre). Elle sert à tout fabriquer. |
| `pot-nola.webp` | La photo du pot que Nola a colorié, recadrée sur le pot. Référence pour les couleurs et les motifs. |
| `generes/plante.webp` | La plante découpée, avec un fond transparent. Dans `index.html` : `IMAGE_PLANTE`. |
| `generes/fond.webp` | L'illustration sans la plante, sans le cadre de l'iPad ni la barre du bas. Dans `index.html` : `IMAGE_FOND`. |
| `generes/icone.png` | L'icône de l'écran d'accueil (180 × 180). Dans `index.html` : les balises `apple-touch-icon` et `icon` du `<head>`. |
| `generes/masque.png` | Le masque de la plante (étape intermédiaire). |

## Refaire les images

Il faut Python 3 et Pillow (`pip install pillow`). Depuis le dossier `Plante/` :

```bash
python3 sources/scripts/decoupe_plante.py
```

```bash
python3 sources/scripts/effacer_plante.py
```

```bash
python3 sources/scripts/icone.py
```

1. `decoupe_plante.py` repère la plante (les verts, les contours sombres voisins et les bâtonnets en bois), garde le plus gros morceau et bouche les petits trous. Il produit `plante.webp` et `masque.png`.
2. `effacer_plante.py` remplit chaque ligne cachée par la plante avec un dégradé entre les couleurs de gauche et de droite, puis adoucit avec un léger flou. Il produit `fond.webp`. **À lancer après le premier script.**
3. `icone.py` découpe un carré centré sur le pot, puis le réduit à 180 × 180.

Ces scripts redonnent exactement les images utilisées (vérifié). Les coordonnées de découpe sont en pixels de `illustration-ipad.webp` (896 × 1195). Le pied de la plante est en (475, 567) dans l'illustration, ce qui correspond au point (429, 527) du décor (`VERS_DECOR` dans `index.html`).

## Remettre une image dans l'appli

Convertir le fichier en data URI (`data:image/webp;base64,…`), puis remplacer la valeur de la constante correspondante dans `index.html`. Par exemple :

```bash
python3 -c "import base64; print('data:image/webp;base64,' + base64.b64encode(open('sources/generes/fond.webp','rb').read()).decode())"
```

⚠️ Le dépôt GitHub est **public** : ne pas y ajouter de photo où l'on voit des personnes, ni les vraies photos de la plante prises dans l'appli.
