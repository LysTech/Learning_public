---
type: paper
uid: "2026-06-19-httpsarxivorgpdf230108243"
title: "Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture"
authors: ["Mahmoud Assran", "Quentin Duval", "Ishan Misra", "Piotr Bojanowski", "Pascal Vincent", "Michael Rabbat", "Yann LeCun", "Nicolas Ballas"]
year: 2023
venue: "arXiv"
doi: "10.48550/arXiv.2301.08243"
url: "https://arxiv.org/pdf/2301.08243"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "brainstorming"
tags: ["arxiv", "brainstorming", "paper"]
source: "arxiv"
added: 2026-06-22
---
## Summary
This paper demonstrates an approach for learning highly semantic image representations without relying on hand-crafted data-augmentations. We introduce the Image-based Joint-Embedding Predictive Architecture (I-JEPA), a non-generative approach for self-supervised learning from images. The idea behind I-JEPA is simple: from a single context block, predict the representations of various target blocks in the same image. A core design choice to guide I-JEPA towards producing semantic representations is the masking strategy; specifically, it is crucial to (a) sample target blocks with sufficiently large scale (semantic), and to (b) use a sufficiently informative (spatially distributed) context block. Empirically, when combined with Vision Transformers, we find I-JEPA to be highly scalable. For instance, we train a ViT-Huge/14 on ImageNet using 16 A100 GPUs in under 72 hours to achieve strong downstream performance across a wide range of tasks, from linear classification to object counting and depth prediction.

## Links
- Source: https://arxiv.org/pdf/2301.08243
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1517550035582193755

## My notes
-
