# Callables in Python — Simple Demo

This folder contains a very small demo showing two ideas:

- How to annotate a parameter that is a function (`typing.Callable`).
- How to make an object callable by implementing `__call__`.

What is included

- `main.py`:
  - `apply_operation(a, b, op)`: shows a typed `Callable[[int, int], int]` parameter.
  - `Doubler`: a minimal callable class with `__call__` returning `2 * x`.

Quick exercises

- Change `Doubler` to multiply by 3 instead, and verify the output.
- Add a small lambda to `apply_operation`, e.g. `lambda a, b: a - b`.