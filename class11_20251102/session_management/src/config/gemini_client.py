from agents import (  # pyright: ignore[reportMissingImports]
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_default_openai_client,
    set_tracing_disabled,
)
from config import Config

# Create external client for Gemini API
external_client = AsyncOpenAI(
    base_url=Config.gemini_api_url,
    api_key=Config.gemini_api_key,
)

# Set as default client
set_default_openai_client(external_client)

# Disable tracing
set_tracing_disabled(True)

# Create and export the model
model = OpenAIChatCompletionsModel(
    model=Config.gemini_api_model,
    openai_client=external_client,
)

__all__ = ["model", "external_client"]