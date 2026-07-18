# Chapter 9
# AnalysisResult — The Investigation Object

---

> *"An investigation is not a collection of independent analyses.
> It is a coherent body of knowledge."*

---

# 9.1 Introduction

Throughout the previous chapters, one object has repeatedly appeared without being fully explained.

`AnalysisResult`

At first glance, it appears deceptively simple.

It contains the results produced by the different analyzers.

Nothing more.

Many developers would therefore be tempted to dismiss it as a simple container.

That conclusion would be a mistake.

Although `AnalysisResult` contains very little business logic, it is one of the most important architectural components of the entire framework.

Its purpose is not computation.

Its purpose is orchestration.

---

# 9.2 The Orchestration Problem

Imagine that WebInvestigator contains only two analyzers.

```
Inventory Analyzer

Image Analyzer
```

The main program might simply do something similar to:

```
inventory = ...

images = ...
```

Perfectly reasonable.

Now imagine that the framework evolves.

```
Inventory

Images

Metadata

Statistics

Duplicates

Filenames

OCR

Certificates

Colors

Archives

...

```

The orchestration layer slowly becomes responsible for carrying an ever-growing number of variables.

Eventually the execution flow begins to resemble this:

```
inventory

images

duplicates

statistics

metadata

colors

archives

ocr

...

```

Every new analyzer requires another variable.

Another parameter.

Another function signature.

Another opportunity for mistakes.

The architecture becomes increasingly fragile.

---

## Design Rationale

The problem is not the number of analyzers.

The problem is that the orchestration layer becomes responsible for remembering every analyzer that exists.

Architectural complexity gradually migrates toward the application's entry point.

`AnalysisResult` prevents this migration.

---

# 9.3 A Growing Investigation

Instead of creating one variable per analyzer, WebInvestigator models the investigation itself.

Conceptually:

```
Investigation

│

├── Inventory

├── Images

├── Metadata

├── Statistics

├── Duplicates

├── Filenames

└── ...

```

Notice the subtle difference.

The framework no longer manipulates isolated analysis results.

It manipulates a single investigation.

Each analyzer contributes new observations.

No analyzer owns the investigation.

Every analyzer enriches it.

This mirrors the way real investigations evolve.

---

# 9.4 An Investigation Is More Than Its Parts

Consider a criminal investigation.

Different specialists may contribute:

- fingerprints;

- DNA;

- surveillance footage;

- witness statements;

- financial records.

Each expert produces independent observations.

The investigation itself is the combination of all those observations.

No individual report represents the complete investigation.

`AnalysisResult` follows exactly the same philosophy.

Each analyzer produces knowledge.

The investigation object gradually accumulates that knowledge.

---

# 9.5 Ownership

One important consequence of this design concerns ownership.

Who owns image information?

The image analyzer creates it.

Afterwards, however, the information belongs to the investigation.

Not to the analyzer.

This distinction prevents analyzers from becoming long-lived managers of information.

Analyzers perform work.

The investigation stores knowledge.

---

# 9.6 Communication Without Dependencies

Earlier chapters emphasized that analyzers should not communicate directly.

`AnalysisResult` explains how that collaboration nevertheless occurs.

Suppose the duplicate analyzer needs image hashes.

Should it call the image analyzer?

No.

The image analyzer has already enriched the investigation.

The duplicate analyzer simply reads the information already available.

Conceptually:

```
Image Analyzer

│

▼

AnalysisResult

│

▼

Duplicate Analyzer
```

The analyzers never know about one another.

They only know about the investigation.

This greatly reduces coupling.

---

## Architect's Note

One of the earliest architectural temptations was allowing analyzers to call one another directly.

Initially this appeared convenient.

Very quickly it became obvious that dependencies would spread throughout the project.

The idea was abandoned before the architecture stabilized.

Instead, every analyzer now collaborates indirectly through shared models.

Looking back, this decision probably eliminated an entire category of future maintenance problems.

---

# 9.7 Progressive Enrichment

One interesting property of `AnalysisResult` is that it starts almost empty.

At the beginning of an investigation:

```
AnalysisResult
```

contains very little information.

After each analyzer completes:

```
AnalysisResult

├── Inventory
```

then

```
AnalysisResult

├── Inventory

├── Images
```

then

```
AnalysisResult

├── Inventory

├── Images

├── Metadata
```

and so on.

The investigation evolves naturally.

Nothing is replaced.

Knowledge accumulates.

---

# 9.8 Future Growth

Imagine WebInvestigator ten years from now.

Perhaps it contains:

- OCR analysis;
- AI classification;
- steganography detection;
- malware signatures;
- PDF analysis;
- browser fingerprinting;
- TLS inspection.

Will the orchestration layer require major redesign?

No.

Every new analyzer simply contributes another piece of knowledge to the investigation.

This is the real strength of `AnalysisResult`.

Growth affects content.

Not architecture.

---

# 9.9 Why Not a Database?

Some readers may wonder why investigation results are not immediately written into a database.

The answer lies in responsibility.

`AnalysisResult` represents the investigation while it is being built.

Persistence is a separate concern.

Whether results are eventually exported as:

- JSON,
- SQLite,
- PostgreSQL,
- HTML,
- PDF,

does not change the internal architecture.

The investigation exists independently from its storage mechanism.

Keeping these concerns separate preserves flexibility.

---

# 9.10 A Stable Center

One useful way to visualize the architecture is as a wheel.

```
             Image Analyzer

                    │

Metadata ───────────┼────────── Filename

                    │

            AnalysisResult

                    │

Duplicates ─────────┼──────── Statistics

                    │

               Future Modules
```

The analyzers may continue growing indefinitely.

The center remains stable.

Good architectures often possess such stable centers.

They provide continuity while allowing the surrounding system to evolve.

---

# 9.11 Summary

`AnalysisResult` is much more than a container.

It represents the investigation itself.

By progressively accumulating structured knowledge, it allows independent analyzers to collaborate without introducing direct dependencies.

This design keeps the orchestration layer simple, enables future expansion and provides a stable foundation for the entire framework.

Its apparent simplicity hides one of the most influential architectural decisions in WebInvestigator.

---

## Next Chapter

The next chapter examines another cornerstone of the architecture:

**Output Isolation.**

Why do analyzers never print?

Why are JSON exports implemented separately?

Why is presentation considered an independent architectural layer?

Although these choices initially appear to require more work, they dramatically reduce long-term complexity.