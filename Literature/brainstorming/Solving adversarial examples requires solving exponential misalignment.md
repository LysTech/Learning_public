---
type: paper
uid: "2026-05-07-i-wouldnt-be-surprised-if-brain-tuning-image-models-made-them-more-robust-to-this-sort-of-thing-ad"
title: "Solving adversarial examples requires solving exponential misalignment"
authors: ["Alessandro Salvatore", "Stanislav Fort", "Surya Ganguli"]
year: 2026
venue: "arXiv"
doi: "10.48550/arXiv.2603.03507"
url: "https://arxiv.org/abs/2603.03507"
status: to-read
rating: 
shared_by: "Thomas R."
channel: "brainstorming"
tags: ["ai", "arxiv", "brainstorming", "llm-enriched", "paper"]
source: "arxiv"
added: 2026-06-12
---
## Summary
Adversarial attacks - input perturbations imperceptible to humans that fool neural networks - remain both a persistent failure mode in machine learning, and a phenomenon with mysterious origins. To shed light, we define and analyze a network's perceptual manifold (PM) for a class concept as the space of all inputs confidently assigned to that class by the network. We find, strikingly, that the dimensionalities of neural network PMs are orders of magnitude higher than those of natural human concepts. Since volume typically grows exponentially with dimension, this suggests exponential misalignment between machines and humans, with exponentially many inputs confidently assigned to concepts by machines but not humans. Furthermore, this provides a natural geometric hypothesis for the origin of adversarial examples: because a network's PM fills such a large region of input space, any input will be very close to any class concept's PM. Our hypothesis thus suggests that adversarial robustness cannot be attained without dimensional alignment of machine and human PMs, and therefore makes strong predictions: both robust accuracy and distance to any PM should be negatively correlated with the PM dimension. We confirmed these predictions across 18 different networks of varying robust accuracy. Crucially, we find even the most robust networks are still exponentially misaligned, and only the few PMs whose dimensionality approaches that of human concepts exhibit alignment to human perception. Our results connect the fields of alignment and adversarial examples, and suggest the curse of high dimensionality of machine PMs is a major impediment to adversarial robustness.

## Key points
- Neural network perceptual manifolds are exponentially higher-dimensional than natural human concepts, creating exponential misalignment
- Adversarial examples arise naturally from this geometric property: inputs are necessarily close to multiple class boundaries in high-dimensional space
- Robust accuracy and distance to perceptual manifolds are negatively correlated with PM dimensionality across diverse networks
- Even state-of-the-art robust models exhibit exponential misalignment; only models with human-aligned PM dimensionality show robust perception
- Connecting adversarial robustness to alignment suggests dimensional alignment is necessary for true adversarial robustness

## Notes
I wouldn't be surprised if brain tuning image models made them more robust to this sort of thing (adversarial examples): https://arxiv.org/abs/2603.03507 testable prediction: br...

## Links
- Source: https://arxiv.org/abs/2603.03507
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1501840898651328582

## My notes
-
