# Software Engineering Methods For AI-Driven Deductive Legal Reasoning

This repository is meant to accompany the Onward! 2024 paper titled "Software Engineering Methods For AI-Driven Deductive Legal Reasoning" authored by Rohan Padhye. The repository contains LLM prompts and traces corresponding to the examples in the paper.

## System Prompt


See `system-prompt.txt` for the system prompt used in all examples. For all examples listed in the paper, the system prompt contained the exact same excerpt of statutes from the [Internal Revenue Code](https://uscode.house.gov/browse/prelim@title26) as listed in the paper's Appendix A.

## Claude Transcripts

The folder `ClaudeTranscripts` contains transcripts of conversations with [Anthropic's Claude 3 Opus](https://www.anthropic.com/claude) which formed the basis of examples provided in the paper. The model version used for these transcripts was `claude-3-opus-20240229` with `temperature=0` and `max_tokens=2000`.

In each transcript file, messages (system prompt, user prompt, AI response) are separated by a line containing only `---`.