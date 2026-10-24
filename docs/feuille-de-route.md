# Feuille de route

## Historique (toutes les séances du plan initial sont terminées)

| Séance | Contenu | Commit |
|---|---|---|
| 1 | Accueil, nom, date, compteur, carte d'identité, illustration | `f583985` |
| 2 | Photo du jour, album Polaroïd, visionneuse | `f583985` |
| 3 | Journal quotidien (règle, feuilles, arrosage, humeur, note, dessin), courbe | `f583985` |
| 4 | « Le saviez-vous ? » (carte à retourner), glossaire, dictionnaire illustré | `f583985` |
| 5 | Arrosage et bulle de soif, mission du jour, SOS plante, badges, icône iPad | `f583985` |
| 6 | Film en accéléré, « Présenter ma plante » (diaporama et impression) | `b378957` |
| 7 | Mode chercheuse, quiz QCM, sauvegarde et restauration | `7dcb076` |
| — | Protections du stockage, rappel de sauvegarde | `230e32c` |

## Décisions prises (à respecter)

**Techniques**
- **Un seul fichier `index.html`**, explicitement demandé : pas de manifeste, pas de service worker, pas de fichiers séparés, pas de dépendance externe. Les images sont intégrées en data URI.
- **Stockage** : le journal dans localStorage, les photos et dessins dans IndexedDB. Les noms de stockage ne changent jamais. Les migrations IndexedDB ne font qu'ajouter.
- **Déploiement** : GitHub `kluzi/Plante-CM2` (branche `main`) → Netlify, relié au dépôt. Chaque push publie à la même adresse, ce qui conserve les photos.
- **Dépôt git propre au dossier `Plante/`** : le dossier personnel est lui-même un dépôt, il ne faut jamais committer depuis là.
- **Tests locaux** sur `http://127.0.0.1:8765`, pas `localhost:8765`, qui contient des données de l'utilisateur. Toujours vider les données de test après.

**Fonctionnelles** (choisies par Nola, avec 2 options proposées à chaque fois)
- Style « Jardin coloré ». Accueil illustré par **la scène de l'illustration de Nola** (fond, pot, plante découpée), qui remplace le pot dessiné en SVG. **Seuls les papillons bougent**, pas la plante.
- Polaroïds pour l'album, règle à glisser pour la taille, courbe en « tige ».
- Carte à retourner pour l'info du jour, petits dessins SVG pour le dictionnaire.
- Bulle qui parle pour la soif, autocollants pour les badges.
- Diaporama (plutôt qu'une affiche) pour la présentation. Film sans export vidéo.
- Cahier d'expérience en 5 étapes (plutôt qu'une comparaison avant / après automatique), quiz en QCM.

**Façon de travailler**
- Avant de coder : résumer en 3 lignes ce qui va être fait. Proposer 2 options à Nola pour chaque choix de design ou de contenu.
- Ne construire que la séance ou la fonction demandée. Après chaque livraison : expliquer comment tester sur l'iPad.

## Bugs connus et limites

- **Pas vérifié sur un vrai iPad** :
  - le menu Partager de la sauvegarde ;
  - l'impression ou le PDF du diaporama (logique `@media print` non testée) ;
  - l'arrêt de la règle sur un cran au doigt ;
  - le dessin au doigt sans faire défiler la page ;
  - l'appareil photo via `capture="environment"`.
- **Sans Internet**, l'appli ne se charge pas (conséquence du fichier unique sans service worker).
- **La croissance de l'illustration dépend de l'âge**, pas des vraies mesures du journal.
- **Quand la plante est petite**, de légères traces floues restent visibles sur le mur, là où la plante a été effacée de l'illustration.
- **Journal** : changer de jour sans enregistrer perd ce qui était en cours de saisie, sans prévenir.
- **Première ouverture d'une nouvelle version** chez une utilisatrice qui a déjà des données : plusieurs fêtes de badges s'enchaînent. C'est voulu (rattrapage), mais ça peut surprendre.
- **Cosmétique** :
  - le commentaire de la section A parle encore des « prochaines séances » ;
  - les commentaires « ÉCRAN n » du HTML ne sont pas dans l'ordre.
- **Sauvegarde** : le fichier contient les photos en base64, donc il peut peser plusieurs dizaines de Mo avec beaucoup de photos.

## À clarifier

- **La variété exacte** de la cucurbitacée (courge ? citrouille ?) : **à définir**. La carte d'identité indique « à confirmer ».
- La photo de la vraie plante de Nola (sur le rebord de la fenêtre), qui a inspiré le dessin, n'a pas été conservée. Ce n'est pas grave : le dessin vient maintenant de l'illustration.

Réglé : les sources des images sont archivées dans `sources/`, et l'adresse du site est https://plante-cm2.netlify.app/.

## Prochaines tâches suggérées (par priorité)

1. **Tester sur l'iPad** (https://plante-cm2.netlify.app/) les points listés plus haut, et faire une première sauvegarde des vraies données de Nola.
2. **Prévenir** quand on quitte une fiche du journal non enregistrée.
3. **Faire grandir l'illustration selon la dernière taille mesurée** (si elle existe) plutôt que selon l'âge seul.
4. **Option hors ligne** sans casser la règle du fichier unique (à discuter, peut-être impossible sur iOS sans service worker).
5. **Contenus** : enrichir les infos, missions et questions quand Nola aura tout vu (30 infos ou 20 missions par cycle).
6. **Indiquer la variété** dans la carte d'identité quand elle sera connue.
7. **Ménage cosmétique** : commentaires de la section A et numérotation des écrans HTML.
