# Chapter 4
# Overall Architecture

---

> *"A system is easier to understand when viewed as a flow rather than as a collection of files."*

---

# 4.1 Introduction

Before examining individual modules, it is important to understand how WebInvestigator behaves as a complete system.

One of the most common mistakes when approaching an unfamiliar codebase is to read files one after another.

Although this method eventually reveals how the software works, it rarely explains **why the files are organized this way**.

WebInvestigator is designed around a simple idea:

> **Data flows through independent processing stages.**

Each stage has a clearly defined responsibility.

Each stage transforms data.

Each stage passes its results to the next.

Once this principle is understood, the rest of the architecture becomes significantly easier to follow.

---

# 4.2 A Data-Oriented Architecture

Many applications are organized around user interfaces.

Others revolve around databases.

WebInvestigator is different.

Its architecture revolves around **data processing**.

Everything begins with digital evidence.

Everything ends with structured analysis results.

Between these two points lies a sequence of independent processing stages.

```
        Digital Evidence
               │
               ▼
        File Discovery
               │
               ▼
        Analysis Modules
               │
               ▼
        Analysis Results
               │
               ▼
      Output / Export Layer
```

The framework is therefore best understood as a pipeline.

Each component performs one transformation before passing control to the next stage.

---

# 4.3 Inputs

The framework deliberately avoids making assumptions about where evidence originates.

Evidence may come from:

- an HTTrack mirror;
- a ZIP archive;
- a local directory;
- extracted media;
- downloaded resources;
- future acquisition modules.

To WebInvestigator, these sources are equivalent.

Once evidence is available locally, every analyzer operates using the same abstractions.

This separation keeps acquisition independent from analysis.

---

# 4.4 Discovery

The first responsibility of the framework is discovering available files.

No analysis can begin before the available evidence has been identified.

This responsibility belongs exclusively to the scanner.

The scanner does not interpret files.

It does not inspect images.

It does not compute hashes.

Its only purpose is answering one question:

> **What exists?**

The result of this stage is a complete inventory of available artefacts.

---

# 4.5 Analysis

Once evidence has been discovered, specialized analyzers begin their work.

Each analyzer is responsible for one specific type of analysis.

Examples include:

- inventory analysis;
- filename inspection;
- image analysis;
- metadata extraction;
- duplicate detection;
- future analyzers.

An analyzer receives information.

It performs one transformation.

It produces structured results.

Nothing more.

Importantly, analyzers should remain independent whenever possible.

They should neither know nor care how other analyzers operate internally.

This dramatically reduces coupling.

---

# 4.6 Shared Models

As analyzers grow, exchanging raw dictionaries rapidly becomes problematic.

Different developers may choose different keys.

Types become inconsistent.

Validation becomes difficult.

To avoid these issues, WebInvestigator relies on shared models.

Models define a common language.

Instead of saying:

```
{
    "width": 1024,
    "height": 768
}
```

the framework exchanges objects whose structure is explicitly defined.

This provides several advantages.

- predictable interfaces;

- improved readability;

- static type checking;

- easier documentation;

- simpler maintenance.

Models therefore represent contracts between different architectural layers.

---

# 4.7 Aggregating Results

One analyzer rarely produces enough information to describe an investigation.

A complete investigation may involve dozens of independent analyses.

Managing dozens of separate return values would quickly become impractical.

Instead, WebInvestigator introduces a central aggregation object.

```
Inventory
      │
Filename Analysis
      │
Image Analysis
      │
Metadata
      │
Duplicates
      │
      ▼
AnalysisResult
```

Rather than returning numerous unrelated objects, analyzers progressively enrich a shared representation of the investigation.

This architecture scales naturally as additional analyzers are introduced.

Future chapters examine this design in detail.

---

# 4.8 Output

Analysis and presentation are intentionally separated.

This distinction is fundamental.

An analyzer computes information.

It never decides how that information should be displayed.

Likewise, output modules never perform analysis.

They simply present existing data.

```
Analyzer
     │
     ▼
Structured Data
     │
     ▼
Console Output

or

JSON Export

or

Future HTML Report

or

Future PDF Report
```

Because outputs consume structured models rather than implementation details, new export formats can be added without modifying analyzers.

---

# 4.9 Layer Responsibilities

The architecture can therefore be summarized as five distinct layers.

```
+----------------------------------+
|        Evidence Sources          |
+----------------------------------+

               │

+----------------------------------+
|        Discovery Layer           |
+----------------------------------+

               │

+----------------------------------+
|         Analysis Layer           |
+----------------------------------+

               │

+----------------------------------+
|      Shared Data Models          |
+----------------------------------+

               │

+----------------------------------+
|         Output Layer             |
+----------------------------------+
```

Each layer communicates with adjacent layers only.

Responsibilities never overlap.

This greatly simplifies maintenance.

---

# 4.10 Why This Architecture?

Several alternative designs were considered.

For example:

- analyzers directly printing results;

- analyzers exporting JSON themselves;

- analyzers calling each other;

- analyzers returning unrelated dictionaries.

Although each approach would have worked initially, they all introduce tighter coupling.

The chosen architecture deliberately favors separation.

Each component should remain useful independently from the rest of the framework.

This principle significantly improves extensibility.

---

# 4.11 Scalability

One useful way of evaluating an architecture is asking how it behaves after several years of development.

Imagine that WebInvestigator eventually contains:

- 50 analyzers;
- 30 report generators;
- multiple acquisition modules;
- graphical interfaces;
- command-line interfaces;
- automation pipelines.

Would the current architecture still work?

The answer should be yes.

That is precisely why the framework is organized around independent layers instead of direct dependencies between modules.

Growth should increase functionality.

It should not increase architectural complexity at the same rate.

---

# 4.12 Architectural Flow

The complete execution flow can be summarized as follows.

```
Local Evidence
      │
      ▼
Scanner
      │
      ▼
Inventory
      │
      ▼
Analyzer #1
      │
      ▼
Analyzer #2
      │
      ▼
Analyzer #3
      │
      ▼
AnalysisResult
      │
      ▼
Console Output
      │
      ├────────► JSON Export
      │
      ├────────► HTML Report
      │
      └────────► Future Plugins
```

Every investigation follows this same logical path.

Regardless of how many analyzers are eventually introduced, the overall architecture remains unchanged.

---

# 4.13 Summary

WebInvestigator is fundamentally a data-processing pipeline.

Evidence enters the framework.

Specialized analyzers enrich the available information.

Structured models transport results between architectural layers.

Finally, output modules present or export those results.

Each layer performs one responsibility.

Each responsibility belongs to one layer.

This simple rule explains most architectural decisions found throughout the project.

---

## Next Chapter

Now that the overall architecture has been introduced, the next chapter explores the repository itself.

Rather than discussing execution flow, it explains why the project is organized into its current directory structure and why each package exists.