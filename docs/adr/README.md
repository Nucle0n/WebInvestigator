# Architectural Decision Records (ADRs)

Architectural Decision Records (ADRs) document the significant architectural decisions made during the evolution of WebInvestigator.

Each ADR explains:

- the context in which a decision was made,
- the decision itself,
- the consequences of that decision,
- the alternatives that were considered.

Unlike the [Architecture Handbook](../handbook/README.md), which explains the architectural philosophy of the project, ADRs record the reasoning behind individual architectural choices.

---

## Why ADRs?

Software architecture evolves over time.

Without written decisions, the reasons behind important design choices are easily forgotten, making future evolution more difficult.

ADRs preserve that knowledge and provide historical context for contributors.

---

## Relationship with the Architecture Handbook

The two document collections are complementary.

| Handbook | ADRs |
|----------|------|
| Explains the architecture | Records architectural decisions |
| Educational | Historical |
| Describes principles | Documents specific choices |
| Rarely changes | Grows throughout the life of the project |

---

## ADR Format

Every ADR follows the same structure.

```text
Title

Summary

Status

Date

Context

Decision

Consequences

Alternatives Considered

Related Handbook Chapters
```

This consistency makes the collection easier to read and maintain.

---

## Status Values

Current status values are:

- **Accepted** — the decision is active.
- **Proposed** — under discussion.
- **Deprecated** — no longer recommended.
- **Superseded** — replaced by a newer ADR.

---

## Creating a New ADR

A new ADR should be created whenever a significant architectural decision is made.

Typical examples include:

- introducing a new architectural component,
- changing communication between major components,
- modifying architectural contracts,
- changing the execution model,
- introducing a new extension mechanism.

Routine bug fixes, refactoring and feature additions that do not change the architecture do not require an ADR.

---

## Numbering

ADRs are numbered sequentially.

Once assigned, an ADR number is never reused.

---

## Current Collection

The following ADRs document the architectural foundations and ongoing evolution of WebInvestigator.

| ADR | Title |
|-----|-------|
| [ADR-0001](0001-analysisresult-as-the-central-aggregation-model.md) | AnalysisResult as the Central Aggregation Model |
| [ADR-0002](0002-independent-analyzers.md) | Independent Analyzers |
| [ADR-0003](0003-passive-domain-models.md) | Passive Domain Models |
| [ADR-0004](0004-output-isolation.md) | Output Isolation |
| [ADR-0005](0005-configuration-as-a-single-entry-point.md) | Configuration as a Single Entry Point |
| [ADR-0006](0006-offline-first-architecture.md) | Offline-First Architecture |
| [ADR-0007](0007-investigation-pipeline.md) | Investigation Pipeline |
| [ADR-0008](0008-error-handling-philosophy.md) | Error Handling Philosophy |
| [ADR-0009](0009-observability-as-an-architectural-concern.md) | Observability as an Architectural Concern |
| [ADR-0010](0010-incremental-architecture.md) | Incremental Architecture |
| [ADR-0011](0011-testing-as-an-architectural-safety-net.md) | Testing as an Architectural Safety Net |
| [ADR-0012](0012-stable-architectural-interfaces.md) | Stable Architectural Interfaces |

As WebInvestigator evolves, this collection will continue to grow, preserving the architectural history of the project one decision at a time.