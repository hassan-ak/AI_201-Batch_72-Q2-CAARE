# Dataclasses — Beginner Friendly Examples

This folder contains a friendly walkthrough of Python dataclasses aimed at beginners.

Files
- `main.py`: runnable examples demonstrating basic dataclasses, defaults, `frozen`, `__post_init__`, and inheritance.

Requirements
- Python 3.10 or newer (for `list | None` style and better typing support). Earlier 3.8+ will work if you adjust syntax.

# Dataclasses — Quick Explanation for Beginners

Dataclasses are a lightweight way to create classes that are primarily used to store data. They reduce boilerplate by automatically generating common methods such as `__init__`, `__repr__`, and comparison methods based on class attributes.

Why use dataclasses?

- Less boilerplate: no need to write `__init__`, `__repr__`, or `__eq__` by hand for simple containers.
- Clearer intent: dataclasses signal that the class is a simple data container (like a record).
- Works well with type hints: use `typing` to express field types and improve tooling support.

Key features

- Automatic method generation: `__init__`, `__repr__`, `__eq__`, and others.
- `field(...)` for advanced options: `default`, `default_factory`, `repr`, and `compare`.
- `frozen=True` to make instances immutable (useful for value objects).
- `__post_init__` to run additional initialization or validation after the generated `__init__` runs.
- `ClassVar` to mark class-level constants that should not be treated as fields.

Small examples

- Simple dataclass

```python
from dataclasses import dataclass

@dataclass
class Point:
	x: float
	y: float

# creates Point(1.0, 2.0) with auto-generated __init__ and readable __repr__
```

- Mutable defaults safe pattern

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Team:
	name: str
	members: List[str] = field(default_factory=list)

# each Team gets its own list instance (avoids shared-list pitfalls)
```

- Derived values and validation using `__post_init__`

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Person:
	first: str
	last: str
	full_name: Optional[str] = None

	def __post_init__(self):
		if self.full_name is None:
			self.full_name = f"{self.first} {self.last}"
```

When to prefer plain classes

- If your class needs complex behavior, heavy encapsulation, or many custom methods, a regular class may be clearer.

Suggested next steps

- Use `typing` (`Optional`, `List`, `ClassVar`, `TypeVar`) to make dataclasses safer and clearer.
- Try `mypy` or `pyright` to statically check code that uses dataclasses.
- Practice: convert a few small plain classes into dataclasses and observe boilerplate reduction.

This `README` focuses on the conceptual side — see `main.py` for runnable examples that demonstrate these ideas.
