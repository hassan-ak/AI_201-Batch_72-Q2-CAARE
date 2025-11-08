"""Pydantic models for request/response validation."""

from datetime import datetime
from typing import Any, Optional
from pydantic import BaseModel, Field


# Request Models
class CreateSessionRequest(BaseModel):
    """Request model for creating a new session."""
    
    user_id: Optional[str] = Field(None, description="Optional user identifier")
    session_name: Optional[str] = Field(None, description="Optional session name for identification")
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "user_123",
                "session_name": "Customer Support Chat"
            }
        }


class SendMessageRequest(BaseModel):
    """Request model for sending a message to the agent."""
    
    message: str = Field(..., description="Message text to send to the agent", min_length=1)
    
    class Config:
        json_schema_extra = {
            "example": {
                "message": "Hello, how can you help me?"
            }
        }


# Response Models
class MessageItem(BaseModel):
    """Individual message in conversation history."""
    
    role: str = Field(..., description="Message role: 'user' or 'assistant'")
    content: str = Field(..., description="Message content")
    timestamp: Optional[datetime] = Field(None, description="Message timestamp")


class SessionResponse(BaseModel):
    """Response model for session information."""
    
    session_id: str = Field(..., description="Unique session identifier")
    created_at: Optional[datetime] = Field(None, description="Session creation timestamp")
    message_count: int = Field(0, description="Number of messages in the session")
    user_id: Optional[str] = Field(None, description="User identifier if provided")
    session_name: Optional[str] = Field(None, description="Session name if provided")


class MessageResponse(BaseModel):
    """Response model for agent message."""
    
    message: str = Field(..., description="Agent's response message")
    session_id: str = Field(..., description="Session identifier")
    timestamp: Optional[datetime] = Field(default_factory=datetime.now, description="Response timestamp")


class ErrorDetail(BaseModel):
    """Error detail model."""
    
    code: str = Field(..., description="Error code")
    message: str = Field(..., description="Human-readable error message")


class ErrorResponse(BaseModel):
    """Standard error response model."""
    
    success: bool = Field(False, description="Always false for error responses")
    error: ErrorDetail = Field(..., description="Error details")


class SuccessResponse(BaseModel):
    """Standard success response wrapper."""
    
    success: bool = Field(True, description="Always true for success responses")
    data: Any = Field(..., description="Response data")
    message: Optional[str] = Field(None, description="Optional success message")
    
    class Config:
        json_schema_extra = {
            "example": {
                "success": True,
                "data": {},
                "message": "Operation completed successfully"
            }
        }

