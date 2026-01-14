"""
Exercise 1: Decorators
=======================

Decorators are a powerful Python feature for modifying function behavior.
They're functions that wrap other functions.

JavaScript equivalent (sort of):
    const withLogging = (fn) => (...args) => {
        console.log('Calling', fn.name);
        return fn(...args);
    };

Python:
    def with_logging(fn):
        def wrapper(*args, **kwargs):
            print(f'Calling {fn.__name__}')
            return fn(*args, **kwargs)
        return wrapper

    @with_logging
    def my_function():
        pass

The @decorator syntax is just sugar for:
    my_function = with_logging(my_function)

EXERCISES:
Complete each exercise below. Run with: python3 01_decorators.py
"""

import time
import functools


# Exercise 1.1: Basic decorator without arguments

def simple_logger(func):
    """
    A decorator that prints when a function is called.
    Should print: "Calling {function_name}"
    """
    @functools.wraps(func)  # Preserves function metadata
    def wrapper(*args, **kwargs):
        # YOUR CODE HERE
        # Print the message, then call and return the original function
        pass
    return wrapper


@simple_logger
def greet(name):
    """Greet someone."""
    return f"Hello, {name}!"


# Exercise 1.2: Decorator that modifies return value

def uppercase_result(func):
    """
    A decorator that converts the return value to uppercase.
    Only works for functions returning strings.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # YOUR CODE HERE
        pass
    return wrapper


@uppercase_result
def get_greeting(name):
    return f"hello, {name}"


# Exercise 1.3: Decorator with timing

def timer(func):
    """
    A decorator that measures and prints execution time.
    Print: "{function_name} took {time:.4f} seconds"
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        # YOUR CODE HERE
        # Call function, measure time, print, return result
        pass
    return wrapper


@timer
def slow_function():
    """A slow function for testing."""
    time.sleep(0.1)
    return "done"


# Exercise 1.4: Decorator with arguments

def repeat(times):
    """
    A decorator factory that repeats a function call.
    Returns a list of results from each call.

    @repeat(3)
    def say_hello():
        return "hello"

    say_hello()  # Returns ["hello", "hello", "hello"]
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # YOUR CODE HERE
            pass
        return wrapper
    return decorator


@repeat(3)
def get_random():
    import random
    return random.randint(1, 100)


# Exercise 1.5: Decorator for validation

def validate_positive(func):
    """
    A decorator that ensures all numeric arguments are positive.
    Raises ValueError if any numeric arg is <= 0.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Check args
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError(f"Arguments must be positive, got {arg}")
        # Check kwargs
        for key, value in kwargs.items():
            if isinstance(value, (int, float)) and value <= 0:
                raise ValueError(f"Arguments must be positive, got {key}={value}")
        # YOUR CODE HERE - call and return the function
        pass
    return wrapper


@validate_positive
def calculate_area(width, height):
    return width * height


# Exercise 1.6: Memoization decorator

def memoize(func):
    """
    A decorator that caches function results.
    If called with same arguments, return cached result.

    This is a simple version - functools.lru_cache is better for production.
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        # Create a cache key from args
        # YOUR CODE HERE
        pass
    return wrapper


@memoize
def fibonacci(n):
    """Calculate fibonacci number (slow recursive version)."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Exercise 1.7: Class-based decorator

class CountCalls:
    """
    A decorator class that counts how many times a function is called.
    Access count via decorator.count attribute.
    """

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        # YOUR CODE HERE
        # Increment count, then call and return the function
        pass


@CountCalls
def say_hello():
    return "Hello!"


# Exercise 1.8: Decorator that retries on failure

def retry(max_attempts=3, delay=0.1):
    """
    A decorator that retries a function if it raises an exception.
    Waits 'delay' seconds between attempts.
    Re-raises the last exception if all attempts fail.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    # YOUR CODE HERE
                    pass
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator


# Test function for retry
fail_count = 0

@retry(max_attempts=3, delay=0.01)
def flaky_function():
    """Fails twice, then succeeds."""
    global fail_count
    fail_count += 1
    if fail_count < 3:
        raise ValueError("Temporary failure")
    return "Success!"


# Exercise 1.9: Multiple decorators (stacking)
# Decorators are applied bottom-up

def bold(func):
    """Wrap result in <b> tags."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper


def italic(func):
    """Wrap result in <i> tags."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper


# The order matters!
@bold
@italic
def styled_text(text):
    """Return styled text."""
    return text


# @bold(@italic(styled_text)) -> <b><i>text</i></b>


# Exercise 1.10: Decorator that adds methods to a function

def with_metadata(author, version):
    """
    A decorator that adds metadata attributes to a function.
    Adds .author and .version attributes.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        # YOUR CODE HERE
        # Add author and version attributes to wrapper
        pass
    return decorator


@with_metadata(author="Alice", version="1.0.0")
def my_tool():
    """A tool function."""
    return "Tool executed"


# ============= TESTS (Don't modify below) =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1.1
    result = greet("World")
    assert result == "Hello, World!"
    print("✓ Exercise 1.1 passed")

    # Test 1.2
    result = get_greeting("world")
    assert result == "HELLO, WORLD"
    print("✓ Exercise 1.2 passed")

    # Test 1.3
    result = slow_function()
    assert result == "done"
    print("✓ Exercise 1.3 passed")

    # Test 1.4
    results = get_random()
    assert len(results) == 3
    assert all(isinstance(r, int) for r in results)
    print("✓ Exercise 1.4 passed")

    # Test 1.5
    assert calculate_area(5, 3) == 15
    try:
        calculate_area(-5, 3)
        assert False, "Should raise ValueError"
    except ValueError:
        pass
    print("✓ Exercise 1.5 passed")

    # Test 1.6
    start = time.time()
    result = fibonacci(30)
    elapsed = time.time() - start
    assert result == 832040
    assert elapsed < 1, "Memoization should make this fast"
    print("✓ Exercise 1.6 passed")

    # Test 1.7
    say_hello()
    say_hello()
    say_hello()
    assert say_hello.count == 3
    print("✓ Exercise 1.7 passed")

    # Test 1.8
    fail_count = 0  # Reset
    result = flaky_function()
    assert result == "Success!"
    assert fail_count == 3
    print("✓ Exercise 1.8 passed")

    # Test 1.9
    result = styled_text("hello")
    assert result == "<b><i>hello</i></b>"
    print("✓ Exercise 1.9 passed")

    # Test 1.10
    assert my_tool.author == "Alice"
    assert my_tool.version == "1.0.0"
    assert my_tool() == "Tool executed"
    print("✓ Exercise 1.10 passed")

    print("\n🎉 All tests passed! Great job!")
