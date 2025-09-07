# Model Configuration Patterns (OpenAI Agents SDK)

This lesson shows four practical ways to configure models and providers when building agents with the OpenAI Agents SDK. Each pattern fits a different need: app-wide defaults, per-agent overrides, per-run overrides, and a debug-friendly setup with environment variables and verbose logs.

## What you’ll learn

- How to configure the model globally for the whole app
- How to set a model per agent using a model object
- How to override model settings per run via `RunConfig`
- How to load credentials from `.env` and enable debug logging

## Where the demo lives

```
class04_20250907/05_model_configuration/
└─ model_configuration/
	 ├─ pyproject.toml
	 └─ src/model_configuration/
			├─ main.py                 # CLI entry points wiring
			├─ global_config_main.py   # App-wide defaults (model name string)
			├─ agent_config_main.py    # Per-agent model object
			├─ runner_config_main.py   # Per-run overrides via RunConfig
			└─ debug_mode_main.py      # .env + verbose logging for troubleshooting
```

The project defines helpful commands in `pyproject.toml`.

## Quick start (with `uv`)

From the `model_configuration/` folder:

```bash
uv sync

# App-wide defaults
uv run run-global-config

# Per-agent model object
uv run run-agent-config

# Per-run overrides
uv run run-runner-config

# Debug mode (.env + verbose logs)
uv run run-debug-mode
```

If you run the debug mode, ensure you have a `.env` file (or set env vars in your shell). See `.env.example` in the project folder.

## Pattern 1 — Global defaults (simple, app-wide)

Set the default OpenAI client and API once, then use a plain model name string in agents. Good for small apps where one model/provider is used everywhere.

File: `global_config_main.py`

Pros:

- Minimal setup; one place to change provider/model

Cons:

- Harder to mix different models/providers in different areas

## Pattern 2 — Agent-level model object

Attach a concrete model instance to a specific agent. Useful when different agents need different models or providers.

File: `agent_config_main.py`

Pros:

- Clear per-agent control; easy to mix models

Cons:

- Slightly more boilerplate per agent

## Pattern 3 — Runner-level overrides (per run)

Keep the agent generic, but override model/provider at execution time using `RunConfig`. Great for AB testing, canaries, or dynamic choices per request.

File: `runner_config_main.py`

Pros:

- Maximum flexibility per request

Cons:

- More moving parts; ensure sane defaults to avoid config sprawl

## Pattern 4 — Debug mode with .env + verbose logs

Load credentials from environment variables and enable verbose logs to see requests and decisions in your terminal. Ideal during integration and troubleshooting.

File: `debug_mode_main.py`

Pros:

- Safer secret handling; great visibility into agent runs

Cons:

- Slightly noisier output; remember to disable in production

## Credential handling (important)

Prefer environment variables or secret managers. Avoid hard-coding API keys in source files.

If adapting these examples, set and read:

- `BASE_URL` — model provider base URL
- `API_KEY` — your provider key
- `MODEL_NAME` — the model ID to use

See `model_configuration/.env.example` for guidance.

## Troubleshooting

- 401/403: check key and base URL
- Import errors: ensure you run from the project root and used `uv sync`
- No logs in debug mode: ensure `enable_verbose_stdout_logging()` is called and `.env` is present
