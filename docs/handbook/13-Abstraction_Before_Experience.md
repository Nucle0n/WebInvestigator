# Chapter 13
# Abstraction Before Experience

---

> *"Generality is expensive. Pay for it only when you know you need it."*

---

# 13.1 Introduction

One of the most seductive ideas in software engineering is generalization.

Developers naturally enjoy building flexible systems.

A function becomes a library.

A module becomes a framework.

A class becomes a generic abstraction capable of handling every imaginable situation.

At first glance, this seems like good engineering.

After all, if software is more generic, surely it will be more reusable.

Experience suggests otherwise.

Many software projects become unnecessarily complicated not because they lack abstractions, but because they introduce them too early.

WebInvestigator deliberately follows a different philosophy.

Abstractions should emerge from experience.

Not imagination.

---

# 13.2 The Temptation of the Perfect Framework

Imagine writing the first image analyzer.

Its responsibility is modest.

```
Image

↓

Extract information

↓

ImageInfo
```

Nothing more is required.

However, a developer may immediately begin asking questions.

"What if tomorrow we need audio analyzers?"

"What if we later support databases?"

"What if plugins need custom pipelines?"

"What if analyzers become distributed?"

These are reasonable questions.

They are also dangerous.

Designing software around hypothetical requirements frequently creates complexity that never becomes useful.

WebInvestigator intentionally resists this temptation.

---

# 13.3 The Cost of Imaginary Requirements

Software is full of "what if."

What if another format appears?

What if we support cloud execution?

What if artificial intelligence replaces this module?

What if users request live monitoring?

Every "what if" introduces another layer of abstraction.

Eventually, the project begins solving problems that do not actually exist.

This phenomenon is often called **overengineering**.

Overengineering rarely feels excessive while it is happening.

Each abstraction appears individually justified.

The accumulated complexity only becomes visible months later.

---

## Common Pitfall

A surprising number of unnecessary abstractions originate from future requirements that never arrive.

Designing for the future is important.

Designing for every possible future is not.

---

# 13.4 Experience Before Abstraction

One of the recurring principles of WebInvestigator is remarkably simple.

> **Implement the concrete solution first.**

Observe it.

Use it.

Maintain it.

Only afterwards decide whether a reusable abstraction actually exists.

This sequence is important.

Abstractions extracted from working software tend to represent genuine patterns.

Abstractions invented beforehand often represent guesses.

Software architecture should prefer observations over guesses.

---

# 13.5 The Rule of Three

A useful guideline appears repeatedly in software engineering.

Do not generalize after one implementation.

Do not necessarily generalize after two.

When the same pattern naturally appears a third time, abstraction becomes worth considering.

This idea is commonly known as the **Rule of Three**.

Although not a strict law, it encourages developers to delay abstraction until recurring structures become visible.

WebInvestigator informally follows this philosophy.

Patterns should reveal themselves.

Not be predicted.

---

## Historical Note

Several utility functions originally existed only once.

Early in the project, there was no attempt to build generic helper libraries.

Only after similar code appeared repeatedly were common behaviors extracted into reusable components.

This approach significantly reduced speculative abstractions.

---

# 13.6 Generalizing the Right Thing

There is another subtle danger.

Sometimes developers correctly identify duplication but generalize the wrong concept.

Consider two analyzers.

Both compute hashes.

The immediate temptation might be creating a generic analyzer.

```
GenericAnalyzer

↓

Image Analyzer

↓

Duplicate Analyzer
```

The problem is that hashing is not the analyzer's responsibility.

Hashing is a capability.

The reusable component should therefore be the hashing algorithm itself.

The analyzers remain independent.

The shared capability becomes reusable.

Good abstractions emerge at the correct level.

---

# 13.7 Flexibility Versus Simplicity

Flexibility has a cost.

Every configuration option increases complexity.

Every extension point introduces additional decisions.

Every generic interface expands the mental model developers must understand.

Good architecture constantly balances two opposing forces.

```
Too Little Abstraction

↓

Duplication

↓

Maintainability Problems
```

versus

```
Too Much Abstraction

↓

Complexity

↓

Maintainability Problems
```

The optimal solution usually lies somewhere between these extremes.

---

# 13.8 YAGNI

One of the best-known principles in agile software development is commonly summarized as:

> **You Aren't Gonna Need It.**

Usually abbreviated as **YAGNI**.

Its message is frequently misunderstood.

YAGNI does not discourage planning.

It discourages implementing features before they become necessary.

WebInvestigator adopts a similar mindset.

Architectural flexibility is desirable.

Architectural speculation is not.

The framework should remain prepared for growth without implementing every imaginable future today.

---

# 13.9 Evolution Instead of Prediction

Perhaps the most important lesson learned during the development of WebInvestigator is that architecture evolves.

The first scanner was not perfect.

The first models were not perfect.

The first analyzers were not perfect.

None of them needed to be.

They simply needed to be good enough to reveal the next architectural decision.

This incremental evolution produced a stronger architecture than attempting to design every component perfectly from the beginning.

Experience became the architect.

---

## Architect's Note

Several times during development it became tempting to introduce plugin systems long before multiple plugins existed.

Likewise, there was an urge to create generic analyzer hierarchies after writing only one or two analyzers.

These ideas were deliberately postponed.

The framework first needed to demonstrate recurring patterns.

Only then would abstraction become justified.

In retrospect, postponing these decisions kept the codebase considerably simpler.

---

# 13.10 Simplicity Ages Well

Complexity accumulates.

Simplicity survives.

Every unnecessary abstraction added today becomes another concept future contributors must learn.

Every unnecessary interface becomes another file to maintain.

Every unnecessary inheritance hierarchy becomes another obstacle during refactoring.

The opposite is also true.

Simple architectures remain understandable.

Understandable software tends to survive.

This observation explains why WebInvestigator repeatedly favors concrete implementations until experience demonstrates a clear benefit from abstraction.

---

# 13.11 Summary

Generalization is a powerful architectural tool.

Like every powerful tool, it should be used deliberately.

WebInvestigator does not reject abstraction.

It rejects premature abstraction.

Reusable patterns should emerge naturally from repeated experience.

When they do, they often become obvious.

Until then, the simplest working solution is usually the best investment.

---

## Next Chapter

Simple architectures must also remain resilient.

The true quality of a framework is revealed not only by how it handles success, but by how it responds to failure.

The next chapter explores Error Handling and Failure Philosophy, explaining why WebInvestigator treats failures as part of the investigation rather than as reasons to abandon it.

**[Error Handling and Failure Philosophy](./14-Error_Handling_and_Failure_Philosophy.md)**