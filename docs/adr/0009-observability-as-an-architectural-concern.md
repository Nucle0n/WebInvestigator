# ADR-0009
# Observability as an Architectural Concern

> **This ADR establishes structured logging as an architectural component rather than an implementation detail.**

**Status:** Accepted

**Date:** 2026-07-18

---

## Context

WebInvestigator executes multiple analyzers across potentially large investigation datasets.

Understanding what happened during an investigation is essential for debugging, validating results and diagnosing unexpected behavior.

Allowing each component to produce arbitrary output would quickly lead to inconsistent messages, duplicated information and tightly coupled analysis code.

The framework therefore required a consistent approach to reporting execution progress and operational information.

---

## Decision

Logging is treated as a dedicated architectural concern.

Components report meaningful execution events through the project's logging facilities rather than producing arbitrary console output.

Log messages describe the execution of the framework, while analysis results describe the investigation itself.

Logging remains independent from presentation and does not replace structured analysis results.

---

## Consequences

### Positive

- Execution becomes easier to understand and diagnose.
- Logging behavior remains consistent across all components.
- Analysis code stays independent from presentation.
- Logging destinations can evolve without modifying analyzers.
- Automated tools can process execution logs more easily.

### Negative

- Components must follow common logging conventions.
- Additional infrastructure is required to manage logging.

### Trade-offs

The framework accepts a dedicated logging mechanism in exchange for improved observability and long-term maintainability.

Separating execution information from investigation results keeps both responsibilities clearly defined.

---

## Alternatives Considered

### Console Output Everywhere

Each component could write directly to the console.

This approach was rejected because presentation becomes tightly coupled to analysis logic and execution output quickly becomes inconsistent.

### No Logging

The framework could rely solely on exceptions and analysis results.

This approach was rejected because execution flow, diagnostics and operational information would be difficult to reconstruct.

### Analyzer-Specific Logging

Each analyzer could define its own logging strategy.

This approach was rejected because it would lead to inconsistent formats and make investigation execution harder to follow.

---

## Related Handbook Chapters

- Chapter 08 — *Single Responsibility Everywhere*
- Chapter 10 — *Failure as a First-Class Citizen*
- Chapter 12 — *Separation of Concerns*
- Chapter 20 — *Extensibility Without Complexity*