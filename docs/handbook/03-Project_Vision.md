# Chapter 3
# Project Vision

---

> *Architecture is not about writing code.
> It is about making future code easier to write.*

---

# 3.1 Vision Before Features

Most software projects begin with a list of features.

WebInvestigator did not.

The project began with a philosophy.

Features are temporary.

Architecture remains.

Every feature implemented today will eventually evolve, be replaced or become obsolete.

Architectural principles, however, should remain stable for years.

For this reason, WebInvestigator has always prioritized architecture over feature count.

Adding new capabilities is important.

Adding them without compromising the overall design is even more important.

---

# 3.2 The Core Objective

The primary objective of WebInvestigator can be summarized in one sentence.

> Build a reusable framework that simplifies digital investigations through independent analysis modules.

Every important word in this sentence matters.

**Reusable**

The framework should never solve only one investigation.

Every module should remain applicable to future investigations whenever possible.

---

**Framework**

WebInvestigator is not intended to become a monolithic application.

Instead, it provides a foundation upon which investigation workflows can be assembled.

---

**Independent**

Each analyzer should perform one task.

Nothing more.

Nothing less.

Dependencies between analyzers should remain minimal.

---

**Analysis**

The framework assists investigations.

It does not replace investigators.

Interpretation remains a human responsibility.

---

# 3.3 Transparency

One principle has guided every architectural decision since the beginning.

The framework should never become a black box.

Every result produced by WebInvestigator should be understandable.

Whenever possible, the user should know:

- where data comes from;

- how it was produced;

- which analyzer generated it;

- which assumptions were made.

Hidden processing inevitably reduces trust.

Transparent processing increases confidence.

This philosophy explains why WebInvestigator favors explicit processing pipelines over highly abstract automation.

---

# 3.4 Simplicity

Software complexity grows naturally.

Simplicity does not.

Keeping a codebase understandable requires continuous effort.

Whenever two solutions provide similar capabilities, WebInvestigator deliberately favors the simpler one.

This does not mean choosing simplistic designs.

It means avoiding unnecessary complexity.

Examples include:

- avoiding premature abstractions;

- avoiding unnecessary inheritance;

- avoiding overly generic architectures;

- avoiding speculative development.

The project intentionally follows the principle:

> **Do not build today's solution around tomorrow's assumptions.**

Future requirements should be addressed when they actually exist.

Not before.

---

# 3.5 Incremental Development

One characteristic of WebInvestigator is its incremental evolution.

Large features are never implemented all at once.

Instead, development follows small, verifiable steps.

For example:

```
Read image dimensions
        ↓
Compute SHA-256
        ↓
Compute perceptual hash
        ↓
Detect exact duplicates
        ↓
Detect visually similar images
        ↓
Cluster similar images
```

Each step produces a working project.

Each commit represents meaningful progress.

Each feature remains independently testable.

This strategy provides several advantages.

Bugs become easier to identify.

Git history becomes significantly more readable.

Refactoring becomes less risky.

Architectural mistakes are detected earlier.

---

# 3.6 Separation of Responsibilities

One responsibility.

One module.

This principle appears repeatedly throughout the project.

For example:

The scanner discovers files.

It does not analyze them.

The image analyzer extracts image information.

It does not display results.

Console output formats information.

It does not compute analysis.

Models describe data.

They do not perform analysis.

Keeping responsibilities separate makes every component easier to understand, test and replace.

This philosophy ultimately led to the current layered architecture.

---

# 3.7 Extensibility

Every architectural decision should make adding new analyzers easier rather than harder.

Whenever a new capability is introduced, developers should not need to redesign the framework.

Instead, they should simply implement another analyzer.

This objective strongly influenced the current architecture.

Adding support for new investigation techniques should require minimal modifications to existing code.

Ideally, existing modules remain untouched.

Only new modules are added.

This greatly reduces regression risks.

---

# 3.8 Offline First

Digital evidence is fragile.

Websites disappear.

Domains expire.

Online services evolve.

API providers change their pricing.

Evidence collected today may no longer exist tomorrow.

For that reason, WebInvestigator prioritizes local artefacts whenever possible.

Mirror copies.

Downloaded media.

Archived websites.

Extracted metadata.

Analysis performed on stable local datasets remains reproducible years later.

This philosophy also improves scientific reproducibility.

Two investigators working on the same dataset should obtain identical results.

---

# 3.9 Developer Experience

WebInvestigator is primarily developed by programmers.

Therefore, the framework should remain pleasant to extend.

Good developer experience is considered an architectural feature.

Code should be:

- readable;

- predictable;

- well documented;

- strongly typed;

- consistently organized.

Every new contributor should be able to understand the project structure before understanding the implementation details.

Architecture should guide development.

Not the opposite.

---

# 3.10 Open Source by Design

Although WebInvestigator originally began as a personal project, its architecture gradually evolved toward open-source development.

This decision influenced numerous aspects of the project.

Code clarity became more important.

Documentation became essential.

Git history became part of the documentation.

Architectural decisions needed to be justified rather than merely implemented.

Open source is not simply about publishing source code.

It is about enabling others to understand, maintain and extend that code.

This handbook is part of that objective.

---

# 3.11 Long-Term Maintainability

Many software projects fail because maintaining them eventually becomes more difficult than rewriting them.

WebInvestigator explicitly attempts to avoid that outcome.

Maintainability is therefore considered a first-class design objective.

Every architectural decision should reduce future maintenance costs whenever possible.

Sometimes this means writing slightly more code today.

If that prevents significantly greater complexity tomorrow, the decision is usually worthwhile.

The project optimizes for longevity rather than short-term development speed.

---

# 3.12 Guiding Principles

The philosophy of WebInvestigator can be summarized by the following principles.

- Build reusable components.

- Prefer clarity over cleverness.

- Keep responsibilities separate.

- Design for extensibility.

- Develop incrementally.

- Document architectural decisions.

- Favor reproducibility.

- Keep the framework transparent.

- Make contributors productive.

- Preserve maintainability.

Whenever uncertainty arises, these principles should take precedence over implementation convenience.

They define the identity of the project.

---

## Next Chapter

Now that the project's philosophy has been established, the next chapter introduces the overall architecture of WebInvestigator.

Rather than examining individual modules, it presents the framework as a complete system, following the journey of data from raw evidence to structured analysis reports.