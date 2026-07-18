# Chapter 15
# Configuration as Architecture

---

> *"Code defines capabilities. Configuration defines behavior."*

---

# 15.1 Introduction

Every software project eventually reaches the same moment.

Someone opens the source code to modify a simple value.

Perhaps the investigation directory has changed.

Perhaps a report should now be exported elsewhere.

Perhaps another file extension should be ignored.

The modification itself is trivial.

The fact that source code had to be edited is not.

This distinction marks an important step in the evolution of a software project.

Well-designed software separates **behavior** from **configuration**.

WebInvestigator follows this principle from the beginning.

---

# 15.2 Code Should Describe Rules

Source code exists to express logic.

It explains **how** the framework behaves.

Configuration answers different questions.

- Which investigation should be executed?

- Where should reports be written?

- Which analyzers are enabled?

- Which file extensions should be ignored?

These questions are not algorithms.

They are choices.

Choices belong in configuration.

Algorithms belong in code.

---

# 15.3 The Wrong Place

Consider the following example.

```
scanner = Scanner(
    Path("investigations/AtelierDeLea")
)
```

This works.

But it immediately couples the software to one investigation.

The framework has quietly become specific instead of generic.

Now imagine another contributor.

The very first modification they make is editing the source code.

Nothing is technically broken.

Yet the architecture has become less flexible.

---

## Common Pitfall

Hardcoded values often appear harmless because they are easy to introduce.

Unfortunately, they also become surprisingly difficult to remove once they spread throughout the codebase.

---

# 15.4 One Source of Truth

Configuration has another important responsibility.

Consistency.

Suppose five modules require the investigation directory.

Without a centralized configuration, each component may define its own value.

Soon, different parts of the framework begin operating on different assumptions.

The architecture has lost coherence.

Instead, WebInvestigator favors a single source of truth.

Every configurable value should ideally exist in exactly one place.

Every component should consult that location.

No component should invent its own configuration.

---

# 15.5 Configuration Is Not Logic

Another temptation deserves attention.

As configuration files become richer, developers begin adding logic.

Conditional rules.

Expressions.

Embedded scripts.

Soon, the configuration language becomes almost as complicated as the programming language itself.

This evolution should be approached carefully.

Configuration should remain descriptive.

Not procedural.

Its purpose is to select behavior.

Not to implement it.

---

## Design Rationale

Whenever configuration begins resembling a programming language, it is worth asking whether that complexity actually belongs in the application itself.

Simple configuration tends to remain understandable for many years.

Mini programming languages rarely do.

---

# 15.6 Predictability

One of the advantages of explicit configuration is predictability.

When developers open a dedicated configuration file, they immediately know where operational decisions are located.

No searching through dozens of modules.

No hidden constants.

No undocumented assumptions.

The architecture communicates its intentions clearly.

Predictable software is easier to understand.

Understandable software is easier to maintain.

---

# 15.7 Configuration and Testing

Configuration also improves testing.

Suppose one test requires scanning an empty directory.

Another requires a directory containing corrupted images.

A third requires a deeply nested archive.

Without configurable paths, each test would require modifying the source code.

With proper configuration, the same framework executes every scenario without changing a single implementation file.

Architecture and testing reinforce one another.

---

# 15.8 Evolution Without Modification

Imagine that WebInvestigator eventually supports:

- local investigations;

- remote investigations;

- cloud storage;

- compressed archives;

- live monitoring.

None of these capabilities should require rewriting the framework's core simply to select a different source.

Configuration allows software to evolve by describing new environments rather than rewriting existing logic.

This distinction becomes increasingly valuable as projects mature.

---

## Architect's Note

The project currently relies on a straightforward `config.py`.

This simplicity is intentional.

Future versions may introduce richer configuration mechanisms, but only if real requirements justify additional complexity.

The goal is not to build the most powerful configuration system.

The goal is to build the simplest one that continues to serve the framework effectively.

---

# 15.9 Configuration Reflects Intent

Configuration says something about the architecture itself.

It reveals what the designers expected users to customize.

A value exposed through configuration represents an intentional extension point.

Everything else remains part of the framework's internal implementation.

Choosing what becomes configurable is therefore an architectural decision.

Too little configuration limits flexibility.

Too much configuration overwhelms users.

Finding the right balance requires experience.

---

# 15.10 Simplicity Over Cleverness

Configuration systems sometimes become impressive engineering projects.

Nested inheritance.

Variable substitution.

Dynamic expressions.

Plugin loading.

Environment resolution.

While these features can be useful, they also increase cognitive load.

WebInvestigator deliberately favors straightforward configuration.

A contributor should understand the framework's operational settings within minutes.

Not after reading an additional manual.

Simple configuration reduces friction for everyone.

---

# 15.11 Summary

Configuration is more than a collection of values.

It defines the environment in which the architecture operates.

By separating operational choices from implementation logic, WebInvestigator becomes easier to test, easier to reuse and easier to evolve.

Good architecture does not eliminate configuration.

It gives configuration a clearly defined role.

---

## Next Part

The architectural principles that shape WebInvestigator have now been established.

Designing a good architecture, however, is only the beginning. Long-lived software also depends on engineering practices that protect those principles as the framework grows and changes.

The next part begins by exploring Testing as Architectural Protection, introducing the first of several engineering practices that help preserve architectural quality throughout the life of a project.

**[Testing as Architectural Protection](./16-Testing_as_Architectural_Protection.md)**