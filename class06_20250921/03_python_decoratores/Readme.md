# Python Decorators — Simple Guide

Decorators let you “wrap” a function with extra behavior without changing its code. Common uses:
- Logging
- Timing
- Caching
- Access control/validation

Think of a decorator as a reusable wrapper: it takes a function, adds something before/after it runs, and returns a new function.

## Basic idea

```python
def decorator(func):
    def wrapper():
        print("Before")
        result = func()
        print("After")
        return result
    return wrapper

@decorator
def greet(name):
    print(f"Hello")

greet("Hassan")
```

Output:
```
Before
Hello
After
```

## Why use decorators?
- Keep business logic clean
- Reuse cross-cutting concerns
- DRY: write once, apply to many functions

## This lesson includes a small UV simple app
Folder: `06_python_decoratores/simple-decorators-app`

What it shows:
- A timing decorator (measure how long a function takes)
- A logging decorator (print function name and args)
- Stacking multiple decorators

### Quick start
From `simple-decorators-app/`:

```bash
uv sync
uv run python basic.py
uv run python advance.py
```

You’ll see logs and timing around sample functions.

## Notes
- Use `functools.wraps` to preserve function metadata (name, docstring)
- Decorators can take parameters (decorator factory)
- You can apply multiple decorators; they run top-down
