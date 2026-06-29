---
type: paper
uid: "2026-02-13-this-is-20-the-use-models-for-emulating-brain-representations-idea"
title: "Brain-optimized inference improves reconstructions of fMRI brain activity"
authors: ["Kneeland R", "Ojeda J", "St-Yves G", "Naselaris T"]
year: 2023
venue: "ArXiv"
doi: ""
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC10760191/"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "brainstorming-core"
tags: ["ai", "brainstorming-core", "llm-enriched", "paper", "url"]
source: "url"
added: 2026-04-09
---
## Summary
The release of large datasets and developments in AI have led to dramatic improvements in decoding methods that reconstruct seen images from human brain activity. We evaluate the prospect of further improving recent decoding methods by optimizing for consistency between reconstructions and brain activity during inference. We sample seed reconstructions from a base decoding method, then iteratively refine these reconstructions using a brain-optimized encoding model that maps images to brain activity. At each iteration, we sample a small library of images from an image distribution (a diffusion model) conditioned on a seed reconstruction from the previous iteration. We select those that best approximate the measured brain activity when passed through our encoding model, and use these images for structural guidance during the generation of the small library in the next iteration. We reduce the stochasticity of the image distribution at each iteration, and stop when a criterion on the "width" of the image distribution is met. We show that when this process is applied to recent decoding methods, it outperforms the base decoding method as measured by human raters, a variety of image feature metrics, and alignment to brain activity. These results demonstrate that reconstruction quality can be significantly improved by explicitly aligning decoding distributions to brain activity distributions, even when the seed reconstruction is output from a state-of-the-art decoding algorithm. Interestingly, the rate of refinement varies systematically across visual cortex, with earlier visual areas generally converging more slowly and preferring narrower image distributions, relative to higher-level brain areas. Brain-optimized inference thus offers a succinct and novel method for improving reconstructions and exploring the diversity of representations across visual brain areas.

## Key points
- Iterative refinement of reconstructions using brain-optimized encoding models during inference
- Combines diffusion model sampling with brain activity alignment to improve reconstruction quality
- Outperforms base decoding methods on human ratings, image feature metrics, and brain activity alignment
- Reveals systematic variation in representation diversity across visual cortex, with earlier areas preferring narrower distributions
- Demonstrates that explicit alignment between decoding and brain activity distributions improves reconstruction fidelity

## Notes
this is 20% the use models for emulating brain representations idea: https://pmc.ncbi.nlm.nih.gov/articles/PMC10760191/

## Links
- Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10760191/
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1471946796828856391

## My notes
-
