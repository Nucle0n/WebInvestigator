# Architectural Decision Records (ADRs)

Architectural Decision Records (ADRs) document the significant architectural decisions made during the evolution of WebInvestigator.

Each ADR explains:

- the context in which a decision was made,
- the decision itself,
- the consequences of that decision,
- the alternatives that were considered.

Unlike the Architecture Handbook, which explains the architectural philosophy of the project, ADRs record the reasoning behind individual architectural choices.

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

The first ADRs document the architectural foundations of WebInvestigator.

Subsequent ADRs record the project's architectural evolution as new decisions are made.