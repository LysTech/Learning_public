---
type: paper
uid: "2026-02-01-this-is-very-cool"
title: "Improving neural network representations using human similarity judgments"
authors: ["Lukas Muttenthaler", "Lorenz Linhardt", "Jonas Dippel", "Robert A. Vandermeulen", "Katherine Hermann", "Andrew K. Lampinen", "Simon Kornblith"]
year: 2023
venue: "arXiv"
doi: "10.48550/arXiv.2306.04507"
url: "https://arxiv.org/pdf/2306.04507"
status: to-read
rating: 
shared_by: "Thomas R."
channel: "brainstorming-core"
tags: ["ai", "arxiv", "brainstorming-core", "llm-enriched", "paper"]
source: "arxiv"
added: 2026-04-09
---
## Summary
Deep neural networks have reached human-level performance on many computer vision tasks. However, the objectives used to train these networks enforce only that similar images are embedded at similar locations in the representation space, and do not directly constrain the global structure of the resulting space. Here, we explore the impact of supervising this global structure by linearly aligning it with human similarity judgments. We find that a naive approach leads to large changes in local representational structure that harm downstream performance. Thus, we propose a novel method that aligns the global structure of representations while preserving their local structure. This global-local transform considerably improves accuracy across a variety of few-shot learning and anomaly detection tasks. Our results indicate that human visual representations are globally organized in a way that facilitates learning from few examples, and incorporating this global structure into neural network representations improves performance on downstream tasks.

## Key points
- Neural networks optimize for local similarity but lack explicit constraints on global hierarchical organization present in human vision
- Proposes a global-local transform: a linear transformation that aligns global structure with human judgments while preserving task-relevant local structure
- Uses fMRI data from the THINGS dataset to ground human similarity judgments
- Demonstrates substantial improvements on few-shot learning and anomaly detection benchmarks
- Shows that human visual representations contain organizational principles (e.g., hierarchical categorization) that benefit downstream learning efficiency

## Notes
This is very cool: https://arxiv.org/pdf/2306.04507  CLIP optimises for eg tabby cat images to be close to each other, but not explicitly for tabby cats to be near other sorts o...

## Links
- Source: https://arxiv.org/pdf/2306.04507
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1467522662963220490

## My notes
-
