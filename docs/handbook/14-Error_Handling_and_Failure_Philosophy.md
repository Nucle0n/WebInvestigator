# Chapter 14
# Error Handling and Failure Philosophy

---

> *"An investigation should not collapse because one piece of evidence is missing."*

---

# 14.1 Introduction

Every non-trivial software system eventually encounters failure.

A file cannot be opened.

An image is corrupted.

Metadata is malformed.

A checksum cannot be computed.

An unexpected exception occurs.

These situations are inevitable.

The real architectural question is therefore not:

> "Will failures happen?"

but rather:

> "How should the framework behave when they do?"

For WebInvestigator, the answer is guided by the nature of the problem it solves.

It is an investigation framework.

Investigations are rarely perfect.

Evidence may be incomplete, damaged or contradictory.

The software should reflect that reality.

---

# 14.2 Failure Is Information

Many applications treat an error as the end of execution.

An exception is raised.

The process terminates.

The user receives an error message.

For certain categories of software, this behavior is entirely appropriate.

A banking transaction should not continue after a critical integrity failure.

An operating system kernel cannot safely ignore memory corruption.

An investigation, however, is different.

If one image cannot be analyzed, the remaining 5,000 images are still valuable.

The inability to process one file is itself information.

Failure should therefore become part of the investigation rather than automatically ending it.

---

# 14.3 The Cost of Stopping Too Early

Imagine a directory containing 12,000 files.

One image is corrupted.

If the framework aborts immediately, the investigator loses every remaining result.

The architecture has allowed one defective file to invalidate an entire investigation.

That is rarely a desirable trade-off.

Instead, WebInvestigator favors resilience.

Failures should remain local whenever possible.

---

## Design Rationale

Stopping the whole investigation should be reserved for situations where continuing would produce misleading or fundamentally unreliable results.

Individual file failures rarely meet that threshold.

---

# 14.4 Localizing Failure

One recurring objective throughout the architecture is reducing the impact of change.

The same philosophy applies to failures.

Errors should remain as close as possible to their origin.

If the Image Analyzer encounters an unreadable file, the failure belongs to that file.

It should not automatically become the failure of every analyzer.

Nor should it become the failure of the entire investigation.

Local failures preserve global progress.

---

# 14.5 Exceptions Are Not the Enemy

Programming discussions sometimes portray exceptions as something to avoid.

This is a misunderstanding.

Exceptions communicate abnormal situations.

They are useful.

The important architectural decision concerns where they are handled.

Deep inside the framework, exceptions often carry valuable technical information.

At higher architectural levels, that information must usually be transformed into structured investigation results.

The exception itself is transient.

The investigation remains.

---

# 14.6 Reporting Without Panic

An investigator deserves to know what happened.

Silently ignoring failures is almost as dangerous as stopping immediately.

Suppose an analyzer skips twenty files.

If those failures disappear without trace, confidence in the investigation decreases.

Instead, failures should be reported explicitly.

The framework therefore distinguishes between:

- successful observations;

- unavailable observations;

- failed observations.

All three contribute to understanding the investigation.

---

## Architect's Note

During early experimentation it was tempting to surround large portions of the pipeline with broad `try/except` blocks.

Although this prevented crashes, it also hid useful diagnostic information.

The architecture gradually evolved toward handling failures closer to their source while preserving meaningful reporting for the investigator.

---

# 14.7 Recover Whenever Possible

A resilient investigation framework should continually ask:

> "Can I continue safely?"

If the answer is yes, execution should generally proceed.

This philosophy mirrors real investigations.

A damaged fingerprint does not invalidate witness testimony.

A corrupted image does not invalidate directory statistics.

Independent evidence remains valuable even when one source fails.

---

# 14.8 Error Handling Is Part of the Design

Error handling is often treated as an implementation detail.

In reality, it is an architectural decision.

It influences:

- user confidence;

- debugging;

- automation;

- testing;

- future extensibility.

Designing the happy path is only half of architecture.

Designing graceful failure is equally important.

---

# 14.9 Summary

WebInvestigator views failures as evidence rather than catastrophe.

Whenever possible, errors remain local, are reported clearly and allow the investigation to continue.

By treating resilience as an architectural principle instead of an afterthought, the framework remains useful even when the investigated data is imperfect.

---

## Next Chapter

A robust framework is defined not only by how it handles failures, but also by how it adapts to different environments.

That adaptability should come from configuration, not from modifying the source code.

The next chapter explores Configuration as Architecture, explaining why separating operational choices from implementation logic is essential to building software that evolves gracefully.

**[Configuration as Architecture](./15-Configuration_as_Architecture.md)**