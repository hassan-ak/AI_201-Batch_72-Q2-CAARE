"""Message endpoints for chatbot interactions."""

from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from fast_api.dependencies import verify_api_key
from fast_api.models import (
    SendMessageRequest,
    MessageResponse,
    MessageItem,
    SuccessResponse,
)
from fast_api.services.session import SessionService
from fast_api.services.agent import AgentService

router = APIRouter(prefix="/sessions/{session_id}/messages", tags=["messages"])


@router.post(
    "",
    response_model=SuccessResponse,
    status_code=status.HTTP_200_OK,
    summary="Send a message to the agent",
    description="Sends a message to the AI agent within a session. The agent will respond using the conversation history from the session.",
)
async def send_message(
    session_id: str,
    request: SendMessageRequest,
    api_key: str = Depends(verify_api_key),
) -> SuccessResponse:
    """
    Send a message to the agent in a session.
    
    Args:
        session_id: Session identifier
        request: Message request with message text
        api_key: Validated API key (from dependency)
        
    Returns:
        SuccessResponse with agent's response
        
    Raises:
        HTTPException: 500 if agent execution fails
    """
    try:
        # Get or create session
        session = SessionService.get_or_create_session(session_id)
        
        # Run agent with message
        agent_response = await AgentService.run_agent(
            message=request.message,
            session=session,
        )
        
        # Create response
        message_response = MessageResponse(
            message=agent_response,
            session_id=session_id,
            timestamp=datetime.now(),
        )
        
        return SuccessResponse(
            success=True,
            data=message_response.model_dump(),
            message="Message processed successfully",
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing message: {str(e)}",
        )


@router.get(
    "",
    response_model=SuccessResponse,
    summary="Get conversation history",
    description="Retrieves all messages in the conversation history for a session, returned in chronological order.",
)
async def get_messages(
    session_id: str,
    api_key: str = Depends(verify_api_key),
) -> SuccessResponse:
    """
    Get conversation history for a session.
    
    Args:
        session_id: Session identifier
        api_key: Validated API key (from dependency)
        
    Returns:
        SuccessResponse with list of messages in chronological order
        
    Raises:
        HTTPException: 404 if session not found
    """
    try:
        # Get or create session
        session = SessionService.get_or_create_session(session_id)
        
        # Get all items from session
        items = await session.get_items()
        
        # Convert to MessageItem format
        messages = [
            MessageItem(
                role=item.get("role", "unknown"),
                content=item.get("content", ""),
            ).model_dump()
            for item in items
        ]
        
        return SuccessResponse(
            success=True,
            data={"messages": messages, "session_id": session_id, "count": len(messages)},
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Session not found or error retrieving messages: {str(e)}",
        )

