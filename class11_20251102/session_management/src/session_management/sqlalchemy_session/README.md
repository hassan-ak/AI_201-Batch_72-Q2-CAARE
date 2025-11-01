# SQLAlchemySession - Production-Ready Session Storage

SQLAlchemySession provides production-ready session storage using SQLAlchemy, supporting PostgreSQL, MySQL, SQLite, and other databases. Perfect for scalable, multi-user applications.

## 📚 Reference Documentation

- [OpenAI Agents SDK - SQLAlchemy Sessions](https://openai.github.io/openai-agents-python/sessions/sqlalchemy_session/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

## 🎯 Benefits

### ✅ **Production-Ready**

- Battle-tested with production databases
- Supports connection pooling
- Handles concurrent access safely
- Transaction management

### ✅ **Database Flexibility**

- **PostgreSQL**: Full-featured, recommended for production
- **MySQL**: Widely used in web applications
- **SQLite**: Good for development/testing
- **Any SQLAlchemy-supported database**

### ✅ **Scalability**

- Supports high-traffic applications
- Connection pooling for efficiency
- Can handle thousands of concurrent sessions
- Designed for distributed systems

### ✅ **Integration**

- Works with existing SQLAlchemy setups
- Easy to integrate with Django, Flask, FastAPI
- Can share database with other application data

## 🚀 Quick Start

### Installation

First, install the required database driver:

```bash
# For PostgreSQL
uv add asyncpg

# For MySQL
uv add aiomysql

# For SQLite (usually included)
uv add aiosqlite
```

### Basic Usage

```python
from agents import Agent, Runner
from agents.extensions.memory import SQLAlchemySession

# Using database URL
session = SQLAlchemySession.from_url(
    "user_123",
    url="postgresql+asyncpg://user:pass@localhost/db",
    create_tables=True
)

# Using existing engine
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine("postgresql+asyncpg://user:pass@localhost/db")
session = SQLAlchemySession(
    "user_123",
    engine=engine,
    create_tables=True
)

# Use with agent
agent = Agent(name="Assistant")
result = await Runner.run(agent, "Hello", session=session)
```

## 📖 Usage Examples

### Example 1: PostgreSQL (Production)

```python
import asyncio
from agents import Agent, Runner
from agents.extensions.memory import SQLAlchemySession

async def main():
    # PostgreSQL connection
    session = SQLAlchemySession.from_url(
        "user_123",
        url="postgresql+asyncpg://user:password@localhost/myapp",
        create_tables=True
    )

    agent = Agent(name="Assistant")
    result = await Runner.run(agent, "Hello", session=session)
    print(result.final_output)

asyncio.run(main())
```

### Example 2: MySQL

```python
session = SQLAlchemySession.from_url(
    "user_123",
    url="mysql+aiomysql://user:password@localhost/myapp",
    create_tables=True
)
```

### Example 3: SQLite (Development)

```python
# File-based SQLite
session = SQLAlchemySession.from_url(
    "user_123",
    url="sqlite+aiosqlite:///sessions.db",
    create_tables=True
)

# In-memory SQLite (testing)
session = SQLAlchemySession.from_url(
    "user_123",
    url="sqlite+aiosqlite:///:memory:",
    create_tables=True
)
```

### Example 4: Using Existing Engine

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from agents.extensions.memory import SQLAlchemySession

# Create engine (can be shared across application)
engine = create_async_engine(
    "postgresql+asyncpg://user:pass@localhost/db",
    pool_size=10,
    max_overflow=20
)

# Use with SQLAlchemySession
session = SQLAlchemySession(
    "user_123",
    engine=engine,
    create_tables=True
)

# Clean up when done
await engine.dispose()
```

## 🔧 API Reference

### `SQLAlchemySession.from_url()`

Create a session using a database URL:

```python
SQLAlchemySession.from_url(
    session_id: str,                    # Unique session identifier
    url: str,                           # SQLAlchemy database URL
    create_tables: bool = True          # Whether to create tables automatically
) -> SQLAlchemySession
```

**Database URL Format:**

- PostgreSQL: `postgresql+asyncpg://user:password@host:port/database`
- MySQL: `mysql+aiomysql://user:password@host:port/database`
- SQLite: `sqlite+aiosqlite:///path/to/file.db`
- SQLite (memory): `sqlite+aiosqlite:///:memory:`

### `SQLAlchemySession()`

Create a session using an existing engine:

```python
SQLAlchemySession(
    session_id: str,                    # Unique session identifier
    engine: AsyncEngine,                # SQLAlchemy async engine
    create_tables: bool = True          # Whether to create tables automatically
) -> SQLAlchemySession
```

## 🗄️ Database Setup

### PostgreSQL Setup

1. **Install PostgreSQL** (if not already installed)

2. **Create database:**

```sql
CREATE DATABASE myapp_sessions;
```

3. **Install Python driver:**

```bash
uv add asyncpg
```

4. **Use in code:**

```python
session = SQLAlchemySession.from_url(
    "user_123",
    url="postgresql+asyncpg://user:pass@localhost/myapp_sessions",
    create_tables=True
)
```

### MySQL Setup

1. **Install MySQL** (if not already installed)

2. **Create database:**

```sql
CREATE DATABASE myapp_sessions;
```

3. **Install Python driver:**

```bash
uv add aiomysql
```

4. **Use in code:**

```python
session = SQLAlchemySession.from_url(
    "user_123",
    url="mysql+aiomysql://user:pass@localhost/myapp_sessions",
    create_tables=True
)
```

## 📊 When to Use SQLAlchemySession

### ✅ **Use SQLAlchemySession when:**

- Building production applications
- You need PostgreSQL, MySQL, or other production databases
- Handling multiple concurrent users
- Integrating with existing SQLAlchemy setups
- You need connection pooling
- Building scalable, distributed systems

### ❌ **Consider SQLiteSession when:**

- Building simple applications
- You only need local file storage
- Prototyping quickly
- Single-user applications

## 💡 Best Practices

### 1. Connection Pooling

Configure appropriate pool settings:

```python
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine(
    "postgresql+asyncpg://user:pass@localhost/db",
    pool_size=10,        # Base pool size
    max_overflow=20,     # Maximum overflow connections
    pool_pre_ping=True  # Verify connections before using
)
```

### 2. Environment Variables

Store database credentials securely:

```python
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
session = SQLAlchemySession.from_url(
    "user_123",
    url=DATABASE_URL,
    create_tables=True
)
```

### 3. Error Handling

Handle connection errors gracefully:

```python
import asyncio
from sqlalchemy.exc import SQLAlchemyError

async def safe_run():
    try:
        session = SQLAlchemySession.from_url(
            "user_123",
            url=DATABASE_URL,
            create_tables=True
        )
        result = await Runner.run(agent, "Hello", session=session)
        return result
    except SQLAlchemyError as e:
        print(f"Database error: {e}")
        # Handle error appropriately
```

### 4. Cleanup

Properly dispose of engines:

```python
async def main():
    engine = create_async_engine(DATABASE_URL)
    try:
        session = SQLAlchemySession("user_123", engine=engine)
        # Use session...
    finally:
        await engine.dispose()
```

## 🔍 Complete Example

See `main.py` for a complete working example demonstrating SQLAlchemySession usage.

## 🚀 Running the Example

```bash
# From the project root
uv run python -m session_management.02_sqlalchemy_session.main
```

**Note:** Make sure you have the required database driver installed:

- For SQLite: `uv add aiosqlite`
- For PostgreSQL: `uv add asyncpg`
- For MySQL: `uv add aiomysql`

## 📝 Comparison with Other Session Types

| Feature            | SQLAlchemySession               | SQLiteSession  | AdvancedSQLiteSession |
| ------------------ | ------------------------------- | -------------- | --------------------- |
| Database Support   | PostgreSQL, MySQL, SQLite, etc. | SQLite only    | SQLite only           |
| Production Ready   | ✅ Yes                          | ⚠️ Limited     | ⚠️ Limited            |
| Scalability        | ✅ Excellent                    | ⚠️ Single-file | ⚠️ Single-file        |
| Connection Pooling | ✅ Yes                          | ❌ No          | ❌ No                 |
| Multi-user         | ✅ Yes                          | ⚠️ Limited     | ⚠️ Limited            |
| Setup Complexity   | ⭐⭐⭐                          | ⭐             | ⭐⭐                  |

## ⚠️ Important Notes

1. **Async Operations**: SQLAlchemySession requires async/await. Use `await Runner.run()` instead of `Runner.run_sync()`.

2. **Database Drivers**: You must install the appropriate async driver for your database:

   - PostgreSQL: `asyncpg`
   - MySQL: `aiomysql`
   - SQLite: `aiosqlite`

3. **Connection Strings**: Use async SQLAlchemy drivers in the connection string (e.g., `postgresql+asyncpg://` not `postgresql://`).

4. **Table Creation**: Set `create_tables=True` on first use to automatically create required tables.

## 🔗 Related Session Types

- **[SQLiteSession](../01_sqlite_session/README.md)** - Simple local storage
- **[AdvancedSQLiteSession](../03_advanced_sqlite_session/README.md)** - Enhanced features
- **[EncryptedSession](../04_encrypted_session/README.md)** - Secure storage
