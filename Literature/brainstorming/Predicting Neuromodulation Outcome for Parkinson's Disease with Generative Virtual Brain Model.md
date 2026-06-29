---
type: paper
uid: "2026-06-06-httpsarxivorgpdf260329176"
title: "Predicting Neuromodulation Outcome for Parkinson's Disease with Generative Virtual Brain Model"
authors: ["Siyuan Du", "Siyi Li", "Shuwei Bai", "Ang Li", "Haolin Li", "Mingqing Xiao", "Yang Pan", "Dongsheng Li", "Weidi Xie", "Yanfeng Wang", "Ya Zhang", "Chencheng Zhang", "Jiangchao Yao"]
year: 2026
venue: "arXiv"
doi: "10.48550/arXiv.2603.29176"
url: "https://arxiv.org/pdf/2603.29176"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "brainstorming"
tags: ["arxiv", "brainstorming", "llm-enriched", "paper"]
source: "arxiv"
added: 2026-06-12
---
## Summary
Parkinson's disease (PD) affects over ten million people worldwide. Although temporal interference (TI) and deep brain stimulation (DBS) are promising therapies, inter-individual variability limits empirical treatment selection, increasing non-negligible surgical risk and cost. Previous explorations either resort to limited statistical biomarkers that are insufficient to characterize variability, or employ AI-driven methods which is prone to overfitting and opacity. We bridge this gap with a pretraining-finetuning framework to predict outcomes directly from resting-state fMRI. Critically, a generative virtual brain foundation model, pretrained on a collective dataset (2707 subjects, 5621 sessions) to capture universal disorder patterns, was finetuned on PD cohorts receiving TI (n=51) or DBS (n=55) to yield individualized virtual brains with high fidelity to empirical functional connectivity (r=0.935). By constructing counterfactual estimations between pathological and healthy neural states within these personalized models, we predicted clinical responses (TI: AUPR=0.853; DBS: AUPR=0.915), substantially outperforming baselines. External and prospective validations (n=14, n=11) highlight the feasibility of clinical translation. Moreover, our framework provides state-dependent regional patterns linked to response, offering hypothesis-generating mechanistic insights.

## Key points
- Generative virtual brain foundation model pretrained on 2707 subjects captures universal neural disorder patterns
- Personalized virtual brains achieve high fidelity to empirical functional connectivity (r=0.935) through finetuning on patient cohorts
- Counterfactual analysis between pathological and healthy states enables prediction of treatment response without requiring extensive labeled data
- Substantially outperforms baselines with AUPR of 0.853 (TI) and 0.915 (DBS) in outcome prediction
- External and prospective validations demonstrate clinical translation feasibility with mechanistic insights into state-dependent regional patterns

## Links
- Source: https://arxiv.org/pdf/2603.29176
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1512872080108949717

## My notes
-
