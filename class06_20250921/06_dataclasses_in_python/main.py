"""Dataclasses for beginners

This file demonstrates dataclasses from the very beginning with
small, self-contained examples. Run it with Python 3.10+.
"""

from dataclasses import dataclass, field
from typing import List, Optional, ClassVar


# 1) The simplest dataclass: automatic __init__, __repr__, and comparison
@dataclass
class Point:
    x: float
    y: float


def demo_simple_dataclass() -> None:
    p = Point(1.0, 2.0)
    print("Simple dataclass:", p)


# 2) Default values and default_factory for mutable defaults
@dataclass
class Team:
    name: str
    members: List[str] = field(default_factory=list)


def demo_defaults() -> None:
    t = Team("Avengers")
    t.members.append("Iron Man")
    t.members.append("Captain America")
    print("Team with members:", t)


# 3) Immutable dataclass (frozen=True)
@dataclass(frozen=True)
class Color:
    r: int
    g: int
    b: int


def demo_frozen() -> None:
    c = Color(255, 0, 0)
    print("Frozen dataclass:", c)
    try:
        # this will raise FrozenInstanceError when running
        c.r = 128  # type: ignore
    except Exception as e:
        print("Attempt to mutate frozen dataclass raised:", type(e).__name__)


# 4) Post-initialization processing with __post_init__
@dataclass
class Person:
    first: str
    last: str
    full_name: Optional[str] = None

    def __post_init__(self) -> None:
        # compute derived field if not provided
        if self.full_name is None:
            self.full_name = f"{self.first} {self.last}"


def demo_post_init() -> None:
    p = Person("Ada", "Lovelace")
    print("Person with derived field:", p)


# 5) Dataclass inheritance and ClassVar usage
@dataclass
class Employee(Person):
    employee_id: int = 0
    company: ClassVar[str] = "OpenAI"


def demo_inheritance() -> None:
    e = Employee("Grace", "Hopper", employee_id=42)
    print("Employee (inherits Person):", e)
    print("Company (ClassVar):", Employee.company)

@dataclass
class PIAIC_Student:
    national_language: ClassVar[str] = "Urdu"
    name: str
    age: int
    courses: list | None = field(default_factory=list)

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    @classmethod
    def find_national_language(cls) -> str:
        return f"National language is {cls.national_language}."
    
def demo_PIAIC_Student():
    piaic_student = PIAIC_Student(name="Ali", age=30)
    print(piaic_student)
    piaic_student.courses.append("Python")
    print(piaic_student)
    print(piaic_student.name)
    print(piaic_student.age)
    print(piaic_student.courses)
    print(piaic_student.greet())
    print(PIAIC_Student.find_national_language())
    print(PIAIC_Student.national_language)

def main() -> None:
    print("--- Dataclasses demo starting ---")
    demo_simple_dataclass()
    demo_defaults()
    demo_frozen()
    demo_post_init()
    demo_inheritance()
    demo_PIAIC_Student()
    print("--- Dataclasses demo finished ---")


if __name__ == "__main__":
    main()


