"""
Pattern: Debug mode with .env + verbose logs.

Loads credentials from environment variables using python-dotenv, enables verbose stdout
logging to inspect requests/responses, and runs a simple sync prompt. Use this to
troubleshoot authentication, provider wiring, and prompt/response flow.
"""

from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_tracing_disabled,
    set_default_openai_client,
    OpenAIChatCompletionsModel,
    enable_verbose_stdout_logging,
)
from dotenv import load_dotenv
import os

# Load environment variables from a local .env file (if present)
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

# Basic validation: fail fast if required vars are missing
if not BASE_URL or not API_KEY or not MODEL_NAME:
    raise ValueError("BASE_URL, API_KEY, and MODEL_NAME must be set in environment variables.")

# Create client from env-based configuration
external_client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)

set_default_openai_client(external_client)

set_tracing_disabled(True)

# Agent uses a concrete model object
agent = Agent(
    name="Test Agent",
    instructions="You are a helpful assistant that responds in a single line.",
    model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=external_client),
)


def debug_mode_main():
    # Turn on verbose logs to stdout (great for debugging)
    enable_verbose_stdout_logging()
    
    """Run a sync prompt with verbose logging enabled."""
    result = Runner.run_sync(agent, "What is the capital of France?")
    print(result.final_output)
