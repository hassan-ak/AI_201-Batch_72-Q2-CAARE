# Task List: FastAPI Chatbot API Implementation

Based on PRD: `prd-fastapi-chatbot.md`

## Relevant Files

- `class11_20251102/fast-api/pyproject.toml` - Project configuration file, needs FastAPI dependencies added
- `class11_20251102/fast-api/src/fast_api/__init__.py` - Package initialization, currently has placeholder main function
- `class11_20251102/fast-api/src/fast_api/main.py` - **NEW** Main FastAPI application entry point
- `class11_20251102/fast-api/src/fast_api/models.py` - **NEW** Pydantic models for request/response validation
- `class11_20251102/fast-api/src/fast_api/dependencies.py` - **NEW** API key authentication dependency functions
- `class11_20251102/fast-api/src/fast_api/routes/__init__.py` - **NEW** Routes package initialization
- `class11_20251102/fast-api/src/fast_api/routes/sessions.py` - **NEW** Session management endpoints (create, get, list sessions)
- `class11_20251102/fast-api/src/fast_api/routes/messages.py` - **NEW** Message endpoints (send message, get conversation history)
- `class11_20251102/fast-api/src/fast_api/services/__init__.py` - **NEW** Services package initialization
- `class11_20251102/fast-api/src/fast_api/services/agent.py` - **NEW** AI agent configuration and execution service
- `class11_20251102/fast-api/src/fast_api/services/session.py` - **NEW** Session management service (create, retrieve sessions)
- `class11_20251102/fast-api/src/config/__init__.py` - Configuration module, needs DATABASE_URL and API_KEY added to Config class
- `class11_20251102/fast-api/src/config/gemini_client.py` - Gemini model setup, already exists and can be reused
- `class11_20251102/fast-api/.env.example` - **NEW** Example environment variables file for documentation
- `class11_20251102/fast-api/README.md` - Project README, needs to be updated with API documentation and usage instructions

### Notes

- The existing `config` directory structure and `gemini_client.py` pattern can be reused from the current codebase
- All endpoint handlers must be async functions due to SQLAlchemySession and Agent execution requirements
- Follow existing patterns from `session_class` example for SQLAlchemySession usage
- Use FastAPI's dependency injection system (`Depends`) for API key authentication
- FastAPI automatically generates OpenAPI docs, but we should add descriptions and examples to improve them

## Tasks

- [x] 1.0 Project Setup & Dependencies

  - [x] 1.1 Add FastAPI and required dependencies to `pyproject.toml` (fastapi, uvicorn[standard], asyncpg or aiomysql, python-dotenv if not already present, openai-agents[sqlalchemy] if not already present)
  - [x] 1.2 Create project directory structure (`routes/` and `services/` subdirectories in `src/fast_api/`)
  - [x] 1.3 Create `__init__.py` files for `routes/` and `services/` packages
  - [x] 1.4 Create `.env.example` file with required environment variables template (GEMINI_API_KEY, GEMINI_API_URL, GEMINI_API_MODEL, DATABASE_URL, API_KEY)
  - [x] 1.5 Run `uv sync` to install dependencies and verify installation

- [x] 2.0 Configuration & Infrastructure Setup

  - [x] 2.1 Update `src/config/__init__.py` to add `DATABASE_URL` and `API_KEY` to required environment variables list and Config dataclass
  - [x] 2.2 Create `src/fast_api/services/session.py` with SessionService class for managing SQLAlchemySession instances
  - [x] 2.3 Implement database connection pool management (SQLAlchemy async engine) in session service with connection lifecycle methods
  - [x] 2.4 Create `src/fast_api/services/agent.py` with AgentService class for configuring and executing AI agents
  - [x] 2.5 Implement agent initialization using gemini_client model pattern (reuse existing `config/gemini_client.py`)
  - [x] 2.6 Set up FastAPI lifespan events in main app for database connection pool initialization on startup and cleanup on shutdown

- [x] 3.0 Authentication & Security Implementation

  - [x] 3.1 Create `src/fast_api/dependencies.py` with API key validation dependency function
  - [x] 3.2 Implement API key extraction from HTTP header (support `X-API-Key` header or `Authorization: Bearer <key>` format)
  - [x] 3.3 Add API key validation logic comparing against `Config.API_KEY` environment variable
  - [x] 3.4 Implement HTTPException for 401 Unauthorized when API key is missing or invalid
  - [x] 3.5 Create reusable dependency function using FastAPI's `Depends` that can be added to protected route decorators

- [x] 4.0 Core API Endpoints Implementation

  - [x] 4.1 Create `src/fast_api/models.py` with Pydantic models (CreateSessionRequest, SendMessageRequest, SessionResponse, MessageResponse, ErrorResponse, and standard SuccessResponse wrapper)
  - [x] 4.2 Create `src/fast_api/routes/sessions.py` with session-related endpoints
  - [x] 4.3 Implement `POST /sessions` endpoint (create new session, generate UUID session_id, return session response)
  - [x] 4.4 Implement `GET /sessions/{session_id}` endpoint (retrieve session metadata, return 404 if not found)
  - [x] 4.5 Implement `GET /sessions` endpoint (list all sessions, optional query parameters for filtering)
  - [x] 4.6 Create `src/fast_api/routes/messages.py` with message-related endpoints
  - [x] 4.7 Implement `POST /sessions/{session_id}/messages` endpoint (accept message, get or create session, run agent, return response)
  - [x] 4.8 Implement `GET /sessions/{session_id}/messages` endpoint (retrieve conversation history, return messages in chronological order)
  - [x] 4.9 Create `src/fast_api/main.py` with FastAPI app initialization
  - [x] 4.10 Include routers from `routes/sessions.py` and `routes/messages.py` into main app
  - [x] 4.11 Implement `GET /health` or `GET /` health check endpoint (unprotected, returns API status)
  - [x] 4.12 Add API key authentication dependency to all protected endpoints (sessions and messages endpoints, excluding health check)

- [x] 5.0 Error Handling, Response Formatting & Documentation
  - [x] 5.1 Implement standardized response wrapper format in models (success, data, message fields for success; success, error fields for errors)
  - [x] 5.2 Create global exception handlers for common error scenarios (404, 400, 500, etc.)
  - [x] 5.3 Ensure all endpoints return consistent JSON response format using response models
  - [x] 5.4 Add CORS middleware configuration if cross-origin requests are needed (allow appropriate origins, methods, headers)
  - [x] 5.5 Add descriptive docstrings and summary/description parameters to all endpoint decorators for better OpenAPI documentation
  - [x] 5.6 Add response_model parameters to route decorators to ensure schemas appear in /docs
  - [x] 5.7 Test OpenAPI documentation at `/docs` endpoint to verify all endpoints, schemas, and examples are displayed correctly
  - [x] 5.8 Update `README.md` with API documentation, endpoint descriptions, authentication instructions, and usage examples
