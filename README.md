# WebInvestigator

> Modular Python framework for OSINT and forensic analysis of mirrored websites.

---

## Overview

WebInvestigator is a modular Python framework designed to analyze local copies of websites (HTTrack, Wget, etc.) in order to extract technical information useful during OSINT investigations.

Rather than being dedicated to a single investigation, the framework aims to become a reusable toolbox capable of analyzing any mirrored website.

---

## Current Features

### Inventory

- Recursive scan of a mirrored website
- File inventory
- Extension statistics
- Total size calculation
- Largest files listing

### Filename Analysis

- Detection of suspicious filenames
- AI-related keywords
- Screenshot detection
- Reference image detection

### Shopify

- Parsing of `.oembed` files
- Product metadata extraction

### Reports

- Console output
- JSON export

---

## Project Structure

```
WebInvestigator/
│
├── investigations/
│   └── <Investigation>/
│
├── lib/
│   ├── analyzer/
│   ├── model/
│   ├── output/
│   ├── scanner.py
│   └── utils.py
│
├── tests/
│
├── config.py
├── main.py
└── requirements.txt
```

---

## Installation

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run:

```powershell
python main.py
```

---

## Roadmap

### Core Framework

- [x] Recursive scanner
- [x] Inventory model
- [x] Console output
- [x] JSON export

### Current Analysis Modules

- [x] Filename analyzer
- [x] OEmbed analyzer

### Planned Modules

- [ ] Shopify analyzer
- [ ] HTML analyzer
- [ ] JavaScript analyzer
- [ ] CSS analyzer
- [ ] Image analyzer
- [ ] Metadata analyzer
- [ ] Duplicate detector
- [ ] CMS detector

### Reporting

- [ ] HTML report
- [ ] CSV export
- [ ] Markdown report
- [ ] Timeline generation

---

## Long-Term Goals

- Shopify investigation toolkit
- Automatic AI-generated media detection
- Duplicate image detection
- Metadata extraction
- CMS fingerprinting
- Plugin-based architecture
- Multi-investigation support

---

## Development Status

Current version:

**v0.1.0**

The project is under active development and the architecture may evolve before the first stable release.

---

## License

License will be added before the first stable release.