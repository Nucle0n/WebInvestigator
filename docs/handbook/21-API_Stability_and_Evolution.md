# Chapter 21
# API Stability and Evolution

---

> *"An interface is a promise. Breaking that promise should never become routine."*

---

# 21.1 Introduction

Software rarely remains static.

New requirements appear.

Existing models evolve.

Additional metadata becomes useful.

Functions gain new capabilities.

As software grows, change becomes inevitable.

Yet change introduces a dilemma.

How can a framework evolve without constantly forcing every existing component to change alongside it?

Long-lived software answers this question through stable interfaces.

WebInvestigator follows the same philosophy.

Evolution should be continuous.

Disruption should remain exceptional.

---

# 21.2 More APIs Than You Think

When developers hear the word *API*, they often imagine REST endpoints or public libraries.

Architecture tells a different story.

Every interaction between two independent components forms an interface.

A model consumed by several analyzers.

A method exposed by the scanner.

An exporter reading an `AnalysisResult`.

A configuration object shared across the framework.

These are all APIs.

Some are public.

Many are entirely internal.

Their stability matters just as much.

---

# 21.3 Interfaces Are Contracts

Previous chapters introduced the idea of contracts.

This chapter extends that principle.

Whenever one component depends upon another, an agreement exists.

The provider promises to expose certain behavior.

The consumer promises to use that behavior correctly.

As long as both respect the agreement, they remain independent.

Once interfaces change unpredictably, independence begins to disappear.

Stable software therefore depends more on stable contracts than on stable implementations.

---

## Design Rationale

Implementations should evolve freely.

Interfaces should evolve carefully.

Keeping this distinction clear allows developers to improve internal code without forcing unrelated changes throughout the project.

---

# 21.4 Growing Without Breaking

Imagine that `ImageInfo` currently stores:

```
width
height
format
```

Months later, the project gains support for:

```
sha256
phash
mime_type
```

Existing analyzers continue reading width and height.

Nothing changes for them.

The model has grown.

It has not broken.

This illustrates one of the safest forms of evolution.

Adding information is generally less disruptive than redefining existing meaning.

---

# 21.5 Breaking Changes

Not every modification is harmless.

Suppose the field:

```
width
```

is renamed to:

```
horizontal_resolution
```

The new name may appear more descriptive.

Unfortunately, every existing consumer must now change.

The improvement is local.

The consequences are global.

Before introducing such modifications, architects should ask:

> **Does the benefit justify the disruption?**

Sometimes the answer is yes.

Often it is not.

---

## Common Pitfall

Renaming identifiers because a "better name" has been discovered is rarely free.

Every interface change consumes time for every downstream component.

Good naming matters.

Stable naming matters even more.

---

# 21.6 Compatibility Through Addition

Whenever practical, evolution should prefer addition over replacement.

Instead of changing existing behavior, introduce new capabilities alongside it.

Consumers can migrate progressively.

Older code continues functioning.

New code benefits from additional features.

This gradual evolution dramatically reduces maintenance pressure.

Backward compatibility is often less expensive than widespread migration.

---

# 21.7 Internal Freedom

An interesting consequence follows.

Stable interfaces provide freedom behind the scenes.

Suppose an analyzer replaces Pillow with another image library.

As long as the exported `ImageInfo` remains identical, the rest of the framework remains unaffected.

Consumers care about results.

They should not need to understand implementation details.

Well-designed interfaces isolate change.

---

## Architect's Note

One reason WebInvestigator favors models over loosely structured dictionaries is precisely this.

Typed models establish explicit contracts.

Changing those contracts becomes an intentional architectural decision rather than an accidental side effect.

---

# 21.8 Versioning Thoughtfully

Not every change deserves a new version.

Not every version deserves breaking changes.

Frameworks frequently accumulate unnecessary incompatibilities simply because maintaining compatibility appears inconvenient.

WebInvestigator instead encourages restraint.

Breaking interfaces should remain a deliberate architectural event.

Not a routine occurrence during normal development.

---

# 21.9 Stability Builds Confidence

Stable interfaces create confidence.

Contributors know their work will continue functioning.

Tests remain meaningful.

Documentation remains relevant.

Refactoring becomes safer.

Architecture becomes calmer.

Ironically, software capable of evolving continuously often changes less dramatically than software rewritten repeatedly.

Stability encourages gradual improvement.

---

## Historical Perspective

Many successful open-source projects owe part of their longevity to carefully preserving compatibility.

Linux, Python and Git have all evolved enormously over the years.

Yet code written many years ago frequently continues to function with surprisingly few modifications.

Their implementations evolved relentlessly.

Their interfaces evolved cautiously.

This distinction contributed significantly to their success.

---

# 21.10 Summary

Interfaces define the relationships between independent components.

Protecting those relationships allows implementations to evolve without creating unnecessary disruption.

WebInvestigator therefore treats interfaces as long-term promises rather than temporary conveniences.

Stable contracts make sustainable evolution possible.

---

## Next Chapter

As software grows, maintaining architecture becomes less about writing new code and more about improving existing code.

The next chapter explores an activity often misunderstood by developers:

**Refactoring as a First-Class Citizen.**