# Mon Journal de Plante

Application web pour que **Nola (CM2, 10 ans)** suive sa courge sur iPad : photos, journal, courbe, infos, dictionnaire, missions, badges, quiz, présentation à la classe. Elle la construit avec son père, séance par séance. Les 7 séances du plan initial sont terminées.

- Spécification fonctionnelle : [docs/specification.md](docs/specification.md)
- Architecture, stockage, organisation du code : [docs/architecture.md](docs/architecture.md)
- Décisions, bugs connus, prochaines tâches : [docs/feuille-de-route.md](docs/feuille-de-route.md)
- Originaux et scripts des images intégrées : [sources/README.md](sources/README.md)

**Site en ligne : https://plante-cm2.netlify.app/** (c'est l'adresse que Nola utilise sur l'iPad).

## Règles impératives

- **Un seul fichier `index.html`** (HTML, CSS et JS vanilla, aucune dépendance externe, images en data URI). Pas de fichier JS ou CSS séparé, pas de manifeste, pas de service worker.
- **Ne jamais renommer** la clé localStorage `"journal-de-plante"` ni la base IndexedDB `"journal-de-plante-photos"`, et ne jamais supprimer un tiroir. Sinon, les vraies photos de Nola seraient perdues. Pour un nouveau tiroir : l'ajouter à `TIROIRS` et augmenter la version d'`indexedDB.open`.
- **Tout en français**, niveau CM2, ton chaleureux. Noms de code en français. Commentaires simples, sections numérotées (CSS 1–12) et lettrées (JS A–N) pour que l'élève puisse suivre.
- **Avant de coder** : résumer en 3 lignes. **Pour chaque choix de design ou de contenu** : proposer 2 options à Nola. Ne construire que ce qui est demandé.
- Respecter le style « Jardin coloré » (variables `:root`, contours façon feutre). Sur l'accueil, seuls les papillons bougent.

## Ajouter une fonctionnalité

Ajouter une section CSS numérotée, l'écran HTML (`<section class="ecran">`), une section JS lettrée, les écouteurs dans la section « Les boutons », et une tuile `data-ecran` branchée dans le gestionnaire des tuiles. Passer les textes de l'élève dans `echapper()` et les textes pédagogiques dans `surligner()`. Appeler `verifierBadges()` après les actions qui comptent. Les nouveaux champs de données vont dans `donneesVides()`.

## Tester

- Serveur local : `.claude/launch.json`, avec `python3 -m http.server 8765`.
- **Tester sur `http://127.0.0.1:8765`**, jamais sur `localhost:8765`, qui contient des données de l'utilisateur. Vider les données de test ensuite (localStorage et les tiroirs IndexedDB).
- Vérifier en taille iPad portrait (820×1180) et paysage (1180×820), sans défilement horizontal. Pour vérifier la syntaxe : `new Function(code)` dans la page (Node n'est pas installé).
- Après chaque livraison, expliquer comment tester sur l'iPad.

## Livrer

- Le dépôt git est **propre au dossier `Plante/`**. Le dossier personnel `~` est un autre dépôt : ne jamais committer depuis là.
- Remote : `https://github.com/kluzi/Plante-CM2.git`, branche `main`. Le site Netlify est relié au dépôt : un push publie à la même adresse, et les données de l'iPad sont conservées.
- Messages de commit en français, qui décrivent la séance ou le changement.
- **Le dépôt est public** : n'y mettre aucune photo de personnes, ni les données ou photos réelles de Nola.
