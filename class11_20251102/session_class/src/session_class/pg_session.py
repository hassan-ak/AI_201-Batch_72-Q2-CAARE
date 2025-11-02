import asyncio
import uuid
from config import Config
from agents import Agent, Runner,SQLiteSession
from config.gemini_client import gemini_llm_model
from agents.extensions.memory import SQLAlchemySession
from sqlalchemy.ext.asyncio import create_async_engine

async def my_session_demo() -> None:
    #sqlite_session = SQLiteSession("conversation_123_2", "conversation_history.db")
     # Create session using database URL

     # Create your database engine
   # engine = create_async_engine(Config.postgresql_url)
    # session = SQLAlchemySession(
    #     "user-456",
    #     engine=engine,
    #     create_tables=True
    # )
    session = SQLAlchemySession.from_url(
        str(uuid.uuid4()),
        url=Config.postgresql_url,
        create_tables=True
    )

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

def main() -> None:
    asyncio.run(my_session_demo())

if __name__ == "__main__":
    main()