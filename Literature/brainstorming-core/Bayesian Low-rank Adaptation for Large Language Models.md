---
type: paper
uid: "2026-02-19-httpsarxivorgpdf230813111"
title: "Bayesian Low-rank Adaptation for Large Language Models"
authors: ["Adam X. Yang", "Maxime Robeyns", "Xi Wang", "Laurence Aitchison"]
year: 2023
venue: "arXiv"
doi: "10.48550/arXiv.2308.13111"
url: "https://arxiv.org/pdf/2308.13111"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "brainstorming-core"
tags: ["arxiv", "brainstorming-core", "llm-enriched", "paper"]
source: "arxiv"
added: 2026-04-09
---
## Summary
Low-rank adaptation (LoRA) has emerged as a new paradigm for cost-efficient fine-tuning of large language models (LLMs). However, fine-tuned LLMs often become overconfident especially when fine-tuned on small datasets. Bayesian methods, with their inherent ability to estimate uncertainty, serve as potent tools to mitigate overconfidence and enhance calibration. In this work, we introduce Laplace-LoRA, which applies a Bayesian approach to the LoRA parameters. Specifically, Laplace-LoRA applies a Laplace approximation to the posterior over the LoRA parameters, considerably improving the calibration of fine-tuned LLMs.

## Key points
- Combines Bayesian inference with LoRA for efficient fine-tuning of LLMs
- Uses Laplace approximation to estimate uncertainty over LoRA parameters
- Addresses overconfidence in fine-tuned models, especially on small datasets
- Significantly improves calibration of adapted language models
- Maintains computational efficiency of LoRA while adding uncertainty quantification

## Links
- Source: https://arxiv.org/pdf/2308.13111
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1473930205969125396

## My notes
-
