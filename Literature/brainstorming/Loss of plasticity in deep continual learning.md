---
type: paper
uid: "2026-06-10-httpswwwnaturecomarticless41586-024-07711-7"
title: "Loss of plasticity in deep continual learning"
authors: ["Shibhansh Dohare", "J. Fernando Hernandez-Garcia", "Qingfeng Lan", "Parash Rahman", "A. Rupam Mahmood", "Richard S. Sutton"]
year: 2024
venue: "Nature"
doi: "10.1038/s41586-024-07711-7"
url: "https://www.nature.com/articles/s41586-024-07711-7"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "brainstorming"
tags: ["brainstorming", "llm-enriched", "paper", "url"]
source: "url"
added: 2026-06-12
---
## Summary
Artificial neural networks, deep-learning methods and the backpropagation algorithm 1 form the foundation of modern machine learning and artificial intelligence. These methods are almost always used in two phases, one in which the weights of the network are updated and one in which the weights are held constant while the network is used or evaluated. This contrasts with natural learning and many applications, which require continual learning. It has been unclear whether or not deep learning methods work in continual learning settings. Here we show that they do not—that standard deep-learning methods gradually lose plasticity in continual-learning settings until they learn no better than a shallow network. We show such loss of plasticity using the classic ImageNet dataset and reinforcement-learning problems across a wide range of variations in the network and the learning algorithm. Plasticity is maintained indefinitely only by algorithms that continually inject diversity into the network, such as our continual backpropagation algorithm, a variation of backpropagation in which a small fraction of less-used units are continually and randomly reinitialized. Our results indicate that methods based on gradient descent are not enough—that sustained deep learning requires a random, non-gradient component to maintain variability and plasticity.

## Key points
- Standard deep learning methods lose plasticity in continual learning settings, eventually performing no better than shallow networks
- Loss of plasticity occurs across diverse network architectures and learning algorithms when trained on ImageNet and reinforcement learning tasks
- Plasticity can be maintained indefinitely by injecting diversity into networks, such as continual backpropagation which randomly reinitializes less-used units
- Gradient descent alone is insufficient for sustained deep learning; a random, non-gradient component is necessary to maintain variability and plasticity

## Links
- Source: https://www.nature.com/articles/s41586-024-07711-7
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1514330745114595490

## My notes
-
