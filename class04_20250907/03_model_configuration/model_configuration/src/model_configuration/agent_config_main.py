"""
Pattern: Agent-level model object.

Attach a concrete model instance to an Agent. This is useful when different agents in
the same app need different models or providers.

NOTE: Move secrets to environment variables for real deployments.
"""

from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_tracing_disabled,
    set_default_openai_client,
    OpenAIChatCompletionsModel,
)

# Replace with environment variables in production
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
API_KEY = "your_api_key"
MODEL_NAME = "gemini-2.5-flash"

# Default client for the app
external_client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)

set_default_openai_client(external_client)

set_tracing_disabled(True)

# Explicit model object bound to this agent
agent = Agent(
    name="Test Agent",
    instructions="You are a helpful assistant that responds in a single line.",
    model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=external_client),
)


def agent_config_main():
    """Run a sync prompt using the agent-specific model instance."""
    result = Runner.run_sync(agent, "What is the capital of France?")
    print(result.final_output)
