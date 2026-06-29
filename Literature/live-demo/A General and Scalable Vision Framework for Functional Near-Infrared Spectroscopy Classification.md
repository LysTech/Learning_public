---
type: paper
uid: "2025-12-12-read-this-wang-strikes-again"
title: "A General and Scalable Vision Framework for Functional Near-Infrared Spectroscopy Classification"
authors: ["Zenghui Wang", "Jun Zhang", "Yi Xia", "Peng Chen", "Bing Wang"]
year: 2022
venue: "IEEE Transactions on Neural Systems and Rehabilitation Engineering"
doi: "10.1109/tnsre.2022.3190431"
url: "https://ieeexplore.ieee.org/abstract/document/9828508"
status: to-read
rating: 
shared_by: "Thomas R."
channel: "live-demo"
tags: ["ai", "live-demo", "llm-enriched", "paper", "url"]
source: "url"
added: 2026-04-09
---
## Summary
Functional near-infrared spectroscopy (fNIRS), a non-invasive optical technique, is widely used to monitor brain activities for disease diagnosis and brain-computer interfaces (BCIs). Deep learning-based fNIRS classification faces three major barriers: limited datasets, confusing evaluation criteria, and domain barriers. We apply more appropriate evaluation methods to three open-access datasets to solve the first two barriers. For domain barriers, we propose a general and scalable vision fNIRS framework that converts multi-channel fNIRS signals into multi-channel virtual images using the Gramian angular difference field (GADF). We use the framework to train state-of-the-art visual models from computer vision (CV) within a few minutes, and the classification performance is competitive with the latest fNIRS models. In cross-validation experiments, visual models achieve the highest average classification results of 78.68% and 73.92% on mental arithmetic and word generation tasks, respectively. Although visual models are slightly lower than the fNIRS models on unilateral finger- and foot-tapping tasks, the F1-score and kappa coefficient indicate that these differences are insignificant in subject-independent experiments. Furthermore, we study fNIRS signal representations and the classification performance of sequence-to-image methods. We hope to introduce rich achievements from the CV domain to improve fNIRS classification research.

## Key points
- Novel conversion of fNIRS time-series signals to images using GADF enables the reuse of pre-trained vision architectures without domain-specific architecture design
- Achieves 78.68% and 73.92% average classification accuracy on mental arithmetic and word generation tasks respectively, competitive with state-of-the-art fNIRS models
- Demonstrates that visual models perform effectively on multi-channel fNIRS data, suggesting broader applicability of computer vision methods to biomedical signal processing
- Framework bridges the gap between limited fNIRS datasets and rich computer vision literature, providing a pathway for leveraging CV advances in neurotechnology applications
- Evaluation on three open-access datasets with appropriate cross-validation methods establishes rigorous benchmarking standards for the fNIRS classification community

## Notes
read this, wang strikes again!   I was suspicious at first ("transformers for X" sounds..., well) but actually I'm impressed with what I see. I couldn't open the original paper ...

## Links
- Source: https://ieeexplore.ieee.org/abstract/document/9828508
- Discord: https://discord.com/channels/1400359609323229267/1400365362025070743/1448988688473264177

## My notes
-
