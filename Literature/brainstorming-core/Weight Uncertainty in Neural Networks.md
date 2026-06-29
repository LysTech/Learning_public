---
type: paper
uid: "2026-02-19-httpsarxivorgpdf150505424"
title: "Weight Uncertainty in Neural Networks"
authors: ["Charles Blundell", "Julien Cornebise", "Koray Kavukcuoglu", "Daan Wierstra"]
year: 2015
venue: "arXiv"
doi: "10.48550/arXiv.1505.05424"
url: "https://arxiv.org/pdf/1505.05424"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "brainstorming-core"
tags: ["arxiv", "brainstorming-core", "llm-enriched", "paper"]
source: "arxiv"
added: 2026-04-09
---
## Summary
We introduce a new, efficient, principled and backpropagation-compatible algorithm for learning a probability distribution on the weights of a neural network, called Bayes by Backprop. It regularises the weights by minimising a compression cost, known as the variational free energy or the expected lower bound on the marginal likelihood. We show that this principled kind of regularisation yields comparable performance to dropout on MNIST classification. We then demonstrate how the learnt uncertainty in the weights can be used to improve generalisation in non-linear regression problems, and how this weight uncertainty can be used to drive the exploration-exploitation trade-off in reinforcement learning.

## Key points
- Introduces Bayes by Backprop: a principled, backpropagation-compatible algorithm for learning weight distributions in neural networks
- Uses variational free energy (evidence lower bound) as a compression cost for regularization
- Achieves comparable performance to dropout on MNIST while providing uncertainty estimates
- Demonstrates practical applications of weight uncertainty for improved generalization in regression and exploration-exploitation in reinforcement learning

## Links
- Source: https://arxiv.org/pdf/1505.05424
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1473931025229938792

## My notes
-
