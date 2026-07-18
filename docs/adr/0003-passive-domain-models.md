# ADR-0003
# Passive Domain Models

> **This ADR establishes domain models as passive, typed data structures with no analysis or presentation responsibilities.**

**Status:** Accepted

**Date:** 2026-07-18

---

## Context

WebInvestigator exchanges structured information between the scanner, analyzers, the investigation pipeline and output modules.

As the project evolved, domain objects became the natural place to represent files, images, inventory data, metadata and analyzer results.

Allowing these models to perform analysis, formatting or orchestration would make them increasingly difficult to reuse. Their behavior would begin to depend on execution context, output format and surrounding components.

This would blur architectural responsibilities and create implicit coupling between data representation and application behavior.

A clear rule was therefore required to define what domain models are allowed to contain.

---

## Decision

Domain models must remain passive, typed data structures.

They may:

- store structured data;
- define explicit fields and default values;
- express relationships between domain concepts;
- provide basic data-oriented validation when necessary.

They must not:

- perform analysis;
- invoke analyzers;
- control the investigation pipeline;
- print or format output;
- access external resources;
- contain presentation-specific behavior.

Analysis belongs to analyzers.

Orchestration belongs to the pipeline.

Presentation belongs to output modules.

Domain models exist only to represent and transport information between these components.

---

## Consequences

### Positive

- Data structures remain predictable and easy to understand.
- Models can be reused by analyzers, outputs, tests and future interfaces.
- Business logic remains located in clearly identified components.
- Models are easier to serialize into formats such as JSON.
- Unit tests can construct domain objects without triggering hidden behavior.
- Architectural boundaries remain explicit.

### Negative

- Some operations require separate functions or services instead of convenient methods on the model.
- Very small pieces of behavior may appear more verbose when kept outside the data structure.
- Contributors must consciously decide whether a method represents data behavior or application behavior.

### Trade-offs

The project accepts slightly more explicit orchestration in exchange for models that remain stable, portable and independent from their consumers.

This decision favors clear responsibility boundaries over object-oriented convenience.

---

## Alternatives Considered

### Behavior-Rich Domain Models

Models could contain methods for analysis, transformation and output formatting.

This approach was rejected because models would gradually accumulate responsibilities belonging to analyzers and output modules.

They would become more difficult to reuse and would introduce hidden dependencies on application behavior.

### Dictionary-Based Data Exchange

Components could exchange untyped dictionaries instead of dedicated models.

This approach was rejected because dictionaries provide weak contracts, limited discoverability and no reliable indication of required or optional fields.

Typed models make the architecture more explicit and reduce ambiguity between components.

### Presentation Methods on Models

Models could expose methods such as `display()`, `to_console()` or report-specific formatting helpers.

This approach was rejected because presentation requirements vary between interfaces and should not affect the domain layer.

---

## Related Handbook Chapters

- Chapter 07 — *The Domain Model*
- Chapter 09 — *AnalysisResult*
- Chapter 10 — *Output Isolation*
- Chapter 12 — *Separation of Responsibilities*
- Chapter 13 — *Abstraction and Generalization*
- Chapter 26 — *Mistakes We Intentionally Avoided*