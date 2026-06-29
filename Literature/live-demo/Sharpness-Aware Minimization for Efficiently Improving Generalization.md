---
type: paper
uid: "2026-02-03-im-currently-investigating-this"
title: "Sharpness-Aware Minimization for Efficiently Improving Generalization"
authors: ["Foret, Pierre", "Kleiner, Ariel", "Mobahi, Hossein", "Neyshabur, Behnam"]
year: 2020
venue: "arXiv"
doi: "10.48550/arXiv.2010.01412"
url: "https://arxiv.org/abs/2010.01412"
status: to-read
rating: 
shared_by: "Thomas R."
channel: "live-demo"
tags: ["ai", "arxiv", "live-demo", "llm-enriched", "paper"]
source: "arxiv"
added: 2026-04-09
---
## Summary
Sharpness-Aware Minimization (SAM) is an optimization algorithm that improves generalization by seeking flat minima in the loss landscape, rather than sharp ones. By penalizing sharp minima, SAM achieves better validation performance and generalization compared to standard optimizers like AdamW.

## Key points
- Introduces Sharpness-Aware Minimization (SAM), an optimizer that seeks flat minima to improve generalization
- Addresses the problem that standard optimizers like AdamW converge to sharp minima which generalize poorly
- Particularly beneficial for noisy data where the loss landscape is irregular
- Demonstrates substantial improvements in validation loss and generalization across multiple datasets and architectures
- Simple and practical approach that can be integrated with existing optimizers like SGD and Adam

## Notes
I'm currently investigating this: https://arxiv.org/abs/2010.01412  my reasoning: we have noisy data, so the loss landscape is noisy -> so we should incentivise the optimisation...

## Links
- Source: https://arxiv.org/abs/2010.01412
- Discord: https://discord.com/channels/1400359609323229267/1400365362025070743/1468198914619478019

## My notes
-
