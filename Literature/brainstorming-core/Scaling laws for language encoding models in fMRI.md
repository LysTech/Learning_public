---
type: paper
uid: "2025-12-24-httpspmcncbinlmnihgovarticlespmc11258918"
title: "Scaling laws for language encoding models in fMRI"
authors: ["Antonello RJ", "Vaidya AR", "Huth AG"]
year: 2023
venue: "Adv Neural Inf Process Syst"
doi: ""
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC11258918/"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "brainstorming-core"
tags: ["brainstorming-core", "llm-enriched", "paper", "url"]
source: "url"
added: 2026-04-09
---
## Summary
Representations from transformer-based unidirectional language models are known to be effective at predicting brain responses to natural language. However, most studies comparing language models to brains have used GPT-2 or similarly sized language models. Here we tested whether larger open-source models such as those from the OPT and LLaMA families are better at predicting brain responses recorded using fMRI. Mirroring scaling results from other contexts, we found that brain prediction performance scales logarithmically with model size from 125M to 30B parameter models, with ~15% increased encoding performance as measured by correlation with a held-out test set across 3 subjects. Similar logarithmic behavior was observed when scaling the size of the fMRI training set. We also characterized scaling for acoustic encoding models that use HuBERT, WavLM, and Whisper, and we found comparable improvements with model size. A noise ceiling analysis of these large, high-performance encoding models showed that performance is nearing the theoretical maximum for brain areas such as the precuneus and higher auditory cortex. These results suggest that increasing scale in both models and data will yield incredibly effective models of language processing in the brain, enabling better scientific understanding as well as applications such as decoding.

## Key points
- Brain prediction performance scales logarithmically with language model size from 125M to 30B parameters, mirroring scaling laws observed in other domains
- Approximately 15% increased encoding performance measured by correlation with held-out test sets across subjects
- Scaling benefits apply across multiple model families (OPT, LLaMA) and modalities (language and acoustic models)
- Performance in some brain areas (precuneus, higher auditory cortex) approaches theoretical noise ceiling, suggesting fundamental limits to further improvement
- Results support continued scaling of both models and training data for improved neuroscientific understanding and brain decoding applications

## Links
- Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC11258918/
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1453359124955004949

## My notes
-
