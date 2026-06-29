---
type: paper
uid: "2026-02-02-this-is-cool-they-train-audio-embeddings-models-on-3hrs-of-music-data-with-simultaneous-eeg-and-m"
title: "Towards Deep Modeling of Music Semantics using EEG Regularizers"
authors: ["Francisco Raposo", "David Martins de Matos", "Ricardo Ribeiro", "Suhua Tang", "Yi Yu"]
year: 2017
venue: "arXiv"
doi: "10.48550/arXiv.1712.05197"
url: "https://arxiv.org/pdf/1712.05197"
status: to-read
rating: 
shared_by: "Thomas R."
channel: "brainstorming-core"
tags: ["ai", "arxiv", "brainstorming-core", "llm-enriched", "paper"]
source: "arxiv"
added: 2026-04-09
---
## Summary
Modeling of music audio semantics has been previously tackled through learning of mappings from audio data to high-level tags or latent unsupervised spaces. The resulting semantic spaces are theoretically limited, either because the chosen high-level tags do not cover all of music semantics or because audio data itself is not enough to determine music semantics. In this paper, we propose a generic framework for semantics modeling that focuses on the perception of the listener, through EEG data, in addition to audio data. We implement this framework using a novel end-to-end 2-view Neural Network (NN) architecture and a Deep Canonical Correlation Analysis (DCCA) loss function that forces the semantic embedding spaces of both views to be maximally correlated. We also detail how the EEG dataset was collected and use it to train our proposed model. We evaluate the learned semantic space in a transfer learning context, by using it as an audio feature extractor in an independent dataset and proxy task: music audio-lyrics cross-modal retrieval. We show that our embedding model outperforms Spotify features and performs comparably to a state-of-the-art embedding model that was trained on 700 times more data. We further discuss improvements to the model that are likely to improve its performance.

## Key points
- Uses EEG signals as a regularizer to learn music semantics from minimal audio data (3 hours vs. 2000 hours previously required)
- Proposes a 2-view neural network architecture with Deep Canonical Correlation Analysis (DCCA) loss to align audio and EEG semantic embeddings
- Achieves comparable performance to state-of-the-art models trained on 700x more data, demonstrating the power of listener perception as a supervisory signal
- Validates learned embeddings on music audio-lyrics cross-modal retrieval, outperforming Spotify features

## Notes
This is cool: they train audio embeddings models on 3hrs of music data (with simultaneous EEG) and match the previous sota which needed 2000hrs of music. EEG regulariser reduced...

## Links
- Source: https://arxiv.org/pdf/1712.05197
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1467792157057220690

## My notes
-
