from __future__ import annotations

import time
from functools import wraps
from typing import Any, Callable

# Type alias for a decorator
Decorator = Callable[[Callable[..., Any]], Callable[..., Any]]


def log_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that logs function name and arguments before call."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        arg_list = ", ".join([
            *[repr(a) for a in args],
            *[f"{k}={v!r}" for k, v in kwargs.items()],
        ])
        print(f"[LOG] Calling {func.__name__}({arg_list})")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result!r}")
        return result

    return wrapper


def time_it(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that measures and prints execution time."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            end = time.perf_counter()
            print(f"[TIMER] {func.__name__} took {end - start:.4f}s")

    return wrapper


def repeat(n: int) -> Decorator:
    """Decorator factory that repeats a function n times.

    Example:
        @repeat(3)
        def hello():
            print("hi")
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


# Demonstrations --------------------------------------------------------------

@log_calls
@time_it
def add(a: int, b: int) -> int:
    time.sleep(0.1)
    return a + b


@time_it
@log_calls
def greet(name: str) -> str:
    time.sleep(0.05)
    return f"Hello, {name}!"


@log_calls
@repeat(3)
def ping() -> None:
    print("pong")


if __name__ == "__main__":
    # Stacked decorators: note order and output
    print("\n")
    add(2, 3)
    print("\n")
    greet("Hassan")
    print("\n")
    ping()
    print("\n")
    
