---
type: paper
title: "Scaling laws for language encoding models in fMRI"
authors: ["Richard Antonello", "Aditya Vaidya", "Alexander G. Huth"]
year: 2023
venue: "arXiv"
doi: "10.48550/arXiv.2305.11863"
url: "https://arxiv.org/pdf/2305.11863"
status: to-read
rating:
shared_by: "AnthonyK"
channel: "perceived-speech"
tags: ["arxiv", "llm-enriched", "paper", "perceived-speech"]
source: "arxiv"
added: 2026-06-12
---
## Summary
Representations from transformer-based unidirectional language models are known to be effective at predicting brain responses to natural language. However, most studies comparing language models to brains have used GPT-2 or similarly sized language models. Here we tested whether larger open-source models such as those from the OPT and LLaMA families are better at predicting brain responses recorded using fMRI. Mirroring scaling results from other contexts, we found that brain prediction performance scales logarithmically with model size from 125M to 30B parameter models, with ~15% increased encoding performance as measured by correlation with a held-out test set across 3 subjects. Similar logarithmic behavior was observed when scaling the size of the fMRI training set. We also characterized scaling for acoustic encoding models that use HuBERT, WavLM, and Whisper, and we found comparable improvements with model size. A noise ceiling analysis of these large, high-performance encoding models showed that performance is nearing the theoretical maximum for brain areas such as the precuneus and higher auditory cortex. These results suggest that increasing scale in both models and data will yield incredibly effective models of language processing in the brain, enabling better scientific understanding as well as applications such as decoding.

## Key points
- Brain prediction performance scales logarithmically with language model size, showing ~15% improvement from 125M to 30B parameters
- Scaling benefits observed across multiple model families (OPT, LLaMA) and modalities (language and acoustic models using HuBERT, WavLM, Whisper)
- Logarithmic scaling also observed when increasing fMRI training set size
- Noise ceiling analysis reveals performance nearing theoretical maximum in precuneus and higher auditory cortex
- Results suggest continued scaling in models and data will improve brain encoding and enable applications like neural decoding

## Links
- Source: https://arxiv.org/pdf/2305.11863
- Discord: https://discord.com/channels/1400359609323229267/1400365455746662400/1496097012045578310

## My notes
- 
