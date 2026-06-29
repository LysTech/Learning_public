---
type: paper
uid: "2026-06-12-they-do-something-similar-here-and-we-did-try-ti-deconvolve-neural-from-hemo-in-betting-project"
title: "A blind deconvolution approach to recover effective connectivity brain networks from resting state fMRI data"
authors: ["Wu GR", "Liao W", "Stramaglia S", "Ding JR", "Chen H", "Marinazzo D"]
year: 2013
venue: "Med Image Anal"
doi: "10.1016/j.media.2013.01.003"
url: "https://pubmed.ncbi.nlm.nih.gov/23422254/"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "brainstorming"
tags: ["brainstorming", "llm-enriched", "paper", "url"]
source: "url"
added: 2026-06-12
---
## Summary
A great improvement to the insight on brain function that we can get from fMRI data can come from effective connectivity analysis, in which the flow of information between even remote brain regions is inferred by the parameters of a predictive dynamical model. As opposed to biologically inspired models, some techniques as Granger causality (GC) are purely data-driven and rely on statistical prediction and temporal precedence. While powerful and widely applicable, this approach could suffer from two main limitations when applied to BOLD fMRI data: confounding effect of hemodynamic response function (HRF) and conditioning to a large number of variables in presence of short time series. For task-related fMRI, neural population dynamics can be captured by modeling signal dynamics with explicit exogenous inputs; for resting-state fMRI on the other hand, the absence of explicit inputs makes this task more difficult, unless relying on some specific prior physiological hypothesis. In order to overcome these issues and to allow a more general approach, here we present a simple and novel blind-deconvolution technique for BOLD-fMRI signal. In a recent study it has been proposed that relevant information in resting-state fMRI can be obtained by inspecting the discrete events resulting in relatively large amplitude BOLD signal peaks. Following this idea, we consider resting fMRI as 'spontaneous event-related', we individuate point processes corresponding to signal fluctuations with a given signature, extract a region-specific HRF and use it in deconvolution, after following an alignment procedure. Coming to the second limitation, a fully multivariate conditioning with short and noisy data leads to computational problems due to overfitting. Furthermore, conceptual issues arise in presence of redundancy. We thus apply partial conditioning to a limited subset of variables in the framework of information theory, as recently proposed. Mixing these two improvements we compare the differences between BOLD and deconvolved BOLD level effective networks and draw some conclusions.

## Key points
- Proposes blind deconvolution technique to separate neural activity from hemodynamic response function (HRF) effects in resting-state fMRI
- Uses point process detection of spontaneous BOLD signal peaks to estimate region-specific HRF and enable deconvolution
- Applies partial conditioning with information-theoretic variable selection to avoid overfitting with short time series
- Demonstrates differences in effective connectivity networks between raw and deconvolved BOLD data
- Addresses two main limitations of Granger causality applied to fMRI: HRF confounding and high-dimensional conditioning with limited data

## Notes
https://pubmed.ncbi.nlm.nih.gov/23422254/ they do something similar here and we did try ti deconvolve neural from hemo in betting project

## Links
- Source: https://pubmed.ncbi.nlm.nih.gov/23422254/
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1514962648318611477

## My notes
-
