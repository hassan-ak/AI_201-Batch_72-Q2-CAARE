# Session Management - Complete Guide

A comprehensive guide to OpenAI Agents SDK session management implementations, demonstrating all session types with practical examples.

## 📚 Overview

This project demonstrates all session types available in the OpenAI Agents SDK, each with their own implementation, use cases, and benefits. Sessions provide automatic conversation history management, eliminating the need to manually handle memory between agent runs.

## 🔗 Reference Documentation

- [OpenAI Agents SDK - Sessions](https://openai.github.io/openai-agents-python/sessions/)
- [SQLAlchemy Sessions](https://openai.github.io/openai-agents-python/sessions/sqlalchemy_session/)
- [Advanced SQLite Sessions](https://openai.github.io/openai-agents-python/sessions/advanced_sqlite_session/)
- [Encrypted Sessions](https://openai.github.io/openai-agents-python/sessions/encrypted_session/)

## 📁 Project Structure

```
session_management/
├── README.md                           # This file
├── pyproject.toml                     # Project configuration
├── src/
│   ├── config/
│   │   ├── __init__.py                # Configuration module
│   │   └── gemini_client.py           # Gemini model setup
│   └── session_management/
│       ├── __init__.py                # Basic example
│       ├── 01_sqlite_session/        # Basic SQLite implementation
│       │   ├── README.md
│       │   └── main.py
│       ├── 02_sqlalchemy_session/     # Production database sessions
│       │   ├── README.md
│       │   └── main.py
│       ├── 03_advanced_sqlite_session/ # Enhanced features
│       │   ├── README.md
│       │   └── main.py
│       └── 04_encrypted_session/      # Encrypted sessions
│           ├── README.md
│           └── main.py
```

## 🚀 Quick Start

### Step 1: Setup Environment

Create a `.env` file with your Gemini API credentials:

```bash
GEMINI_API_KEY=your_api_key_here
GEMINI_API_URL=https://generativelanguage.googleapis.com/v1beta/openai/
GEMINI_API_MODEL=gemini-2.5-flash
```

### Step 2: Install Dependencies

```bash
uv sync
```

### Step 3: Run Examples

```bash
# Basic SQLite session
uv run python -m session_management.01_sqlite_session.main

# SQLAlchemy session (production)
uv run python -m session_management.02_sqlalchemy_session.main

# Advanced SQLite session
uv run python -m session_management.03_advanced_sqlite_session.main

# Encrypted session
uv run python -m session_management.04_encrypted_session.main
```

## 📖 Session Types Overview

### 1. SQLiteSession - Basic Implementation

**Location**: `01_sqlite_session/`

**Best For:**

- Simple applications
- Local storage
- Quick prototypes
- Development and testing

**Benefits:**

- ✅ Simple & lightweight
- ✅ No external dependencies
- ✅ Flexible (in-memory or file-based)
- ✅ Easy to use

**See**: [SQLiteSession README](src/session_management/01_sqlite_session/README.md)

---

### 2. SQLAlchemySession - Production Ready

**Location**: `02_sqlalchemy_session/`

**Best For:**

- Production applications
- Multi-user systems
- Scalable databases (PostgreSQL, MySQL)
- Integration with existing databases

**Benefits:**

- ✅ Production-ready
- ✅ Multiple database support
- ✅ Connection pooling
- ✅ Scalable and concurrent

**See**: [SQLAlchemySession README](src/session_management/02_sqlalchemy_session/README.md)

---

### 3. AdvancedSQLiteSession - Enhanced Features

**Location**: `03_advanced_sqlite_session/`

**Best For:**

- Applications needing conversation branching
- Usage analytics and tracking
- Structured queries on conversations
- Complex session management

**Benefits:**

- ✅ Conversation branching
- ✅ Usage analytics
- ✅ Structured queries
- ✅ Enhanced session management

**See**: [AdvancedSQLiteSession README](src/session_management/03_advanced_sqlite_session/README.md)

---

### 4. EncryptedSession - Secure Storage

**Location**: `04_encrypted_session/`

**Best For:**

- Sensitive or confidential data
- Compliance requirements (HIPAA, GDPR)
- Financial or medical information
- Data requiring expiration

**Benefits:**

- ✅ Transparent encryption (AES-256)
- ✅ TTL-based expiration
- ✅ Works with any session type
- ✅ Security for sensitive data

**See**: [EncryptedSession README](src/session_management/04_encrypted_session/README.md)

---

## 📊 Comparison Matrix

| Feature              | SQLiteSession  | SQLAlchemySession       | AdvancedSQLiteSession | EncryptedSession      |
| -------------------- | -------------- | ----------------------- | --------------------- | --------------------- |
| **Setup Complexity** | ⭐ Simple      | ⭐⭐⭐ Complex          | ⭐⭐ Moderate         | ⭐⭐ Moderate         |
| **Database Support** | SQLite only    | PostgreSQL, MySQL, etc. | SQLite only           | Any underlying        |
| **Production Ready** | ⚠️ Limited     | ✅ Yes                  | ⚠️ Limited            | ✅ Yes                |
| **Scalability**      | ⚠️ Single-file | ✅ Excellent            | ⚠️ Single-file        | Depends on underlying |
| **Encryption**       | ❌ No          | ❌ No                   | ❌ No                 | ✅ AES-256            |
| **TTL Support**      | ❌ No          | ❌ No                   | ❌ No                 | ✅ Yes                |
| **Branching**        | ❌ No          | ❌ No                   | ✅ Yes                | Depends on underlying |
| **Analytics**        | ❌ No          | ❌ No                   | ✅ Yes                | Depends on underlying |
| **Best For**         | Simple apps    | Production              | Advanced features     | Sensitive data        |

## 🎯 Choosing the Right Session Type

### Decision Tree

```
Do you need encryption?
├─ Yes → Use EncryptedSession (wrap any session)
└─ No → Continue below

Do you need production databases (PostgreSQL, MySQL)?
├─ Yes → Use SQLAlchemySession
└─ No → Continue below

Do you need branching or analytics?
├─ Yes → Use AdvancedSQLiteSession
└─ No → Use SQLiteSession (simplest)
```

### Quick Decision Guide

**Use SQLiteSession if:**

- Building a simple application
- Need local file storage
- Prototyping quickly
- Single-user scenario

**Use SQLAlchemySession if:**

- Building production application
- Need PostgreSQL, MySQL, or other databases
- Handling multiple concurrent users
- Integrating with existing database

**Use AdvancedSQLiteSession if:**

- Need conversation branching
- Want usage analytics
- Need structured queries
- Building complex session management

**Use EncryptedSession if:**

- Handling sensitive data
- Compliance requirements
- Need automatic expiration
- Security is priority

## 💡 Common Patterns

### Pattern 1: Simple Chat Application

```python
from agents import Agent, Runner, SQLiteSession

session = SQLiteSession("user_123", "chat.db")
agent = Agent(name="Assistant")
result = Runner.run_sync(agent, "Hello", session=session)
```

### Pattern 2: Production Application

```python
from agents import Agent, Runner
from agents.extensions.memory import SQLAlchemySession

session = SQLAlchemySession.from_url(
    "user_123",
    url="postgresql+asyncpg://user:pass@localhost/db",
    create_tables=True
)
agent = Agent(name="Assistant")
result = await Runner.run(agent, "Hello", session=session)
```

### Pattern 3: Secure Medical Data

```python
from agents import Agent, Runner
from agents.extensions.memory import EncryptedSession, SQLAlchemySession
import os

underlying = SQLAlchemySession.from_url(
    "patient_123",
    url="postgresql+asyncpg://user:pass@localhost/db",
    create_tables=True
)

session = EncryptedSession(
    "patient_123",
    underlying_session=underlying,
    encryption_key=os.getenv("ENCRYPTION_KEY"),
    ttl=3600  # 1 hour
)

agent = Agent(name="MedicalAssistant")
result = await Runner.run(agent, "Sensitive query", session=session)
```

### Pattern 4: Analytics Tracking

```python
from agents import Agent, Runner
from agents.extensions.memory import AdvancedSQLiteSession

session = AdvancedSQLiteSession(
    "user_123",
    "analytics.db",
    create_tables=True
)

agent = Agent(name="Assistant")
result = await Runner.run(agent, "Hello", session=session)
await session.store_run_usage(result)  # Track usage

stats = await session.get_usage_stats()
print(f"Total cost: ${stats['total_cost']:.2f}")
```

## 📋 Session Operations

All session types support these operations:

```python
# Get all items
items = await session.get_items()

# Add items manually
await session.add_items([
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi!"}
])

# Remove last item
last_item = await session.pop_item()

# Clear session
await session.clear_session()
```

## ⚠️ Important Notes

1. **Sync vs Async**: SQLiteSession works with both sync and async. SQLAlchemySession, AdvancedSQLiteSession, and EncryptedSession require async.

2. **Dependencies**:

   - SQLAlchemySession needs database drivers (`asyncpg`, `aiomysql`, `aiosqlite`)
   - EncryptedSession uses `cryptography` (usually included)

3. **Performance**: Encryption adds slight overhead. Consider this for high-throughput applications.

4. **Key Management**: Store encryption keys securely (environment variables, secrets manager).

## 🔧 Development

### Running Individual Examples

```bash
# SQLiteSession
uv run python -m session_management.01_sqlite_session.main

# SQLAlchemySession
uv run python -m session_management.02_sqlalchemy_session.main

# AdvancedSQLiteSession
uv run python -m session_management.03_advanced_sqlite_session.main

# EncryptedSession
uv run python -m session_management.04_encrypted_session.main
```

### Adding New Session Examples

1. Create new folder in `src/session_management/`
2. Add `main.py` with implementation
3. Add `README.md` with documentation
4. Update this README with overview

## 📚 Additional Resources

- [OpenAI Agents SDK Documentation](https://openai.github.io/openai-agents-python/)
- [Session API Reference](https://openai.github.io/openai-agents-python/api-reference/memory/session/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Cryptography Library](https://cryptography.io/)

## 🤝 Contributing

Feel free to extend these examples with:

- Additional use cases
- Integration patterns
- Performance optimizations
- Security best practices
- Error handling examples

---

**Happy Coding! 🚀**
