"""Session management service for handling SQLAlchemySession instances."""

from typing import Optional
from agents.extensions.memory import SQLAlchemySession
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker
from config import Config


class SessionService:
    """Service for managing database sessions and SQLAlchemySession instances."""
    
    _engine: Optional[AsyncEngine] = None
    _initialized: bool = False
    
    @classmethod
    def initialize(cls) -> None:
        """Initialize the database connection pool."""
        if cls._initialized:
            return
        
        # Create async engine with connection pooling
        cls._engine = create_async_engine(
            Config.database_url,
            pool_size=10,
            max_overflow=20,
            pool_pre_ping=True,  # Verify connections before using
        )
        cls._initialized = True
    
    @classmethod
    async def dispose(cls) -> None:
        """Dispose of the database connection pool."""
        if cls._engine:
            await cls._engine.dispose()
            cls._engine = None
            cls._initialized = False
    
    @classmethod
    def get_or_create_session(cls, session_id: str) -> SQLAlchemySession:
        """
        Get or create a SQLAlchemySession for the given session_id.
        
        Args:
            session_id: Unique identifier for the session
            
        Returns:
            SQLAlchemySession instance
        """
        if not cls._initialized or not cls._engine:
            raise RuntimeError("SessionService not initialized. Call initialize() first.")
        
        # Create session using the engine
        return SQLAlchemySession(
            session_id=session_id,
            engine=cls._engine,
            create_tables=True,
        )
    
    @classmethod
    def get_engine(cls) -> Optional[AsyncEngine]:
        """Get the database engine instance."""
        return cls._engine

