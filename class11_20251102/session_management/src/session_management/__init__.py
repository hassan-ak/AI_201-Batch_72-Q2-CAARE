from agents import Agent, Runner, SQLiteSession
from config.gemini_client import model


def main() -> None:
    """
    Demonstrates session memory in OpenAI Agents SDK.
    
    Sessions automatically maintain conversation history across multiple runs,
    allowing agents to remember context from previous interactions.
    """
    # Create agent
    agent = Agent(
        name="SessionAgent",
        instructions="You are a helpful assistant. Be concise and remember our conversation.",
        model=model,
    )

    # Create a persistent session (conversation history saved to file)
    # Use: SQLiteSession("session_id", "db_file.db") for persistence
    # Or: SQLiteSession("session_id") for temporary memory
    session = SQLiteSession("conversation_123", "conversation_history.db")

    print("=== Session Memory Demo ===")
    print("The agent will automatically remember previous messages.\n")

    # First turn - agent learns information
    print("Turn 1:")
    print("User: What city is the Golden Gate Bridge in?")
    result1 = Runner.run_sync(
        agent,
        "What city is the Golden Gate Bridge in?",
        session=session,
    )
    print(f"Agent: {result1.final_output}\n")

    # Second turn - agent remembers previous context
    print("Turn 2:")
    print("User: What state is it in?")
    result2 = Runner.run_sync(
        agent,
        "What state is it in?",
        session=session,
    )
    print(f"Agent: {result2.final_output}\n")

    # Third turn - continues the conversation
    print("Turn 3:")
    print("User: What's the population of that state?")
    result3 = Runner.run_sync(
        agent,
        "What's the population of that state?",
        session=session,
    )
    print(f"Agent: {result3.final_output}\n")

    print("=== Demo Complete ===")
    print("Notice how the agent remembered the context from previous turns!")
    print("The conversation history is automatically stored in 'conversation_history.db'")


if __name__ == "__main__":
    main()