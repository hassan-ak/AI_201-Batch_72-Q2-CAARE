import os
import asyncio
from dotenv import load_dotenv, find_dotenv
from dataclasses import dataclass
from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
    function_tool,
    RunContextWrapper,
)

_: bool = load_dotenv(find_dotenv())

gemini_api_key: str | None = os.environ.get("GEMINI_API_KEY")

# Tracing disabled
set_tracing_disabled(disabled=True)

# 1. Which LLM Service?
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# 2. Which LLM Model?
llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash", openai_client=external_client
)


@dataclass
class UserContext:
    username: str
    email: str | None = None


@function_tool
async def fetch_user_age(wrapper: RunContextWrapper[UserContext]) -> str:  
    return f"User {wrapper.context.username} is 47 years old."


async def main():
    # Create your context object
    user_info = UserContext(username="John", email="john@example.com")

    # Define an agent that will use the tool above
    agent = Agent[UserContext](  
        name="Assistant",
        tools=[fetch_user_age],
        model=llm_model,
        instructions="You can use the tool to fetch user age.",
    )

    # Run the agent, passing in the local context
    result = await Runner.run(
        starting_agent=agent,
        input="What is the age of the user?",
        context=user_info,
    )

    print(result.final_output)  # Expected output: The user John is 47 years old.

asyncio.run(main())