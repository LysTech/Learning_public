---
type: paper
uid: "2026-06-10-beware-of-some-eeg-papers"
title: "Are EEG-to-Text Models Working?"
authors: ["Hyejeong Jo", "Yiqian Yang", "Juhyeok Han", "Yiqun Duan", "Hui Xiong", "Won Hee Lee"]
year: 2024
venue: "arXiv"
doi: "10.48550/arXiv.2405.06459"
url: "https://arxiv.org/abs/2405.06459"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "brainstorming"
tags: ["arxiv", "brainstorming", "llm-enriched", "paper"]
source: "arxiv"
added: 2026-06-12
---
## Summary
This work critically analyzes existing models for open-vocabulary EEG-to-Text translation. We identify a crucial limitation: previous studies often employed implicit teacher-forcing during evaluation, artificially inflating performance metrics. Additionally, they lacked a critical benchmark - comparing model performance on pure noise inputs. We propose a methodology to differentiate between models that truly learn from EEG signals and those that simply memorize training data. Our analysis reveals that model performance on noise data can be comparable to that on EEG data. These findings highlight the need for stricter evaluation practices in EEG-to-Text research, emphasizing transparent reporting and rigorous benchmarking with noise inputs. This approach will lead to more reliable assessments of model capabilities and pave the way for robust EEG-to-Text communication systems. Code is available at https://github.com/NeuSpeech/EEG-To-Text

## Key points
- Previous EEG-to-Text studies used implicit teacher-forcing during evaluation, artificially inflating reported performance metrics
- Existing models often lack critical noise baselines—models perform similarly on pure noise inputs as on real EEG data
- Proposes methodology to distinguish between models that genuinely learn from EEG signals versus those that memorize training data
- Advocates for stricter evaluation practices including transparent reporting and mandatory noise input benchmarking
- Code released for reproducibility and community validation

## Notes
beware of some eeg papers: https://arxiv.org/abs/2405.06459

## Links
- Source: https://arxiv.org/abs/2405.06459
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1514308065015631913

## My notes
-
