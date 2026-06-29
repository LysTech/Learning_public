---
type: paper
uid: "2026-06-06-vibe-competitor-to-tribe-from-max-planck"
title: "VIBE: Video-Input Brain Encoder for fMRI Response Modeling"
authors: ["Daniel Carlström Schad", "Shrey Dixit", "Janis Keck", "Viktor Studenyak", "Aleksandr Shpilevoi", "Andrej Bicanski"]
year: 2025
venue: "arXiv"
doi: "10.48550/arXiv.2507.17958"
url: "https://arxiv.org/pdf/2507.17958"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "brainstorming"
tags: ["arxiv", "brainstorming", "llm-enriched", "paper"]
source: "arxiv"
added: 2026-06-12
---
## Summary
We present VIBE, a two-stage Transformer that fuses multi-modal video, audio, and text features to predict fMRI activity. Representations from open-source models (Qwen2.5, BEATs, Whisper, SlowFast, V-JEPA) are merged by a modality-fusion transformer and temporally decoded by a prediction transformer with rotary embeddings. Trained on 65 hours of movie data from the CNeuroMod dataset and ensembled across 20 seeds, VIBE attains mean parcel-wise Pearson correlations of 0.3225 on in-distribution Friends S07 and 0.2125 on six out-of-distribution films. An earlier iteration of the same architecture obtained 0.3198 and 0.2096, respectively, winning Phase-1 and placing second overall in the Algonauts 2025 Challenge.

## Key points
- Two-stage Transformer architecture combining modality fusion and temporal prediction for fMRI encoding
- Integrates multi-modal features from video, audio, and text using off-the-shelf pre-trained models
- Trained on 65 hours of movie data from CNeuroMod dataset with ensemble across 20 seeds
- Achieved state-of-the-art performance on Algonauts 2025 Challenge: 0.3225 correlation on in-distribution and 0.2125 on out-of-distribution test sets
- Demonstrates effective generalization of brain encoding models across different movie stimuli

## Notes
https://arxiv.org/pdf/2507.17958 - VIBE, competitor to tribe from max planck

## Links
- Source: https://arxiv.org/pdf/2507.17958
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1512867033115787416

## My notes
-
