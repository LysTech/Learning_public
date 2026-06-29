---
type: paper
uid: "2025-08-07-the-meta-megeeg-word-decoding-papers-seem-to-use-this-clip-loss-ie-a-contrastive-loss-function"
title: "Decoding individual words from non-invasive brain recordings across 723 participants"
authors: ["d'Ascoli, Stéphane", "Bel, Corentin", "Rapin, Jérémy", "Banville, Hubert", "Benchetrit, Yohann", "Pallier, Christophe", "King, Jean-Rémi"]
year: 2024
venue: "arXiv"
doi: "10.48550/arXiv.2412.17829"
url: "https://arxiv.org/pdf/2412.17829v1"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "brainstorming-core"
tags: ["ai", "arxiv", "brainstorming-core", "llm-enriched", "paper"]
source: "arxiv"
added: 2026-04-09
---
## Summary
This work demonstrates word decoding from non-invasive brain recordings (MEG/EEG) across a large cohort of 723 participants using contrastive learning approaches. The study employs spatial attention mechanisms to remap channels to 2D space and applies artifact removal preprocessing, achieving robust decoding performance without explicit source localization.

## Key points
- Large-scale word decoding from MEG/EEG across 723 participants, establishing benchmark performance
- Uses contrastive loss (CLIP-style) for learning word representations from brain activity
- Spatial attention layer remaps sensor channels to 2D space as an alternative to explicit source localization
- Extensive preprocessing and artifact removal critical to performance
- Demonstrates that source localization/reconstruction techniques could potentially further improve decoding accuracy

## Notes
The Meta MEG/EEG word decoding papers seem to use this CLIP loss, ie a contrastive loss function: https://arxiv.org/pdf/2412.17829v1 https://www.nature.com/articles/s42256-023-0...

## Links
- Source: https://arxiv.org/pdf/2412.17829v1
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1402912654363721778

## My notes
-
