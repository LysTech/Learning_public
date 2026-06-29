---
type: paper
uid: "2026-05-20-1330246797465223211-reward-model-rlhf-context-benchmark"
title: "RewardBench: Evaluating Reward Models for Language Modeling"
authors: ["Nathan Lambert", "Valentina Pyatkin", "Jacob Morrison", "LJ Miranda", "Bill Yuchen Lin", "Khyathi Chandu", "Nouha Dziri", "Sachin Kumar", "Tom Zick", "Yejin Choi", "Noah A. Smith", "Hannaneh Hajishirzi"]
year: 2024
venue: "arXiv"
doi: "10.48550/arXiv.2403.13787"
url: "https://arxiv.org/pdf/2403.13787"
status: to-read
rating: 
shared_by: "Thomas R."
channel: "brainstorming"
tags: ["arxiv", "brainstorming", "llm-enriched", "paper"]
source: "arxiv"
added: 2026-06-12
---
## Summary
Reward models (RMs) are at the crux of successfully using RLHF to align pretrained models to human preferences, yet there has been relatively little study that focuses on evaluation of those models. Evaluating reward models presents an opportunity to understand the opaque technologies used for alignment of language models and which values are embedded in them. Resources for reward model training and understanding are sparse in the nascent open-source community around them. To enhance scientific understanding of reward models, we present RewardBench, a benchmark dataset and code-base for evaluation. The RewardBench dataset is a collection of prompt-chosen-rejected trios spanning chat, reasoning, and safety, to benchmark how reward models perform on challenging, structured and out-of-distribution queries. We create specific comparison datasets for RMs that have subtle, but verifiable reasons (e.g. bugs, incorrect facts) why one answer should be preferred to another. On the RewardBench leaderboard, we evaluate reward models trained with a variety of methods, such as the direct MLE training of classifiers and the implicit reward modeling of Direct Preference Optimization (DPO). We present many findings on propensity for refusals, reasoning limitations, and instruction following shortcomings of various reward models towards a better understanding of the RLHF process.

## Key points
- First comprehensive benchmark for evaluating reward models across diverse domains (chat, reasoning, safety)
- Includes structured comparison datasets with subtle differences and verifiable preference reasons (bugs, incorrect facts)
- Evaluates multiple reward modeling approaches including direct MLE training and Direct Preference Optimization (DPO)
- Identifies key shortcomings: propensity for refusals, reasoning limitations, and instruction following deficiencies
- Provides open-source codebase and leaderboard to enhance scientific understanding of RLHF alignment

## Notes
<@1330246797465223211> reward model (RLHF context) benchmark https://arxiv.org/pdf/2403.13787

## Links
- Source: https://arxiv.org/pdf/2403.13787
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1506574182052397066

## My notes
-
