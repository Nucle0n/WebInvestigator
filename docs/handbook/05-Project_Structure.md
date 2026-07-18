# Chapter 5
# Project Structure

---

> *"Every directory tells a story.
> A well-designed repository tells the architecture."*

---

# 5.1 Introduction

One of the easiest ways to estimate the maturity of a software project is to examine its directory tree.

A repository is never just a collection of files.

It reflects the way developers think about their software.

In small projects, the directory structure often grows organically.

New files are added wherever they seem convenient.

Responsibilities gradually overlap.

Dependencies become increasingly difficult to understand.

Eventually, developers spend more time navigating the repository than implementing new features.

WebInvestigator deliberately attempts to avoid this evolution.

Its repository is organized according to architectural responsibilities rather than implementation convenience.

Understanding this organization is essential before examining individual modules.

---

# 5.2 Organizing Around Responsibilities

A common mistake consists of organizing projects around file types.

For example:

```
images/
json/
classes/
scripts/
utilities/
```

Although such structures appear simple at first, they quickly become problematic.

Files that collaborate closely become physically separated.

Responsibilities become scattered across the repository.

Developers are forced to constantly jump between unrelated directories.

Instead, WebInvestigator groups code according to **what it does**, not according to **what it is**.

Each package represents one architectural responsibility.

This distinction may appear subtle.

Its long-term impact is considerable.

---

# 5.3 A High-Level Overview

At the time of writing, the project is organized around the following structure.

```
WebInvestigator/

├── investigations/
├── reports/
├── tests/
├── lib/
│   ├── analyzer/
│   ├── model/
│   ├── output/
│   ├── scanner.py
│   └── utils.py
│
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

Each element exists for a specific reason.

Nothing has been introduced accidentally.

---

# 5.4 The Entry Point

```
main.py
```

Every application begins somewhere.

In WebInvestigator, that responsibility belongs to `main.py`.

Its purpose is intentionally limited.

It coordinates the execution of the framework.

It does not perform analysis.

It does not implement business logic.

It simply orchestrates the different architectural layers.

Keeping the entry point lightweight has several advantages.

First, execution flow remains immediately understandable.

Second, business logic remains testable independently from application startup.

Finally, future interfaces—such as a graphical application, a REST API or a command-line interface—can reuse the same internal components without duplicating logic.

The entry point starts the framework.

It should never become the framework.

---

# 5.5 Configuration

```
config.py
```

Configuration deserves its own location.

Hardcoding values throughout the project inevitably creates maintenance problems.

Paths.

Extensions.

Constants.

Feature flags.

Default behaviours.

Keeping these values centralized provides a single source of truth.

Whenever configuration changes, developers know exactly where to look.

Equally important, analyzers remain focused on analysis instead of configuration management.

---

# 5.6 The Scanner

```
lib/scanner.py
```

Before anything can be analysed, evidence must be discovered.

This responsibility belongs exclusively to the scanner.

The scanner traverses directories.

It identifies files.

It constructs an inventory.

It deliberately avoids interpreting what it finds.

This distinction is fundamental.

Discovering evidence and understanding evidence are two completely different responsibilities.

Separating them makes both considerably simpler.

---

# 5.7 The Analyzer Package

```
lib/analyzer/
```

The analyzer package contains the core intelligence of the framework.

Each analyzer performs one type of analysis.

Nothing more.

Examples include:

- image inspection;

- filename analysis;

- metadata extraction;

- duplicate detection.

Every analyzer shares several important characteristics.

It receives structured input.

It performs one transformation.

It returns structured output.

An analyzer never decides how results are displayed.

It never communicates directly with another analyzer.

This independence allows the project to grow horizontally.

Adding another analyzer should resemble adding another tool to a toolbox—not modifying every existing tool.

---

# 5.8 The Model Package

```
lib/model/
```

Software inevitably manipulates data.

The question is not whether data structures exist.

The question is where they belong.

WebInvestigator isolates every shared data structure inside the `model` package.

This package defines the vocabulary spoken by the entire framework.

Examples include:

- inventory objects;

- image information;

- analysis results;

- future metadata models.

By centralizing shared structures, every architectural layer communicates using the same language.

This dramatically reduces ambiguity.

Models therefore become contracts between independent components.

---

# 5.9 The Output Package

```
lib/output/
```

Presenting information is a responsibility of its own.

Console rendering.

JSON export.

Future HTML reports.

Future PDF generation.

These are all presentation concerns.

Keeping them inside a dedicated package prevents presentation logic from leaking into analyzers.

This separation also makes supporting additional output formats remarkably inexpensive.

A new output module simply consumes existing models.

The analysis pipeline remains unchanged.

---

# 5.10 Tests

```
tests/
```

Testing is intentionally separated from production code.

Although obvious, this decision has important consequences.

Tests document expected behaviour.

They provide confidence during refactoring.

They reduce regression risks.

Perhaps more importantly, they encourage modular architecture.

Code that cannot easily be tested often indicates responsibilities that have become too tightly coupled.

In this sense, testability is frequently a useful indicator of architectural quality.

---

# 5.11 Investigations

```
investigations/
```

Unlike the framework itself, this directory contains data rather than software.

Each investigation represents a dataset.

The framework analyses these datasets.

It should never depend on their specific content.

Keeping investigations separate from the codebase reinforces an important architectural principle:

**Data and behaviour evolve independently.**

The framework may change.

Datasets may change.

Neither should require modifications to the other.

---

# 5.12 Reports

```
reports/
```

Analysis produces knowledge.

Reports preserve it.

Generated reports are intentionally isolated from the framework itself.

This prevents generated artefacts from polluting source code.

It also simplifies version control.

Source files describe how analyses are performed.

Reports describe what those analyses discovered.

These are fundamentally different concerns.

---

# 5.13 Why This Structure Scales

At first glance, the repository may appear larger than necessary.

A beginner could reasonably ask:

> Why not place everything inside a single directory?

The answer is simple.

Because software rarely remains small.

The cost of introducing structure early is negligible.

The cost of introducing it late can be enormous.

As the number of analyzers grows, responsibilities remain stable.

Developers immediately know where new code belongs.

Architectural consistency becomes self-reinforcing.

Good directory structures reduce the number of design decisions developers must make every day.

That reduction is one of the hidden sources of maintainability.

---

# 5.14 A Repository as Documentation

One of the objectives of WebInvestigator is that its directory tree should already explain part of the architecture.

Ideally, a new contributor should be capable of opening the repository and immediately identifying:

- where analyses live;

- where data models are defined;

- where outputs are generated;

- where datasets are stored;

- where execution begins.

When a repository naturally answers these questions, it has become more than a collection of files.

It has become documentation.

---

## Next Part

The foundations of WebInvestigator are now in place.

Understanding an architecture, however, requires more than knowing its philosophy and organization. It requires observing how its components collaborate to transform raw evidence into meaningful knowledge.

The next part begins by exploring the Investigation Pipeline, following the complete life cycle of an investigation from discovery to structured analysis.

**[The Investigation Pipeline](./06-The_Investigation_Pipeline.md)**