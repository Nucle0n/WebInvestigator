# Chapter 6
# The Investigation Pipeline

---

> *"Software architecture is best understood by following data as it travels through the system."*

---

# 6.1 Introduction

The previous chapters introduced the philosophy and the structure of WebInvestigator.

We now know why the project exists.

We know how the repository is organized.

What remains unanswered is perhaps the most important question of all:

> **What actually happens when an investigation starts?**

Rather than studying isolated modules, this chapter follows the complete life cycle of a single piece of evidence as it travels through the framework.

This journey illustrates how the different architectural layers collaborate while remaining largely independent.

Throughout this chapter, imagine that an investigator has mirrored a suspicious website using HTTrack.

Among thousands of downloaded files is a single image:

```
investigations/
└── SuspiciousShop/
    └── assets/
        └── products/
            └── dragon_lamp.webp
```

Our objective is simple.

Understand how this file moves through the architecture until meaningful information is produced.

---

# 6.2 Stage One — Discovery

Before any analysis can begin, the framework must answer a fundamental question:

> **What evidence is available?**

This responsibility belongs entirely to the scanner.

The scanner walks through the investigation directory recursively.

It neither opens nor interprets files.

Instead, it records their existence.

Conceptually, its work resembles this:

```
Filesystem

│
├── index.html
├── style.css
├── script.js
├── dragon_lamp.webp
├── logo.png
└── ...

        │

        ▼

Scanner

        │

        ▼

Inventory
```

Notice something important.

At this stage, the framework still knows nothing about images.

The file could contain a photograph, an icon, or random binary data.

The scanner does not care.

Its mission ends once every artefact has been identified.

This extremely narrow responsibility makes the scanner both simple and reliable.

---

# 6.3 Stage Two — Selecting Relevant Evidence

Not every analyzer is interested in every file.

An image analyzer has no reason to inspect HTML documents.

A metadata analyzer may ignore text files.

Each analyzer therefore selects only the artefacts that concern it.

For example:

```
Inventory

├── html
├── css
├── javascript
├── png
├── jpg
├── webp
└── svg

        │

        ▼

Image Analyzer

        │

        ▼

Only image files
```

This filtering occurs naturally through the responsibilities of the analyzer itself.

The scanner remains completely unaware of which analyzers will eventually consume its inventory.

This is another example of loose coupling.

---

# 6.4 Stage Three — Analysis

The image analyzer now receives one file.

Its task is extremely precise.

Extract information.

Nothing more.

For our example image, the analyzer may determine:

- image dimensions;

- image format;

- file size;

- SHA-256 checksum;

- perceptual hash;

- future metadata.

Notice what does **not** happen.

The analyzer does not print anything.

It does not generate reports.

It does not compare the image with other investigations.

It simply transforms raw evidence into structured information.

Conceptually:

```
dragon_lamp.webp

        │

        ▼

Image Analyzer

        │

        ▼

ImageInfo
```

The output is no longer merely a file.

It has become knowledge.

---

# 6.5 Structured Knowledge

Why create an `ImageInfo` object instead of simply returning a dictionary?

Because architecture values consistency.

Imagine three different developers implementing three analyzers independently.

One returns:

```python
{
    "width": 512
}
```

Another returns:

```python
{
    "image_width": 512
}
```

A third chooses:

```python
{
    "w": 512
}
```

Every solution is technically correct.

Together, they create architectural chaos.

Shared models prevent this situation.

Every analyzer speaks the same language.

Every consumer understands that language.

Communication becomes predictable.

---

# 6.6 The Growing Investigation

One image rarely tells the whole story.

The investigation continues.

Another analyzer inspects filenames.

Another extracts metadata.

Another searches for duplicates.

Another computes statistics.

Each contributes one additional piece of information.

None of them attempts to understand the investigation alone.

Instead, they progressively enrich a shared representation.

Conceptually:

```
Inventory
      │
      ├──────────────┐
      │              │
      ▼              ▼

Image        Filename

Analyzer      Analyzer

      │              │
      └──────┬───────┘
             ▼

      AnalysisResult
```

This architecture allows dozens of analyzers to collaborate without depending directly on one another.

---

# 6.7 Why Aggregation Matters

Imagine that every analyzer returned its own independent object.

The main program might quickly resemble this:

```python
inventory = ...
images = ...
duplicates = ...
filenames = ...
metadata = ...
statistics = ...
colors = ...
thumbnails = ...
...
```

As the framework grows, the orchestration code becomes increasingly difficult to maintain.

Adding one analyzer requires modifying every place where results are passed around.

Instead, WebInvestigator progressively enriches a single object.

Each analyzer contributes new knowledge.

No analyzer needs to know what previous analyzers have already produced.

This greatly simplifies the pipeline.

---

# 6.8 Stage Four — Presentation

At this point, the investigation has been completed.

No further analysis remains.

Only presentation.

This responsibility belongs entirely to the output layer.

The output modules never inspect files themselves.

They never calculate hashes.

They never analyse images.

They simply transform structured models into representations suitable for humans or machines.

For example:

```
AnalysisResult

      │

      ├────────► Console

      ├────────► JSON

      ├────────► HTML

      ├────────► PDF

      └────────► Future Exporters
```

Notice that none of these outputs require modifications to the analyzers.

The pipeline remains unchanged.

Only new consumers are added.

---

# 6.9 Why This Matters

At first glance, this architecture may appear slightly more complicated than necessary.

A beginner could reasonably ask:

> "Why not print the results directly from each analyzer?"

Because today's output is rarely tomorrow's output.

A developer may initially want console output.

Later, another contributor requests JSON.

Months afterwards, someone proposes an HTML report.

Eventually, another developer builds a graphical interface.

If analyzers already contain presentation logic, every new output requires modifying every analyzer.

If analyzers only produce structured data, nothing changes.

New outputs simply consume existing models.

One architectural decision avoids years of future refactoring.

---

# 6.10 Following the Data

Looking back, the journey of our single image now appears remarkably simple.

```
dragon_lamp.webp

        │

        ▼

Scanner

        │

        ▼

Inventory

        │

        ▼

Image Analyzer

        │

        ▼

ImageInfo

        │

        ▼

AnalysisResult

        │

        ▼

Console

JSON

HTML

PDF

Future Outputs
```

At no point did the image analyzer need to know how reports are generated.

At no point did the scanner need to understand image formats.

At no point did output modules manipulate raw files.

Each layer remained focused on its own responsibility.

That simplicity is intentional.

---

# 6.11 Summary

The architecture of WebInvestigator is fundamentally a transformation pipeline.

Raw evidence gradually becomes structured knowledge.

Each stage performs one clearly defined responsibility.

Each stage passes its results to the next.

Because responsibilities remain isolated, the framework grows by adding components rather than modifying existing ones.

This property is one of the main reasons why the architecture has remained maintainable despite the steady addition of new analysis capabilities.

---

## Next Chapter

Having followed data through the framework, we are now ready to examine one of its most important architectural concepts:

**The Domain Model.**

The next chapter explains why WebInvestigator relies on shared models, how they define a common language between architectural layers, and why this decision became one of the cornerstones of the project.