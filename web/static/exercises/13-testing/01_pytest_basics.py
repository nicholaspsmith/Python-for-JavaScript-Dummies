"""
Exercise 1: Testing with pytest
================================

pytest is Python's most popular testing framework.
It's simpler than unittest and more powerful.

JavaScript equivalent: Jest
    test('adds numbers', () => {
        expect(add(1, 2)).toBe(3);
    });

Python with pytest:
    def test_add():
        assert add(1, 2) == 3

Key features:
- Simple assert statements (no special assertion methods)
- Automatic test discovery (files starting with test_)
- Fixtures for setup/teardown
- Parametrized tests
- Rich plugins ecosystem

EXERCISES:
To run these tests: pytest 01_pytest_basics.py -v
"""

import pytest
from typing import List, Optional


# ========== CODE TO TEST ==========

def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def divide(a: float, b: float) -> float:
    """Divide a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def find_max(numbers: List[int]) -> Optional[int]:
    """Find maximum in list. Returns None for empty list."""
    if not numbers:
        return None
    return max(numbers)


def is_palindrome(s: str) -> bool:
    """Check if string is a palindrome (case insensitive)."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]


class Calculator:
    """A simple calculator class."""

    def __init__(self, initial_value: float = 0):
        self.value = initial_value
        self.history: List[str] = []

    def add(self, n: float) -> 'Calculator':
        self.value += n
        self.history.append(f"+ {n}")
        return self

    def subtract(self, n: float) -> 'Calculator':
        self.value -= n
        self.history.append(f"- {n}")
        return self

    def multiply(self, n: float) -> 'Calculator':
        self.value *= n
        self.history.append(f"* {n}")
        return self

    def clear(self) -> 'Calculator':
        self.value = 0
        self.history.clear()
        return self


class ShoppingCart:
    """A shopping cart for testing."""

    def __init__(self):
        self.items: dict[str, dict] = {}

    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"price": price, "quantity": quantity}

    def remove_item(self, name: str) -> None:
        if name in self.items:
            del self.items[name]

    def get_total(self) -> float:
        return sum(
            item["price"] * item["quantity"]
            for item in self.items.values()
        )

    def clear(self) -> None:
        self.items.clear()


# ========== TESTS ==========

# Exercise 1.1: Basic tests with assert

def test_add_positive_numbers():
    """Test adding positive numbers."""
    # YOUR CODE HERE
    # assert add(2, 3) == ???
    pass


def test_add_negative_numbers():
    """Test adding negative numbers."""
    # YOUR CODE HERE
    pass


def test_add_zero():
    """Test adding zero."""
    # YOUR CODE HERE
    pass


# Exercise 1.2: Testing exceptions with pytest.raises

def test_divide_by_zero():
    """Test that dividing by zero raises ValueError."""
    # Use: with pytest.raises(ValueError):
    # YOUR CODE HERE
    pass


def test_divide_by_zero_message():
    """Test the exception message."""
    # Use: with pytest.raises(ValueError) as exc_info:
    #      assert "zero" in str(exc_info.value)
    # YOUR CODE HERE
    pass


# Exercise 1.3: Testing with multiple assertions

def test_find_max():
    """Test find_max with various inputs."""
    # Test with positive numbers
    # Test with negative numbers
    # Test with empty list
    # Test with single element
    # YOUR CODE HERE
    pass


# Exercise 1.4: Parametrized tests
# Run same test with different inputs

@pytest.mark.parametrize("input_str,expected", [
    ("racecar", True),
    ("hello", False),
    ("A man a plan a canal Panama", True),
    ("", True),
    ("a", True),
    # Add more test cases
])
def test_is_palindrome(input_str, expected):
    """Test palindrome detection with various inputs."""
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("a,b,expected", [
    # Add test cases for add function
    # (1, 2, 3),
    # (-1, 1, 0),
    # etc.
])
def test_add_parametrized(a, b, expected):
    """Parametrized test for add function."""
    # YOUR CODE HERE
    pass


# Exercise 1.5: Fixtures for setup/teardown

@pytest.fixture
def calculator():
    """Fixture that provides a fresh Calculator instance."""
    return Calculator(initial_value=10)


@pytest.fixture
def shopping_cart():
    """Fixture that provides a ShoppingCart with some items."""
    cart = ShoppingCart()
    cart.add_item("Apple", 1.00, 5)
    cart.add_item("Banana", 0.50, 3)
    return cart


def test_calculator_add(calculator):
    """Test calculator add using fixture."""
    # calculator starts at 10 (from fixture)
    # YOUR CODE HERE
    pass


def test_calculator_chain(calculator):
    """Test method chaining."""
    # Test: calculator.add(5).subtract(3).multiply(2)
    # YOUR CODE HERE
    pass


def test_shopping_cart_total(shopping_cart):
    """Test cart total calculation."""
    # Cart has: 5 Apples at $1 + 3 Bananas at $0.50
    # YOUR CODE HERE
    pass


def test_shopping_cart_add_item(shopping_cart):
    """Test adding items to cart."""
    # YOUR CODE HERE
    pass


# Exercise 1.6: Fixture with cleanup (yield)

@pytest.fixture
def temp_file(tmp_path):
    """Fixture that creates a temp file and cleans up after."""
    file_path = tmp_path / "test.txt"
    file_path.write_text("test content")
    yield file_path
    # Cleanup happens automatically with tmp_path


def test_temp_file_exists(temp_file):
    """Test that temp file was created."""
    # YOUR CODE HERE
    pass


def test_temp_file_content(temp_file):
    """Test temp file content."""
    # YOUR CODE HERE
    pass


# Exercise 1.7: Testing classes

class TestCalculator:
    """Group calculator tests in a class."""

    def test_initial_value(self):
        """Test default initial value."""
        calc = Calculator()
        # YOUR CODE HERE
        pass

    def test_custom_initial_value(self):
        """Test custom initial value."""
        calc = Calculator(100)
        # YOUR CODE HERE
        pass

    def test_history_tracking(self):
        """Test that operations are tracked in history."""
        calc = Calculator()
        calc.add(5).subtract(3)
        # YOUR CODE HERE
        pass

    def test_clear(self):
        """Test clear resets value and history."""
        calc = Calculator(10)
        calc.add(5)
        calc.clear()
        # YOUR CODE HERE
        pass


# Exercise 1.8: Markers for test organization

@pytest.mark.slow
def test_slow_operation():
    """A slow test (marked for selective running)."""
    import time
    time.sleep(0.1)
    assert True


@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    """Test for a feature not yet implemented."""
    pass


@pytest.mark.skipif(True, reason="Conditional skip example")
def test_conditional():
    """Test that's conditionally skipped."""
    pass


# Exercise 1.9: Approximate comparisons

def test_float_division():
    """Test float division with approximate comparison."""
    result = 1 / 3
    # Use pytest.approx() for float comparisons
    # YOUR CODE HERE
    # assert result == pytest.approx(???, rel=1e-9)
    pass


def test_list_of_floats():
    """Test list of floats."""
    results = [0.1 + 0.2, 0.3]
    # 0.1 + 0.2 != 0.3 due to float precision
    # Use pytest.approx() for the comparison
    # YOUR CODE HERE
    pass


# Exercise 1.10: Conftest and shared fixtures
# In a real project, you'd put shared fixtures in conftest.py

# Example of what would go in conftest.py:
"""
# conftest.py
import pytest

@pytest.fixture(scope="session")
def database():
    '''Session-scoped database connection.'''
    db = connect_to_db()
    yield db
    db.close()

@pytest.fixture
def clean_db(database):
    '''Transaction-scoped clean database.'''
    database.begin_transaction()
    yield database
    database.rollback()
"""


# ============= RUN TESTS =============
if __name__ == "__main__":
    print("Run tests with: pytest 01_pytest_basics.py -v")
    print("Or for more detail: pytest 01_pytest_basics.py -v --tb=short")
    print("\nTo run specific tests:")
    print("  pytest 01_pytest_basics.py -v -k 'test_add'")
    print("\nTo skip slow tests:")
    print("  pytest 01_pytest_basics.py -v -m 'not slow'")
