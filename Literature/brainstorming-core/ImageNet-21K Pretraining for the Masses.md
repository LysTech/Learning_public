---
type: paper
uid: "2025-12-15-this-leads-me-to-wonder-whether-masked-modelling-of-sequences-is-a-better-way-to-leverage-all-our-da-2"
title: "ImageNet-21K Pretraining for the Masses"
authors: ["Ridnik, Tal", "Ben-Baruch, Emanuel", "Noy, Asaf", "Zelnik-Manor, Lihi"]
year: 2021
venue: "arXiv"
doi: "10.48550/arXiv.2104.10972"
url: "https://arxiv.org/pdf/2104.10972:"
status: to-read
rating: 
shared_by: "Thomas R."
channel: "brainstorming-core"
tags: ["ai", "arxiv", "brainstorming-core", "llm-enriched", "paper"]
source: "arxiv"
added: 2026-04-09
---
## Summary
This paper introduces semantic softmax, a novel pretraining scheme that exploits the hierarchical structure of ImageNet-21K by training multiple classification heads at different levels of semantic abstraction (up to 11 levels). The method is combined with knowledge distillation to improve downstream task performance without requiring direct access to ImageNet-21K.

## Key points
- Semantic softmax leverages hierarchical structure of ImageNet-21K with multi-level classification heads (up to 11 abstraction levels)
- Knowledge distillation from a semantic softmax model to a second semantic softmax model improves robustness to label noise and generalizes learned semantic relationships
- Consistent improvements across 6 out of 7 downstream tasks compared to standard ImageNet pretraining
- Approach makes large-scale hierarchical pretraining accessible without direct access to ImageNet-21K data

## Notes
https://arxiv.org/pdf/2101.12037: this leads me to wonder whether masked modelling of sequences is a better way to leverage all our data than auto-encoder. needs to be checked e...

## Links
- Source: https://arxiv.org/pdf/2104.10972:
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1450038342510051361

## My notes
-
