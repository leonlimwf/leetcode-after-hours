# LeetCode After Hours

**One problem. One honest attempt. A little better every day.**

[![Practice: LeetCode](https://img.shields.io/badge/Practice-LeetCode-FFA116?style=flat-square)](https://leetcode.com/u/leonlimwf/)
![Language: Python](https://img.shields.io/badge/Language-Python-3776AB?style=flat-square)
![Coach: ChatGPT](https://img.shields.io/badge/Coach-ChatGPT-10A37F?style=flat-square)
![Schedule: Singapore](https://img.shields.io/badge/Schedule-00%3A00%20%2F%2005%3A00%20SGT-24292F?style=flat-square)

This is my daily coding practice journal in public. I started this habit to improve my problem-solving skills, become more comfortable writing Python, and prepare for technical interviews. The goal is to understand why an approach works, explain its time and space costs, and build consistency over time.

## My routine

| Time · Asia/Singapore | What happens |
| --- | --- |
| **00:00 · midnight** | ChatGPT picks a fresh Easy or Medium problem from suitable interview topics, with variety and no repeats. The automation pulls the latest repository changes and publishes the day's question brief. |
| **During practice** | I write my first instinct, attempt the problem, and submit on LeetCode. I ask for hints when stuck and sometimes work through full code with ChatGPT. |
| **05:00 · morning check** | ChatGPT checks the journal and public LeetCode progress, analyzes the actual code's time and auxiliary space complexity, and commits and pushes confirmed completed solutions and available analysis. |

Question selection is randomized among appropriate fresh candidates, guided by what I have already practiced. This is a learning routine, not a claim that every solution was produced independently or without assistance.

## AI assistance and automation

**This repository is set up and maintained automatically by ChatGPT through the Codex desktop app.** ChatGPT helps with question selection, coaching, complexity explanations, progress tracking, and scheduled GitHub updates. The practice, submissions, and learning are mine; code may include AI assistance, which I acknowledge openly.

The existing local automation runs at midnight and 5am in Singapore time. It reads my private Word journal and tracking ledger, then exports a small public snapshot using [the sync script](scripts/sync.py). My full journal, conversation history, authentication details, and local file paths are kept out of the published snapshot.

Scheduled updates require the computer to be on, the desktop app running, and GitHub authentication available. Delivery can be delayed. GitHub Actions is not used as a second scheduler because a hosted runner cannot read my local journal or continue my coaching chat. See [the automation guide](docs/automation.md) for the setup and recovery steps.

GitHub Actions runs regression tests and archive/privacy validation on pushes and pull requests. It has read-only repository permissions, receives no private journal or LeetCode credentials, and does not publish solutions. The local workflow uses a public-only progress lookup, no-repeat inventory, exact journal-code extraction, crash-safe publishing locks, and cached exports to make retries predictable.

## Explore the practice log

- [Daily questions](QUESTIONS.md): dated assignments, difficulty, topics, and links.
- [Confirmed completions](PROGRESS.md): accepted history and links to archived code.
- [Solutions](solutions/): Python code copied from the journal after acceptance is confirmed.
- [Public progress data](data/progress.json): a compact snapshot used to generate the indexes.

A public Accepted submission and a learner-confirmed completion are recorded separately. Profile evidence alone does not turn an unfinished entry into a confirmed completion. Missing code or complexity analysis is labeled explicitly instead of being filled with an invented solution.

## What I am working toward

Recognizing common patterns in arrays, hash maps, stacks, linked lists, and trees. Turning an initial idea into working code. Handling edge cases and debugging calmly. Explaining tradeoffs clearly enough to walk an interviewer through my reasoning.

The practice history starts on **16 September 2026**. Earlier confirmed solutions were imported from my journal with my approval. Git commits reflect when records are published; past submissions are not backdated into artificial daily commits.

---

Problems belong to [LeetCode](https://leetcode.com/). Briefs are paraphrased for my practice; the original problem pages are linked throughout. This is a personal learning project, not an official LeetCode or OpenAI project.
