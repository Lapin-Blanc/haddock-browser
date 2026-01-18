# Versioning et releases

## Strategie
- Branches courtes pour chaque travail pedagogique.
- Merge dans `main` uniquement lorsque la version est stable et executable.
- Tag annoté sur `main` pour marquer une version livrable.
- Chaque tag correspond a une GitHub Release avec des notes orientees apprentissage.

## Convention de tags
- `v0.1.0`, `v1.0.0`, etc.
- La version suit SemVer, mais le rythme est guide par les paliers pedagogiques.

## Roadmap pedagogique (titres)
- v0 : pre-version interne
- v1 : bases de navigation
- v2 : navigation avancee
- v3 : parametres et page d'accueil
- v4 : favoris

## Workflow Git complet (exemple)
```bash
git checkout -b chore/v0-1-0-docs
git add .
git commit -m "docs: add versioning notes"
git checkout main
git merge --no-ff chore/v0-1-0-docs
git push origin main

git tag -a v0.1.0 -m "v0.1.0: pedagogic release"
git push origin v0.1.0
```

## Releases et artefacts
Une release GitHub est creee automatiquement a chaque tag `vX.Y.Z`.
Le workflow CI/CD construit un standalone Windows via `build-scripts/build-win.ps1` et attache un zip a la release.
Le standalone (dossier `.dist`) est plus lourd qu'un binaire simple, mais reste facile a distribuer aux eleves.
