"""Generics in Python — beginner-friendly demos

This file collects short examples showing how to use `TypeVar`, `Generic`,
and typed functions/classes in a beginner-friendly way.
"""

from typing import TypeVar, Generic, Protocol, Dict, List
from dataclasses import dataclass, field


# 1) Generic function using TypeVar
# TypeVar creates a placeholder type variable. Use it when the same
# type appears in multiple places (input and return) so type checkers
# can infer relationships between them.
T = TypeVar("T")


def first_element(items: List[T]) -> T:
    """Return the first element from a list of T.

    This function works for lists of any type. The TypeVar `T` tells the
    type checker that the return value has the same type as the list items.
    """
    return items[0]


# 2) Generic mapping lookup
K = TypeVar("K")
V = TypeVar("V")


def get_value(container: Dict[K, V], key: K) -> V:
    """Lookup `key` in `container`.

    Using generic key `K` and value `V` keeps the function flexible while
    preserving type relationships for static checkers.
    """
    return container[key]


# 3) Generic class example: Stack[T]
# Generic classes let you parameterize containers and data structures.
# Here `Stack[T]` can store `int`, `str`, or any other type when used
# as `Stack[int]`, `Stack[str]`, etc.
@dataclass
class Stack(Generic[T]):
    # `items` is a list of T; default_factory avoids sharing the same list
    # between instances (common mutable-default pitfall).
    items: List[T] = field(default_factory=list)

    def push(self, item: T) -> None:
        """Push an item of type T onto the stack."""
        self.items.append(item)

    def pop(self) -> T:
        """Pop and return an item of type T from the stack."""
        return self.items.pop()


def main() -> None:
    print("--- Generics demo starting ---")

    a = first_element([1, 2, 3])
    b = first_element(["a", "b"])  # inferred as str
    print("first_element ints:", a)
    print("first_element strs:", b)

    val = get_value({"a": 1, "b": 2}, "a")
    print("get_value result:", val)

    s = Stack[int]()
    s.push(10)
    s.push(20)
    print("Stack after pushes:", s.items)
    print("Popped from stack:", s.pop())


    print("--- Generics demo finished ---")


if __name__ == "__main__":
    main()

