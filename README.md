# Web Investigator

> Framework Python d'analyse OSINT de sites Web aspirés (HTTrack, Wget, etc.)

---

## Objectif

Web Investigator est un outil permettant d'analyser automatiquement une copie locale d'un site Web.

L'objectif est de produire un rapport technique contenant notamment :

- inventaire des fichiers
- analyse des médias
- extraction des métadonnées
- analyse HTML
- analyse JavaScript
- détection de CMS
- analyse Shopify
- génération de rapports

Le projet est volontairement modulaire afin de pouvoir ajouter facilement de nouveaux analyseurs.

---

## État actuel

Fonctionnalités disponibles :

- ✅ Scan récursif du miroir
- ✅ Inventaire des extensions
- ✅ Calcul de la taille totale
- ✅ Classement des plus gros fichiers
- ✅ Détection de noms de fichiers intéressants
- ✅ Lecture des fichiers `.oembed`
- ✅ Export JSON de l'inventaire

---

## Architecture

```
AtelierDeLea_OSINT
│
├── main.py
├── config.py
├── requirements.txt
│
├── lib
│   ├── extractor.py
│   ├── parser.py
│   ├── oembed_parser.py
│   ├── report.py
│   └── utils.py
│
├── reports
│   ├── csv
│   ├── html
│   └── json
│
└── logs
```

---

## Lancement

Créer l'environnement virtuel :

```powershell
python -m venv .venv
```

Activation :

```powershell
.\.venv\Scripts\Activate.ps1
```

Installation des dépendances :

```powershell
pip install -r requirements.txt
```

Lancement :

```powershell
python main.py
```

---

## Roadmap

### Phase 1

- [x] Inventaire du miroir
- [x] Export JSON

### Phase 2

- [x] Analyse des fichiers `.oembed`
- [x] Détection de noms de fichiers remarquables

### Phase 3

- [ ] Analyse HTML
- [ ] Analyse JavaScript
- [ ] Analyse CSS

### Phase 4

- [ ] Analyse des images
- [ ] EXIF
- [ ] SHA256
- [ ] Perceptual Hash
- [ ] Détection des doublons

### Phase 5

- [ ] Détection automatique du CMS
- [ ] Shopify
- [ ] WordPress
- [ ] WooCommerce
- [ ] Prestashop

### Phase 6

- [ ] Rapport HTML complet
- [ ] Rapport CSV
- [ ] Rapport JSON enrichi

---

## Objectif final

Construire un framework OSINT réutilisable permettant d'analyser rapidement une copie locale d'un site Web afin d'en extraire les informations techniques les plus pertinentes.