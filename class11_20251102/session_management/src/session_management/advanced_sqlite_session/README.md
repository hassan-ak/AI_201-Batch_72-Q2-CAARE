# AdvancedSQLiteSession - Enhanced SQLite with Advanced Features

AdvancedSQLiteSession extends SQLiteSession with conversation branching, usage analytics, and structured queries. Perfect for applications that need advanced session management capabilities.

## 📚 Reference Documentation

- [OpenAI Agents SDK - Advanced SQLite Sessions](https://openai.github.io/openai-agents-python/sessions/advanced_sqlite_session/)
- [SQLiteSession - Basic](https://openai.github.io/openai-agents-python/sessions/)

## 🎯 Benefits

### ✅ **Conversation Branching**
- Create multiple conversation paths from any point
- Explore different dialogue directions
- Useful for "what-if" scenarios and A/B testing

### ✅ **Usage Analytics**
- Track token usage per run
- Monitor conversation costs
- Analyze usage patterns
- Store and query usage statistics

### ✅ **Structured Queries**
- Query conversations by metadata
- Filter by date, user, or other criteria
- Advanced session management operations
- Better organization of conversation data

### ✅ **Enhanced Management**
- List all sessions
- Query session metadata
- Better tracking of conversation state
- Analytics on conversation patterns

## 🚀 Quick Start

```python
from agents import Agent, Runner
from agents.extensions.memory import AdvancedSQLiteSession

# Create advanced session
session = AdvancedSQLiteSession(
    session_id="user_123",
    db_path="sessions.db",
    create_tables=True
)

# Use with agent
agent = Agent(name="Assistant")
result = await Runner.run(agent, "Hello", session=session)

# Store usage data
await session.store_run_usage(result)

# Create conversation branch
branch_id = await session.create_branch_from_turn(turn_number=2)
```

## 📖 Key Features

### 1. Conversation Branching

Create alternative conversation paths from any turn:

```python
import asyncio
from agents import Agent, Runner
from agents.extensions.memory import AdvancedSQLiteSession

async def main():
    session = AdvancedSQLiteSession(
        "user_123",
        "sessions.db",
        create_tables=True
    )
    
    agent = Agent(name="Assistant")
    
    # Initial conversation
    result1 = await Runner.run(agent, "I love pizza", session=session)
    result2 = await Runner.run(agent, "What's my favorite food?", session=session)
    
    # Create branch from turn 2
    branch_id = await session.create_branch_from_turn(2)
    
    # Continue on branch with different question
    branch_session = AdvancedSQLiteSession(branch_id, "sessions.db")
    result3 = await Runner.run(
        agent,
        "Tell me about Italian cuisine",
        session=branch_session
    )

asyncio.run(main())
```

**Use Cases:**
- Exploring alternative conversation paths
- A/B testing different conversation flows
- Creating "what-if" scenarios
- Recovering from errors by branching

### 2. Usage Analytics

Track token usage and costs for each run:

```python
async def track_usage():
    session = AdvancedSQLiteSession(
        "user_123",
        "sessions.db",
        create_tables=True
    )
    
    agent = Agent(name="Assistant")
    result = await Runner.run(agent, "Hello", session=session)
    
    # Store usage data
    await session.store_run_usage(result)
    
    # Get usage statistics
    stats = await session.get_usage_stats()
    print(f"Total runs: {stats.get('total_runs', 0)}")
    print(f"Total tokens: {stats.get('total_tokens', 0)}")
    print(f"Total cost: {stats.get('total_cost', 0)}")
```

**Benefits:**
- Monitor API costs
- Track usage per session
- Analyze conversation patterns
- Budget management

### 3. Structured Queries

Query conversations with advanced filtering:

```python
async def query_examples():
    session = AdvancedSQLiteSession(
        "user_123",
        "sessions.db",
        create_tables=True
    )
    
    # Get items with metadata
    items = await session.get_items()
    
    # List all sessions
    sessions = await session.list_sessions()
    for sess in sessions:
        print(f"Session: {sess['session_id']}")
        print(f"Created: {sess['created_at']}")
        print(f"Items: {sess['item_count']}")
```

## 🔧 API Reference

### Constructor

```python
AdvancedSQLiteSession(
    session_id: str,                    # Unique session identifier
    db_path: str,                       # Database file path
    create_tables: bool = True          # Create tables automatically
) -> AdvancedSQLiteSession
```

### Key Methods

#### `create_branch_from_turn()`

Create a conversation branch from a specific turn:

```python
branch_id = await session.create_branch_from_turn(
    turn_number: int                   # Turn to branch from (0-indexed)
) -> str                               # Returns new branch session ID
```

#### `store_run_usage()`

Store usage statistics for a run:

```python
await session.store_run_usage(
    result: RunResult                  # Result from Runner.run()
) -> None
```

#### `get_usage_stats()`

Get aggregated usage statistics:

```python
stats = await session.get_usage_stats() -> dict
# Returns: {
#     'total_runs': int,
#     'total_tokens': int,
#     'total_cost': float,
#     ...
# }
```

#### `list_sessions()`

List all sessions in the database:

```python
sessions = await session.list_sessions() -> List[dict]
# Returns list of session dictionaries with metadata
```

## 📊 When to Use AdvancedSQLiteSession

### ✅ **Use AdvancedSQLiteSession when:**
- You need conversation branching functionality
- You want to track usage analytics
- You need structured queries on conversations
- You're building applications with complex session management
- You need to analyze conversation patterns
- You want better organization of conversation data

### ❌ **Consider SQLiteSession when:**
- You only need basic session storage
- You don't need branching or analytics
- You want the simplest possible solution

### ❌ **Consider SQLAlchemySession when:**
- You need production databases (PostgreSQL, MySQL)
- You need better scalability
- You're building distributed systems

## 💡 Use Cases

### Use Case 1: Conversation Exploration

```python
# User asks a question
result1 = await Runner.run(agent, "Tell me about AI", session=session)

# Explore different responses by branching
branch_id = await session.create_branch_from_turn(0)
branch_session = AdvancedSQLiteSession(branch_id, "sessions.db")

# Different follow-up on branch
result2 = await Runner.run(
    agent,
    "Focus on machine learning",
    session=branch_session
)
```

### Use Case 2: Cost Tracking

```python
# Track costs for each conversation
results = []
for question in questions:
    result = await Runner.run(agent, question, session=session)
    await session.store_run_usage(result)
    results.append(result)

# Analyze costs
stats = await session.get_usage_stats()
print(f"Total cost: ${stats['total_cost']:.2f}")
print(f"Average per run: ${stats['total_cost']/stats['total_runs']:.2f}")
```

### Use Case 3: Error Recovery

```python
try:
    result = await Runner.run(agent, "Complex query", session=session)
except Exception as e:
    # Create branch before the error
    branch_id = await session.create_branch_from_turn(
        await session.get_current_turn() - 1
    )
    # Continue from safe point
    branch_session = AdvancedSQLiteSession(branch_id, "sessions.db")
    result = await Runner.run(agent, "Simpler query", session=branch_session)
```

## 🔍 Complete Example

See `main.py` for a complete working example demonstrating all advanced features.

## 🚀 Running the Example

```bash
# From the project root
uv run python -m session_management.03_advanced_sqlite_session.main
```

## 📝 Comparison with Other Session Types

| Feature | AdvancedSQLiteSession | SQLiteSession | SQLAlchemySession |
|---------|----------------------|--------------|-------------------|
| Basic Storage | ✅ | ✅ | ✅ |
| Branching | ✅ | ❌ | ❌ |
| Usage Analytics | ✅ | ❌ | ❌ |
| Structured Queries | ✅ | ⚠️ Limited | ⚠️ Limited |
| Database Support | SQLite only | SQLite only | Multiple DBs |
| Production Ready | ⚠️ Limited | ⚠️ Limited | ✅ Yes |

## ⚠️ Important Notes

1. **Async Operations**: AdvancedSQLiteSession requires async/await. Use `await Runner.run()` instead of `Runner.run_sync()`.

2. **Database Schema**: The advanced session uses an enhanced schema. Make sure `create_tables=True` on first use.

3. **Branching Overhead**: Creating many branches can increase database size. Consider cleanup strategies.

4. **Usage Tracking**: `store_run_usage()` requires the result object from `Runner.run()`. Make sure to pass the actual result.

## 💡 Best Practices

1. **Branching Strategy**: Only create branches when needed to avoid database bloat.

2. **Usage Tracking**: Track usage consistently for accurate analytics:
   ```python
   result = await Runner.run(agent, message, session=session)
   await session.store_run_usage(result)  # Always track
   ```

3. **Database Maintenance**: Periodically clean up old branches and sessions:
   ```python
   # List and clean old sessions
   sessions = await session.list_sessions()
   for sess in sessions:
       if is_old(sess):
           await session.delete_session(sess['session_id'])
   ```

4. **Branch Naming**: Use descriptive session IDs for branches:
   ```python
   branch_id = f"{base_session_id}_branch_{datetime.now().timestamp()}"
   ```

## 🔗 Related Session Types

- **[SQLiteSession](../01_sqlite_session/README.md)** - Basic storage
- **[SQLAlchemySession](../02_sqlalchemy_session/README.md)** - Production databases
- **[EncryptedSession](../04_encrypted_session/README.md)** - Secure storage

