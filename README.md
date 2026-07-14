# WebInvestigator

> Modular Python framework for offline OSINT and forensic analysis of mirrored websites.

---

## Overview

WebInvestigator is an open-source Python framework designed to analyze local copies of websites mirrored with tools such as HTTrack or Wget.

Rather than being dedicated to a single investigation, WebInvestigator provides a reusable and extensible architecture capable of analyzing any mirrored website through independent analysis modules.

The project focuses on producing structured technical information that can be used during OSINT investigations, digital forensics, or website analysis.

---

## Project Principles

- Generic framework before investigation-specific features
- Architecture evolves only when justified by a concrete need
- One analyzer = one responsibility
- Analyzers never print directly to the console
- Analyzers return typed models
- Outputs are handled by the output layer
- Small commits with one conceptual change

---

# Architecture

```
Mirrored Website
        │
        ▼
     Scanner
        │
        ▼
    Inventory
        │
        ▼
 AnalysisResult
        │
        ├── Filename Analyzer
        ├── OEmbed Analyzer
        ├── Image Analyzer
        ├── HTML Analyzer
        ├── JavaScript Analyzer
        ├── CSS Analyzer
        └── Shopify Analyzer
        │
        ▼
       Outputs
```

---

## Current Features

### Scanner

- Recursive directory scanning
- Complete file inventory
- Extension statistics
- Total size calculation
- Largest files detection

### Implemented Analyzers

#### Filename Analyzer

- Suspicious filename detection
- AI-related filename detection
- Screenshot detection
- Reference image detection

#### OEmbed Analyzer

- `.oembed` parsing
- Product metadata extraction

### Outputs

- Console reporting
- JSON export

---

## Project Structure

```text
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
├── ROADMAP.md
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Nucle0n/WebInvestigator.git
cd WebInvestigator
```

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

Run the framework:

```powershell
python main.py
```

---

## Development Roadmap

The complete development roadmap is available in:

```
ROADMAP.md
```

Current focus:

- Core framework
- Image Analyzer
- HTML Analyzer
- Shopify Analyzer
- Reporting improvements

---

## Development Status

Current version:

**v0.1.0**

Current status:

- Core framework operational
- Modular architecture established
- Active development

---

## Planned Analysis Modules

- Image analysis
- HTML analysis
- JavaScript analysis
- CSS analysis
- Shopify analysis
- Metadata extraction
- Duplicate detection
- CMS fingerprinting

---

## Long-Term Vision

The long-term goal is to build a generic, modular and extensible framework capable of analyzing mirrored websites independently of the underlying technology.

Future capabilities may include:

- Plugin system
- Multi-investigation support
- Image similarity analysis
- Timeline generation
- Graph visualization
- Investigation comparison

---

## License

A license will be added before the first stable release.