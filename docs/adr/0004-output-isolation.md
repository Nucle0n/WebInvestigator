# ADR-0004
# Output Isolation

> **This ADR separates analysis from presentation by restricting all output generation to dedicated output modules.**

**Status:** Accepted

**Date:** 2026-07-18

---

## Context

WebInvestigator is intended to support multiple ways of presenting investigation results.

Command-line output, JSON exports, graphical interfaces and future integrations should all be able to consume the same analysis without modifying the analyzers themselves.

If analyzers were allowed to print information directly, they would become coupled to a particular presentation format.

Every new interface would require modifying analysis code instead of simply introducing a new output module.

Presentation concerns would gradually spread throughout the codebase, making analyzers less reusable and more difficult to maintain.

A strict separation between analysis and presentation was therefore required.

---

## Decision

Analyzers must never generate user-facing output.

Their responsibility ends once they have populated the appropriate section of the `AnalysisResult` model.

All presentation is delegated to dedicated output modules.

Output modules are responsible for transforming analysis data into a specific representation, such as:

- console output;
- JSON reports;
- graphical interfaces;
- future reporting formats.

Analyzers remain completely unaware of how their results will eventually be displayed.

---

## Consequences

### Positive

- Analysis logic remains independent from presentation.
- New output formats can be introduced without modifying analyzers.
- Output implementations can evolve independently.
- Unit testing becomes simpler because analyzers produce data instead of text.
- The same analysis can be reused by multiple interfaces simultaneously.

### Negative

- Even simple console messages require an output module.
- Developers must resist the temptation to add temporary `print()` statements that become permanent.
- Output formatting occasionally requires additional mapping code.

### Trade-offs

The project accepts slightly more indirection in exchange for complete separation between analysis and presentation.

This decision prioritizes architectural flexibility over short-term convenience.

---

## Alternatives Considered

### Direct Console Output from Analyzers

Each analyzer could print its own findings directly.

This approach was rejected because presentation logic would become permanently embedded inside analysis code.

Supporting additional interfaces would require modifying every affected analyzer.

### Mixed Analysis and Reporting

Analyzers could both compute results and generate reports.

This approach was rejected because it combines two unrelated responsibilities within the same component.

As presentation requirements evolve independently from analysis, this design would inevitably increase coupling.

### Output Callbacks

Analyzers could receive callback functions responsible for displaying information.

Although this reduces direct dependencies on the console, presentation concerns would still influence analyzer implementations.

This approach was therefore rejected in favor of complete output isolation.

---

## Related Handbook Chapters

- Chapter 08 — *Analyzer Architecture*
- Chapter 09 — *AnalysisResult*
- Chapter 10 — *Output Isolation*
- Chapter 11 — *Loose Coupling and Dependency Management*
- Chapter 12 — *Separation of Responsibilities*
- Chapter 20 — *Extensibility Without Complexity*
- Chapter 26 — *Mistakes We Intentionally Avoided*