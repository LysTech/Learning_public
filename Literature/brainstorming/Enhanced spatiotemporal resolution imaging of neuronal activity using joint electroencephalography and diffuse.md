---
type: paper
uid: "2026-06-10-reconstruction-can-however-be-aided-temporally-by-eeg"
title: "Enhanced spatiotemporal resolution imaging of neuronal activity using joint electroencephalography and diffuse optical tomography"
authors: ["Cao J", "Huppert TJ", "Grover P", "Kainerstorfer JM"]
year: 2021
venue: "Neurophotonics"
doi: "10.1117/1.NPh.8.1.015002"
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC7778454/"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "brainstorming"
tags: ["ai", "brainstorming", "llm-enriched", "paper", "url"]
source: "url"
added: 2026-06-12
---
## Summary
Significance: Electroencephalography (EEG) and functional near-infrared spectroscopy (fNIRS) are both commonly used methodologies for neuronal source reconstruction. While EEG has high temporal resolution (millisecond-scale), its spatial resolution is on the order of centimeters. On the other hand, in comparison to EEG, fNIRS, or diffuse optical tomography (DOT), when used for source reconstruction, can achieve relatively high spatial resolution (millimeter-scale), but its temporal resolution is poor because the hemodynamics that it measures evolve on the order of several seconds. This has important neuroscientific implications: e.g., if two spatially close neuronal sources are activated sequentially with only a small temporal separation, single-modal measurements using either EEG or DOT alone would fail to resolve them correctly. Aim: We attempt to address this issue by performing joint EEG and DOT neuronal source reconstruction. Approach: We propose an algorithm that utilizes DOT reconstruction as the spatial prior of EEG reconstruction, and demonstrate the improvements using simulations based on the ICBM152 brain atlas. Results: We show that neuronal sources can be reconstructed with higher spatiotemporal resolution using our algorithm than using either modality individually. Further, we study how the performance of the proposed algorithm can be affected by the locations of the neuronal sources, and how the performance can be enhanced by improving the placement of EEG electrodes and DOT optodes. Conclusions: We demonstrate using simulations that two sources separated by 2.3-3.3 cm and 50 ms can be recovered accurately using the proposed algorithm by suitably combining EEG and DOT, but not by either in isolation. We also show that the performance can be enhanced by optimizing the electrode and optode placement according to the locations of the neuronal sources.

## Key points
- Proposes joint EEG-DOT neuronal source reconstruction algorithm to overcome single-modality limitations
- Demonstrates recovery of sources separated by 2.3-3.3 cm spatially and 50 ms temporally, which neither modality alone can achieve
- Uses DOT reconstruction as spatial prior to guide EEG reconstruction, leveraging complementary spatiotemporal strengths
- Shows performance can be further enhanced through optimized electrode and optode placement
- Validated using simulations on ICBM152 brain atlas

## Notes
reconstruction can however be aided temporally by eeg: https://pmc.ncbi.nlm.nih.gov/articles/PMC7778454/

## Links
- Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC7778454/
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1514309350016155729

## My notes
-
