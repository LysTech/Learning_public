---
type: paper
uid: "2025-10-06-a-useful-toolbox-for-getting-single-trial-beta-weights-can-be-fitted-to-the-voxel-reconstruction"
title: "Improving the accuracy of single-trial fMRI response estimates using GLMsingle"
authors: ["Jacob S Prince", "Ian Charest", "Jan W Kurzawski", "John A Pyles", "Michael J Tarr", "Kendrick N Kay"]
year: 2022
venue: "eLife"
doi: "10.7554/elife.77599"
url: "https://github.com/cvnlab/GLMsingle"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "perceived-speech"
tags: ["ai", "github", "llm-enriched", "perceived-speech", "resource"]
source: "github"
added: 2026-04-09
---
## Summary
Advances in artificial intelligence have inspired a paradigm shift in human neuroscience, yielding large-scale functional magnetic resonance imaging (fMRI) datasets that provide high-resolution brain responses to thousands of naturalistic visual stimuli. Because such experiments necessarily involve brief stimulus durations and few repetitions of each stimulus, achieving sufficient signal-to-noise ratio can be a major challenge. We address this challenge by introducing GLMsingle , a scalable, user-friendly toolbox available in MATLAB and Python that enables accurate estimation of single-trial fMRI responses ( glmsingle.org ). Requiring only fMRI time-series data and a design matrix as inputs, GLMsingle integrates three techniques for improving the accuracy of trial-wise general linear model (GLM) beta estimates. First, for each voxel, a custom hemodynamic response function (HRF) is identified from a library of candidate functions. Second, cross-validation is used to derive a set of noise regressors from voxels unrelated to the experiment. Third, to improve the stability of beta estimates for closely spaced trials, betas are regularized on a voxel-wise basis using ridge regression. Applying GLMsingle to the Natural Scenes Dataset and BOLD5000, we find that GLMsingle substantially improves the reliability of beta estimates across visually-responsive cortex in all subjects. Comparable improvements in reliability are also observed in a smaller-scale auditory dataset from the StudyForrest experiment. These improvements translate into tangible benefits for higher-level analyses relevant to systems and cognitive neuroscience. We demonstrate that GLMsingle: (i) helps decorrelate response estimates between trials nearby in time; (ii) enhances representational similarity between subjects within and across datasets; and (iii) boosts one-versus-many decoding of visual stimuli. GLMsingle is a publicly available tool that can significantly improve the quality of past, present, and future neuroimaging datasets sampling brain activity across many experimental conditions.

## Key points
- Integrates three complementary techniques: custom HRF identification, noise regressor extraction via cross-validation, and ridge regression regularization
- Substantially improves reliability of single-trial fMRI beta estimates across visually-responsive cortex
- Demonstrates practical benefits for representational similarity, cross-subject generalization, and visual stimulus decoding
- Publicly available in both MATLAB and Python with minimal inputs required (fMRI time-series and design matrix)
- Validated on multiple large-scale datasets including Natural Scenes Dataset, BOLD5000, and StudyForrest

## Notes
a useful toolbox for getting single trial beta weights: https://github.com/cvnlab/GLMsingle (can be fitted to the voxel reconstruction data from the kernel flow2 pipeline). pape...

## Links
- Source: https://github.com/cvnlab/GLMsingle
- Discord: https://discord.com/channels/1400359609323229267/1400365455746662400/1424742997051965480

## My notes
-
