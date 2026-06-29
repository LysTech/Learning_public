---
type: paper
uid: "2025-08-07-it-is-also-interesting-to-note-that-when-it-comes-to-fmri-data-nobody-is-feeding-raw-sensor-data-to-2"
title: "MEG Source Localization via Deep Learning"
authors: ["Pantazis D", "Adler A"]
year: 2021
venue: "Sensors (Basel)"
doi: "10.3390/s21134278"
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC8271934/"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "brainstorming-core"
tags: ["ai", "brainstorming-core", "llm-enriched", "paper", "url"]
source: "url"
added: 2026-04-09
---
## Summary
We present a deep learning solution to the problem of localization of magnetoencephalography (MEG) brain signals. The proposed deep model architectures are tuned to single and multiple time point MEG data, and can estimate varying numbers of dipole sources. Results from simulated MEG data on the cortical surface of a real human subject demonstrated improvements against the popular RAP-MUSIC localization algorithm in specific scenarios with varying SNR levels, inter-source correlation values, and number of sources. Importantly, the deep learning models had robust performance to forward model errors resulting from head translation and rotation and a significant reduction in computation time, to a fraction of 1 ms, paving the way to real-time MEG source localization.

## Key points
- Deep learning models outperform RAP-MUSIC algorithm for MEG source localization in specific scenarios
- Robust to forward model errors resulting from head translation and rotation during acquisition
- Achieves sub-millisecond computation times, enabling real-time MEG source localization
- Models flexibly handle varying numbers of dipole sources and both single and multiple timepoint data
- Validated on simulated MEG data with systematic evaluation across SNR levels and inter-source correlation values

## Notes
It is also interesting to note that when it comes to fMRI data, nobody is feeding raw sensor data to the models (https://medarc-ai.github.io/mindeye2/ - these people are related...

## Links
- Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC8271934/
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1402914009891606539

## My notes
-
