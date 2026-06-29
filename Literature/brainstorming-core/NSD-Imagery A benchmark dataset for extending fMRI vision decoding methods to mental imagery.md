---
type: paper
uid: "2026-02-10-they-found-no-carryover-from-visual-recon-to-mental-imagery"
title: "NSD-Imagery: A benchmark dataset for extending fMRI vision decoding methods to mental imagery"
authors: ["Reese Kneeland", "Paul S. Scotti", "Ghislain St-Yves", "Jesse Breedlove", "Kendrick Kay", "Thomas Naselaris"]
year: 2025
venue: "arXiv"
doi: "10.48550/arXiv.2506.06898"
url: "https://arxiv.org/abs/2506.06898"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "brainstorming-core"
tags: ["arxiv", "brainstorming-core", "llm-enriched", "paper"]
source: "arxiv"
added: 2026-04-09
---
## Summary
We release NSD-Imagery, a benchmark dataset of human fMRI activity paired with mental images, to complement the existing Natural Scenes Dataset (NSD), a large-scale dataset of fMRI activity paired with seen images that enabled unprecedented improvements in fMRI-to-image reconstruction efforts. Recent models trained on NSD have been evaluated only on seen image reconstruction. Using NSD-Imagery, it is possible to assess how well these models perform on mental image reconstruction. This is a challenging generalization requirement because mental images are encoded in human brain activity with relatively lower signal-to-noise and spatial resolution; however, generalization from seen to mental imagery is critical for real-world applications in medical domains and brain-computer interfaces, where the desired information is always internally generated. We provide benchmarks for a suite of recent NSD-trained open-source visual decoding models (MindEye1, MindEye2, Brain Diffuser, iCNN, Takagi et al.) on NSD-Imagery, and show that the performance of decoding methods on mental images is largely decoupled from performance on vision reconstruction. We further demonstrate that architectural choices significantly impact cross-decoding performance: models employing simple linear decoding architectures and multimodal feature decoding generalize better to mental imagery, while complex architectures tend to overfit visual training data. Our findings indicate that mental imagery datasets are critical for the development of practical applications, and establish NSD-Imagery as a useful resource for better aligning visual decoding methods with this goal.

## Key points
- Introduces NSD-Imagery benchmark pairing fMRI with mental imagery to test generalization of vision decoding models
- Performance on seen image reconstruction is largely decoupled from mental imagery reconstruction performance
- Simple linear decoding architectures and multimodal feature decoders generalize better to mental imagery than complex models
- Benchmarks multiple recent models (MindEye1, MindEye2, Brain Diffuser, iCNN, Takagi et al.) trained on NSD
- Demonstrates that mental imagery datasets are critical for real-world applications in medical imaging and brain-computer interfaces

## Notes
they found no carryover from visual recon to mental imagery: https://arxiv.org/abs/2506.06898

## Links
- Source: https://arxiv.org/abs/2506.06898
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1470908290652176458

## My notes
-
