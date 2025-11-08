"""Dependencies for FastAPI routes, including authentication."""

from fastapi import Header, HTTPException, status
from config import Config


async def verify_api_key(
    x_api_key: str | None = Header(None, alias="X-API-Key"),
    authorization: str | None = Header(None),
) -> str:
    """
    Verify API key from request headers.
    
    Supports two authentication methods:
    1. X-API-Key header: X-API-Key: <api_key>
    2. Authorization Bearer: Authorization: Bearer <api_key>
    
    Args:
        x_api_key: API key from X-API-Key header
        authorization: Authorization header value
        
    Returns:
        The validated API key
        
    Raises:
        HTTPException: 401 if API key is missing or invalid
    """
    # Try X-API-Key header first
    api_key = x_api_key
    
    # If not found, try Authorization Bearer header
    if not api_key and authorization:
        if authorization.startswith("Bearer "):
            api_key = authorization.replace("Bearer ", "", 1)
    
    # Validate API key
    if not api_key or api_key != Config.api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key. Please provide a valid API key in the X-API-Key header or Authorization Bearer token.",
        )
    
    return api_key

