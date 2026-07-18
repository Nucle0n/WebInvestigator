# ADR-0007
# Investigation Pipeline

> **This ADR establishes the investigation pipeline as the primary orchestration model for all analysis workflows.**

**Status:** Accepted

**Date:** 2026-07-18

---

## Context

WebInvestigator performs multiple independent analyses on a common investigation dataset.

Without a defined execution model, analyzers could be invoked in arbitrary ways, leading to inconsistent workflows, duplicated orchestration logic and unclear execution order.

As the number of analyzers grows, coordinating them individually would make the framework increasingly difficult to understand, extend and maintain.

The project required a single, predictable execution model capable of orchestrating every investigation consistently.

---

## Decision

WebInvestigator executes investigations through a centralized analysis pipeline.

The pipeline is responsible for coordinating the execution of analyzers in a well-defined sequence.

Each analyzer performs a single analysis task and contributes its findings to a shared `AnalysisResult` instance.

Analyzers remain unaware of one another and communicate only through the architectural contracts already established by the framework.

The pipeline itself contains orchestration logic only.

It does not perform analysis, presentation or domain-specific processing.

---

## Consequences

### Positive

- Every investigation follows the same execution model.
- Analyzer execution remains predictable and easy to understand.
- New analyzers can be integrated without modifying existing analyzers.
- Responsibilities remain clearly separated between orchestration and analysis.
- The overall execution flow becomes easier to test and document.

### Negative

- The pipeline introduces an additional orchestration layer.
- Complex execution strategies may require future evolution of the pipeline implementation.

### Trade-offs

The project accepts a centralized orchestration component in exchange for a simpler and more maintainable execution model.

Pipeline complexity is considered preferable to distributing orchestration responsibilities across analyzers.

---

## Alternatives Considered

### Independent Analyzer Execution

Each analyzer could be invoked manually or by individual modules.

This approach was rejected because execution logic would become duplicated and inconsistent across the project.

### Analyzer Chaining

Analyzers could invoke subsequent analyzers directly.

This approach was rejected because it creates tight coupling between components and makes execution order part of analyzer behavior.

Such coupling conflicts with the architectural principle of analyzer independence.

### Event-Driven Execution

Analyzers could publish and subscribe to analysis events.

This approach was rejected because it introduces additional architectural complexity without providing sufficient benefits for the current scope of the framework.

---

## Related Handbook Chapters

- Chapter 06 — *The Investigation Pipeline*
- Chapter 08 — *Single Responsibility Everywhere*
- Chapter 09 — *Architectural Contracts*
- Chapter 11 — *Loose Coupling*
- Chapter 12 — *Separation of Concerns*
- Chapter 24 — *Designing for Evolution*