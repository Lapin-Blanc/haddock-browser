# Navigateur Haddock

Navigateur web pedagogique minimaliste developpe en Python (PySide6). Chaque version introduit uniquement les mecanismes indispensables, afin d'accompagner un public senior qui decouvre Internet sans surcharge fonctionnelle.

## Objectif
Offrir un support concret pour expliquer le Web par iterations courtes : la barre d'adresse, la navigation, puis quelques notions optionnelles quand elles servent un scenario d'apprentissage precis.

## Public cible
- Seniors ou debutants complets qui souhaitent comprendre comment naviguer sur Internet.
- Formateurs qui veulent montrer les briques de base d'un navigateur sans distraire avec des options modernes.

## Installation
Prerequis : Python 3.11+ et la dependance PySide6 (QtWebEngine integre).

```bash
python -m venv .venv
# Windows :
.venv\Scripts\activate
# Linux / macOS :
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```

## Execution

```bash
python src/app.py
```

## Roadmap pedagogique (v0 -> v4)
- **v0** : barre d'adresse, bouton Aller, affichage de la page chargee.
- **v1** : boutons retour / avance / recharger + barre d'adresse synchronisee.
- **v2** : page d'accueil simple et historique lineaire.
- **v3** : onglets, uniquement si le besoin pedagogique est etabli.
- **v4** : favoris limites aux cas d'apprentissage utiles.
