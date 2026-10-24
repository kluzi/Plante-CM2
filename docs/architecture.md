# Architecture technique

## Vue d'ensemble

- **Un seul fichier : `index.html`** (environ 500 Ko, 4 600 lignes). HTML, CSS et JavaScript « vanilla », sans bibliothèque, sans étape de construction, sans dépendance externe.
- Les **images sont intégrées** sous forme de data URI : icône PNG 180×180, `IMAGE_FOND` et `IMAGE_PLANTE` en WebP.
- **Pas de service worker ni de manifeste** (choix : un seul fichier). L'appli a donc besoin d'Internet pour se charger. On l'installe sur l'iPad avec Partager → « Sur l'écran d'accueil », grâce aux balises `apple-mobile-web-app-*`.
- **Déploiement** : on pousse sur GitHub `kluzi/Plante-CM2` (dépôt public, branche `main`). Le site Netlify, relié au dépôt, publie automatiquement, toujours à la même adresse : **https://plante-cm2.netlify.app/**.

## Autres fichiers du dépôt

| Fichier | Rôle |
|---|---|
| `index.html` | Toute l'application. |
| `CLAUDE.md` | Les instructions pour reprendre le développement. |
| `docs/` | La spécification, cette architecture, la feuille de route. |
| `sources/` | Les originaux des images (illustration, pot recadré), les images produites et les scripts Python/Pillow pour les refaire. Voir `sources/README.md`. L'appli ne les charge pas. |
| `.gitignore` | Ignore `.claude/` et `.DS_Store`. |
| `.claude/launch.json` | (Non versionné) Serveur local de test : `python3 -m http.server 8765`. |

## Organisation du fichier `index.html`

L'ordre est le suivant : `<head>` (balises iPad, icône) → `<style>` → écrans HTML → fenêtres → `<script>` des images → `<script>` principal.

### CSS (`<style>`, sections numérotées)

1. Couleurs (variables `:root`, inspirées du pot)
2. Page
3. Briques de base (`.carte`, `.bouton`, `.arc-en-ciel`)
4. Bienvenue
5. Accueil (plante, tuiles, carte d'identité, message)
6. Photos (séance 2)
7. Journal (séance 3)
8. Le saviez-vous ? et dictionnaire (séance 4)
9. Arrosage, missions, SOS, badges (séance 5)
10. Film et présentation, y compris `@media print` (séance 6)
11. Chercheuse, quiz, sauvegarde (séance 7)
12. iPad en paysage (grille sur deux colonnes)

Viennent ensuite les règles pour les petits écrans et `prefers-reduced-motion`.

### Écrans HTML (`<section class="ecran">`, un seul visible à la fois)

`ecran-bienvenue`, `ecran-accueil`, `ecran-photos`, `ecran-journal`, `ecran-dictionnaire`, `ecran-sos`, `ecran-badges`, `ecran-presentation`, `ecran-chercheuse`, `ecran-quiz`, `ecran-sauvegarde`.

Dans le fichier, les commentaires « ÉCRAN n » ne sont pas dans l'ordre. C'est seulement cosmétique.

Les **fenêtres par-dessus** sont `#modal-ajout` (photo), `#visionneuse`, `#modal-arrosage`, `#modal-badge` (fête), `#film`, `#diaporama` et `#bulle-mot`. On les ouvre et ferme avec l'attribut `hidden`.

### JavaScript (`<script>`, sections A à N)

| Section | Contenu |
|---|---|
| (bloc à part) | `IMAGE_FOND`, `IMAGE_PLANTE` : longues data URI, à ne pas lire. |
| A. Données | `CLE_MEMOIRE`, `donneesVides()`, `charger()`, `enregistrer()`, `donnees`. |
| B. Dates | `lireDate`, `texteDeDate`, `aujourdhuiTexte`, `veille`, `ecartEnJours`, `ageEnJours`, `dateEnFrancais`, `dateCourte`. |
| C. Étapes | `ETAPES`, `etapeDuJour()`. |
| D. Fiche | `FICHE`, `afficherFiche()`. |
| E. Dessin | E1 le décor (`VERS_DECOR`), E2 la courge (`dessinerPlante`, `cotyledon`, `JOUR_IMAGE`), `dessinerFruit`, `dessiner(idSvg, jours, assoiffee)`. |
| F. Écrans | `montrerEcran(id)`, `afficherAccueil()`, `afficherBienvenue()`. |
| G. Photos | G1 la boîte IndexedDB (`ouvrirBoite`, `dansLeTiroir(tiroir, mode, action)`), G2 réduction, G3 écran, G4 ajout, G5 visionneuse. |
| H. Journal | H1 entrées (`entreeDu`, `rangerEntree`, `derniereValeur`, `echapper`), H2 fiche (règle, feuilles, pastilles, dessin), H3 `dessinerCourbe(idSvg, idResume)`, H4 carnet. |
| I. Savoir | I1 `INFOS`, I2 `GLOSSAIRE` et `surligner(texte, sauf)`, I3 `DESSINS_MOTS`, I4 la bulle, I5 la page dictionnaire. |
| J. Soins | J1 arrosage et soif (`etatSoif`, `PAROLES_PLANTE`), J2 séries, J3 `MISSIONS`, J4 `SOUCIS`, J5 `BADGES` et `verifierBadges()`. |
| K. Film et présentation | K1 film, K2 préparation (`donnees.presentation`), K3 diaporama et impression. |
| L. Chercheuse, quiz, sauvegarde | L1 expériences, L2 `QUESTIONS` et quiz, L3 export et import. |
| M. Boutons | Tous les `addEventListener` (les tuiles se branchent par `data-ecran`). |
| N. Démarrage | Titres arc-en-ciel, fiche, `storage.persist()`, premier écran, mise à jour au retour sur l'appli. |

## Stockage

### localStorage — clé `"journal-de-plante"` (⚠️ ne jamais la renommer)

```js
{
  version: 1,
  plante: { nom, dateDepart: "AAAA-MM-JJ" },
  journal: [ { date, taille|null, feuilles|null, arrosage: "oui"|"non"|null,
               humeur: "super"|"bien"|"bof"|"triste"|null, note, aUnDessin, lieu?: "ecole"|null } ],
  badges: [ "cle", … ],
  missions: { "AAAA-MM-JJ": numeroMission },
  experiences: [ { id, question, hypothese, protocole, observations: [{date, texte}],
                   resultat: "vraie"|"fausse"|"incertain"|null, conclusion, creeeLe } ],
  quiz: { meilleur, parties },
  presentation?: { prenom, photos: [dates], infos: [numeros], mots: [cles] },
  reglages: { carteRetournee, nbCartes, derniereSauvegarde }
}
```

`charger()` fusionne avec `donneesVides()`. Un nouveau champ de premier niveau apparaît donc tout seul chez les anciens utilisateurs.

### IndexedDB — base `"journal-de-plante-photos"`, version 2 (⚠️ ne jamais la renommer)

- Tiroir `photos` (clé `date`) : `{ date, grande: Blob, miniature: Blob, ajouteeLe }`.
- Tiroir `dessins` (clé `date`) : `{ date, image: Blob PNG }`, ajouté en version 2.
- **Pour ajouter un tiroir** : l'ajouter à `TIROIRS` et passer à la version 3. `onupgradeneeded` ne crée que ce qui manque. Ne jamais supprimer de tiroir.

### Fichier de sauvegarde

`ma-plante-AAAA-MM-JJ.json` contient `{ format: "journal-de-plante", version: 1, creeeLe, donnees, photos: [{date, ajouteeLe, grande, miniature}], dessins: [{date, image}] }`. Les images y sont des data URI.

Les données sont rattachées à **l'adresse du site** et, sur l'iPad, à l'icône de l'écran d'accueil, qui a une mémoire séparée de Safari.

## Dessin de la plante

- Le SVG de la scène fait 805 × 1006 (`IMAGE_FOND`, c'est-à-dire l'illustration dont on a effacé la plante).
- La plante utilise ses propres coordonnées : le pied de la tige est en `(150, 236)`. `VERS_DECOR` la pose dans la terre du pot.
- Avant `JOUR_IMAGE` (jour 9), la plante est dessinée en SVG : graine, crochet, cotylédons. Ensuite, c'est `IMAGE_PLANTE`, la plante découpée dans l'illustration. Elle est agrandie à partir du pied, de 0,4 à 1, jusqu'au jour 35.
- Quand la plante a très soif, `dessiner(..., true)` applique un filtre `feColorMatrix` de désaturation.
- Les images ont été produites avec des scripts Python/Pillow, archivés dans `sources/scripts/`. Ils redonnent exactement les mêmes images.

## Conventions de code

- **Tout est en français** : les noms de variables et de fonctions, et des commentaires simples pour qu'une élève de CM2 puisse suivre.
- **Un ajout de fonctionnalité** = une section CSS numérotée, des écrans HTML, une section JS lettrée (avec des sous-parties numérotées), le branchement dans la section « Boutons », une tuile `data-ecran`. Appeler `verifierBadges()` après une action qui peut faire gagner un badge.
- Tout texte tapé par l'élève passe par `echapper()`. Les textes pédagogiques passent par `surligner()` pour faire apparaître les mots du glossaire.
- Les messages courts s'affichent avec `montrerMessage(texte)`. Une suppression demande toujours de toucher deux fois.
