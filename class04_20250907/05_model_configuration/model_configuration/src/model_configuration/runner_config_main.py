"""
Pattern: Runner-level overrides (per run).

Keep your Agent generic and override the model/provider at execution time via RunConfig.
This is great for AB tests, canary rollouts, or user-specific routing without changing the agent.

NOTE: Move secrets to environment variables in production.
"""

from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_tracing_disabled,
    set_default_openai_client,
    OpenAIChatCompletionsModel,
)
from agents.run import RunConfig

# Replace with environment variables in production
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
API_KEY = "your_api_key"
MODEL_NAME = "gemini-2.5-flash"

# Default client
external_client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)

set_default_openai_client(external_client)

set_tracing_disabled(True)

# A concrete model object to supply via RunConfig
model = OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=external_client)

# RunConfig lets us override settings per call
config = RunConfig(model=model, tracing_disabled=True, model_provider=external_client)

# A generic agent that can run with different RunConfigs
agent = Agent(
    name="Test Agent",
    instructions="You are a helpful assistant that responds in a single line.",
)

def runner_config_main():
    """Run a sync prompt with per-run config overriding defaults."""
    result = Runner.run_sync(agent, "What is the capital of France?", run_config=config)
    print(result.final_output)
