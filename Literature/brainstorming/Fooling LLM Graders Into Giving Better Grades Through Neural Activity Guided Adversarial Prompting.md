---
type: paper
uid: "2026-05-07-since-our-current-work-is-on-llms-this-is-another-interesting-adversarial-attack-appending-magic"
title: "Fooling LLM Graders Into Giving Better Grades Through Neural Activity Guided Adversarial Prompting"
authors: ["Atsushi Yamamura", "Surya Ganguli"]
year: 2024
venue: "arXiv"
doi: "10.48550/arXiv.2412.15275"
url: "https://arxiv.org/pdf/2412.15275"
status: to-read
rating: 
shared_by: "Thomas R."
channel: "brainstorming"
tags: ["arxiv", "brainstorming", "llm-enriched", "paper"]
source: "arxiv"
added: 2026-06-12
---
## Summary
The deployment of artificial intelligence (AI) in critical decision-making and evaluation processes raises concerns about inherent biases that malicious actors could exploit to distort decision outcomes. We propose a systematic method to reveal such biases in AI evaluation systems and apply it to automated essay grading as an example. Our approach first identifies hidden neural activity patterns that predict distorted decision outcomes and then optimizes an adversarial input suffix to amplify such patterns. We demonstrate that this combination can effectively fool large language model (LLM) graders into assigning much higher grades than humans would. We further show that this white-box attack transfers to black-box attacks on other models, including commercial closed-source models like Gemini. They further reveal the existence of a "magic word" that plays a pivotal role in the efficacy of the attack. We trace the origin of this magic word bias to the structure of commonly-used chat templates for supervised fine-tuning of LLMs and show that a minor change in the template can drastically reduce the bias. This work not only uncovers vulnerabilities in current LLMs but also proposes a systematic method to identify and remove hidden biases, contributing to the goal of ensuring AI safety and security.

## Key points
- Systematically identifies hidden neural activity patterns in LLMs that predict susceptibility to grade inflation
- Develops white-box adversarial suffix optimization that transfers to black-box attacks on closed-source models like Gemini
- Discovers 'magic words' whose efficacy traces to standard chat template structures used in supervised fine-tuning
- Proposes simple template modifications to drastically reduce model susceptibility to the attack
- Demonstrates practical vulnerability in deployed LLM grading systems relevant to AI safety and security

## Notes
since our current work is on LLMs this is another interesting adversarial attack: https://arxiv.org/pdf/2412.15275 (appending magic prompts to get better grades from LLM graders)

## Links
- Source: https://arxiv.org/pdf/2412.15275
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1501857801310306408

## My notes
-
