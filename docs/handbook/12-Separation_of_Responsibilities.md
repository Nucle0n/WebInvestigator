# Chapter 12
# Separation of Responsibilities

---

> *"The art of software architecture is deciding where a responsibility belongs."*

---

# 12.1 Introduction

Every software system performs many different tasks.

It discovers information.

It transforms data.

It stores knowledge.

It communicates with users.

It reports results.

None of these activities are inherently difficult.

The challenge lies elsewhere.

The challenge is deciding **which component should perform which responsibility.**

Poor architectural decisions rarely introduce new responsibilities.

Instead, they place existing responsibilities in the wrong location.

Over time, components begin to accumulate unrelated tasks.

Their purpose becomes increasingly difficult to describe.

Eventually, developers stop asking:

> "What is this component responsible for?"

and begin asking:

> "What isn't it responsible for?"

That moment usually signals the beginning of architectural decay.

WebInvestigator attempts to prevent this evolution through one simple principle.

> **Every responsibility should have a natural home.**

---

# 12.2 The Cost of Mixed Responsibilities

Imagine an analyzer responsible for image inspection.

Initially, it performs three operations.

- Read an image.
- Compute a perceptual hash.
- Return an `ImageInfo`.

Simple.

A few weeks later, console output is added.

Then JSON export.

Then progress reporting.

Then performance statistics.

Then cache management.

Nothing seems alarming.

Each addition appears reasonable.

Months later, the component now performs six unrelated jobs.

No single developer consciously designed a complex analyzer.

Complexity emerged gradually.

This is how most large software systems become difficult to maintain.

Rarely through one catastrophic decision.

Almost always through many small ones.

---

## Historical Note

Early versions of WebInvestigator occasionally blurred the boundary between analysis and presentation.

The problem did not appear immediately.

Only after several analyzers had been written did duplicated formatting logic begin to emerge.

Rather than accepting that duplication, presentation responsibilities were extracted into dedicated output modules.

This was one of the first major architectural refactorings of the project.

---

# 12.3 Recognizing Responsibilities

A useful exercise when designing software is asking a deceptively simple question.

> "What sentence best describes this component?"

For example:

> "The Image Analyzer extracts information from image files."

Excellent.

Its purpose is immediately obvious.

Now consider another description.

> "The Image Analyzer extracts image information, exports JSON, manages configuration, caches results, displays console output and computes statistics."

This description feels uncomfortable.

Not because any individual responsibility is wrong.

But because they clearly belong to different concerns.

A component should be easy to describe.

Difficulty describing a component is often an early indicator that it has acquired responsibilities it should not own.

---

# 12.4 Responsibility Is Not Size

One common misconception deserves clarification.

Small components are not automatically well designed.

A component containing twenty lines of code may still violate architectural principles.

Conversely, a component containing several hundred lines may still possess a single, well-defined responsibility.

Responsibility concerns purpose.

Not size.

The objective is therefore not writing the smallest possible modules.

The objective is writing modules whose reason for existence remains obvious.

---

# 12.5 A Practical Example

Consider a future OCR analyzer.

Its responsibility is straightforward.

```
Image

↓

Extract text

↓

OCRResult
```

Now imagine extending it.

```
Image

↓

Extract text

↓

Translate text

↓

Detect language

↓

Generate HTML

↓

Upload results

↓

Send email notification
```

Has the OCR algorithm become more advanced?

No.

The analyzer has simply become responsible for unrelated concerns.

The architecture has lost clarity.

Each new feature should therefore trigger a simple question.

> "Does this responsibility naturally belong here?"

If the answer is uncertain, it probably belongs somewhere else.

---

# 12.6 Responsibility Boundaries

One useful mental model is imagining that every component owns a territory.

Crossing that boundary should be rare.

The scanner owns discovery.

Analyzers own analysis.

Models own representation.

Outputs own presentation.

Configuration owns configuration.

Tests own verification.

Each territory has clearly defined borders.

Healthy architectures respect those borders.

Unhealthy architectures ignore them.

---

## Design Rationale

Separating responsibilities may initially appear to introduce more files.

This is true.

However, the number of files is rarely the limiting factor in software engineering.

Human understanding is.

A developer can navigate many small, well-defined files far more easily than a handful of files with poorly defined purposes.

The architecture therefore optimizes for comprehension rather than minimizing the file count.

---

# 12.7 Responsibility and Change

There is another way to recognize responsibilities.

Observe what causes a component to change.

Suppose tomorrow we decide to improve console formatting.

Which component should change?

Only the output layer.

Suppose we discover a faster perceptual hashing algorithm.

Which component should change?

Only the image analyzer.

Suppose JSON exports now require additional metadata.

Which component should change?

Only the JSON exporter.

Ideally, every change request should naturally point toward one component.

When multiple unrelated components must change simultaneously, responsibility boundaries may need reconsideration.

---

# 12.8 Architectural Gravity

Responsibilities have a tendency to drift.

Developers naturally place new code wherever it appears most convenient.

This phenomenon might be called **architectural gravity**.

Without continuous discipline, responsibilities slowly migrate toward central components.

The entry point becomes larger.

Utility modules become catch-all toolboxes.

Analyzers acquire formatting logic.

Models acquire business logic.

Eventually, the architecture resembles a city that expanded without urban planning.

Every new building solved an immediate problem.

The city itself became increasingly difficult to navigate.

Good architecture requires resisting this gravitational pull.

---

# 12.9 The Unix Philosophy

One of the oldest ideas in software engineering comes from the Unix world.

> **Do one thing. Do it well.**

Although WebInvestigator is not a Unix application in the traditional sense, this philosophy influenced many architectural decisions.

A scanner discovers files.

An analyzer analyzes.

An output module presents.

Each component performs one job exceptionally well.

The result is not merely cleaner code.

It is software whose behavior remains predictable even as the project grows.

---

# 12.10 Responsibility and Collaboration

Separating responsibilities does not isolate components.

Quite the opposite.

Well-defined responsibilities improve collaboration.

Because each component has a clearly defined role, interactions become simpler.

Every module knows:

- what it receives;

- what it produces;

- what it should ignore.

The framework therefore behaves like a team of specialists.

Each expert performs one task.

The investigation succeeds because those experts collaborate—not because one expert attempts to perform every task.

---

# 12.11 Summary

Responsibility is one of the fundamental building blocks of software architecture.

Components should not be judged primarily by their size or complexity.

They should be judged by the clarity of their purpose.

When responsibilities remain focused, software remains understandable.

When responsibilities begin to overlap, complexity follows naturally.

Much of WebInvestigator's architecture can ultimately be understood as a continuous effort to keep every responsibility in its proper place.

---

## Next Chapter

The next chapter explores another question that every long-lived project eventually faces:

**When should software become more generic?**

Generalization is often presented as a virtue.

In reality, premature generalization is responsible for a surprising amount of unnecessary complexity.

We will examine why WebInvestigator deliberately resists abstraction until experience demonstrates that it is truly needed.