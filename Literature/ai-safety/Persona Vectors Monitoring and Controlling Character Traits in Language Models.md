---
type: paper
uid: "2026-05-27-httpsarxivorgabs250721509"
title: "Persona Vectors: Monitoring and Controlling Character Traits in Language Models"
authors: ["Runjin Chen", "Andy Arditi", "Henry Sleight", "Owain Evans", "Jack Lindsey"]
year: 2025
venue: "arXiv"
doi: "10.48550/arXiv.2507.21509"
url: "https://arxiv.org/abs/2507.21509"
status: to-read
rating: 
shared_by: "Thomas R."
channel: "ai-safety"
tags: ["ai", "ai-safety", "arxiv", "llm-enriched", "paper"]
source: "arxiv"
added: 2026-06-12
---
## Summary
Large language models interact with users through a simulated 'Assistant' persona. While the Assistant is typically trained to be helpful, harmless, and honest, it sometimes deviates from these ideals. In this paper, we identify directions in the model's activation space-persona vectors-underlying several traits, such as evil, sycophancy, and propensity to hallucinate. We confirm that these vectors can be used to monitor fluctuations in the Assistant's personality at deployment time. We then apply persona vectors to predict and control personality shifts that occur during training. We find that both intended and unintended personality changes after finetuning are strongly correlated with shifts along the relevant persona vectors. These shifts can be mitigated through post-hoc intervention, or avoided in the first place with a new preventative steering method. Moreover, persona vectors can be used to flag training data that will produce undesirable personality changes, both at the dataset level and the individual sample level. Our method for extracting persona vectors is automated and can be applied to any personality trait of interest, given only a natural-language description.

## Key points
- Automated method to extract persona vectors for any personality trait from natural-language descriptions
- Persona vectors enable real-time monitoring of character trait fluctuations in deployed LLMs
- Intended and unintended personality changes from finetuning strongly correlate with shifts along relevant persona vectors
- Post-hoc intervention and preventative steering can mitigate unwanted personality changes during training
- Framework identifies problematic training data at both dataset and individual sample levels that would produce undesirable personality shifts

## Notes
https://arxiv.org/abs/2507.21509  what happens to persona vectors when you brain-tune a model? the procedure defined in the paper would allow us to extract, e.g., a "Viktor pers...

## Links
- Source: https://arxiv.org/abs/2507.21509
- Discord: https://discord.com/channels/1400359609323229267/1499786973009936524/1509100971584651345

## My notes
-
