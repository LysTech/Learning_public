---
type: paper
uid: "2026-02-19-httpspapersnipsccpaperfilespaper2018hasha981f2b708044d6fb4a71a1463242520-abstracthtml"
title: "Evidential Deep Learning to Quantify Classification Uncertainty"
authors: ["Sensoy, Murat", "Kaplan, Lance", "Kandemir, Melih"]
year: 2018
venue: "Advances in Neural Information Processing Systems"
doi: "10.36227/techrxiv.174900814.43483543/v1"
url: "https://papers.nips.cc/paper_files/paper/2018/hash/a981f2b708044d6fb4a71a1463242520-Abstract.html"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "brainstorming-core"
tags: ["brainstorming-core", "llm-enriched", "paper", "resource", "url"]
source: "url"
added: 2026-04-09
---
## Summary
Deterministic neural nets have been shown to learn effective predictors on a wide range of machine learning problems. However, as the standard approach is to train the network to minimize a prediction loss, the resultant model remains ignorant to its prediction confidence. Orthogonally to Bayesian neural nets that indirectly infer prediction uncertainty through weight uncertainties, we propose explicit modeling of the same using the theory of subjective logic. By placing a Dirichlet distribution on the class probabilities, we treat predictions of a neural net as subjective opinions and learn the function that collects the evidence leading to these opinions by a deterministic neural net from data. The resultant predictor for a multi-class classification problem is another Dirichlet distribution whose parameters are set by the continuous output of a neural net. We provide a preliminary analysis on how the peculiarities of our new loss function drive improved uncertainty estimation. We observe that our method achieves unprecedented success on detection of out-of-distribution queries and endurance against adversarial perturbations.

## Key points
- Explicitly models prediction uncertainty using subjective logic and Dirichlet distributions on class probabilities
- Deterministic neural network learns evidence functions that parameterize the Dirichlet distribution rather than learning weight uncertainties
- Achieves state-of-the-art performance on out-of-distribution detection and adversarial robustness compared to Bayesian approaches
- Provides theoretical analysis of the proposed loss function and its role in improving uncertainty estimation

## Links
- Source: https://papers.nips.cc/paper_files/paper/2018/hash/a981f2b708044d6fb4a71a1463242520-Abstract.html
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1473926493733257256

## My notes
-
