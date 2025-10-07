# sync-vs-async-agent-execution (Demo)

A tiny packaged app demonstrating synchronous vs asynchronous AI agent execution using the OpenAI Agents SDK, plus a realistic demo showing how to overlap agent calls with other I/O using `asyncio`.

## Project layout

```
sync-vs-async-agent-execution/
├─ pyproject.toml
└─ src/sync_vs_async_agent_execution/
	├─ main.py             # CLI entry points wiring
	├─ sync_main.py        # Sync (blocking) agent call example
	├─ async_main.py       # Async (awaitable) agent call example
	├─ sync_main_demo.py   # Sequential flow (DB log then agent)
	└─ async_main_demo.py  # Parallel flow (DB log and agent together)
```

## Prerequisites

- Python (managed by `uv`)
- `uv` installed (https://docs.astral.sh/uv/)
- A valid API key for the selected model provider

## Setup

Install dependencies and create the virtualenv:

```bash
uv sync
```

Optionally select the interpreter in VS Code from `.venv`.

## Configure credentials

Keep secrets out of source control. Prefer environment variables and load them at runtime.

Suggested variables if you adapt the code:

- `GEMINI_BASE_URL` → e.g. `https://generativelanguage.googleapis.com/v1beta/openai/`
- `GEMINI_API_KEY`  → your key from Google AI Studio

If you modify the client initialization, use `os.getenv("GEMINI_API_KEY")` etc. Don’t commit secrets.

## Run

This project defines CLI scripts in `pyproject.toml`:

```bash
# Minimal examples
uv run run-sync         # blocking agent call
uv run run-async        # async (awaited) agent call

# Realistic UX demo
uv run run-sync-demo    # sequential: DB log, then agent
uv run run-async-demo   # parallel: DB log + agent concurrently
```

In the demo runs you’ll be prompted for your name/email. The async version should complete faster because it overlaps the agent call with the DB log (simulated delay).

## Notes

- `Runner.run_sync(...)` blocks until completion.
- `await Runner.run(...)` allows other tasks to progress until the agent finishes.
- Use `asyncio.create_task(...)` and `asyncio.gather(...)` to run multiple awaitables concurrently.

## Troubleshooting

- Authentication errors → check API key and base URL
- `uv` not found → follow install docs linked above
- Network issues → retry, or check provider status
