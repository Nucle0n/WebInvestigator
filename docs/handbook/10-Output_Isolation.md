# Chapter 10
# Output Isolation

---

> *"Producing information and presenting information are two fundamentally different responsibilities."*

---

# 10.1 Introduction

One of the earliest architectural decisions made during the development of WebInvestigator was also one of the least visible.

Analyzers would never produce user-visible output.

At first glance, this rule may appear arbitrary.

After all, once an analyzer has computed a result, printing it immediately seems perfectly reasonable.

For very small scripts, this approach works well.

Many automation scripts are little more than:

```
Read data

↓

Process data

↓

print(result)
```

Nothing is inherently wrong with this design.

In fact, it is often the simplest possible solution.

However, WebInvestigator was never intended to remain a small script.

It was intended to become a framework.

Frameworks require different architectural choices.

---

# 10.2 The Hidden Cost of print()

Imagine the following image analyzer.

```
Read image

↓

Compute SHA-256

↓

Compute perceptual hash

↓

Print results
```

Initially, everything works perfectly.

The investigator launches the program and immediately sees useful information.

A few weeks later, another requirement appears.

The same information must now be exported as JSON.

The analyzer suddenly becomes responsible for two outputs.

```
Read image

↓

Analyze

├── Console

└── JSON
```

A few months later, an HTML report is requested.

Then a graphical interface.

Then an API.

Eventually the analyzer resembles this:

```
Analyze

├── Console

├── JSON

├── HTML

├── PDF

└── GUI
```

The analyzer has quietly acquired responsibilities that have nothing to do with analysis.

Its original purpose has become diluted.

---

## Common Pitfall

Presentation logic often enters a project gradually.

Rarely does someone decide to build a monolithic analyzer.

Instead, every new requirement adds "just one more print()" or "just one more export."

Years later, developers discover that business logic and presentation have become inseparable.

Good architecture prevents this situation before it appears.

---

# 10.3 Analysis Produces Knowledge

An analyzer answers questions.

For example:

- What are the dimensions of this image?

- Which checksum identifies it?

- Is another file visually similar?

These answers represent knowledge.

Knowledge exists independently from the way it is displayed.

Whether the information eventually appears as:

- plain text;

- colored terminal output;

- JSON;

- HTML;

- XML;

- PDF;

- graphical widgets;

does not change the information itself.

Presentation changes.

Knowledge does not.

This distinction lies at the heart of the output architecture.

---

# 10.4 A Different Perspective

Instead of asking:

> "How should the analyzer display its results?"

WebInvestigator asks a different question:

> "How should another component display the analyzer's results?"

This small change in perspective completely transforms the architecture.

The analyzer becomes responsible only for producing structured information.

Everything else becomes someone else's responsibility.

---

# 10.5 The Output Layer

The output layer exists for one purpose.

Transform structured models into representations intended for either humans or machines.

Conceptually:

```
AnalysisResult

        │

        ▼

Output Layer

        │

        ├── Console

        ├── JSON

        ├── HTML

        ├── PDF

        └── Future Outputs
```

Notice that every output receives exactly the same information.

Only the representation changes.

---

# 10.6 Why This Matters

Suppose tomorrow someone wishes to create a web interface for WebInvestigator.

Should every analyzer require modification?

Ideally, no.

The analyzers already produce structured models.

The web interface simply becomes another consumer of those models.

Exactly the same applies to:

- REST APIs;

- desktop applications;

- mobile applications;

- automated pipelines;

- cloud services.

All of them consume the same investigation.

Only the presentation differs.

---

## Architect's Note

Early prototypes of WebInvestigator occasionally allowed analyzers to display their own results.

While convenient during experimentation, this quickly became repetitive.

Every analyzer needed formatting code.

Every analyzer decided how information should appear.

Every analyzer solved the same presentation problems independently.

The duplication became obvious.

Presentation was therefore extracted into dedicated output modules long before the framework reached its current architecture.

Looking back, this decision significantly simplified every analyzer that followed.

---

# 10.7 Formatting Is a Responsibility

Formatting may appear trivial.

It is not.

Consider a single SHA-256 hash.

One output might display:

```
SHA-256:
A41F...
```

Another might display:

```json
{
    "sha256": "A41F..."
}
```

A graphical interface might show:

```
✔ SHA-256 Available
```

The information is identical.

Only the representation changes.

Formatting is therefore a genuine architectural responsibility.

It deserves its own dedicated layer.

---

# 10.8 Testing Becomes Simpler

Separating outputs from analyzers also improves testing.

Testing an analyzer becomes straightforward.

Provide known input.

Verify the generated models.

No console capture.

No formatted strings.

No ANSI escape sequences.

No JSON serialization.

Likewise, output modules can be tested independently.

Provide known models.

Verify the produced representation.

Each component now has a clearly defined scope.

---

# 10.9 Architectural Parallels

The idea of separating computation from presentation is not unique to WebInvestigator.

It appears repeatedly across software engineering.

The Unix philosophy encourages programs to produce data that other programs can consume.

Model–View–Controller separates business logic from presentation.

Clean Architecture isolates application rules from user interfaces.

Although WebInvestigator was not explicitly designed around any single architectural pattern, it naturally converged toward the same principle:

> **Business logic should not depend on presentation.**

The recurrence of this idea across different architectural styles suggests that it addresses a fundamental problem rather than a framework-specific one.

---

# 10.10 The Long-Term Benefit

Good architecture is often invisible.

Nobody notices when adding a new output requires writing only one additional module.

Nobody notices when analyzers remain unchanged despite years of evolution.

These absences are precisely the benefits of output isolation.

The architecture quietly absorbs change.

Developers remain focused on implementing new capabilities rather than rewriting existing ones.

This is one of the defining characteristics of maintainable software.

---

# 10.11 Summary

Output isolation is not about avoiding `print()`.

It is about protecting analyzers from responsibilities that do not belong to them.

By separating analysis from presentation, WebInvestigator allows both layers to evolve independently.

Analyzers remain focused on producing knowledge.

Output modules remain focused on communicating that knowledge.

Together, they create an architecture capable of supporting new interfaces without disturbing existing analysis code.

---

## Next Chapter

Having explored how information leaves the framework, the next chapter examines another essential architectural principle:

**Loose Coupling and Dependency Management.**

Why should components know as little as possible about one another?

How can independent modules still collaborate effectively?

These questions lie at the foundation of every maintainable software architecture.