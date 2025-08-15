# Hello Agent - Packaged App (Gemini via OpenAI-Compatible)

> Build a **packaged** Python application with the [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) using **Gemini API**.

## 1. Create a Packaged App

Run:

```bash
uv init --package agents_packaged
```

This will create a new **package-style UV project**.  
If you’re unsure about setting up environments and selecting the interpreter in VS Code, follow the instructions from **[Step 02](../../02_uv/02_packaged_application/README.md)**.

## 2. Cleanup Default Code

- In `/src/agents_packaged/__init__.py`, delete the placeholder/example code.
- In your `pyproject.toml`, remove any pre-defined `scripts` section (we’ll add our own later).

## 3. Install the OpenAI Agents SDK

```bash
uv add openai-agents
```

To confirm installation:

- Open `pyproject.toml`
- Look under `[project] dependencies` — you should see:

```toml
openai-agents>= "..."
```

## 4. Get Your Gemini API Key

Follow the instructions from **[Step 06](../../06_get_api_key/readme.md)** to create and obtain your **Google Gemini API key**.

## 5. Create `main.py`

Inside `/src/agents_packaged/`, create `main.py` and add:

```python
from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, OpenAIChatCompletionsModel, set_tracing_disabled

# Store credentials (REMOVE before committing)
api_key = "your_api_key_here"
model = "gemini-2.5-flash-lite"

# Configure Gemini as the external client
external_client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=api_key,
)
set_default_openai_client(external_client)

# Register the model (Chat Completions) and disable tracing (not supported for Gemini)
llm_model = OpenAIChatCompletionsModel(
    model=model,
    openai_client=external_client,
)
set_tracing_disabled(True)

# Define your agent
agent = Agent(
    name="simple_agent",
    instructions="You are a helpful assistant, specialized in providing single-line responses.",
    model=llm_model
)

# Wrap execution in a function (packaged app style)
def run_agent():
    response = Runner.run_sync(agent, "What is AI?")
    print(response.final_output)
```

## 6. Add Script Entry Point

Edit `pyproject.toml` and add under `[project.scripts]`:

```toml
[project.scripts]
agents-packaged = "agents_packaged.main:run_agent"
```

This allows you to run your packaged app without typing `python main.py`.

## 7. Run the App

```bash
uv run agents-packaged
```

If all is set up correctly, you’ll see something like:

```
Artificial Intelligence is the simulation of human intelligence in machines.
```

## Notes & Troubleshooting

- **API Key Safety:** Never commit your API key to Git. Use environment variables or `.env` files for production.
- **Why disable tracing?** OpenAI tracing works only with OpenAI endpoints. Gemini doesn’t support it.
- **Why packaged app?** Makes it easier to reuse code, distribute as a library, and run via CLI.
