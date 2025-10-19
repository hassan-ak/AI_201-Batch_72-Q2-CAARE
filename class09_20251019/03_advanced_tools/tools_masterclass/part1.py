import os
from dotenv import load_dotenv, find_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool, StopAtTools, set_tracing_disabled

_: bool = load_dotenv(find_dotenv())
set_tracing_disabled(True)

# ONLY FOR TRACING
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")

gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")

# 1. Which LLM Service?
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# 2. Which LLM Model?
llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

@function_tool
def get_weather(city: str) -> str:
    """A simple function to get the weather for a user."""
    print("===> get_weather tool called")
    return "Sunny"

@function_tool
def get_travel_plan(city: str) -> str:
    """Plan Travel for your city"""
    print("===> get_travel_plan tool called")
    return "Do not forget to visit the local market."


base_agent: Agent = Agent(
    name="WeatherAgent",
    instructions="You are a helpful assistant.",
    model=llm_model,
    tools=[get_weather, get_travel_plan],
    tool_use_behavior=StopAtTools(stop_at_tool_names=["get_travel_plan"]),
    # tool_use_behavior="stop_on_first_tool"
)

res = Runner.run_sync(base_agent, "What is weather in Lahore")
# res = Runner.run_sync(base_agent, "Make me travel plan for Lahore")
# res = Runner.run_sync(base_agent, "What is weather in Lahore and make me travel plan for Lahore")

print(res.final_output)

# 1. NLP answer = loop finished
# 2. tool call = loop continue - loop finish

# tool call = ASK Question from Human = loop pause
