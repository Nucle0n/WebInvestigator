# Chapter 27
# Architectural Decision Records (ADR)

---

> *"The greatest architectural decisions are often forgotten long before they become important again."*

---

# 27.1 Introduction

Every software architecture is shaped by decisions.

Some are small.

Others influence the project for years.

Should models remain passive?

Should analyzers communicate directly?

Should configuration be centralized?

Should responsibilities be split or merged?

Eventually, every architect answers these questions.

The surprising part is not that these decisions are made.

It is how quickly their reasons disappear.

Months later, new contributors often encounter a design and wonder:

> "Why was it done this way?"

If the answer exists only in someone's memory, the architecture has already begun to lose one of its most valuable assets.

Its history.

---

# 27.2 Decisions Are Knowledge

Source code records implementations.

Tests record expected behavior.

Documentation explains usage.

None of these necessarily explains why a particular architectural decision exists.

Yet the reasoning behind a decision is often more valuable than the decision itself.

Knowing *what* was built is useful.

Knowing *why* it was built allows future developers to judge whether the original reasoning still applies.

Architecture depends upon preserving both.

---

## Design Rationale

A decision without its reasoning eventually becomes indistinguishable from an arbitrary constraint.

Recording the reasoning preserves the ability to evaluate the decision intelligently in the future.

---

# 27.3 What Is an ADR?

An Architectural Decision Record is a small document describing an important architectural choice.

It is intentionally lightweight.

A typical ADR answers only a few questions.

- What decision was made?

- Why was it necessary?

- Which alternatives were considered?

- What consequences are expected?

The objective is not producing lengthy documentation.

The objective is preserving architectural intent.

---

# 27.4 Capturing Context

Good decisions depend upon context.

Suppose someone discovers an ADR stating:

> "Analyzers must remain independent."

Without additional explanation, the rule may appear arbitrary.

Now consider another version.

> "Analyzers remain independent to preserve modularity, simplify testing and allow future parallel execution."

The decision remains identical.

The understanding becomes dramatically richer.

Context transforms rules into reasoning.

---

# 27.5 Architecture Evolves

One common misunderstanding deserves attention.

Recording a decision does not imply that the decision can never change.

An ADR captures why a choice was appropriate at a particular moment.

Years later, circumstances may evolve.

Hardware changes.

Requirements change.

User expectations change.

When this happens, the original ADR should not be erased.

It should be complemented by a new one explaining why the previous decision no longer represents the best solution.

Architecture benefits from preserving its own history.

---

## Architect's Note

Replacing old decisions without preserving their reasoning often causes projects to repeat the same debates every few years.

Remembering previous trade-offs is frequently more valuable than remembering previous implementations.

---

# 27.6 Alternatives Matter

Many architectural documents describe only the chosen solution.

Equally important are the solutions that were rejected.

Suppose an ADR simply states:

> "Analysis results are aggregated through `AnalysisResult`."

A future contributor may still wonder why analyzers do not communicate directly.

Now imagine the ADR also explains:

- direct analyzer communication was considered;

- it increased coupling;

- it complicated testing;

- it reduced future parallelization opportunities.

Suddenly the decision becomes far more convincing.

Rejected alternatives often teach as much as accepted ones.

---

# 27.7 ADRs Build Trust

Software projects inevitably change contributors.

Original architects leave.

New developers arrive.

Without historical context, newcomers often hesitate.

Every architectural decision appears open to reconsideration.

Well-written ADRs reduce this uncertainty.

Contributors understand not only the architecture itself, but also the thinking that produced it.

Confidence grows.

Discussions become more productive.

Architecture becomes more consistent across time.

---

# 27.8 Keeping ADRs Lightweight

One danger deserves mentioning.

Architectural documentation can easily become excessive.

Lengthy reports.

Complex diagrams.

Extensive meeting notes.

These rarely remain current.

An effective ADR should remain concise.

Future contributors should be able to understand the decision in a few minutes.

If documenting architecture becomes burdensome, developers will eventually stop doing it.

Simplicity encourages continuity.

---

## Common Pitfall

An outdated ADR is usually more harmful than no ADR at all.

If a decision changes significantly, its documentation should evolve alongside it.

Architecture and architectural knowledge should never drift apart.

---

# 27.9 ADRs as Conversations Across Time

Perhaps the most interesting aspect of an ADR is that it connects developers who may never meet.

An architect writing today explains a decision to someone joining the project years later.

The reader may never know the original author.

The author may never know the future reader.

Yet a conversation still occurs.

Architecture becomes a dialogue across time rather than a collection of undocumented assumptions.

---

## Historical Perspective

Architectural Decision Records became increasingly popular in software engineering as projects grew in scale and longevity.

Although formats differ, the underlying philosophy remains remarkably consistent.

The goal is not documenting every decision.

It is preserving the reasoning behind the decisions that significantly influence the future evolution of the system.

---

# 27.10 The Architecture of WebInvestigator

Many of the principles described throughout this handbook naturally lend themselves to ADRs.

For example:

- analyzers communicate through `AnalysisResult`;

- models remain passive;

- outputs never perform analysis;

- responsibilities remain separated;

- premature optimization is avoided.

None of these decisions should survive merely because they appear in source code.

Their reasoning deserves preservation as well.

Architecture is stronger when future contributors understand not only *how* the framework works, but *why* it was designed that way.

---

# 27.11 Summary

Architecture is more than structure.

It is accumulated knowledge.

Architectural Decision Records preserve that knowledge by recording the reasoning behind important design choices.

In doing so, they transform architecture from a collection of implementation details into a body of shared understanding that can outlive any individual contributor.

---

## Next Chapter

Every architectural decision ultimately reflects a deeper responsibility.

Knowing **what** to build is important.

Knowing **what not to build** is often even more important.

The final chapter of this section explores one of the defining characteristics of experienced software architects:

**When to Say No.**