# Chapter 8
# The Analyzer Architecture

---

> *"A good analyzer does one thing, does it well, and can be forgotten once its work is done."*

---

# 8.1 Introduction

If WebInvestigator has a heart, it is undoubtedly the analyzer layer.

Scanners discover evidence.

Models describe evidence.

Outputs present evidence.

Analyzers transform evidence into knowledge.

Everything interesting happens here.

Despite their importance, analyzers deliberately remain among the simplest components of the framework.

This simplicity is not accidental.

It is one of the project's strongest architectural decisions.

---

# 8.2 One Analyzer, One Responsibility

Every analyzer exists for exactly one reason.

Not two.

Not "roughly one."

Exactly one.

An image analyzer analyzes images.

A filename analyzer analyzes filenames.

A metadata analyzer analyzes metadata.

Nothing more.

At first this rule may appear overly strict.

In practice it provides remarkable long-term benefits.

Imagine an analyzer responsible for:

- reading EXIF metadata,
- calculating SHA-256,
- detecting duplicates,
- exporting JSON,
- printing console output.

Such a component would work.

It would also be almost impossible to evolve safely.

Changing one responsibility risks breaking another.

Testing becomes increasingly difficult.

Refactoring becomes dangerous.

Eventually nobody wants to modify it.

Software engineers have a name for this phenomenon.

It is commonly called a **God Object**.

WebInvestigator deliberately avoids creating them.

---

# 8.3 Small Components Scale Better

One of the recurring themes throughout this handbook is that software grows.

Architecture should therefore be evaluated according to how it behaves after years of development, not after the first thousand lines of code.

Suppose that five years from now, WebInvestigator contains:

- 60 analyzers;
- several thousand unit tests;
- multiple contributors;
- plugins developed by third parties.

Would large analyzers still be manageable?

Probably not.

Small analyzers, however, remain understandable regardless of how many other analyzers exist.

Complexity grows linearly instead of exponentially.

This property is one of the principal reasons behind the current architecture.

---

# 8.4 An Analyzer Is a Transformation

One useful way to think about an analyzer is as a mathematical function.

It receives information.

It transforms that information.

It returns new information.

Nothing else.

Conceptually:

```
Input

      │

      ▼

Analyzer

      │

      ▼

Output
```

Notice what is absent.

No user interface.

No logging.

No report generation.

No configuration management.

No orchestration.

These responsibilities belong elsewhere.

Keeping analyzers pure makes them predictable.

Predictable components are easier to trust.

---

# 8.5 Independence

An analyzer should never require intimate knowledge of another analyzer.

Consider two examples.

### Poor Design

```
Image Analyzer

        │

        ▼

calls

        ▼

Duplicate Analyzer

        ▼

calls

        ▼

Metadata Analyzer
```

Each analyzer depends on another.

Changing one risks affecting all the others.

This architecture quickly becomes fragile.

---

### Preferred Design

```
               Inventory

                    │

     ┌──────────────┼──────────────┐

     ▼              ▼              ▼

 Image        Metadata      Filename

 Analyzer      Analyzer      Analyzer

     │              │              │

     └──────────────┼──────────────┘

                    ▼

             AnalysisResult
```

Every analyzer collaborates.

None depends directly on another.

The orchestration layer coordinates execution.

Analyzers remain independent.

---

# 8.6 Communication Through Models

If analyzers never call one another, how do they collaborate?

Through shared models.

The image analyzer enriches the investigation.

The filename analyzer enriches the same investigation.

The duplicate analyzer enriches it again.

Every analyzer contributes information.

None requires knowledge of how previous information was obtained.

This architecture resembles several specialists examining the same crime scene.

Each expert writes a report.

The investigation combines those reports later.

Experts do not rewrite each other's conclusions.

---

# 8.7 Stateless by Design

Whenever possible, analyzers should remain stateless.

Their behaviour should depend only on the information they receive.

Not on previous executions.

Not on hidden caches.

Not on global variables.

Stateless components are significantly easier to:

- understand;
- test;
- parallelize;
- reuse.

Although certain future analyzers may legitimately require internal state, stateless design remains the preferred default.

---

# 8.8 Error Isolation

Failures should remain local.

Suppose an analyzer encounters an unsupported image format.

Should the entire investigation stop?

Usually not.

Ideally, the analyzer reports the problem while allowing the remaining analyzers to continue.

This principle is known as **error isolation**.

Independent analyzers naturally support this behaviour.

One failure should never invalidate unrelated analyses.

Investigations often involve imperfect evidence.

The framework should therefore remain resilient.

---

# 8.9 Designing for the Unknown

One of the strengths of the analyzer architecture is that it was designed without knowing which analyzers would eventually exist.

At the time the architecture was defined, only a handful of analyzers had been implemented.

Yet the architecture already anticipated future growth.

Today it may include:

- image analysis;
- filename inspection;
- duplicate detection.

Tomorrow it might include:

- OCR;
- EXIF correlation;
- machine learning classification;
- steganography detection;
- certificate inspection;
- archive reconstruction.

The architecture should welcome these additions naturally.

Not require redesign.

---

# 8.10 The Cost of Coupling

Software architecture is often a matter of minimizing future costs.

Coupling is one of those costs.

Imagine an analyzer responsible for computing image hashes.

Several months later, another analyzer needs the same hashes.

Should it call the first analyzer?

Perhaps.

Should it duplicate the code?

Certainly not.

The preferred solution is different.

Move the shared behaviour into a reusable service.

Both analyzers depend on the service.

Neither depends on the other.

This distinction may appear minor.

It often determines whether an architecture remains maintainable after several years.

---

# 8.11 Testability

A useful consequence of small analyzers is testability.

Testing an analyzer should be straightforward.

Provide known input.

Execute the analyzer.

Verify the produced model.

Nothing else.

If writing a unit test becomes unexpectedly difficult, it often indicates that the analyzer has acquired responsibilities it should not have.

In this sense, testing is more than quality assurance.

It is an architectural feedback mechanism.

Well-designed analyzers naturally become easy to test.

Poorly designed analyzers resist testing.

---

# 8.12 Future Parallelism

One interesting property of independent analyzers is that they create opportunities for future optimization.

Today, analyzers may execute sequentially.

Tomorrow, independent analyzers could execute simultaneously.

```
Inventory

      │

      ▼

┌──────────────┐
│ Thread Pool  │
└──────────────┘

   │    │    │

   ▼    ▼    ▼

Image  Meta Filename

Analyzer Analyzer Analyzer

   │    │    │

   └────┼────┘

        ▼

AnalysisResult
```

Because analyzers avoid direct dependencies, introducing parallel execution becomes largely an orchestration problem rather than an architectural one.

Good architecture often enables capabilities long before they become necessary.

---

# 8.13 Summary

The analyzer layer is intentionally conservative.

Every analyzer performs one responsibility.

Every analyzer remains largely independent.

Communication occurs through shared models.

Presentation belongs elsewhere.

Errors remain isolated.

Together, these principles allow WebInvestigator to grow by addition rather than modification.

This property lies at the core of the framework's long-term maintainability.

---

## Next Chapter

The previous chapters explained how analyzers produce knowledge.

The next chapter examines the object that unifies all of that knowledge:

**AnalysisResult.**

Although it appears deceptively simple, it solves one of the most important orchestration problems in the entire architecture.