---
type: paper
uid: "2025-09-12-next-thing-im-doing-for-this-project-is-to-run-metas-code-for-their-meg-paper-and-a-change-3s-c"
title: "Decoding speech perception from non-invasive brain recordings"
authors: ["Alexandre Défossez", "Charlotte Caucheteux", "Jérémy Rapin", "Ori Kabeli", "Jean-Rémi King"]
year: 2023
venue: "Nature Machine Intelligence"
doi: "10.1038/s42256-023-00714-5"
url: "https://www.nature.com/articles/s42256-023-00714-5"
status: to-read
rating: 
shared_by: "Thomas R."
channel: "perceived-speech"
tags: ["ai", "brainstorming-core", "llm-enriched", "paper", "perceived-speech", "url"]
source: "url"
added: 2026-04-09
---
## Summary
Decoding speech from brain activity is a long-awaited goal in both healthcare and neuroscience. Invasive devices have recently led to major milestones in this regard: deep-learning algorithms trained on intracranial recordings can now start to decode elementary linguistic features such as letters, words and audio-spectrograms. However, extending this approach to natural speech and non-invasive brain recordings remains a major challenge. Here we introduce a model trained with contrastive learning to decode self-supervised representations of perceived speech from the non-invasive recordings of a large cohort of healthy individuals. To evaluate this approach, we curate and integrate four public datasets, encompassing 175 volunteers recorded with magneto-encephalography or electro-encephalography while they listened to short stories and isolated sentences. The results show that our model can identify, from 3 seconds of magneto-encephalography signals, the corresponding speech segment with up to 41% accuracy out of more than 1,000 distinct possibilities on average across participants, and with up to 80% in the best participants—a performance that allows the decoding of words and phrases absent from the training set. The comparison of our model with a variety of baselines highlights the importance of a contrastive objective, pretrained representations of speech and a common convolutional architecture simultaneously trained across multiple participants. Finally, the analysis of the decoder’s predictions suggests that they primarily depend on lexical and contextual semantic representations. Overall, this effective decoding of perceived speech from non-invasive recordings delineates a promising path to decode language from brain activity, without putting patients at risk of brain surgery.

## Key points
- Achieves speech decoding from non-invasive MEG/EEG recordings across large cohorts without requiring invasive intracranial electrodes
- Contrastive learning objective with pretrained speech representations enables generalization to unseen speech
- Model trained across multiple participants simultaneously, addressing inter-subject variability in brain signals
- Decoded representations are primarily driven by lexical and contextual semantic information
- Integrated dataset of 175 volunteers across 4 public datasets enables robust evaluation and reproducibility

## Notes
next thing I'm doing for this project is to run Meta's code for their MEG paper, and (a) change 3s chunks to 25s chunks, (b) change transformer layers for embeddings. This'll ta...

## Links
- Source: https://www.nature.com/articles/s42256-023-00714-5
- Discord: https://discord.com/channels/1400359609323229267/1400365455746662400/1415947119063203982

## My notes
-
