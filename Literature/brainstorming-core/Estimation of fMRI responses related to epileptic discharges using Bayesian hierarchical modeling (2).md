---
type: paper
title: "Estimation of fMRI responses related to epileptic discharges using Bayesian hierarchical modeling"
authors: ["Zhengchen Cai", "Nicolás von Ellenrieder", "Andreas Koupparis", "Hui Ming Khoo", "Satoru Ikemoto", "Masataka Tanaka", "Chifaou Abdallah", "Saba Rammal", "Francois Dubeau", "Jean Gotman"]
year: 2023
venue: "Human Brain Mapping"
doi: "10.1002/hbm.26490"
url: "https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/hbm.26490?download=true&campaigns=%5B%7B%22position%22%3A%22ereader-last-page%22%2C%22uri%22%3A%22uri%3A707b1a3c-73e6-4188-b21f-2b05b70307d8%22%7D%2C%7B%22position%22%3A%22ereader-first-page%22%2C%22uri%22%3A%22uri%3A7691ea89-90f5-4086-9241-486673caed61%22%7D%5D"
status: to-read
rating:
shared_by: "Thomas R."
channel: "brainstorming-core"
tags: ["ai", "brainstorming-core", "llm-enriched", "paper", "url"]
source: "url"
added: 2026-04-09
---
## Summary
Simultaneous electroencephalography–functional MRI (EEG‐fMRI) is a unique and noninvasive method for epilepsy presurgical evaluation. When selecting voxels by null‐hypothesis tests, the conventional analysis may overestimate fMRI response amplitudes related to interictal epileptic discharges (IEDs), especially when IEDs are rare. We aimed to estimate fMRI response amplitudes represented by blood oxygen level dependent (BOLD) percentage changes related to IEDs using a hierarchical model. It involves the local and distributed hemodynamic response homogeneity to regularize estimations. Bayesian inference was applied to fit the model. Eighty‐two epilepsy patients who underwent EEG‐fMRI and subsequent surgery were included in this study. A conventional voxel‐wise general linear model was compared to the hierarchical model on estimated fMRI response amplitudes and on the concordance between the highest response cluster and the surgical cavity. The voxel‐wise model overestimated fMRI responses compared to the hierarchical model, evidenced by a practically and statistically significant difference between the estimated BOLD percentage changes. Only the hierarchical model differentiated brief and long‐lasting IEDs with significantly different BOLD percentage changes. Overall, the hierarchical model outperformed the voxel‐wise model on presurgical evaluation, measured by higher prediction performance. When compared with a previous study, the hierarchical model showed higher performance metric values, but the same or lower sensitivity. Our results demonstrated the capability of the hierarchical model of providing more physiologically reasonable and more accurate estimations of fMRI response amplitudes induced by IEDs. To enhance the sensitivity of EEG‐fMRI for presurgical evaluation, it may be necessary to incorporate more appropriate spatial priors and bespoke decision strategies.

## Key points
- Conventional voxel-wise GLM overestimates fMRI responses to interictal epileptic discharges, particularly when discharges are rare
- Hierarchical Bayesian model with local and distributed hemodynamic response homogeneity priors provides more accurate and physiologically reasonable estimates
- Successfully differentiates BOLD responses between brief and long-lasting IEDs, which voxel-wise GLM cannot
- Demonstrates higher prediction performance for presurgical evaluation compared to conventional GLM on 82 epilepsy patients
- Suggests incorporating spatial priors and decision strategies beyond standard GLM may improve EEG-fMRI sensitivity for clinical applications

## Notes
GLM replacement candidate with reasonable priors imposed on the betas :  https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/hbm.26490?download=true&campaigns=%5B%7B%22positio...

## Links
- Source: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/hbm.26490?download=true&campaigns=%5B%7B%22position%22%3A%22ereader-last-page%22%2C%22uri%22%3A%22uri%3A707b1a3c-73e6-4188-b21f-2b05b70307d8%22%7D%2C%7B%22position%22%3A%22ereader-first-page%22%2C%22uri%22%3A%22uri%3A7691ea89-90f5-4086-9241-486673caed61%22%7D%5D
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1455230379064692788

## My notes
- 
