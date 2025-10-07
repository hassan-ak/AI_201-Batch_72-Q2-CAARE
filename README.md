# AI-201: Fundamentals of Agentic AI (Batch 72 - CAARE)

This repository contains course materials, demos, and quizzes used in the AI-201 classroom series. Each class folder is named with the class number and date and contains lessons, code samples, and exercises.

## Quick links

- Classes:
  - `class01_20250817/` — Introduction, uv, traditional LLMs, n8n
  - `class02_20250824/` — uv apps and packaged applications, n8n basics
  - `class03_20250831/` — APIs, SDKs, OpenAI Agents SDK examples
  - `class04_20250907/` — Async vs Sync agents, model configuration, design patterns
  - `class05_20250914/` — Prompt & Context Engineering, Image/Video generation
  - `class06_20250921/` — Python topics: decorators, dataclasses, generics, callables

- Quizzes: `quizzes/` — contains per-class MCQ quizzes (e.g., `quizzes/class05_20250914`)

## Quick start

- Browse the class folders for lesson READMEs and examples.
- Many demos use `uv` to create and run simple Python apps. If you want to run a demo:

  ```bash
  # from the demo folder (example)
  cd class04_20250907/02_sync_vs_async_agent_execution/sync-vs-async-agent-execution
  uv sync
  uv run run-sync-demo
  ```

## Contributing

- Add new lessons inside `classXX_YYYYMMDD/` with descriptive readmes and runnable examples.
- Place quizzes under `quizzes/classXX_YYYYMMDD/`.
- Avoid committing secrets; use environment variables for API keys.

## License

This repository follows the LICENSE at the project root.
