# Sync vs Async Agent Execution

Learn how to run AI agents synchronously vs asynchronously, why it matters for user experience and throughput, and how to structure small apps to run agent work in parallel with other I/O tasks.

## What you’ll learn

- The difference between blocking (sync) and non-blocking (async) agent calls
- When to use `Runner.run_sync(...)` vs `await Runner.run(...)` from the OpenAI Agents SDK
- A practical pattern to run agent work alongside other tasks (e.g., logging to DB) concurrently

## Where the demo lives

This lesson contains a small packaged project under:

```
class04_20250907/02_sync_vs_async_agent_execution/
└─ sync-vs-async-agent-execution/
	 ├─ pyproject.toml
	 └─ src/sync_vs_async_agent_execution/
			├─ main.py             # CLI entry points wiring
			├─ sync_main.py        # Sync (blocking) agent call
			├─ async_main.py       # Async (awaitable) agent call
			├─ sync_main_demo.py   # Realistic sync flow (sequential)
			└─ async_main_demo.py  # Realistic async flow (parallel)
```

The project exposes convenient commands via `pyproject.toml` so you don’t need to write file paths.

## Quick start (with `uv`)

From the `sync-vs-async-agent-execution/` folder:

1) Install environment and lock dependencies

```bash
uv sync
```

2) Run the baseline examples

```bash
uv run run-sync        # blocking agent call
uv run run-async       # non-blocking agent call (awaited)
```

3) Run the realistic UX demo (compares sequential vs parallel)

```bash
uv run run-sync-demo   # sequential: DB log, then agent
uv run run-async-demo  # parallel: DB log and agent together
```

You’ll be prompted for your name/email in the demo. The async version should finish faster because it overlaps the agent call with the database log (simulated delay).

## How it works (high level)

- Sync path: uses `Runner.run_sync(agent, prompt)` which blocks the current thread until the agent finishes.
- Async path: uses `await Runner.run(agent, prompt)` which yields control so other async tasks can progress while the agent is running.

In the demo pair:

- `sync_main_demo.py` logs the user to DB (simulated `time.sleep`) and only then calls the agent. Total time ≈ sum of both.
- `async_main_demo.py` runs both concurrently using `asyncio.create_task(...)` and `await asyncio.gather(...)`. Total time ≈ max of the two.

## Configure credentials (important)

The demo uses the OpenAI Agents SDK with a Gemini-compatible endpoint. For security, you should keep API keys in environment variables (never hard-code in source or commits).

Suggested environment variables:

- `GEMINI_BASE_URL` → e.g. `https://generativelanguage.googleapis.com/v1beta/openai/`
- `GEMINI_API_KEY`  → your key from Google AI Studio

If you adapt the code, read these with `os.getenv(...)` and pass them to the SDK client. If you use the provided code as-is, ensure you replace any placeholder keys locally and DO NOT commit secrets.

## When to choose sync vs async

- Use sync when:
	- Simplicity beats concurrency
	- Running a single short task where blocking is acceptable
- Use async when:
	- You want to overlap the agent call with other I/O (DB, HTTP, file)
	- You handle many parallel user requests or background jobs
	- You need responsive UIs or APIs while long tasks run

## Troubleshooting

- 401/403 errors: check your API key and base URL
- Timeouts/network errors: verify internet access and provider status
- `uv` not found: install from https://docs.astral.sh/uv/