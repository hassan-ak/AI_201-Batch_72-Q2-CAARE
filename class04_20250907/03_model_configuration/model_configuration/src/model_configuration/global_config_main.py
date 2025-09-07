"""
Pattern: Global defaults.

Configure the default OpenAI client and API once for the whole app. Agents can then
reference the model by name (string). This is the simplest pattern if your app uses
one provider/model everywhere.

NOTE: For production, do NOT hard-code secrets. Prefer environment variables or secret managers.
"""

from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_tracing_disabled,
    set_default_openai_client,
    set_default_openai_api
)

# Replace these with environment variables in real apps
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
API_KEY = "your_api_key"
MODEL_NAME = "gemini-2.5-flash"

# Create a single client and set as default for the app
external_client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)

set_default_openai_client(external_client)

set_tracing_disabled(True)

# Set the default API for OpenAI-compatible providers (chat_completions here)
set_default_openai_api("chat_completions")

# Agent uses a plain string model (resolved via defaults)
agent = Agent(
    name="Test Agent",
    instructions="You are a helpful assistant that responds in a single line.",
    model=MODEL_NAME,
)


def global_config_main():
    """Run a simple sync prompt to show the configured defaults in action."""
    result = Runner.run_sync(agent, "What is the capital of France?")
    print(result.final_output)
