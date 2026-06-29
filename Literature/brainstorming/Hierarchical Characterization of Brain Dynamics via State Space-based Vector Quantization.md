---
type: paper
uid: "2026-06-07-we-should-look-into-tokenization-of-brain-data-especially-in-the-context-of-next-brain-state-pred"
title: "Hierarchical Characterization of Brain Dynamics via State Space-based Vector Quantization"
authors: ["Yanwu Yang", "Thomas Wolfers"]
year: 2025
venue: "arXiv"
doi: "10.48550/arXiv.2506.22952"
url: "https://arxiv.org/pdf/2506.22952"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "brainstorming"
tags: ["ai", "arxiv", "brainstorming", "llm-enriched", "paper"]
source: "arxiv"
added: 2026-06-12
---
## Summary
Understanding brain dynamics through functional Magnetic Resonance Imaging (fMRI) remains a fundamental challenge in neuroscience, particularly in capturing how the brain transitions between various functional states. Recently, metastability, which refers to temporarily stable brain states, has offered a promising paradigm to quantify complex brain signals into interpretable, discretized representations. In particular, compared to cluster-based machine learning approaches, tokenization approaches leveraging vector quantization have shown promise in representation learning with powerful reconstruction and predictive capabilities. However, most existing methods ignore brain transition dependencies and lack a quantification of brain dynamics into representative and stable embeddings. In this study, we propose a Hierarchical State space-based Tokenization network, termed HST, which quantizes brain states and transitions in a hierarchical structure based on a state space-based model. We introduce a refined clustered Vector-Quantization Variational AutoEncoder (VQ-VAE) that incorporates quantization error feedback and clustering to improve quantization performance while facilitating metastability with representative and stable token representations. We validate our HST on two public fMRI datasets, demonstrating its effectiveness in quantifying the hierarchical dynamics of the brain and its potential in disease diagnosis and reconstruction performance. Our method offers a promising framework for the characterization of brain dynamics, facilitating the analysis of metastability.

## Key points
- Introduces hierarchical tokenization of fMRI brain states and transitions using state space-based vector quantization
- Proposes refined VQ-VAE with quantization error feedback and clustering to improve stability and representativeness of learned tokens
- Demonstrates effectiveness for quantifying brain metastability—temporarily stable functional states—across two public fMRI datasets
- Extends tokenization paradigm (common in EEG) to fMRI with potential applications in disease diagnosis and signal reconstruction
- Addresses gap between token-based representation learning and brain dynamics modeling by incorporating transition dependencies

## Notes
we should look into tokenization of brain data, especially in the context of next brain (state) prediction.   seems like a common thing ppl do with EEG but haven’t seen it with ...

## Links
- Source: https://arxiv.org/pdf/2506.22952
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1513081433458085968

## My notes
-
