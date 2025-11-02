import asyncio
from config import Config
from agents import Agent, Runner,SQLiteSession
from config.gemini_client import gemini_llm_model

async def my_session_demo() -> None:
    session = SQLiteSession("conversation_123_2", "conversation_history.db")
    print("=== Session Memory Demo ===")
    assistant_agent = Agent(
    name="Assistant",
    instructions="Reply very concisely.",
    model=gemini_llm_model,
   )
    result = await Runner.run(
        assistant_agent,
        "What is the capital of Pakistan?",
        session=session,
    )
    print(f"Assistant: {result.final_output}")
    result = await Runner.run(
        assistant_agent,
        "What is the population?",
        session=session,
    )
    print(f"Assistant: {result.final_output}")
    # Get all items in a session
    items = await session.get_items()
    print(f"Items: {items}")
# Add new items to a session
    new_items = [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi there!"}
    ]
    await session.add_items(new_items)
    items = await session.get_items()
    print(f"Items2: {items}")

# Remove and return the most recent item
    last_item = await session.pop_item()
    print(f"Last item: {last_item}")  # {"role": "assistant", "content": "Hi there!"}

# Clear all items from a session
    await session.clear_session()

def main() -> None:
    asyncio.run(my_session_demo())

# if __name__ == "__main__":
#     main()