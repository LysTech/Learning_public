---
type: paper
uid: "2026-06-06-mixture-of-experts-decoder-afire"
title: "Improving Multimodal Brain Encoding Model with Dynamic Subject-awareness Routing"
authors: ["Xuanhua Yin", "Runkai Zhao", "Weidong Cai"]
year: 2025
venue: "arXiv"
doi: "10.48550/arXiv.2510.04670"
url: "https://arxiv.org/pdf/2510.04670"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "brainstorming"
tags: ["arxiv", "brainstorming", "llm-enriched", "paper"]
source: "arxiv"
added: 2026-06-12
---
## Summary
Naturalistic fMRI encoding must handle multimodal inputs, shifting fusion styles, and pronounced inter-subject variability. We introduce AFIRE (Agnostic Framework for Multimodal fMRI Response Encoding), an agnostic interface that standardizes time-aligned post-fusion tokens from varied encoders, and MIND, a plug-and-play Mixture-of-Experts decoder with a subject-aware dynamic gating. Trained end-to-end for whole-brain prediction, AFIRE decouples the decoder from upstream fusion, while MIND combines token-dependent Top-K sparse routing with a subject prior to personalize expert usage without sacrificing generality. Experiments across multiple multimodal backbones and subjects show consistent improvements over strong baselines, enhanced cross-subject generalization, and interpretable expert patterns that correlate with content type. The framework offers a simple attachment point for new encoders and datasets, enabling robust, plug-and-improve performance for naturalistic neuroimaging studies.

## Key points
- Introduces AFIRE, an agnostic framework that standardizes multimodal encoder outputs for flexible downstream processing
- Proposes MIND, a plug-and-play Mixture-of-Experts decoder with subject-aware dynamic gating using Top-K sparse routing
- Achieves consistent improvements over baselines across multiple multimodal backbones with enhanced cross-subject generalization
- Expert activation patterns correlate interpretably with content type, enabling analysis of subject-specific neural processing
- Framework design allows seamless integration with new encoders and neuroimaging datasets

## Notes
https://arxiv.org/pdf/2510.04670 - mixture of experts decoder, AFIRE

## Links
- Source: https://arxiv.org/pdf/2510.04670
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1512864813586321409

## My notes
-
