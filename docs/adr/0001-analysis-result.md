# ADR-0001
# AnalysisResult as the Central Aggregation Model

> **This ADR establishes the architectural contract through which all analysis results are exchanged within the framework.**

**Status:** Accepted

**Date:** 2026-07-18

---

## Context

WebInvestigator is designed as a pipeline composed of independent analyzers.

Each analyzer extracts information from the investigation without depending on the results of other analyzers.

As the framework began to grow, every analyzer naturally produced its own output object. Passing multiple independent objects between successive pipeline stages quickly became cumbersome.

Adding a new analyzer required updating several function signatures throughout the application. Every additional result increased coupling between the pipeline and individual analyzers, making future evolution progressively more difficult.

A more scalable mechanism for transporting analysis results was required.

---

## Decision

Introduce a single `AnalysisResult` model responsible for aggregating the output of every analyzer.

Each analyzer writes only to its dedicated section of the `AnalysisResult` instance.

Pipeline stages exchange a single object regardless of the number of analyzers executed.

The `AnalysisResult` model acts solely as a structured container.

It contains no business logic and performs no analysis.

---

## Consequences

### Positive

- Pipeline interfaces remain stable as new analyzers are introduced.
- Adding a new analyzer no longer requires changing method signatures throughout the project.
- Outputs consume a single well-defined object.
- Analyzer responsibilities remain isolated.
- Future extensions have a predictable integration point.
- The architecture scales linearly as additional analyzers are added.

### Negative

- The central model grows over time as new analysis domains are introduced.
- Care must be taken to preserve clear ownership of each section to avoid turning `AnalysisResult` into an unstructured container.

### Trade-offs

The project accepts a larger central aggregation model in exchange for significantly lower coupling between components.

This decision intentionally favors long-term maintainability over minimizing the size of individual data structures.

---

## Alternatives Considered

### Independent Result Objects

Each analyzer could have continued returning its own object.

This approach was rejected because every new analyzer would require modifications to the pipeline and every consumer of analysis results.

The resulting coupling would increase continuously as the framework evolved.

### Generic Dictionary-Based Storage

Analysis results could have been stored inside a generic dictionary.

This approach was rejected because it sacrifices explicit typing, discoverability and IDE support.

A strongly typed model provides a clearer contract between analyzers and output modules.

---

## Related Handbook Chapters

- Chapter 06 — *The Investigation Pipeline*
- Chapter 07 — *The Domain Model*
- Chapter 09 — *AnalysisResult*
- Chapter 24 — *Technical Debt versus Architectural Debt*