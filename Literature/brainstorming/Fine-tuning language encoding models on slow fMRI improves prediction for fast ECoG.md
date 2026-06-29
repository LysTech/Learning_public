---
type: paper
uid: "2026-06-02-fmri-ecog-1156152140780277761"
title: "Fine-tuning language encoding models on slow fMRI improves prediction for fast ECoG"
authors: ["Aditya R. Vaidya", "Richard J. Antonello", "Alexander G. Huth"]
year: 2026
venue: "arXiv"
doi: "10.48550/arXiv.2605.19224"
url: "https://arxiv.org/pdf/2605.19224"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "brainstorming"
tags: ["arxiv", "brainstorming", "llm-enriched", "paper"]
source: "arxiv"
added: 2026-06-12
---
## Summary
Neuroscientists have recently turned to intracranial brain recording methods, like electrocorticography (ECoG), for human experiments because of the fine spatial and temporal resolution that they afford. Models trained on this data, however, are fundamentally restricted by the patient populations that can receive the implants necessary for recording. We propose using non-invasive fMRI to bridge the gap in training data. Using spoken language representations fine-tuned on fMRI, we build encoding models of ECoG. These representations showed improved prediction performance in ECoG, even though the temporal resolution of fMRI is two orders of magnitude worse. Prediction improved in frequency bands well beyond what is directly measured in fMRI. Next, to test the procedure's generalization ability, we fine-tuned models on fMRI responses that were temporally downsampled by a factor of 2. Despite the loss in resolution, these models were able to predict fMRI and ECoG responses at levels comparable to the original fMRI-tuned models. Finally, we showed that ECoG performance steadily scales with the amount of fMRI-tuning data. Our results show that "slow" data like fMRI can be a valuable resource for building better models of "fast" brain data like ECoG. In the future, integrating across multiple recording methods may further improve performance in other applications, like decoding.

## Key points
- Fine-tuning on fMRI improves ECoG encoding model performance even with drastically different temporal resolutions
- Improved predictions extend to frequency bands beyond those directly measured in fMRI
- Models remain effective when fMRI is downsampled by 2×, demonstrating robustness to resolution loss
- Performance scales systematically with the amount of fMRI training data used
- Multi-modal integration across invasive and non-invasive recording methods can unlock larger training datasets for brain encoding models

## Notes
https://arxiv.org/pdf/2605.19224 fmri <-> ecog <@1156152140780277761>

## Links
- Source: https://arxiv.org/pdf/2605.19224
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1511446724634214432

## My notes
-
