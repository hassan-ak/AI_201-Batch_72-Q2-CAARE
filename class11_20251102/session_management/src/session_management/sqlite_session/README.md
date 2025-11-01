# SQLiteSession - Basic Session Implementation

SQLiteSession is the default, lightweight session implementation using SQLite. It's perfect for simple applications, local storage, and quick prototypes.

## 📚 Reference Documentation

- [OpenAI Agents SDK - Sessions](https://openai.github.io/openai-agents-python/sessions/)
- [SQLiteSession API Reference](https://openai.github.io/openai-agents-python/api-reference/memory/session/#sqlitesession)

## 🎯 Benefits

### ✅ **Simple & Lightweight**

- No external dependencies (SQLite is built into Python)
- Minimal setup required
- Perfect for local development

### ✅ **Flexible Storage Options**

- **In-memory**: Temporary sessions (lost when program ends)
- **File-based**: Persistent sessions (saved across restarts)

### ✅ **Easy to Use**

- Simple API with just two parameters
- No configuration needed
- Works out of the box

### ✅ **Portable**

- Single database file
- Easy to backup and transfer
- Cross-platform compatible

## 🚀 Quick Start

```python
from agents import Agent, Runner, SQLiteSession

# Temporary session (in-memory)
session = SQLiteSession("user_123")

# Persistent session (file-based)
session = SQLiteSession("user_123", "conversations.db")

# Use with agent
agent = Agent(name="Assistant")
result = Runner.run_sync(agent, "Hello", session=session)
```

## 📖 Usage Examples

### Example 1: Temporary Session

Use for one-time conversations or testing:

```python
from agents import Agent, Runner, SQLiteSession

session = SQLiteSession("temp_chat")  # No filename = in-memory

agent = Agent(name="Assistant")
result = Runner.run_sync(agent, "Hello", session=session)
# Conversation is lost when program ends
```

### Example 2: Persistent Session

Use for production applications or when you need data to persist:

```python
from agents import Agent, Runner, SQLiteSession

session = SQLiteSession("user_123", "conversations.db")

agent = Agent(name="Assistant")
result = Runner.run_sync(agent, "Hello", session=session)
# Conversation is saved to 'conversations.db'
# Will persist across program restarts
```

### Example 3: Multiple Sessions

Different sessions maintain separate conversation histories:

```python
user1_session = SQLiteSession("user_1", "conversations.db")
user2_session = SQLiteSession("user_2", "conversations.db")

# Each user has their own conversation history
result1 = Runner.run_sync(agent, "Hello", session=user1_session)
result2 = Runner.run_sync(agent, "Hello", session=user2_session)
```

## 🔧 API Reference

### Constructor

```python
SQLiteSession(
    session_id: str,           # Unique identifier for the session
    db_path: str | None = None # Optional database file path
)
```

**Parameters:**

- `session_id`: Unique string identifying this session (e.g., `"user_123"`, `"thread_abc"`)
- `db_path`: Optional path to SQLite database file. If not provided, uses in-memory database.

**Returns:**

- A `SQLiteSession` instance that implements the `Session` protocol

### Session Operations

All session operations are async:

```python
import asyncio

async def operations():
    session = SQLiteSession("user_123", "conversations.db")

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

asyncio.run(operations())
```

## 📊 When to Use SQLiteSession

### ✅ **Use SQLiteSession when:**

- Building simple applications
- You need local file storage
- Developing prototypes quickly
- Testing and development
- Single-user applications
- Small to medium conversation volumes

### ❌ **Consider alternatives when:**

- You need multi-user production databases (use `SQLAlchemySession`)
- You require encryption (use `EncryptedSession`)
- You need conversation branching/analytics (use `AdvancedSQLiteSession`)
- You want OpenAI-hosted storage (use `OpenAIConversationsSession`)

## 💡 Best Practices

1. **Choose meaningful session IDs:**

   ```python
   # Good
   SQLiteSession("user_12345", "conversations.db")
   SQLiteSession("thread_abc", "threads.db")

   # Avoid
   SQLiteSession("session1", "db.db")  # Not descriptive
   ```

2. **Use descriptive database filenames:**

   ```python
   # Good
   SQLiteSession("user_123", "user_conversations.db")
   SQLiteSession("support_ticket_456", "support.db")
   ```

3. **Organize databases by purpose:**

   ```python
   # Separate databases for different contexts
   user_chats = SQLiteSession("user_123", "user_chats.db")
   support_tickets = SQLiteSession("ticket_456", "support_tickets.db")
   ```

4. **Handle file permissions:**
   - Ensure your application has write permissions to the database directory
   - Consider database file cleanup for old sessions

## 🔍 Complete Example

See `main.py` for a complete working example demonstrating both temporary and persistent SQLiteSession usage.

## 🚀 Running the Example

```bash
# From the project root
uv run python -m session_management.01_sqlite_session.main
```

## 📝 Comparison with Other Session Types

| Feature          | SQLiteSession | SQLAlchemySession       | AdvancedSQLiteSession    |
| ---------------- | ------------- | ----------------------- | ------------------------ |
| Setup Complexity | ⭐ Simple     | ⭐⭐⭐ Complex          | ⭐⭐ Moderate            |
| Database Support | SQLite only   | PostgreSQL, MySQL, etc. | SQLite only              |
| Persistence      | ✅ File-based | ✅ Production DBs       | ✅ File-based            |
| Analytics        | ❌            | ❌                      | ✅ Usage tracking        |
| Branching        | ❌            | ❌                      | ✅ Conversation branches |
| Encryption       | ❌            | ❌                      | ❌                       |
| Best For         | Simple apps   | Production              | Advanced features        |

## ⚠️ Limitations

1. **Single database type**: Only supports SQLite
2. **No built-in encryption**: Data is stored in plain text
3. **No analytics**: No usage tracking or statistics
4. **No branching**: Cannot create conversation branches
5. **File-based**: Not suitable for distributed systems without additional setup

## 🔗 Related Session Types

- **[SQLAlchemySession](../02_sqlalchemy_session/README.md)** - Production databases
- **[AdvancedSQLiteSession](../03_advanced_sqlite_session/README.md)** - Enhanced features
- **[EncryptedSession](../04_encrypted_session/README.md)** - Secure storage
