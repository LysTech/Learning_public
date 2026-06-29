---
type: paper
uid: "2026-02-21-httpsarxivorgpdf260216284"
title: "Fast KV Compaction via Attention Matching"
authors: ["Adam Zweiger", "Xinghong Fu", "Han Guo", "Yoon Kim"]
year: 2026
venue: "arXiv"
doi: "10.48550/arXiv.2602.16284"
url: "https://arxiv.org/pdf/2602.16284"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "brainstorming-core"
tags: ["arxiv", "brainstorming-core", "llm-enriched", "paper"]
source: "arxiv"
added: 2026-04-09
---
## Summary
Scaling language models to long contexts is often bottlenecked by the size of the key-value (KV) cache. In deployed settings, long contexts are typically managed through compaction in token space via summarization. However, summarization can be highly lossy, substantially harming downstream performance. Recent work on Cartridges has shown that it is possible to train highly compact KV caches in latent space that closely match full-context performance, but at the cost of slow and expensive end-to-end optimization. This work describes an approach for fast context compaction in latent space through Attention Matching, which constructs compact keys and values to reproduce attention outputs and preserve attention mass at a per-KV-head level. We show that this formulation naturally decomposes into simple subproblems, some of which admit efficient closed-form solutions. Within this framework, we develop a family of methods that significantly push the Pareto frontier of compaction time versus quality, achieving up to 50x compaction in seconds on some datasets with little quality loss.

## Key points
- Proposes Attention Matching for fast KV cache compaction in latent space, addressing computational bottlenecks in long-context LLMs
- Constructs compact keys and values to reproduce attention outputs and preserve per-KV-head attention mass
- Decomposes the compaction problem into simple subproblems with efficient closed-form solutions
- Achieves up to 50x compaction on some datasets in seconds with little quality loss, significantly improving the compaction time vs. quality Pareto frontier
- Offers substantial speedup improvements over prior work like Cartridges while maintaining comparable performance

## Links
- Source: https://arxiv.org/pdf/2602.16284
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1474773975677538315

## My notes
-
