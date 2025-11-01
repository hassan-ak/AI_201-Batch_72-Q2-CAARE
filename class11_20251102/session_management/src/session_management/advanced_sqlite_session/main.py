import asyncio
from agents import Agent, Runner
from agents.extensions.memory import AdvancedSQLiteSession
from config.gemini_client import model


async def main_async() -> None:
    """
    Demonstrates AdvancedSQLiteSession - enhanced SQLite with advanced features.
    
    AdvancedSQLiteSession provides:
    - Conversation branching
    - Usage analytics and tracking
    - Structured queries
    - Enhanced session management
    """
    # Create agent
    agent = Agent(
        name="AdvancedSQLiteAgent",
        instructions="You are a helpful assistant. Be concise and remember our conversation.",
        model=model,
    )

    print("=== AdvancedSQLiteSession Demo ===\n")
    print("Advanced features: branching, analytics, and structured queries.\n")

    # Create advanced session
    session = AdvancedSQLiteSession(
        session_id="user_123",
        db_path="advanced_sessions.db",
        create_tables=True,
    )

    # Basic conversation
    print("--- Basic Conversation ---")
    print("Turn 1:")
    result1 = await Runner.run(
        agent,
        "What city is the Golden Gate Bridge in?",
        session=session,
    )
    print(f"Agent: {result1.final_output}\n")

    print("Turn 2:")
    result2 = await Runner.run(
        agent,
        "What state is it in?",
        session=session,
    )
    print(f"Agent: {result2.final_output}\n")

    # Store usage analytics
    print("--- Usage Analytics ---")
    await session.store_run_usage(result1)
    await session.store_run_usage(result2)
    print("✅ Stored usage data for both runs\n")

    # Get usage statistics
    stats = await session.get_usage_stats()
    print(f"📊 Usage Statistics:")
    print(f"   Total runs: {stats.get('total_runs', 0)}")
    print(f"   Total tokens: {stats.get('total_tokens', 0)}")
    print()

    # Conversation branching
    print("--- Conversation Branching ---")
    print("Creating a branch from turn 2...")
    
    branch_id = await session.create_branch_from_turn(2)
    print(f"✅ Created branch with ID: {branch_id}\n")

    # Continue on branch
    print("Continuing conversation on branch:")
    branch_session = AdvancedSQLiteSession(
        session_id=branch_id,
        db_path="advanced_sessions.db",
        create_tables=True,
    )
    
    result3 = await Runner.run(
        agent,
        "What's the population of that state?",
        session=branch_session,
    )
    print(f"Agent: {result3.final_output}\n")

    # Get conversation history with metadata
    print("--- Structured Queries ---")
    items = await session.get_items()
    print(f"📝 Conversation has {len(items)} items\n")

    # Get sessions list
    print("--- Session Management ---")
    sessions = await session.list_sessions()
    print(f"📋 Total sessions in database: {len(sessions)}")
    for sess in sessions[:5]:  # Show first 5
        print(f"   - Session ID: {sess['session_id']}")
    print()

    print("=== Demo Complete ===")
    print("\n💡 Advanced Features Available:")
    print("  - Conversation branching")
    print("  - Usage tracking and analytics")
    print("  - Structured queries")
    print("  - Enhanced session management")


def main() -> None:
    """Entry point for AdvancedSQLiteSession demo."""
    asyncio.run(main_async())


if __name__ == "__main__":
    main()

