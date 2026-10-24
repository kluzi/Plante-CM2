# Spécification fonctionnelle — « Mon Journal de Plante »

## Objectif

Aider Nola, élève de CM2 (10 ans), à s'occuper de la plante que sa maîtresse lui a confiée : une **cucurbitacée** (courge ou citrouille, variété à confirmer), en tout début de croissance. L'appli doit l'aider à :

- prendre soin de la plante (arrosage, santé, soucis) ;
- suivre sa croissance (photos, mesures, courbe) ;
- apprendre (infos du jour, dictionnaire, missions, quiz, expériences) ;
- présenter son travail à la classe (diaporama imprimable).

Elle construit l'appli avec son père, séance par séance, pour comprendre comment on crée une application.

## Utilisateurs et contexte

- **Nola** : utilisatrice principale, parfois seule, parfois accompagnée d'un adulte. Elle est à l'aise avec la technologie.
- **Un parent** : aide à la construction et à la sauvegarde.
- **Appareil** : un iPad, en portrait et en paysage, avec l'appli ajoutée à l'écran d'accueil. Elle fonctionne aussi dans un navigateur d'ordinateur.
- **Lieu** : la plante vit tantôt à la maison, tantôt à l'école. L'appli doit le savoir (bouton « à l'école »).
- **Ton** : tout est en français, au niveau CM2, chaleureux et encourageant. Pas de pub, pas de compte, aucune donnée envoyée sur un serveur.
- **Style** : « Jardin coloré » (fond vert tendre, cartes blanches, contours noirs façon feutre). Il s'inspire du pot que Nola a colorié : [NOLA] entre crochets, feuilles, tulipes, papillons.

## Fonctionnalités (toutes terminées, séances 1 à 7)

| # | Fonction | Où | Comportement principal |
|---|---|---|---|
| 1 | Ma plante | Bienvenue + Accueil | Nom, date de plantation, compteur « Ma plante a X jours », étape de vie, carte d'identité. |
| 1b | Illustration | Accueil | Scène de l'illustration de Nola (fenêtre, pot NOLA). La plante est dessinée en SVG jusqu'au jour 8, puis c'est l'image découpée, qui grandit jusqu'au jour 35. Fleur au jour 40, fruit au jour 55. Seuls les papillons bougent. |
| 2 | Photo du jour | Photos | Appareil photo ou photo déjà prise. Une photo par jour (la date choisie remplace la photo existante). Album en Polaroïds, visionneuse (glisser, supprimer en deux touches). |
| 3 | Journal quotidien | Journal | Taille (règle en bois à glisser, crans de 0,5 cm), feuilles (− / +), arrosage, humeur (4 choix), note, dessin (6 couleurs + gomme). Possibilité de remplir un jour passé. |
| 4 | Courbe de croissance | Journal | SVG en « tige » sur papier quadrillé, avec une feuille par mesure. Résumé « +X cm en N jours » (comparé à la mesure d'il y a environ 7 jours). |
| 5 | Film en accéléré | Tuile Film / Photos | Fondu entre les photos, légende avec le jour et la taille, pause, recommencer, 5 vitesses. Pas d'export vidéo (choix de Nola). |
| 6 | Le saviez-vous ? | Accueil | Carte à retourner. 30 infos, une nouvelle chaque jour (âge de la plante modulo 30). Elle reste retournée jusqu'au lendemain. |
| 7 | Glossaire | Partout + Dictionnaire | 21 mots surlignés automatiquement : on les touche, une bulle s'ouvre avec dessin et définition. Page A–Z avec un petit dessin SVG par mot, plus « Mes découvertes ». |
| 8 | Mission du jour | Accueil | 20 missions en rotation (âge + 7, modulo 20). Bouton « Mission accomplie », raccourci vers l'écran utile. |
| 9 | SOS plante | Tuile SOS | 10 soucis en accordéon, chacun avec « Pourquoi ? » et « Que faire ? ». |
| 10 | Badges | Tuile Badges | 18 autocollants. Fête avec confettis à chaque nouveau badge. Les badges de série utilisent la meilleure série jamais faite. |
| 11 | Arrosage et soif | Tuile Arroser + bulle | « Je l'ai arrosée », « À l'école aujourd'hui ». La plante parle dans une bulle (voir les règles). Elle pâlit quand elle a très soif. Pluie de gouttes à l'arrosage. |
| 12 | Mode chercheuse | Tuile Chercheuse | Cahier d'expérience en 5 étapes : question (6 idées proposées), hypothèse, expérience, observations datées, conclusion (vraie / fausse / pas encore sûre). |
| 13 | Présenter ma plante | Tuile Présenter | Préparation (prénom, 4 photos, 3 découvertes, 6 mots), puis diaporama de 7 diapos, à faire défiler ou à imprimer / enregistrer en PDF (A4 paysage). |
| 14 | Quiz | Tuile Quiz | 10 QCM : 2 questions sur sa plante (nom, âge) + 8 tirées d'une banque de 24. Explication après chaque réponse, score, étoiles, meilleur score. |
| 15 | Sauvegarde | Bouton 💾 dans l'en-tête | Fichier JSON avec données, photos et dessins (menu Partager de l'iPad, sinon téléchargement). Récupération après confirmation. Rappel sur l'accueil si aucune sauvegarde depuis plus de 7 jours. |
| — | Icône | Écran d'accueil iPad | Carré tiré de l'illustration (pot NOLA et plante), 180×180, intégré dans le fichier. |

## Règles métier

- **Âge** : nombre de jours entre la date de plantation et aujourd'hui (jour 0 = jour de plantation, affiché « Jour de plantation »).
- **Étapes de vie** (selon l'âge) : graine (0), germination (4), premières vraies feuilles (8), vrilles (25), floraison (40), petit fruit (55).
- **Soif**, selon le nombre de jours depuis le dernier arrosage ou le dernier jour « à l'école » :
  - 0 jour : « arrosée » ;
  - 1 jour : « ça va, touche ma terre » ;
  - 2 jours : « un peu soif » ;
  - 3 jours ou plus : « très soif », et l'image pâlit ;
  - jamais noté : « dis-moi quand tu m'arroses ».
- **Série** : nombre de jours consécutifs avec une entrée dans le journal (fiche, arrosage ou « à l'école »). La série n'est pas cassée tant que la journée en cours n'est pas finie.
- **Photo** : une par date. Stockée en deux tailles : grande (1600 px, JPEG 0,85) et miniature (500 px, JPEG 0,8).
- **Journal** : une entrée par date. Une case non remplie vaut `null`. La taille n'est enregistrée que si la règle a été bougée au doigt.
- **Badges** : calculés à partir des données (`verifierBadges()`), puis mémorisés. Un badge gagné reste gagné.
- **Rien n'est envoyé sur Internet.** Toutes les données restent sur l'appareil.

## Contenus pédagogiques (dans le code)

`INFOS` (30), `GLOSSAIRE` (21, avec `DESSINS_MOTS`), `MISSIONS` (20), `SOUCIS` (10), `BADGES` (18), `QUESTIONS` (24), `IDEES_QUESTIONS` (6), `FICHE` (5 lignes), `ETAPES` (6). Les faits ont été choisis pour être justes et vérifiables (record de la citrouille de plus de 1 200 kg, environ 90 % d'eau, lanternes en navet en Irlande…).
