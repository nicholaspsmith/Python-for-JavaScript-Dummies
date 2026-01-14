"""
Exercise 1: Type Hints
=======================

Python type hints are like TypeScript annotations.
They don't enforce types at runtime but help with:
- Documentation
- IDE support (autocomplete, error detection)
- Static type checkers (mypy, pyright)

JavaScript/TypeScript:
    function add(a: number, b: number): number {
        return a + b;
    }

Python:
    def add(a: int, b: int) -> int:
        return a + b

Type hints are optional but highly recommended for larger projects.

EXERCISES:
Complete each exercise below. Run with: python3 01_type_hints.py
Then try running: mypy 01_type_hints.py (if mypy is installed)
"""

from typing import (
    List, Dict, Set, Tuple, Optional, Union,
    Callable, Any, TypeVar, Generic, Literal,
    TypedDict, Protocol
)
from dataclasses import dataclass


# Exercise 1.1: Basic type hints

def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


def concatenate(items: list[str]) -> str:
    """
    Concatenate a list of strings with spaces.
    Add type hint: list of strings -> string
    """
    # YOUR CODE HERE
    pass


def find_max(numbers: ???) -> ???:
    """
    Find the maximum number in a list.
    Return None if list is empty.

    Add type hints for:
    - numbers: list of floats
    - return: Optional float (could be None)
    """
    if not numbers:
        return None
    return max(numbers)


# Exercise 1.2: Optional and Union types

def greet(name: str, greeting: Optional[str] = None) -> str:
    """
    Greet someone with optional custom greeting.
    Optional[str] means str | None
    """
    if greeting is None:
        greeting = "Hello"
    return f"{greeting}, {name}!"


def process_input(value: Union[str, int]) -> str:
    """
    Process input that could be string or int.
    Union[str, int] means str | int (Python 3.10+)
    """
    # YOUR CODE HERE
    # Return string representation
    pass


def parse_id(id_value: ???) -> int:
    """
    Parse an ID that could be string or int.

    Add type hint: accepts str | int, returns int
    """
    return int(id_value)


# Exercise 1.3: Collection type hints

def get_unique_words(text: str) -> set[str]:
    """
    Return unique words from text.
    Add type hint: returns set of strings
    """
    # YOUR CODE HERE
    pass


def count_items(items: list[str]) -> dict[str, int]:
    """
    Count occurrences of each item.
    Add type hint: returns dict mapping string to int
    """
    # YOUR CODE HERE
    pass


def get_coordinates() -> tuple[float, float]:
    """
    Return x, y coordinates.
    Add type hint: returns tuple of two floats
    """
    # YOUR CODE HERE
    pass


# Exercise 1.4: Callable types (function types)

def apply_twice(func: Callable[[int], int], value: int) -> int:
    """
    Apply a function twice.
    Callable[[int], int] means: function that takes int, returns int
    """
    return func(func(value))


def create_multiplier(factor: int) -> Callable[[int], int]:
    """
    Create a multiplier function.

    Add return type hint: returns a function int -> int
    """
    def multiplier(x: int) -> int:
        return x * factor
    return multiplier


# Exercise 1.5: TypeVar for generics

T = TypeVar('T')

def first_element(items: list[T]) -> Optional[T]:
    """
    Return first element of list, or None if empty.
    T is a type variable - works with any type.
    """
    # YOUR CODE HERE
    pass


def identity(value: T) -> T:
    """Return the input unchanged. Preserves type."""
    return value


K = TypeVar('K')
V = TypeVar('V')

def get_or_default(d: dict[K, V], key: K, default: V) -> V:
    """
    Get value from dict or return default.
    Uses two type variables for key and value types.
    """
    # YOUR CODE HERE
    pass


# Exercise 1.6: TypedDict for structured dictionaries

class UserDict(TypedDict):
    """
    A typed dictionary for user data.
    Like TypeScript interface for objects.
    """
    name: str
    age: int
    email: str


def create_user(name: str, age: int, email: str) -> UserDict:
    """Create a user dictionary with proper typing."""
    # YOUR CODE HERE
    pass


class ConfigDict(TypedDict, total=False):
    """
    A config dict with optional keys.
    total=False means all keys are optional.
    """
    debug: bool
    log_level: str
    timeout: int


# Exercise 1.7: Literal types

def set_log_level(level: Literal["DEBUG", "INFO", "WARNING", "ERROR"]) -> None:
    """
    Set log level. Only specific string values allowed.
    """
    print(f"Log level set to {level}")


def get_direction(dx: int, dy: int) -> Literal["up", "down", "left", "right", "none"]:
    """
    Return direction based on delta x and y.
    Add return type with Literal for specific strings.
    """
    if dy < 0:
        return "up"
    elif dy > 0:
        return "down"
    elif dx < 0:
        return "left"
    elif dx > 0:
        return "right"
    else:
        return "none"


# Exercise 1.8: Protocol (structural typing)

class Printable(Protocol):
    """
    A protocol for objects that can be printed.
    Like TypeScript interface - defines structure.
    """
    def __str__(self) -> str: ...


def print_all(items: list[Printable]) -> None:
    """Print all items that implement __str__."""
    for item in items:
        print(str(item))


class HasLength(Protocol):
    """Protocol for objects with a length."""
    def __len__(self) -> int: ...


def get_length(obj: HasLength) -> int:
    """
    Get length of any object with __len__.
    Works with list, str, dict, etc.
    """
    return len(obj)


# Exercise 1.9: Generic classes

class Box(Generic[T]):
    """
    A generic container class.
    Like TypeScript: class Box<T> { value: T; }
    """

    def __init__(self, value: T):
        self.value = value

    def get(self) -> T:
        return self.value

    def set(self, value: T) -> None:
        self.value = value


class Stack(Generic[T]):
    """
    A generic stack implementation.
    Add type hints to all methods.
    """

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        """Push item onto stack."""
        # YOUR CODE HERE
        pass

    def pop(self) -> Optional[T]:
        """Pop and return top item, or None if empty."""
        # YOUR CODE HERE
        pass

    def peek(self) -> Optional[T]:
        """Return top item without removing, or None if empty."""
        # YOUR CODE HERE
        pass

    def is_empty(self) -> bool:
        """Check if stack is empty."""
        # YOUR CODE HERE
        pass


# Exercise 1.10: Dataclasses with type hints

@dataclass
class Point:
    """
    A 2D point using dataclass.
    Dataclasses require type hints and auto-generate __init__, __repr__, etc.
    """
    x: float
    y: float

    def distance_from_origin(self) -> float:
        """Calculate distance from origin."""
        return (self.x ** 2 + self.y ** 2) ** 0.5


@dataclass
class Rectangle:
    """
    A rectangle dataclass.
    Add type hints for width, height (floats) and color (optional string).
    """
    width: float
    height: float
    color: Optional[str] = None

    def area(self) -> float:
        """Calculate area."""
        # YOUR CODE HERE
        pass

    def perimeter(self) -> float:
        """Calculate perimeter."""
        # YOUR CODE HERE
        pass


# ============= TESTS (Don't modify below) =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1.1
    assert add(2, 3) == 5
    assert concatenate(["hello", "world"]) == "hello world"
    assert find_max([1.5, 2.5, 0.5]) == 2.5
    assert find_max([]) is None
    print("✓ Exercise 1.1 passed")

    # Test 1.2
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Alice", "Hi") == "Hi, Alice!"
    assert process_input("hello") == "hello"
    assert process_input(42) == "42"
    assert parse_id("123") == 123
    assert parse_id(456) == 456
    print("✓ Exercise 1.2 passed")

    # Test 1.3
    assert get_unique_words("hello world hello") == {"hello", "world"}
    assert count_items(["a", "b", "a"]) == {"a": 2, "b": 1}
    coords = get_coordinates()
    assert isinstance(coords, tuple) and len(coords) == 2
    print("✓ Exercise 1.3 passed")

    # Test 1.4
    assert apply_twice(lambda x: x * 2, 3) == 12
    times_five = create_multiplier(5)
    assert times_five(3) == 15
    print("✓ Exercise 1.4 passed")

    # Test 1.5
    assert first_element([1, 2, 3]) == 1
    assert first_element([]) is None
    assert first_element(["a", "b"]) == "a"
    assert identity(42) == 42
    assert get_or_default({"a": 1}, "a", 0) == 1
    assert get_or_default({"a": 1}, "b", 0) == 0
    print("✓ Exercise 1.5 passed")

    # Test 1.6
    user = create_user("Alice", 30, "alice@test.com")
    assert user["name"] == "Alice"
    assert user["age"] == 30
    print("✓ Exercise 1.6 passed")

    # Test 1.7
    set_log_level("DEBUG")  # Should work
    assert get_direction(0, -1) == "up"
    assert get_direction(1, 0) == "right"
    print("✓ Exercise 1.7 passed")

    # Test 1.8
    assert get_length([1, 2, 3]) == 3
    assert get_length("hello") == 5
    assert get_length({"a": 1, "b": 2}) == 2
    print("✓ Exercise 1.8 passed")

    # Test 1.9
    box: Box[int] = Box(42)
    assert box.get() == 42
    box.set(100)
    assert box.get() == 100

    stack: Stack[int] = Stack()
    assert stack.is_empty() == True
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None
    print("✓ Exercise 1.9 passed")

    # Test 1.10
    p = Point(3.0, 4.0)
    assert p.distance_from_origin() == 5.0

    rect = Rectangle(10.0, 5.0, "red")
    assert rect.area() == 50.0
    assert rect.perimeter() == 30.0
    assert rect.color == "red"
    print("✓ Exercise 1.10 passed")

    print("\n🎉 All tests passed! Great job!")
    print("\nTip: Run 'pip install mypy && mypy 01_type_hints.py' to check types statically")
