"""Agent service for configuring and executing AI agents."""

from agents import Agent, Runner
from agents.extensions.memory import SQLAlchemySession
from config.gemini_client import model


class AgentService:
    """Service for managing AI agent configuration and execution."""
    
    _agent: Agent | None = None
    
    @classmethod
    def get_agent(cls) -> Agent:
        """
        Get or create the AI agent instance.
        
        Returns:
            Configured Agent instance
        """
        if cls._agent is None:
            cls._agent = Agent(
                name="ChatbotAssistant",
                instructions="You are a helpful assistant. Be concise, friendly, and remember our conversation context.",
                model=model,
            )
        return cls._agent
    
    @classmethod
    async def run_agent(
        cls,
        message: str,
        session: SQLAlchemySession,
    ) -> str:
        """
        Run the agent with a message and session.
        
        Args:
            message: User message to send to the agent
            session: SQLAlchemySession for conversation history
            
        Returns:
            Agent's response as a string
        """
        agent = cls.get_agent()
        result = await Runner.run(
            agent,
            message,
            session=session,
        )
        return result.final_output

