"""Session management endpoints."""

import uuid
from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from fast_api.dependencies import verify_api_key
from fast_api.models import (
    CreateSessionRequest,
    SessionResponse,
    SuccessResponse,
    ErrorResponse,
    ErrorDetail,
)
from fast_api.services.session import SessionService
from agents.extensions.memory import SQLAlchemySession

router = APIRouter(prefix="/sessions", tags=["sessions"])


@router.post(
    "",
    response_model=SuccessResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new conversation session",
    description="Creates a new conversation session with a unique session ID. The session will be used to maintain conversation history.",
)
async def create_session(
    request: CreateSessionRequest,
    api_key: str = Depends(verify_api_key),
) -> SuccessResponse:
    """
    Create a new conversation session.
    
    Args:
        request: Session creation request with optional metadata
        api_key: Validated API key (from dependency)
        
    Returns:
        SuccessResponse with session information
    """
    # Generate unique session ID
    session_id = str(uuid.uuid4())
    
    # Create session using SessionService
    session = SessionService.get_or_create_session(session_id)
    
    # Get initial items count (should be 0 for new session)
    items = await session.get_items()
    message_count = len(items)
    
    # Create session response
    session_response = SessionResponse(
        session_id=session_id,
        created_at=datetime.now(),
        message_count=message_count,
        user_id=request.user_id,
        session_name=request.session_name,
    )
    
    return SuccessResponse(
        success=True,
        data=session_response.model_dump(),
        message="Session created successfully",
    )


@router.get(
    "/{session_id}",
    response_model=SuccessResponse,
    summary="Get session information",
    description="Retrieves metadata for a specific session, including session ID, creation time, and message count.",
)
async def get_session(
    session_id: str,
    api_key: str = Depends(verify_api_key),
) -> SuccessResponse:
    """
    Get session information by session ID.
    
    Args:
        session_id: Unique session identifier
        api_key: Validated API key (from dependency)
        
    Returns:
        SuccessResponse with session information
        
    Raises:
        HTTPException: 404 if session not found
    """
    try:
        # Get or create session (will create if doesn't exist, but we want to check if it has messages)
        session = SessionService.get_or_create_session(session_id)
        
        # Get session items to determine if session exists and get message count
        items = await session.get_items()
        message_count = len(items)
        
        # If session has no messages, we can't determine when it was created
        # For now, we'll return the session info with current timestamp
        session_response = SessionResponse(
            session_id=session_id,
            created_at=datetime.now(),  # Note: SQLAlchemySession doesn't expose creation time directly
            message_count=message_count,
        )
        
        return SuccessResponse(
            success=True,
            data=session_response.model_dump(),
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Session not found: {str(e)}",
        )


@router.get(
    "",
    response_model=SuccessResponse,
    summary="List all sessions",
    description="Returns a list of all available sessions. Note: This is a simplified implementation. In production, you may want to add pagination and filtering.",
)
async def list_sessions(
    user_id: Optional[str] = Query(None, description="Filter sessions by user ID"),
    api_key: str = Depends(verify_api_key),
) -> SuccessResponse:
    """
    List all sessions (simplified implementation).
    
    Note: SQLAlchemySession doesn't provide a built-in way to list all sessions.
    This is a placeholder implementation. In production, you would need to
    maintain a separate table or use AdvancedSQLiteSession which supports this.
    
    Args:
        user_id: Optional filter by user ID
        api_key: Validated API key (from dependency)
        
    Returns:
        SuccessResponse with list of sessions (empty for now)
    """
    # Note: SQLAlchemySession doesn't have a built-in method to list all sessions
    # This would require maintaining a separate sessions table or using AdvancedSQLiteSession
    # For now, we return an empty list with a note
    return SuccessResponse(
        success=True,
        data={"sessions": [], "message": "Session listing requires additional implementation"},
    )

