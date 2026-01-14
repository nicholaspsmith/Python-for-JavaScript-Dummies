"""
Exercise 1: Functions Basics
=============================

Python functions are similar to JavaScript but with some key differences.

JavaScript:
    function add(a, b) { return a + b; }
    const add = (a, b) => a + b;

Python:
    def add(a, b):
        return a + b
    add = lambda a, b: a + b

Key differences:
- 'def' keyword instead of 'function'
- Colon and indentation instead of braces
- No hoisting (must define before use)
- 'lambda' for anonymous functions (limited to single expression)
- All parameters are passed by "assignment" (like JS references)

EXERCISES:
Complete each exercise below. Run with: python3 01_functions_basics.py
"""


# Exercise 1.1: Basic function definition

def greet(name):
    """
    Return a greeting string: "Hello, {name}!"

    This is a docstring - Python's way of documenting functions.
    JavaScript uses JSDoc comments, Python uses docstrings.
    """
    # YOUR CODE HERE
    pass


def add(a, b):
    """Return the sum of a and b."""
    # YOUR CODE HERE
    pass


def is_even(n):
    """Return True if n is even, False otherwise."""
    # YOUR CODE HERE
    pass


# Exercise 1.2: Default parameters
# JavaScript: function greet(name = "World") { ... }
# Python: def greet(name="World"): ...

def greet_with_default(name="World"):
    """Return "Hello, {name}!" with "World" as default."""
    # YOUR CODE HERE
    pass


def power(base, exponent=2):
    """Return base raised to exponent (default 2)."""
    # YOUR CODE HERE
    pass


# IMPORTANT: Default mutable argument gotcha!
# DON'T do this:
#   def append_to(item, lst=[]):  # Bad! List is shared across calls!
#       lst.append(item)
#       return lst
#
# DO this instead:
#   def append_to(item, lst=None):
#       if lst is None:
#           lst = []
#       lst.append(item)
#       return lst

def append_to_list(item, lst=None):
    """
    Append item to list and return the list.
    If no list provided, create a new one.
    Handle the mutable default argument correctly!
    """
    # YOUR CODE HERE
    pass


# Exercise 1.3: Multiple return values
# Python can return multiple values (actually returns a tuple)
# JavaScript: return { min, max }; or return [min, max];
# Python: return min, max (returns tuple)

def min_max(numbers):
    """
    Return the minimum and maximum of numbers as a tuple.
    Return (None, None) if list is empty.
    """
    # YOUR CODE HERE
    pass


def divide_with_remainder(dividend, divisor):
    """
    Return quotient and remainder as a tuple.
    Example: divide_with_remainder(17, 5) -> (3, 2)
    """
    # Hint: Use // for quotient and % for remainder
    # Or use divmod() built-in function
    # YOUR CODE HERE
    pass


# Exercise 1.4: Lambda functions
# JavaScript: const double = x => x * 2;
# Python: double = lambda x: x * 2
# Note: Python lambdas can only be single expressions (no statements)

# Create a lambda that doubles a number
double = ???

# Create a lambda that returns True if a number is positive
is_positive = ???

# Create a lambda that takes two args and returns their product
multiply = ???


# Exercise 1.5: Functions as first-class citizens
# Functions can be passed around, stored in variables, etc.

def apply_operation(x, y, operation):
    """Apply the operation function to x and y."""
    # YOUR CODE HERE
    pass


def make_multiplier(factor):
    """
    Return a function that multiplies its argument by factor.
    This is a closure - the returned function "remembers" factor.

    JavaScript equivalent:
    const makeMultiplier = factor => x => x * factor;
    """
    # YOUR CODE HERE
    pass


# Exercise 1.6: Type hints (optional but recommended)
# Python 3.5+ supports type hints (like TypeScript)
# They don't enforce types but help with documentation and IDE support

def calculate_area(width: float, height: float) -> float:
    """Calculate rectangle area with type hints."""
    # YOUR CODE HERE
    pass


def process_items(items: list[str]) -> dict[str, int]:
    """
    Return a dict mapping each item to its length.
    ["hi", "hello"] -> {"hi": 2, "hello": 5}
    """
    # YOUR CODE HERE
    pass


# Exercise 1.7: Docstrings and help()
# Good Python functions have docstrings. You can access them with help()

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculate Body Mass Index.

    Args:
        weight_kg: Weight in kilograms
        height_m: Height in meters

    Returns:
        BMI value (weight / height^2)

    Example:
        >>> calculate_bmi(70, 1.75)
        22.857142857142858
    """
    # YOUR CODE HERE
    pass


# Exercise 1.8: Nested functions

def outer_function(x):
    """
    Demonstrate nested functions.
    Return the result of an inner function that squares x and adds 1.
    """
    def inner_function(n):
        return n ** 2 + 1

    # Call inner_function with x and return the result
    # YOUR CODE HERE
    pass


def make_counter():
    """
    Return a function that returns incrementing numbers.
    Each call to the returned function gives the next number.

    counter = make_counter()
    counter()  # 1
    counter()  # 2
    counter()  # 3
    """
    count = 0

    def counter():
        nonlocal count  # Needed to modify outer variable
        count += 1
        return count

    return counter


# ============= TESTS (Don't modify below) =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1.1
    assert greet("Alice") == "Hello, Alice!"
    assert add(2, 3) == 5
    assert is_even(4) == True
    assert is_even(5) == False
    print("✓ Exercise 1.1 passed")

    # Test 1.2
    assert greet_with_default() == "Hello, World!"
    assert greet_with_default("Bob") == "Hello, Bob!"
    assert power(3) == 9  # 3^2
    assert power(2, 10) == 1024
    # Test mutable default fix
    result1 = append_to_list(1)
    result2 = append_to_list(2)
    assert result1 == [1], "Should be [1], not shared with other calls"
    assert result2 == [2], "Should be [2], not [1, 2]"
    print("✓ Exercise 1.2 passed")

    # Test 1.3
    assert min_max([3, 1, 4, 1, 5]) == (1, 5)
    assert min_max([]) == (None, None)
    assert divide_with_remainder(17, 5) == (3, 2)
    print("✓ Exercise 1.3 passed")

    # Test 1.4
    assert double(5) == 10
    assert is_positive(5) == True
    assert is_positive(-3) == False
    assert multiply(3, 4) == 12
    print("✓ Exercise 1.4 passed")

    # Test 1.5
    assert apply_operation(10, 3, lambda x, y: x + y) == 13
    assert apply_operation(10, 3, lambda x, y: x - y) == 7
    times_three = make_multiplier(3)
    assert times_three(5) == 15
    assert times_three(10) == 30
    print("✓ Exercise 1.5 passed")

    # Test 1.6
    assert calculate_area(5.0, 3.0) == 15.0
    assert process_items(["hi", "hello"]) == {"hi": 2, "hello": 5}
    print("✓ Exercise 1.6 passed")

    # Test 1.7
    bmi = calculate_bmi(70, 1.75)
    assert 22.8 < bmi < 22.9
    print("✓ Exercise 1.7 passed")

    # Test 1.8
    assert outer_function(3) == 10  # 3^2 + 1
    counter = make_counter()
    assert counter() == 1
    assert counter() == 2
    assert counter() == 3
    print("✓ Exercise 1.8 passed")

    print("\n🎉 All tests passed! Great job!")
