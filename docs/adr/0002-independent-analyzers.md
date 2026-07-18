# ADR-0002
# Independent Analyzers

> **This ADR establishes analyzers as independent architectural units with no direct dependencies between them.**

**Status:** Accepted

**Date:** 2026-07-18

---

## Context

WebInvestigator is designed as a collection of analyzers, each responsible for extracting a specific type of information from an investigation.

As the number of analyzers grows, allowing them to depend on one another would gradually create a complex dependency graph.

Such dependencies would make analyzers more difficult to understand, test and reuse. They would also make execution order increasingly important, reducing the flexibility of the investigation pipeline.

A clear architectural boundary was therefore required to ensure that analyzers could continue evolving independently.

---

## Decision

Each analyzer owns a single responsibility and must remain completely independent from every other analyzer.

Analyzers must never:

- call another analyzer;
- modify another analyzer's results;
- rely on another analyzer having already executed;
- contain business logic belonging to another analyzer.

The only shared communication mechanism is the `AnalysisResult` model.

Each analyzer writes exclusively to its own section of that model.

---

## Consequences

### Positive

- Analyzers can be developed independently.
- New analyzers can be introduced without modifying existing ones.
- Execution order remains flexible.
- Individual analyzers are easier to test in isolation.
- Responsibilities remain explicit and well-defined.
- The framework scales without creating dependency chains.

### Negative

- Some information may appear duplicated across analyzers.
- Shared helper functions must be carefully extracted into generic utilities without introducing hidden coupling.

### Trade-offs

The project intentionally accepts occasional duplication in exchange for strong architectural independence.

Maintaining clear responsibility boundaries is considered more valuable than aggressively eliminating repeated code.

---

## Alternatives Considered

### Analyzer-to-Analyzer Communication

Analyzers could directly invoke one another when additional information was required.

This approach was rejected because it creates hidden dependencies, couples execution order to implementation details and makes individual analyzers difficult to reuse.

### Shared Global State

Analyzers could communicate through shared mutable objects.

This approach was rejected because ownership becomes unclear, debugging becomes more difficult and hidden side effects become increasingly likely as the project evolves.

---

## Related Handbook Chapters

- Chapter 06 — *The Investigation Pipeline*
- Chapter 08 — *Analyzer Architecture*
- Chapter 11 — *Loose Coupling and Dependency Management*
- Chapter 12 — *Separation of Responsibilities*
- Chapter 24 — *Technical Debt versus Architectural Debt*
- Chapter 26 — *Mistakes We Intentionally Avoided*