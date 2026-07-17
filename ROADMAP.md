# WebInvestigator Roadmap

Roadmap for the development of WebInvestigator.

WebInvestigator is designed as a generic and modular OSINT framework
for analysing mirrored websites.

The goal is to build reusable analysis modules rather than tools
dedicated to a single investigation.

---

# Project Principles

- generic framework before investigation-specific features
- architecture evolves only when justified by a concrete need
- one analyzer = one responsibility
- analyzers never print directly to the console
- analyzers return typed models
- outputs are handled by the output layer
- small commits with one conceptual change

# Milestone 1 - Core Framework

## Scanner

- [x] Recursive file scanner
- [x] Inventory generation
- [x] File statistics
- [x] JSON export

## Core Models

- [x] Inventory
- [x] FileInfo
- [x] AnalysisResult

## Analyzers

- [x] Filename Analyzer
- [x] OEmbed Analyzer
- [x] Image Analyzer
- [ ] HTML Analyzer
- [ ] JavaScript Analyzer
- [ ] CSS Analyzer
- [ ] Shopify Analyzer

## Outputs

- [x] Console output
- [x] JSON export
- [ ] CSV export
- [ ] HTML report

## Tests

- [x] Scanner tests
- [ ] Analyzer tests
- [ ] Output tests

# Future Infrastructure

- configurable investigation selection
- unit testing
- logging
- configuration improvements

---

# Milestone 2 - Image Analysis

Goals:

- [x] image metadata
- [x] SHA-256 hashing
- [x] perceptual hashing (pHash)
- [x] duplicate detection
- [x] similarity search

Next improvements:

- [ ] configurable Hamming distance threshold
- [ ] perceptual similarity clustering
- [ ] EXIF extraction
- [ ] image thumbnails

---

# Milestone 3 - HTML Analysis

Goals:

- HTML metadata
- page titles
- meta tags
- JSON-LD
- structured data
- internal/external links

---

# Milestone 4 - Shopify Analysis

Goals:

- theme detection
- installed applications
- Shopify assets
- extensions
- sections
- Liquid hints

---

# Milestone 5 - Reporting

Goals:

- HTML report
- CSV export
- statistics
- summary dashboard

---

# Long-term Ideas

- plugin system
- investigation comparison
- image clustering
- timeline generation
- graph visualization