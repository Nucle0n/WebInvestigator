# Chapter 26
# Mistakes We Intentionally Avoided

---

> *"Good architecture is often defined as much by the decisions that were rejected as by those that were accepted."*

---

# 26.1 Introduction

Throughout this handbook, we have explained many of the decisions that shaped WebInvestigator.

Responsibilities were separated.

Models became contracts.

Analyzers remained independent.

Outputs stayed isolated.

Looking back, however, another observation emerges.

The architecture was not only built by choosing certain ideas.

It was equally shaped by refusing others.

Some of those rejected ideas initially appeared attractive.

Some would even have reduced the amount of code.

Others promised greater flexibility.

Yet each carried long-term consequences that conflicted with the project's goals.

This chapter is therefore not a catalogue of mistakes made.

It is a catalogue of mistakes deliberately avoided.

---

# 26.2 The Temptation of a Giant `main.py`

Every project begins somewhere.

Initially, placing everything inside `main.py` feels perfectly reasonable.

Scanning.

Analysis.

Reporting.

Error handling.

Configuration.

All contained within a single file.

For a small prototype, this approach is often appropriate.

The mistake is not starting there.

The mistake is remaining there after the project has grown.

WebInvestigator deliberately separated orchestration from implementation before the file became unmanageable.

Growth became incremental rather than painful.

---

# 26.3 Analyzers Calling Other Analyzers

This idea appears surprisingly attractive.

Suppose the Duplicate Analyzer requires image hashes.

Why not simply call the Image Analyzer directly?

The implementation seems elegant.

No duplicated work.

Minimal code.

Unfortunately, the architectural cost is hidden.

Analyzers become aware of one another.

Execution order becomes significant.

Testing requires additional setup.

Future parallel execution becomes more complicated.

The architecture gradually transforms into a dependency graph rather than a collection of independent responsibilities.

`AnalysisResult` exists largely to avoid this situation.

Knowledge is shared.

Dependencies are not.

---

## Architect's Note

One of the easiest ways to recognize architectural maturity is observing whether components exchange knowledge or dependencies.

Healthy systems usually exchange knowledge.

Fragile systems exchange dependencies.

---

# 26.4 The Infinite Utility Module

Another common temptation appears through convenience.

A helper function needs a home.

Someone creates:

```
utils.py
```

Another helper arrives.

Then another.

Months later the module contains unrelated functionality from every part of the framework.

Image processing.

String formatting.

Configuration helpers.

Hash utilities.

File discovery.

Nothing belongs together.

Everything resides there.

The module slowly becomes the project's junk drawer.

WebInvestigator instead attempts to place helper functionality close to the responsibility it supports.

Locality preserves clarity.

---

# 26.5 Intelligent Models

At some point developers often wonder:

> "Wouldn't it be cleaner if the model performed the analysis itself?"

Initially this appears elegant.

The object owns its own behavior.

Over time responsibilities begin accumulating.

Models start opening files.

Computing hashes.

Reading metadata.

Performing validation.

Exporting themselves.

The distinction between data and behavior gradually disappears.

WebInvestigator intentionally keeps models simple.

Knowledge remains separated from processing.

This allows analyzers to evolve independently of the data they produce.

---

# 26.6 Global State

Global variables frequently solve immediate problems.

Configuration becomes easily accessible.

Shared caches appear convenient.

Temporary data becomes universally available.

Unfortunately, every global object quietly creates invisible dependencies.

Modules begin relying upon hidden assumptions.

Testing becomes increasingly complicated.

Execution order matters.

Understanding a component requires understanding the entire application.

WebInvestigator deliberately minimizes shared mutable state.

Explicit dependencies are easier to understand than invisible ones.

---

## Common Pitfall

Global state rarely feels dangerous while a project is small.

Its cost becomes apparent only after many unrelated components begin relying upon it simultaneously.

---

# 26.7 Premature Abstraction

Developers enjoy elegant abstractions.

Generic analyzers.

Universal processors.

Highly configurable pipelines.

Plugin systems.

Many of these ideas eventually become valuable.

The mistake lies in introducing them before real variation exists.

WebInvestigator repeatedly preferred concrete implementations first.

Patterns were allowed to emerge naturally.

Only repeated experience justified additional abstraction.

---

# 26.8 Designing for Every Possible Future

Another subtle temptation accompanies ambitious projects.

Trying to solve problems that do not yet exist.

Support for distributed execution.

Plugin marketplaces.

Cloud synchronization.

Remote investigation nodes.

Versioned extension APIs.

Each capability may eventually become useful.

Adding all of them today would significantly complicate the architecture.

Instead, WebInvestigator attempts to remain ready for future evolution without prematurely implementing future solutions.

Preparation should not become speculation.

---

# 26.9 Confusing Flexibility with Complexity

Many projects become increasingly configurable over time.

Soon every feature requires another option.

Another flag.

Another exception.

Another special case.

Eventually, contributors struggle to understand the framework because every behavior depends on configuration.

Flexibility certainly has value.

So does predictability.

WebInvestigator generally prefers a smaller number of obvious behaviors over an unlimited number of configurable ones.

Simple software often proves more adaptable than excessively flexible software.

---

## Historical Perspective

Many architectural failures become visible only after years of development.

Interestingly, few originate from obviously poor ideas.

Most begin as entirely reasonable shortcuts.

Architecture therefore benefits less from extraordinary intelligence than from consistent restraint.

Knowing which attractive ideas to postpone is often as valuable as knowing which ideas to implement.

---

# 26.10 Looking Back

None of the rejected ideas discussed in this chapter is universally wrong.

Under different constraints, many would represent sensible engineering decisions.

Context always matters.

What distinguishes architecture is not the existence of universal rules.

It is the ability to evaluate trade-offs honestly.

Every rejected shortcut preserved one quality that WebInvestigator considered essential.

Independence.

Clarity.

Predictability.

Long-term maintainability.

Those priorities shaped the architecture far more than any individual implementation.

---

# 26.11 Summary

Architecture is defined as much by restraint as by construction.

Every project presents tempting shortcuts.

Some save time.

Some reduce code.

Some promise future flexibility.

Choosing not to adopt them can require more discipline than implementing them.

The architecture of WebInvestigator reflects those choices.

Its simplicity is not accidental.

It is the cumulative result of many deliberate refusals.

---

## Next Chapter

Every architectural decision tells a story.

Understanding *what* was decided is useful.

Understanding *why* it was decided is far more valuable.

The next chapter introduces one of the most effective practices for preserving architectural knowledge over time:

**Architectural Decision Records (ADR).**