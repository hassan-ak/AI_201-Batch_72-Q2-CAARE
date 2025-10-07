from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_tracing_disabled,
    set_default_openai_client,
    OpenAIChatCompletionsModel,
)
import time
import asyncio

BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
API_KEY = "your_api_key"
MODEL_NAME = "gemini-2.5-flash"

external_client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)

set_default_openai_client(external_client)

set_tracing_disabled(True)

model = OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=external_client)

agent = Agent(
    name="Test Agent",
    instructions="You are a helpful assistant that responds in a single line.",
    model=model,
)


async def run_agent():
    result = await Runner.run(agent, "What is the capital of France?")
    print(f"[AGENT] {result.final_output}")


def get_user_details():
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()
    return {"name": name, "email": email}


async def log_user_to_db(user):
    print("[DB] Starting async user log...")
    await asyncio.sleep(2.0)
    print(f"[DB] Logged user (async): {user}")


async def async_main_demo():
    user = get_user_details()

    print("\n[APP] Async flow starting (parallel)...")
    start = time.perf_counter()

    db_task = asyncio.create_task(log_user_to_db(user))
    agent_task = asyncio.create_task(run_agent())

    await asyncio.gather(agent_task, db_task)

    end = time.perf_counter()

    print(f"[APP] Done (sync) in {end - start:.2f} seconds.")
