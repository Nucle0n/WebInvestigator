# Preface

> *"Good software is not only written.
> It is also understood."*

---

## Why This Handbook Exists

Every software project tells a story.

Some begin as commercial products.
Some emerge from academic research.
Others are born from a personal need.

WebInvestigator belongs to the latter.

The project did not begin with the ambition of creating a framework, nor with the intention of becoming an open-source project. It started with a single objective: assisting the investigation of a suspicious website through automation.

At first, only a few Python scripts were required.

Each script solved one isolated problem encountered during the investigation.

There was no architecture.

There was no roadmap.

There was no intention of building a reusable software project.

Only after several iterations did an important observation emerge.

Most of the code being written had little to do with the investigation itself.

Instead, it solved generic problems that could be reused in countless future investigations.

Directory discovery.

File inventory.

Image analysis.

Metadata extraction.

Filename inspection.

Duplicate detection.

Every new utility quickly proved useful beyond the original investigation.

At that moment, the project fundamentally changed.

The objective was no longer to automate one investigation.

The objective became building the tool that would automate every future investigation.

That change of perspective marks the birth of WebInvestigator.

---

# Why Documentation Matters

Writing software is only part of software engineering.

Understanding *why* software was written in a particular way is equally important.

Source code is excellent at describing implementation.

It rarely explains intention.

Years after a project begins, contributors usually understand what the code does.

What disappears is the reasoning that produced it.

Questions such as:

- Why was this abstraction introduced?
- Why are these modules separated?
- Why is this responsibility located here instead of elsewhere?
- Why wasn't another design chosen?

cannot always be answered by reading code alone.

Without documentation, every generation of contributors eventually repeats the same discussions.

The same architectural mistakes.

The same experiments.

The same dead ends.

This handbook attempts to preserve that knowledge.

---

# Purpose of This Document

This handbook is not an API reference.

It is not a Python tutorial.

It is not a user manual.

Its purpose is to explain the architecture of WebInvestigator from the inside.

More specifically, this document aims to answer four fundamental questions.

1. **Why does the project exist?**

2. **Why is the architecture designed this way?**

3. **How should new functionality be integrated?**

4. **Which architectural decisions have already been made?**

Every chapter contributes to answering one or more of these questions.

---

# Intended Audience

This handbook has been written for several kinds of readers.

## Future Contributors

Developers joining the project should understand not only the codebase but also the philosophy that guides its evolution.

Architecture is easier to preserve than to reinvent.

Understanding previous decisions prevents unnecessary redesigns.

---

## Future Maintainers

Every software project eventually reaches a point where its original authors no longer remember every design decision.

This handbook is therefore also written for future versions of ourselves.

Months or years from now, this document should answer questions that memory alone cannot.

---

## Curious Readers

Some readers may simply be interested in software architecture.

Although WebInvestigator is an OSINT framework, many of its design principles are independent of the application domain.

Topics such as modularity, responsibility separation, incremental development and maintainability are applicable to software projects in general.

---

# Philosophy of This Handbook

This document deliberately focuses on architecture rather than implementation.

Individual functions may evolve.

Classes may be renamed.

Modules may be reorganized.

Architectural principles, however, should remain significantly more stable.

For this reason, most chapters explain decisions instead of listing source code.

Whenever implementation examples are provided, they illustrate concepts rather than document APIs.

This distinction is intentional.

The architecture should remain understandable even after the code changes.

---

# Living Documentation

Unlike traditional software books, this handbook is intended to evolve together with the project.

Every significant architectural decision should eventually appear here.

Whenever the framework grows, this handbook should grow with it.

Documentation should never become an afterthought.

Instead, it should be considered part of the project itself.

A feature is only truly complete when both its implementation and its architectural documentation have been written.

---

# Scope

WebInvestigator is an extensible framework dedicated to assisting digital investigations through reusable analysis modules.

Its scope includes:

- offline website analysis;
- file inventory;
- metadata extraction;
- image analysis;
- content discovery;
- extensible analyzers;
- structured reporting.

The framework deliberately avoids becoming an offensive security platform.

It is not intended to exploit systems.

It is not designed to attack infrastructure.

Its objective is understanding digital artefacts rather than compromising them.

This distinction influences every architectural decision presented throughout this handbook.

---

# A Guiding Principle

If one sentence had to summarize the entire philosophy of WebInvestigator, it would be the following:

> **WebInvestigator was not created to solve a single investigation.**
>
> **It was created to make every future investigation easier than the previous one.**

Everything described in this handbook ultimately derives from that single principle.

---

*Continue with Chapter 2 — "Origin of the Project".*