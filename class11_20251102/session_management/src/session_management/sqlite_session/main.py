from agents import Agent, Runner, SQLiteSession
from config.gemini_client import model


def main() -> None:
    """
    Demonstrates SQLiteSession - the basic session implementation.
    
    SQLiteSession is perfect for:
    - Simple applications
    - Local storage
    - Quick prototypes
    - Development and testing
    """
    # Create agent
    agent = Agent(
        name="SQLiteAgent",
        instructions="You are a helpful assistant. Be concise and remember our conversation.",
        model=model,
    )

    print("=== SQLiteSession Demo ===\n")
    print("SQLiteSession provides lightweight, file-based session storage.\n")

    # Option 1: Temporary session (in-memory, lost when program ends)
    print("--- Temporary Session (In-Memory) ---")
    temp_session = SQLiteSession("temp_conversation")
    
    result1 = Runner.run_sync(
        agent,
        "Remember: my favorite color is blue",
        session=temp_session,
    )
    print(f"Agent: {result1.final_output}\n")

    # Option 2: Persistent session (saved to file)
    print("--- Persistent Session (File-Based) ---")
    persistent_session = SQLiteSession("conversation_123", "sqlite_sessions.db")

    print("Turn 1:")
    print("User: What city is the Golden Gate Bridge in?")
    result2 = Runner.run_sync(
        agent,
        "What city is the Golden Gate Bridge in?",
        session=persistent_session,
    )
    print(f"Agent: {result2.final_output}\n")

    print("Turn 2:")
    print("User: What state is it in?")
    result3 = Runner.run_sync(
        agent,
        "What state is it in?",
        session=persistent_session,
    )
    print(f"Agent: {result3.final_output}\n")

    print("Turn 3:")
    print("User: What's the population of that state?")
    result4 = Runner.run_sync(
        agent,
        "What's the population of that state?",
        session=persistent_session,
    )
    print(f"Agent: {result4.final_output}\n")

    print("=== Demo Complete ===")
    print("The persistent session is saved to 'sqlite_sessions.db'")
    print("Restart the program and the agent will still remember the conversation!")


if __name__ == "__main__":
    main()

