"""Main FastAPI application entry point."""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fast_api.services.session import SessionService
from fast_api.routes import sessions, messages
from fast_api.models import ErrorResponse, ErrorDetail


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan: startup and shutdown events."""
    # Startup: Initialize database connection pool
    SessionService.initialize()
    yield
    # Shutdown: Dispose of database connection pool
    await SessionService.dispose()


# Create FastAPI app with lifespan events
app = FastAPI(
    title="FastAPI Chatbot API",
    description="REST API for chatbot interactions with session persistence",
    version="0.1.0",
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(sessions.router)
app.include_router(messages.router)


# Global exception handlers
@app.exception_handler(status.HTTP_404_NOT_FOUND)
async def not_found_handler(request: Request, exc: Exception):
    """Handle 404 Not Found errors."""
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=ErrorResponse(
            success=False,
            error=ErrorDetail(
                code="NOT_FOUND",
                message="Resource not found",
            ),
        ).model_dump(),
    )


@app.exception_handler(status.HTTP_400_BAD_REQUEST)
async def bad_request_handler(request: Request, exc: Exception):
    """Handle 400 Bad Request errors."""
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=ErrorResponse(
            success=False,
            error=ErrorDetail(
                code="BAD_REQUEST",
                message=str(exc) if str(exc) else "Invalid request",
            ),
        ).model_dump(),
    )


@app.exception_handler(status.HTTP_500_INTERNAL_SERVER_ERROR)
async def internal_server_error_handler(request: Request, exc: Exception):
    """Handle 500 Internal Server Error."""
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=ErrorResponse(
            success=False,
            error=ErrorDetail(
                code="INTERNAL_SERVER_ERROR",
                message="An internal server error occurred",
            ),
        ).model_dump(),
    )


@app.get("/", tags=["health"])
async def root():
    """Root endpoint - returns API status (unprotected)."""
    return {"status": "ok", "message": "FastAPI Chatbot API is running"}


@app.get("/health", tags=["health"])
async def health():
    """Health check endpoint (unprotected)."""
    return {"status": "healthy"}

