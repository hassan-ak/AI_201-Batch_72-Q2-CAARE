# Generics in Python — Beginner Guide

This folder demonstrates how to use generics in Python with simple, practical examples.

What are generics?

Generics let you write code that works with multiple types while keeping type-safety.
You express a placeholder type (commonly `T`, `K`, `V`) with `typing.TypeVar` and use
it in functions or classes so a type checker (like `mypy`) can verify your code.

Key concepts

- `TypeVar`: declare a generic type variable.
- `Generic[...]`: make a class generic over one or more type variables.
- `Protocol`: supports structural typing (duck typing with type checking).

Examples included

- `first_element(items: List[T]) -> T`: a generic function returning an element of the input list.
- `get_value(container: Dict[K, V], key: K) -> V`: typed mapping lookup.
- `Stack[T]`: a generic stack implementation using `Generic[T]`.
- `SupportsLen` and `is_non_empty(...)`: protocol-based example.

Suggested exercises

- Add a `peek()` method to `Stack[T]` returning `Optional[T]`.
- Make `Stack` iterable and annotate the iterator properly.
- Use `TypeVar` bounds (e.g., `T = TypeVar('T', bound='SupportsLen')`) to constrain types.

Next steps

- Combine generics with dataclasses to create generic data containers.
- Learn `ParamSpec` and `Concatenate` for typing higher-order functions and decorators.
- Use `mypy` to check your generics usage and see the benefit of static checks.
