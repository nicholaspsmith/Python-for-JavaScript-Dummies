"""
Exercise 2: *args and **kwargs
===============================

Python has powerful ways to handle variable numbers of arguments.

*args - collect positional arguments into a tuple
**kwargs - collect keyword arguments into a dict

JavaScript equivalents:
- *args is like ...rest for arrays
- **kwargs is like destructuring an options object

def func(*args, **kwargs):
    # args is a tuple of positional args
    # kwargs is a dict of keyword args

JavaScript:
function func(...args) {
    // args is an array
}
function func({ option1, option2, ...rest }) {
    // destructured object
}

EXERCISES:
Complete each exercise below. Run with: python3 02_args_kwargs.py
"""


# Exercise 2.1: *args basics

def sum_all(*numbers):
    """
    Return the sum of all arguments.
    sum_all(1, 2, 3, 4) -> 10
    sum_all() -> 0
    """
    # numbers is a tuple containing all positional arguments
    # YOUR CODE HERE
    pass


def average(*numbers):
    """
    Return the average of all arguments.
    Return 0 if no arguments provided.
    """
    # YOUR CODE HERE
    pass


def concatenate(*strings, separator=" "):
    """
    Concatenate all strings with the given separator.
    concatenate("Hello", "World") -> "Hello World"
    concatenate("a", "b", "c", separator="-") -> "a-b-c"
    """
    # YOUR CODE HERE
    pass


# Exercise 2.2: **kwargs basics

def print_info(**kwargs):
    """
    Return a formatted string with all key-value pairs.
    print_info(name="Alice", age=30) -> "name=Alice, age=30"
    Sort keys alphabetically for consistent output.
    """
    # kwargs is a dict containing all keyword arguments
    # YOUR CODE HERE
    pass


def create_user(**kwargs):
    """
    Create a user dict with defaults.
    Default values:
    - role: "user"
    - active: True

    Any provided kwargs should override defaults.
    create_user(name="Alice") -> {"name": "Alice", "role": "user", "active": True}
    create_user(name="Bob", role="admin") -> {"name": "Bob", "role": "admin", "active": True}
    """
    # YOUR CODE HERE
    pass


# Exercise 2.3: Combining *args and **kwargs

def log_call(func_name, *args, **kwargs):
    """
    Return a string describing a function call.
    log_call("greet", "Alice", greeting="Hello") ->
    "Called greet with args=('Alice',) kwargs={'greeting': 'Hello'}"
    """
    # YOUR CODE HERE
    pass


def make_tag(tag_name, *children, **attributes):
    """
    Create an HTML-like tag string.
    make_tag("div", "Hello", "World", class_="container", id="main") ->
    '<div class="container" id="main">Hello World</div>'

    Note: class_ is used because 'class' is a Python keyword
    Replace underscores in attribute names with nothing (class_ -> class)
    """
    # YOUR CODE HERE
    pass


# Exercise 2.4: Unpacking arguments
# The * and ** operators can also UNPACK sequences/dicts when calling functions

def introduce(name, age, city):
    """Return introduction string."""
    return f"{name} is {age} years old and lives in {city}"


# Use these to test unpacking:
person_tuple = ("Alice", 30, "NYC")
person_dict = {"name": "Bob", "age": 25, "city": "LA"}

# Unpack tuple with *
intro_from_tuple = introduce(*person_tuple)  # Same as introduce("Alice", 30, "NYC")

# Unpack dict with **
intro_from_dict = introduce(**person_dict)  # Same as introduce(name="Bob", age=25, city="LA")


def merge_dicts(*dicts):
    """
    Merge multiple dictionaries into one.
    Later dicts override earlier ones.
    merge_dicts({"a": 1}, {"b": 2}, {"a": 3}) -> {"a": 3, "b": 2}
    """
    # Hint: Use ** unpacking in a dict comprehension or loop
    # YOUR CODE HERE
    pass


# Exercise 2.5: Keyword-only arguments
# Arguments after * must be passed by keyword

def create_rectangle(width, height, *, fill=None, stroke=None):
    """
    Create rectangle dict. fill and stroke must be keyword arguments.
    create_rectangle(10, 20) -> {"width": 10, "height": 20, "fill": None, "stroke": None}
    create_rectangle(10, 20, fill="red") -> {"width": 10, "height": 20, "fill": "red", "stroke": None}
    """
    # YOUR CODE HERE
    pass


# Exercise 2.6: Positional-only arguments (Python 3.8+)
# Arguments before / must be passed positionally

def calculate(x, y, /, operation="add"):
    """
    Calculate based on operation.
    x and y must be positional, operation can be keyword.
    calculate(5, 3) -> 8
    calculate(5, 3, operation="multiply") -> 15
    calculate(5, 3, "subtract") -> 2
    """
    # Supported operations: add, subtract, multiply, divide
    # YOUR CODE HERE
    pass


# Exercise 2.7: Complex signature

def flexible_function(required, *args, option1="default1", **kwargs):
    """
    Demonstrate a complex function signature.
    Return a dict describing all inputs.

    flexible_function("req", 1, 2, 3, option1="custom", extra="value") ->
    {
        "required": "req",
        "args": (1, 2, 3),
        "option1": "custom",
        "kwargs": {"extra": "value"}
    }
    """
    # YOUR CODE HERE
    pass


# Exercise 2.8: Forwarding arguments (decorator pattern preview)

def wrapper_function(func):
    """
    Return a function that calls func with any arguments.
    This pattern is used in decorators.
    """
    def inner(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return inner


# Test the wrapper
@wrapper_function
def sample_func(a, b, c=10):
    return a + b + c


# ============= TESTS (Don't modify below) =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 2.1
    assert sum_all(1, 2, 3, 4) == 10
    assert sum_all() == 0
    assert average(10, 20, 30) == 20.0
    assert average() == 0
    assert concatenate("Hello", "World") == "Hello World"
    assert concatenate("a", "b", "c", separator="-") == "a-b-c"
    print("✓ Exercise 2.1 passed")

    # Test 2.2
    assert print_info(name="Alice", age=30) == "age=30, name=Alice"
    result = create_user(name="Alice")
    assert result == {"name": "Alice", "role": "user", "active": True}
    result = create_user(name="Bob", role="admin")
    assert result == {"name": "Bob", "role": "admin", "active": True}
    print("✓ Exercise 2.2 passed")

    # Test 2.3
    logged = log_call("greet", "Alice", greeting="Hello")
    assert "greet" in logged and "Alice" in logged and "greeting" in logged
    tag = make_tag("div", "Hello", "World", class_="container", id="main")
    assert '<div class="container" id="main">Hello World</div>' == tag or \
           '<div id="main" class="container">Hello World</div>' == tag
    print("✓ Exercise 2.3 passed")

    # Test 2.4
    assert intro_from_tuple == "Alice is 30 years old and lives in NYC"
    assert intro_from_dict == "Bob is 25 years old and lives in LA"
    assert merge_dicts({"a": 1}, {"b": 2}, {"a": 3}) == {"a": 3, "b": 2}
    print("✓ Exercise 2.4 passed")

    # Test 2.5
    rect = create_rectangle(10, 20)
    assert rect == {"width": 10, "height": 20, "fill": None, "stroke": None}
    rect = create_rectangle(10, 20, fill="red")
    assert rect["fill"] == "red"
    print("✓ Exercise 2.5 passed")

    # Test 2.6
    assert calculate(5, 3) == 8
    assert calculate(5, 3, operation="multiply") == 15
    assert calculate(5, 3, "subtract") == 2
    print("✓ Exercise 2.6 passed")

    # Test 2.7
    result = flexible_function("req", 1, 2, 3, option1="custom", extra="value")
    assert result["required"] == "req"
    assert result["args"] == (1, 2, 3)
    assert result["option1"] == "custom"
    assert result["kwargs"] == {"extra": "value"}
    print("✓ Exercise 2.7 passed")

    # Test 2.8
    result = sample_func(1, 2, c=3)
    assert result == 6
    print("✓ Exercise 2.8 passed")

    print("\n🎉 All tests passed! Great job!")
