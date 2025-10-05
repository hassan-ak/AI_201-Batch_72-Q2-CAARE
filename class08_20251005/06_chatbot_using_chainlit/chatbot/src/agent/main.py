from agents import (
    Agent,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)
from config import Config


def create_main_agent() -> Agent:
    config = Config()

    external_client = AsyncOpenAI(
        base_url=config.gemini_api_url, api_key=config.gemini_api_key
    )

    llm_model = OpenAIChatCompletionsModel(
        model=config.gemini_api_model, openai_client=external_client
    )

    set_tracing_disabled(True)

    agent = Agent(
        name="MainAgent",
        instructions="You are a helpful assistant.",
        model=llm_model,
    )

    return agent
