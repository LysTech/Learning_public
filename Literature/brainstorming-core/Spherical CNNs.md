---
type: paper
uid: "2025-09-23-papers-on-graph-spherical-and-curved-manifold-cnns-storing-here-for-future-reference-repos-rela-5"
title: "Spherical CNNs"
authors: ["Taco S. Cohen", "Mario Geiger", "Jonas Koehler", "Max Welling"]
year: 2018
venue: "arXiv"
doi: "10.48550/arXiv.1801.10130"
url: "https://arxiv.org/pdf/1801.10130"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "brainstorming-core"
tags: ["ai", "arxiv", "brainstorming-core", "llm-enriched", "paper"]
source: "arxiv"
added: 2026-04-09
---
## Summary
Convolutional Neural Networks (CNNs) have become the method of choice for learning problems involving 2D planar images. However, a number of problems of recent interest have created a demand for models that can analyze spherical images. Examples include omnidirectional vision for drones, robots, and autonomous cars, molecular regression problems, and global weather and climate modelling. A naive application of convolutional networks to a planar projection of the spherical signal is destined to fail, because the space-varying distortions introduced by such a projection will make translational weight sharing ineffective. In this paper we introduce the building blocks for constructing spherical CNNs. We propose a definition for the spherical cross-correlation that is both expressive and rotation-equivariant. The spherical correlation satisfies a generalized Fourier theorem, which allows us to compute it efficiently using a generalized (non-commutative) Fast Fourier Transform (FFT) algorithm. We demonstrate the computational efficiency, numerical accuracy, and effectiveness of spherical CNNs applied to 3D model recognition and atomization energy regression.

## Key points
- Proposes rotation-equivariant spherical convolution operations that preserve geometric structure on spherical domains
- Spherical cross-correlation satisfies generalized Fourier theorem, enabling efficient computation via non-commutative FFT
- Demonstrates effectiveness on 3D model recognition and molecular property regression tasks
- Addresses limitations of naive planar projections which introduce space-varying distortions incompatible with translational weight sharing
- Provides foundational building blocks for constructing CNNs on curved manifolds beyond standard planar images

## Notes
https://arxiv.org/pdf/1805.07857 https://arxiv.org/pdf/1506.05163 https://arxiv.org/pdf/1312.6203 https://arxiv.org/pdf/2306.03838 https://arxiv.org/pdf/1801.10130 papers on gra...

## Links
- Source: https://arxiv.org/pdf/1801.10130
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1419992061817524276

## My notes
-
