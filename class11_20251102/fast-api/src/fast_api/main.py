"""Main FastAPI application entry point."""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fast_api.services.session import SessionService
from fast_api.routes import sessions, messages


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

# Include routers
app.include_router(sessions.router)
app.include_router(messages.router)


@app.get("/", tags=["health"])
async def root():
    """Root endpoint - returns API status (unprotected)."""
    return {"status": "ok", "message": "FastAPI Chatbot API is running"}


@app.get("/health", tags=["health"])
async def health():
    """Health check endpoint (unprotected)."""
    return {"status": "healthy"}

