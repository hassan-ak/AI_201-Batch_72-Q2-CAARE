# Hello Agent - Simple App (Gemini via OpenAI-Compatible)

A minimal **uv**-based demo that runs an **OpenAI Agents SDK** agent, but with a **Gemini** model through the OpenAI-compatible Chat Completions endpoint.

## What You’ll Build
- A tiny app created with `uv init` that:
  - Uses **OpenAI Agents SDK** primitives (`Agent`, `Runner`)
  - Configures an **OpenAI-compatible client** for **Gemini**
  - Registers a **Chat Completions** model
  - Runs a prompt and prints the final answer

## 1. Create the app (with uv)
From your workspace:
```bash
uv init agents_simple
```
Open the folder in VS Code, **create/activate the environment**, and **select the interpreter** (see your [Step 02](../../02_uv/01_simple_application/README.md)).  
This will scaffold a small project you can run immediately.

## 2. Add the Agents SDK dependency
Inside the project folder:
```bash
uv add openai-agents
```

**Confirm install** by checking `pyproject.toml` → the dependency appears under `[project] dependencies`.

Your `pyproject.toml` should look like this
```toml
[project]
name = "agents-simple"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "openai-agents>=0.2.7",
]
```

## 3. Get your Gemini API key
Follow [Step 06](../../06_get_api_key/readme.md) the API key.  
You can paste it **directly in code** (fast but unsafe) or store it in `.env` (recommended).

**Quick demo way (in code):**
```python
api_key = "your api key here"
```

## 4. Write `main.py`
Create/replace `main.py` with the code below.

```python
# main.py
# Simple Agents SDK demo using Gemini via OpenAI-compatible Chat Completions

import os

from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_default_openai_client,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)

# 1) API key and model
api_key = "your api key here"             # replace with your key
model = "gemini-2.5-flash-lite"           # your chosen Gemini model

# 2) Define an OpenAI-compatible client for Gemini
#    This base_url points to Google's OpenAI-compatible endpoint.
external_client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=api_key,
)
# Make it the default client so SDK calls use it.
set_default_openai_client(external_client)

# 3) Register the model (Chat Completions style) and disable tracing
#    Note: Agents SDK defaults to Responses API when using OpenAI models.
#    Since we are using an OpenAI-compatible Chat Completions backend (Gemini),
#    we explicitly set a Chat Completions model and turn off tracing (not supported here).
llm_model = OpenAIChatCompletionsModel(
    model=model,
    openai_client=external_client,
)

# Tracing is enabled by default for OpenAI; disable for Gemini
set_tracing_disabled(True)

# 4) Define the agent
agent = Agent(
    name="simple_agent",
    instructions="You are a helpful assistant, specialized in providing single-line responses.",
    model=llm_model,
)

# 5) Run the agent and print the answer
response = Runner.run_sync(agent, "What is AI?")
print(response.final_output)
```

## 5. Run the app
From the project root:
```bash
uv run -m main
# or
uv run python main.py
```

You should see a short single-line answer printed.

## Tweaks to Try
- Change `instructions` to adjust tone/format (e.g., “answer in bullet points”).
- Change the `model` to another Gemini variant you have access to.
- Log the entire `response` object to explore available metadata.

## Troubleshooting

**ModuleNotFoundError: No module named 'agents'**  
- Ensure the package installed successfully:
  ```bash
  uv add openai-agents
  ```

**401 Unauthorized**  
- Your API key is missing or invalid. Double-check the key and whether you passed it to `AsyncOpenAI(api_key=...)`.  

**404 / Bad base_url**  
- Verify the `base_url` matches the OpenAI-compatible endpoint you intend to use.

**Tracing error / not supported**  
- Keep `set_tracing_disabled(True)` when using non-OpenAI backends.

**uv can’t find Python / interpreter**  
- Re-open the folder in VS Code and pick the uv-created interpreter ([Step 02](../../02_uv/01_simple_application/README.md) guidance).

---