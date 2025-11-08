# FastAPI Chatbot API

A production-ready REST API for chatbot interactions with session persistence, built with FastAPI and OpenAI Agents SDK.

## Features

- 🤖 **AI Agent Integration**: Powered by Gemini models via OpenAI Agents SDK
- 💾 **Session Persistence**: Automatic conversation history management using SQLAlchemySession
- 🔐 **API Key Authentication**: Secure API access with API key validation
- 📊 **PostgreSQL/MySQL Support**: Production-ready database integration
- 📝 **Auto-generated Documentation**: OpenAPI/Swagger docs at `/docs`
- ✅ **Standardized Responses**: Consistent JSON response format
- 🌐 **CORS Support**: Cross-origin requests enabled

## Quick Start

### Prerequisites

- Python 3.11+
- UV package manager
- PostgreSQL or MySQL database (or SQLite for development)

### Installation

1. **Clone and navigate to the project:**
   ```bash
   cd class11_20251102/fast-api
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your actual values
   ```

4. **Required environment variables:**
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   GEMINI_API_URL=https://generativelanguage.googleapis.com/v1beta/openai/
   GEMINI_API_MODEL=gemini-2.5-flash
   DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/chatbot_db
   API_KEY=your_api_key_here
   ```

5. **Run the server:**
   ```bash
   uv run uvicorn fast_api.main:app --reload
   ```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Authentication

All protected endpoints require API key authentication. You can provide the API key in two ways:

1. **X-API-Key header:**
   ```bash
   curl -H "X-API-Key: your_api_key" http://localhost:8000/sessions
   ```

2. **Authorization Bearer token:**
   ```bash
   curl -H "Authorization: Bearer your_api_key" http://localhost:8000/sessions
   ```

## API Endpoints

### Health Check (Unprotected)

#### `GET /`
Returns API status.

**Response:**
```json
{
  "status": "ok",
  "message": "FastAPI Chatbot API is running"
}
```

#### `GET /health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

### Session Management

#### `POST /sessions`
Create a new conversation session.

**Request Body:**
```json
{
  "user_id": "user_123",
  "session_name": "Customer Support Chat"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "session_id": "550e8400-e29b-41d4-a716-446655440000",
    "created_at": "2025-11-02T13:00:00",
    "message_count": 0,
    "user_id": "user_123",
    "session_name": "Customer Support Chat"
  },
  "message": "Session created successfully"
}
```

#### `GET /sessions/{session_id}`
Get session information.

**Response:**
```json
{
  "success": true,
  "data": {
    "session_id": "550e8400-e29b-41d4-a716-446655440000",
    "created_at": "2025-11-02T13:00:00",
    "message_count": 5
  }
}
```

#### `GET /sessions`
List all sessions (simplified implementation).

**Response:**
```json
{
  "success": true,
  "data": {
    "sessions": [],
    "message": "Session listing requires additional implementation"
  }
}
```

### Messages

#### `POST /sessions/{session_id}/messages`
Send a message to the agent.

**Request Body:**
```json
{
  "message": "Hello, how can you help me?"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "message": "Hello! I'm here to help. What would you like to know?",
    "session_id": "550e8400-e29b-41d4-a716-446655440000",
    "timestamp": "2025-11-02T13:05:00"
  },
  "message": "Message processed successfully"
}
```

#### `GET /sessions/{session_id}/messages`
Get conversation history.

**Response:**
```json
{
  "success": true,
  "data": {
    "messages": [
      {
        "role": "user",
        "content": "Hello, how can you help me?"
      },
      {
        "role": "assistant",
        "content": "Hello! I'm here to help. What would you like to know?"
      }
    ],
    "session_id": "550e8400-e29b-41d4-a716-446655440000",
    "count": 2
  }
}
```

## Error Responses

All errors follow a standardized format:

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message"
  }
}
```

### Common Error Codes

- `NOT_FOUND` (404): Resource not found
- `BAD_REQUEST` (400): Invalid request
- `UNAUTHORIZED` (401): Invalid or missing API key
- `INTERNAL_SERVER_ERROR` (500): Server error

## Example Usage

### Using cURL

```bash
# Create a session
SESSION_ID=$(curl -X POST http://localhost:8000/sessions \
  -H "X-API-Key: your_api_key" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "user_123"}' \
  | jq -r '.data.session_id')

# Send a message
curl -X POST "http://localhost:8000/sessions/$SESSION_ID/messages" \
  -H "X-API-Key: your_api_key" \
  -H "Content-Type: application/json" \
  -d '{"message": "What is the capital of France?"}'

# Get conversation history
curl "http://localhost:8000/sessions/$SESSION_ID/messages" \
  -H "X-API-Key: your_api_key"
```

### Using Python

```python
import requests

API_BASE = "http://localhost:8000"
API_KEY = "your_api_key"
headers = {"X-API-Key": API_KEY}

# Create session
response = requests.post(
    f"{API_BASE}/sessions",
    headers=headers,
    json={"user_id": "user_123"}
)
session_id = response.json()["data"]["session_id"]

# Send message
response = requests.post(
    f"{API_BASE}/sessions/{session_id}/messages",
    headers=headers,
    json={"message": "Hello!"}
)
print(response.json()["data"]["message"])

# Get history
response = requests.get(
    f"{API_BASE}/sessions/{session_id}/messages",
    headers=headers
)
print(response.json()["data"]["messages"])
```

## Project Structure

```
fast-api/
├── src/
│   ├── fast_api/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI app initialization
│   │   ├── models.py            # Pydantic models
│   │   ├── dependencies.py     # API key authentication
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── sessions.py      # Session endpoints
│   │   │   └── messages.py      # Message endpoints
│   │   └── services/
│   │       ├── __init__.py
│   │       ├── agent.py         # Agent configuration and execution
│   │       └── session.py       # Session management logic
│   └── config/
│       ├── __init__.py          # Configuration loading
│       └── gemini_client.py     # Gemini model setup
├── pyproject.toml
├── README.md
└── .env.example
```

## Development

### Running in Development Mode

```bash
uv run uvicorn fast_api.main:app --reload
```

### Running in Production

```bash
uv run uvicorn fast_api.main:app --host 0.0.0.0 --port 8000
```

## Database Configuration

The API uses SQLAlchemySession which supports:

- **PostgreSQL**: `postgresql+asyncpg://user:pass@host:port/dbname`
- **MySQL**: `mysql+aiomysql://user:pass@host:port/dbname`
- **SQLite**: `sqlite+aiosqlite:///path/to/file.db` (for development)

Tables are automatically created on first use (`create_tables=True`).

## Security Notes

- **API Key**: Store your API key securely. Never commit it to version control.
- **CORS**: In production, restrict `allow_origins` to specific domains.
- **Database**: Use strong passwords and SSL connections for production databases.

## License

This project is part of the AI_201-Batch_72-Q2-CAARE-1 course materials.

