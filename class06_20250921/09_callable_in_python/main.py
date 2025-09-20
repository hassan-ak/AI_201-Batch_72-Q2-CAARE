"""Extremely simple callables demo.

Shows one typed `Callable` usage and one callable class. Short and clear.
"""

from typing import Callable


# 1) Typed Callable: a function that accepts a function (op) taking two ints
# and returning an int. We call `op` with a and b.
def apply_operation(a: int, b: int, op: Callable[[int, int], int]) -> int:
    return op(a, b)


def add(a: int, b: int) -> int:
    return a + b


# 2) Callable class: define __call__ so the object can be used like a function.
class Doubler:
    def __call__(self, x: int) -> int:
        return 2 * x


def main() -> None:
    print("apply_operation(add):", apply_operation(2, 3, add))
    d = Doubler()
    print("Doubler call:", d(10))


if __name__ == "__main__":
    main()

