import asyncio
from agents import Agent, Runner
from agents.extensions.memory import SQLAlchemySession
from sqlalchemy.ext.asyncio import create_async_engine
from config import Config
from config.gemini_client import model


async def main_async() -> None:
    """
    Demonstrates SQLAlchemySession - production-ready session implementation.
    
    SQLAlchemySession is perfect for:
    - Production applications
    - Multi-user systems
    - Scalable databases (PostgreSQL, MySQL, etc.)
    - Integration with existing databases
    """
    # Create agent
    agent = Agent(
        name="SQLAlchemyAgent",
        instructions="You are a helpful assistant. Be concise and remember our conversation.",
        model=model,
    )

    print("=== SQLAlchemySession Demo ===\n")
    print("SQLAlchemySession provides production-ready session storage.\n")

    # Example 1: Using SQLite with SQLAlchemy (for development/testing)
    print("--- Example 1: SQLite with SQLAlchemy (Development) ---")
    
    sqlite_session = SQLAlchemySession.from_url(
        "user_123",
        url="sqlite+aiosqlite:///sqlalchemy_sessions.db",
        create_tables=True,
    )

    print("Turn 1:")
    result1 = await Runner.run(
        agent,
        "What city is the Golden Gate Bridge in?",
        session=sqlite_session,
    )
    print(f"Agent: {result1.final_output}\n")

    print("Turn 2:")
    result2 = await Runner.run(
        agent,
        "What state is it in?",
        session=sqlite_session,
    )
    print(f"Agent: {result2.final_output}\n")

    # Example 2: Using in-memory SQLite (for testing)
    print("--- Example 2: In-Memory SQLite (Testing) ---")
    
    memory_session = SQLAlchemySession.from_url(
        "test_user",
        url="sqlite+aiosqlite:///:memory:",
        create_tables=True,
    )

    result3 = await Runner.run(
        agent,
        "Remember: I love Python programming",
        session=memory_session,
    )
    print(f"Agent: {result3.final_output}\n")

    # Example 3: Multiple sessions
    print("--- Example 3: Multiple Sessions ---")
    
    user1_session = SQLAlchemySession.from_url(
        "user_001",
        url="sqlite+aiosqlite:///sqlalchemy_sessions.db",
        create_tables=True,
    )
    
    user2_session = SQLAlchemySession.from_url(
        "user_002",
        url="sqlite+aiosqlite:///sqlalchemy_sessions.db",
        create_tables=True,
    )

    result4 = await Runner.run(
        agent,
        "My name is Alice",
        session=user1_session,
    )
    print(f"User 1 - Agent: {result4.final_output}\n")

    result5 = await Runner.run(
        agent,
        "My name is Bob",
        session=user2_session,
    )
    print(f"User 2 - Agent: {result5.final_output}\n")

    # Example 4: PostgreSQL with Neon (Production)
    postgresql_url, connect_args = Config.get_postgresql_async_url()
    if postgresql_url:
        print("--- Example 4: PostgreSQL with Neon (Production) ---")
        
        try:
            # Create engine with SSL connect_args for asyncpg
            if connect_args:
                engine = create_async_engine(
                    postgresql_url,
                    connect_args=connect_args
                )
                postgres_session = SQLAlchemySession(
                    "user_123",
                    engine=engine,
                    create_tables=True,
                )
            else:
                # No special connect args, use from_url
                postgres_session = SQLAlchemySession.from_url(
                    "user_123",
                    url=postgresql_url,
                    create_tables=True,
                )
            
            result6 = await Runner.run(
                agent,
                "What city is the Golden Gate Bridge in?",
                session=postgres_session,
            )
            print(f"Agent: {result6.final_output}\n")
            
            result7 = await Runner.run(
                agent,
                "What state is it in?",
                session=postgres_session,
            )
            print(f"Agent: {result7.final_output}\n")
            
            print("✅ Successfully connected to PostgreSQL (Neon)")
            print(f"✅ Connection URL: {postgresql_url.split('@')[0]}@...\n")
            
            # Clean up engine if we created it
            if connect_args and hasattr(postgres_session, '_engine'):
                await postgres_session._engine.dispose()
        except Exception as e:
            print(f"⚠️  PostgreSQL connection failed: {e}\n")
            print("💡 Make sure:")
            print("   - POSTGRESQL_URL is set in .env")
            print("   - Database is accessible")
            print("   - asyncpg is installed: uv add asyncpg\n")
    else:
        print("--- Example 4: PostgreSQL with Neon (Skipped) ---")
        print("ℹ️  Set POSTGRESQL_URL in .env to enable PostgreSQL example\n")

    print("=== Demo Complete ===")
    


def main() -> None:
    """Entry point for SQLAlchemySession demo."""
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
