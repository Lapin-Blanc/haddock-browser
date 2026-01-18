# Philosophie - Navigateur Haddock

La documentation souligne les objectifs d'enseignement progressif du Web via un navigateur minimal pense pour un public senior. Le ton reste simple, rassurant et concret.

## Objectif
Proposer un navigateur pedagogique qui introduit les usagers aux notions du Web par paliers successifs, sans surcharge fonctionnelle ni vocabulaire inutile.

## Public cible
- Seniors ou debutants complets souhaitant comprendre les bases d'Internet.
- Formateurs qui veulent illustrer les mecanismes du Web sans se perdre dans des options complexes.

## Principes non negociables
- Minimalisme : chaque version n'introduit qu'un concept cle pour eviter la surcharge cognitive.
- Lisibilite du code : fonctions courtes, nommages explicites, pas de magie.
- Interface previsible : pas de menus ou panneaux supplementaires tant que le concept n'est pas explique.
- Progression explicite : une fonctionnalite = une intention pedagogique clairement documentee.

## Cadre technique
- Python 3.11+, PyQt6 et PyQt6-WebEngine (QWebEngineView).
- Pas de collecte de donnees ni de telemetry.
- Pas d'extensions de style navigateur moderne (comptes, synchronisation, etc.).

## Versions pedagogiques cibles
- v0 : barre d'adresse, bouton Aller, zone d'affichage de page.
- v1 : boutons retour/avance/recharger + synchronisation de la barre d'adresse.
- v2 : page d'accueil configurable et historique simple.
- v3 : onglets (optionnel et uniquement si justifie par un besoin pedagogique).
- v4 : favoris (optionnel, limite a un cas d'apprentissage clair).

## Regles de contribution
- Ne jamais ajouter de fonctionnalite non demandee.
- Favoriser des changements petits et verifies.
- Eviter les refactors cosmetiques.
- Garder `src/app.py` executable via `python src/app.py`.
