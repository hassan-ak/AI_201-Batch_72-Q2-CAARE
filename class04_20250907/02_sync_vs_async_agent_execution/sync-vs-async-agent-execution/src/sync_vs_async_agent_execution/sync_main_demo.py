from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_tracing_disabled,
    set_default_openai_client,
    OpenAIChatCompletionsModel,
)
import time

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


def get_user_details():
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()
    return {"name": name, "email": email}


def log_user_to_db(user):
    print("[DB] Starting sync user log...")
    time.sleep(2.0)
    print(f"[DB] Logged user (sync): {user}")


def sync_main_demo():
    user = get_user_details()

    print("\n[APP] Sync flow starting (sequential)...")
    start = time.perf_counter()

    log_user_to_db(user)

    result = Runner.run_sync(agent, "What is the capital of France?")

    end = time.perf_counter()

    print(f"[AGENT] {result.final_output}")
    print(f"[APP] Done (sync) in {end - start:.2f} seconds.")
