# WebInvestigator Documentation

This directory contains the architectural documentation of WebInvestigator.

The documentation is organized into three complementary collections, each answering a different question about the project.

| Collection | Answers the question |
|------------|----------------------|
| **[Architecture Handbook](handbook/README.md)** | *Why is the architecture designed this way?* |
| **[Architectural Decision Records](adr/README.md)** | *Why was a particular architectural decision made?* |
| **[Technical Architecture Reference](architecture/README.md)** | *How is the system currently implemented?* |

Together, these collections provide a complete understanding of the project's architecture, from its guiding principles to its technical implementation.

---

# Documentation Structure

```text
docs/
├── README.md
├── handbook/
├── adr/
└── architecture/
```

---

# Architecture Handbook

**Location:** [`docs/handbook/`](handbook/)

The Architecture Handbook explains the architectural philosophy of WebInvestigator.

It presents the concepts, principles and design choices that shape the framework.

Unlike the Technical Architecture Reference, the handbook is intended to be read sequentially, much like a book.

---

# Architectural Decision Records (ADRs)

**Location:** [`docs/adr/`](adr/)

Architectural Decision Records document the significant architectural decisions made throughout the evolution of the project.

Each ADR records:

- the context,
- the decision,
- the consequences,
- the alternatives considered.

Unlike the handbook, the ADR collection grows continuously as the architecture evolves.

---

# Technical Architecture Reference

**Location:** [`docs/architecture/`](architecture/)

The Technical Architecture Reference contains implementation-oriented documentation such as:

- architecture diagrams,
- sequence diagrams,
- UML diagrams,
- dependency graphs,
- C4 models,
- module interaction diagrams,
- and other technical reference material.

Unlike the handbook, these documents describe the current implementation of the framework and evolve alongside the codebase.

---

# Documentation Philosophy

The three documentation collections complement one another.

- The **Architecture Handbook** explains the architectural philosophy.
- The **Architectural Decision Records** explain why architectural decisions were made.
- The **Technical Architecture Reference** describes how the architecture is currently implemented.

Together, they document the architecture from concept to implementation while keeping each collection focused on a single responsibility.

---

The documentation is intended to evolve alongside the project.

While the **Architecture Handbook** changes infrequently, the **Architectural Decision Records** and **Technical Architecture Reference** continue to grow as WebInvestigator evolves.