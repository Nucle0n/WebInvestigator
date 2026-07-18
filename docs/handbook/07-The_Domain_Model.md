# Chapter 7
# The Domain Model

---

> *"Software components cannot collaborate unless they speak the same language."*

---

# 7.1 Introduction

Every software system manipulates information.

Some manipulate financial transactions.

Others manipulate customers, invoices or medical records.

WebInvestigator manipulates digital evidence.

Regardless of the programming language, one question inevitably arises:

> **How should information travel through the system?**

At first glance, the answer appears trivial.

Simply pass dictionaries.

Or JSON objects.

Or arbitrary variables.

For very small projects, this approach is perfectly acceptable.

For a framework expected to grow over many years, it rapidly becomes one of the largest sources of technical debt.

The Domain Model exists to prevent this evolution.

Rather than exchanging arbitrary data structures, every architectural layer communicates through explicitly defined models.

These models become the common language of the framework.

---

# 7.2 Information Is an Architectural Concern

Many beginners view data structures as implementation details.

They are not.

The way information is represented influences every aspect of a software architecture.

Poorly defined models lead to:

- inconsistent interfaces;
- duplicated logic;
- difficult documentation;
- fragile integrations;
- unpredictable behaviour.

Conversely, well-designed models make the entire framework easier to understand.

Developers no longer wonder what information an analyzer returns.

The answer is already defined.

Every analyzer returns known objects.

Every consumer expects known objects.

Uncertainty disappears.

---

# 7.3 From Files to Knowledge

Consider a single image discovered during an investigation.

Initially, it is nothing more than a sequence of bytes stored on disk.

```
dragon_lamp.webp
```

This file has no meaning to the framework.

Meaning only appears once analysis begins.

The image analyzer transforms raw bytes into structured information.

Conceptually, the evolution looks like this:

```
Raw File

        │

        ▼

Image Analyzer

        │

        ▼

ImageInfo
```

The important observation is that the analyzer does not merely extract values.

It creates knowledge.

Once represented as an `ImageInfo` object, the image is no longer simply a file.

It becomes a first-class concept inside the architecture.

---

# 7.4 The Problem with Dictionaries

Imagine three developers working independently.

Each needs to return an image width.

Developer A writes:

```python
{
    "width": 512
}
```

Developer B prefers:

```python
{
    "image_width": 512
}
```

Developer C chooses:

```python
{
    "w": 512
}
```

All three implementations work.

None of them are compatible.

The framework gradually becomes a collection of incompatible conventions.

Every consumer must remember which analyzer chose which terminology.

This situation rarely causes immediate failures.

Instead, it creates continuous friction.

Every new feature becomes slightly more expensive to implement.

Every contributor invents another convention.

The architecture slowly fragments.

---

# 7.5 Models as Contracts

WebInvestigator avoids this problem by treating models as contracts.

A contract answers one simple question:

> **What information exists?**

Not:

> **How was it calculated?**

Nor:

> **How will it be displayed?**

Only:

> **What does this concept contain?**

For example, an `ImageInfo` object describes an image.

It does not calculate hashes.

It does not display reports.

It simply defines what an image means inside the framework.

This distinction is fundamental.

Behaviour belongs elsewhere.

Meaning belongs inside the model.

---

# 7.6 A Shared Vocabulary

Once every analyzer uses the same models, something interesting happens.

Developers stop talking about variables.

Instead, they begin talking about concepts.

Rather than saying:

> "Pass the dictionary containing width, height and format."

They simply say:

> "Pass an ImageInfo."

The architecture has acquired its own vocabulary.

This greatly improves communication.

Documentation becomes easier to write.

Code reviews become easier to conduct.

Discussions become more precise.

The framework becomes easier to teach.

One of the hidden benefits of good models is that they simplify human communication as much as software communication.

---

# 7.7 Separating Data from Behaviour

Another important architectural decision concerns responsibility.

Models describe information.

They do not process it.

Suppose an `ImageInfo` object contains:

- dimensions;
- file format;
- checksum;
- perceptual hash.

Should it also calculate those values?

No.

Those responsibilities belong to analyzers.

Likewise, should the model generate JSON?

No.

That responsibility belongs to the output layer.

A model should remain a description of reality.

Nothing more.

This separation keeps every architectural layer focused on its own responsibility.

---

# 7.8 Stable Interfaces

Implementation changes constantly.

Interfaces should not.

Imagine that a future version of the image analyzer uses another library.

Or parallel processing.

Or GPU acceleration.

Or artificial intelligence.

Should every output module require modification?

Ideally, no.

As long as the analyzer still produces the same `ImageInfo` object, nothing else changes.

The implementation has evolved.

The contract has not.

Stable interfaces allow internal improvements without disturbing the rest of the architecture.

This is one of the strongest arguments in favour of explicit models.

---

# 7.9 Building Larger Concepts

Simple models eventually combine into larger ones.

An investigation does not consist of one image.

It consists of many different observations.

Conceptually:

```
ImageInfo

FilenameInfo

MetadataInfo

DuplicateInfo

Statistics

        │

        ▼

AnalysisResult
```

Smaller concepts progressively form larger concepts.

The architecture therefore mirrors reality.

A complete investigation naturally contains many different kinds of information.

---

# 7.10 Why AnalysisResult Exists

One of the most important models inside WebInvestigator is `AnalysisResult`.

At first glance, it may appear to be little more than a container.

In reality, it solves a significant architectural problem.

Without it, every analyzer would introduce another return value.

```
inventory

images

duplicates

metadata

statistics

filenames

...
```

The orchestration layer would become increasingly difficult to maintain.

Instead, every analyzer contributes to the same investigation object.

This architecture scales naturally.

Adding another analyzer no longer changes the pipeline.

It simply enriches an existing representation.

Future chapters examine `AnalysisResult` in much greater detail.

---

# 7.11 Models Outlive Implementations

One useful way to evaluate an architectural decision is to imagine rewriting the framework from scratch.

Suppose WebInvestigator were rewritten in another language.

The scanner would change.

The analyzers would change.

The output modules would change.

Even the build system would change.

Would the concepts of:

- ImageInfo;
- Inventory;
- AnalysisResult;

still exist?

Almost certainly.

This observation reveals something important.

The models describe the problem domain.

Not the implementation.

Good domain models often survive multiple generations of software.

---

# 7.12 Summary

The Domain Model is the shared language of WebInvestigator.

It allows independent components to collaborate without knowing each other's internal implementation.

Models describe concepts.

Analyzers create them.

Output modules consume them.

Together, they provide a stable foundation upon which the rest of the framework can evolve.

Without a consistent domain model, the architecture would gradually fragment into incompatible conventions.

With one, every new feature naturally integrates into an already coherent system.

---

## Next Chapter

A shared language is only valuable if every component speaks it consistently.

Within WebInvestigator, that responsibility belongs to the analyzers.

The next chapter explores the analyzer architecture, explaining why small, independent components remain one of the framework's greatest strengths as it continues to evolve.

**[The Analyzer Architecture](./08-The_Analyzer_Architecture.md)**