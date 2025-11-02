from agents import AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from config import Config

set_tracing_disabled(True)
gemini_external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=Config.gemini_api_key,
    base_url=Config.gemini_api_url,
)

# 2. Which LLM Model?
gemini_llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model=Config.gemini_api_model, openai_client=gemini_external_client
)