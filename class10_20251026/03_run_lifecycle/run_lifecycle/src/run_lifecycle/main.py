from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    function_tool,
    set_tracing_disabled
)
from config import Config
from run_hooks import ExampleRunnerHooks
from rich import print

config = Config()

set_tracing_disabled(True)

# 1. Which LLM Service?
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=config.gemini_api_key,
    base_url=config.gemini_api_url,
)

# 2. Which LLM Model?
llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model=config.gemini_api_model, openai_client=external_client
)


@function_tool
def get_weather(city: str) -> str:
    """A simple function to get the weather for a user."""
    return f"The weather for {city} is sunny."


news_agent: Agent = Agent(
    name="NewsAgent",
    instructions="Provided latest info about the topic when asked.",
    model=llm_model,
)


base_agent: Agent = Agent(
    name="WeatherAgent",
    instructions="You are a helpful assistant. Talk about weather and let news_agent handle the news things",
    model=llm_model,
    tools=[get_weather],
    handoffs=[news_agent],
)


def main():
    res = Runner.run_sync(
        base_agent,
        "What are latest news on GenAI? Also, what's the weather in New York City?",
        hooks=ExampleRunnerHooks(),
    )
    print("\n \n")
    print(res.final_output)
    print("\n \n")

