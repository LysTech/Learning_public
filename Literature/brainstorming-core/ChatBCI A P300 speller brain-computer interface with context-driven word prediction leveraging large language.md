---
type: paper
uid: "2026-02-27-httpswwwnaturecomarticless41598-025-25660-7"
title: "ChatBCI: A P300 speller brain-computer interface with context-driven word prediction leveraging large language models"
authors: ["Hong, Jiazhen", "Wang, Weinan", "Najafizadeh, Laleh"]
year: 2026
venue: "Scientific Reports"
doi: "10.1038/s41598-025-25660-7"
url: "https://www.nature.com/articles/s41598-025-25660-7"
status: to-read
rating: 
shared_by: "Nyx"
channel: "brainstorming-core"
tags: ["brainstorming-core", "llm-enriched", "paper", "url"]
source: "url"
added: 2026-04-09
---
## Summary
P300 speller brain computer interfaces (BCIs) allow users to compose sentences by selecting target keys on a graphical user interface (GUI) through the detection of P300 component in their electroencephalogram (EEG) signals following visual stimuli. Most existing P300 speller BCIs require users to spell all or the first few initial letters of the intended word, letter by letter. Consequently, a large number of keystrokes could be required to write an intended sentence, thereby, increasing user’s time and cognitive load. There is a need for more efficient and user-friendly methods for faster, and practical sentence composition. In this work, we introduce ChatBCI, a P300 speller BCI that leverages the zero-shot learning capabilities of large language models (LLMs) to suggest words from user-spelled initial letters or predict the subsequent word(s), reducing keystrokes and accelerating sentence composition. ChatBCI retrieves word suggestions through remote queries to the GPT-3.5 API. A modified GUI, displaying GPT-3.5 word suggestions as extra keys is designed. Stepwise linear discriminant analysis (SWLDA) is used for the P300 classification. Seven subjects completed two online spelling tasks: 1) copy-spelling a self-composed sentence using ChatBCI, and 2) improvising a sentence using ChatBCI’s word suggestions. Results demonstrate that for the copy-spelling task, on average, ChatBCI outperforms letter-by-letter BCI spellers, reducing time and keystrokes by $$62.14\%$$ and $$53.22\%$$ , respectively, and increasing information transfer rate by $$229.48\%$$ . For the improvised sessions, ChatBCI achieves $$80.68\%$$ keystroke savings across subjects. Overall, ChatBCI, by employing remote LLM queries outperforms traditional spellers without requiring local model training or storage. ChatBCI's (multi-)word prediction capability paves the way for developing next-generation speller BCIs that are efficient and effective for real-time communication, specially for users with communication and motor disabilities.

## Key points
- Integrates GPT-3.5 API for context-aware word suggestions and multi-word prediction in P300 spellers
- Achieves 62.14% time reduction and 53.22% keystroke savings on copy-spelling tasks vs. traditional BCIs
- Improves information transfer rate by 229.48% without requiring local model training or storage
- Demonstrates 80.68% keystroke savings during improvised sentence composition
- Enables more efficient real-time communication for users with motor and speech disabilities

## Links
- Source: https://www.nature.com/articles/s41598-025-25660-7
- Discord: https://discord.com/channels/1400359609323229267/1400360278842937354/1476948468298682582

## My notes
-
