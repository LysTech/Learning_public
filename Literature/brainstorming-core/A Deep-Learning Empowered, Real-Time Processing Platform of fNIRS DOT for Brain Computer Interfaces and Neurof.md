---
type: paper
uid: "2026-01-26-httpspmcncbinlmnihgovarticlespmc12270413"
title: "A Deep-Learning Empowered, Real-Time Processing Platform of fNIRS/DOT for Brain Computer Interfaces and Neurofeedback"
authors: ["Xia Y", "Chen J", "Li J", "Gong T", "Vidal-Rosas EE", "Loureiro R", "Cooper RJ", "Zhao H"]
year: 2025
venue: "IEEE Trans Neural Syst Rehabil Eng"
doi: "10.1109/TNSRE.2025.3553794"
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC12270413/"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "brainstorming-core"
tags: ["brainstorming-core", "llm-enriched", "paper", "url"]
source: "url"
added: 2026-04-09
---
## Summary
Brain-Computer Interfaces (BCI) and Neurofeedback (NFB) approaches, which both rely on real-time monitoring of brain activity, are increasingly being applied in rehabilitation, assistive technology, neurological diseases and behavioral disorders. Functional near-infrared spectroscopy (fNIRS) and diffuse optical tomography (DOT) are promising techniques for these applications due to their non-invasiveness, portability, low cost, and relatively high spatial resolution. However, real-time processing of fNIRS/DOT data remains a significant challenge as it requires establishing a baseline of the measurement, simultaneously performing real-time motion artifact (MA) correction across all channels, and (in the case of DOT) addressing the time-consuming process of image reconstruction. This study proposes a real-time processing system for fNIRS/DOT that integrates baseline calibration, denoising autoencoder (DAE) based MA correction model with a sliding window strategy, and a pre-calculated inverse Jacobian matrix to streamline the reconstructed 3D brain hemodynamics. The DAE model was trained on an extensive whole-head high-density DOT (HD-DOT) dataset and tested on separate motor imagery dataset augmented with artificial MA. The system demonstrated the capability to simultaneously process approximately 750 channels in real-time. Our results show that the DAE-based MA correction method outperformed traditional MA correction in terms of mean squared error and correlation to the known MA-free data while maintaining low latency, which is critical for effective BCI and NFB applications. The system's high-channel, real-time processing capability provides channel-wise oxygenation information and functional 3D imaging, making it well-suited for fNIRS/DOT applications in BCI and NFB, particularly in movement-intensive scenarios such as motor rehabilitation and assistive technology for mobility support.

## Key points
- Proposes a real-time fNIRS/DOT processing system integrating baseline calibration, denoising autoencoder (DAE) for motion artifact correction, and pre-calculated inverse Jacobian matrix for 3D brain imaging
- Demonstrates capability to simultaneously process ~750 channels in real-time with low latency, critical for effective BCI and neurofeedback applications
- DAE-based motion artifact correction outperforms traditional methods while maintaining clinical-grade processing speed
- System provides channel-wise oxygenation information and functional 3D imaging, particularly suited for movement-intensive rehabilitation and assistive technology scenarios

## Links
- Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12270413/
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1465413157399953539

## My notes
-
