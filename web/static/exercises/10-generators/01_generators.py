"""
Exercise 1: Generators and Iterators
=====================================

Generators are functions that yield values one at a time.
They're memory efficient for large sequences.

JavaScript equivalent:
    function* generator() {
        yield 1;
        yield 2;
        yield 3;
    }

Python:
    def generator():
        yield 1
        yield 2
        yield 3

Key differences:
- Python uses 'yield' keyword (same as JS)
- No asterisk in function definition
- Can use 'yield from' to delegate to another generator
- Generator expressions: (x for x in range(10))

EXERCISES:
Complete each exercise below. Run with: python3 01_generators.py
"""


# Exercise 1.1: Basic generator

def count_up_to(n):
    """
    A generator that yields numbers from 1 to n.
    Like range(1, n+1) but as a generator.
    """
    # YOUR CODE HERE
    # Use yield in a loop
    pass


def countdown(n):
    """
    A generator that yields numbers from n down to 1.
    """
    # YOUR CODE HERE
    pass


# Exercise 1.2: Generator with state

def fibonacci_generator(limit):
    """
    A generator that yields Fibonacci numbers up to (but not exceeding) limit.
    """
    # YOUR CODE HERE
    pass


# Exercise 1.3: Infinite generator

def infinite_counter(start=0, step=1):
    """
    An infinite generator that yields start, start+step, start+2*step, ...
    Use itertools.islice() to get a finite number of values.
    """
    # YOUR CODE HERE
    pass


def cycle(items):
    """
    An infinite generator that cycles through items forever.
    cycle([1, 2, 3]) -> 1, 2, 3, 1, 2, 3, 1, ...
    """
    # YOUR CODE HERE
    pass


# Exercise 1.4: Generator that filters

def evens_only(iterable):
    """
    A generator that yields only even numbers from iterable.
    """
    # YOUR CODE HERE
    pass


def filter_by_predicate(iterable, predicate):
    """
    A generator that yields items where predicate(item) is True.
    Like JavaScript's filter() but lazy.
    """
    # YOUR CODE HERE
    pass


# Exercise 1.5: Generator that transforms

def squares(iterable):
    """
    A generator that yields squares of numbers.
    Like JavaScript's map(x => x**2) but lazy.
    """
    # YOUR CODE HERE
    pass


def map_generator(iterable, func):
    """
    A generator that applies func to each item.
    Like JavaScript's map() but lazy.
    """
    # YOUR CODE HERE
    pass


# Exercise 1.6: yield from (delegation)

def flatten(nested_list):
    """
    A generator that flattens a nested list.
    [[1, 2], [3, 4], [5]] -> 1, 2, 3, 4, 5

    Use 'yield from' to delegate to sub-iterables.
    """
    # YOUR CODE HERE
    pass


def chain(*iterables):
    """
    A generator that chains multiple iterables.
    chain([1, 2], [3, 4]) -> 1, 2, 3, 4

    Use 'yield from' for each iterable.
    """
    # YOUR CODE HERE
    pass


# Exercise 1.7: Generator for file processing

def read_large_file_lines(filepath):
    """
    A generator that yields lines from a file one at a time.
    Memory efficient for large files.

    Strip newline characters from each line.
    """
    # YOUR CODE HERE
    pass


def grep_file(filepath, pattern):
    """
    A generator that yields lines containing the pattern.
    Case-insensitive search.
    """
    # YOUR CODE HERE
    pass


# Exercise 1.8: Two-way communication with send()

def accumulator():
    """
    A generator that accumulates values sent to it.
    Yields the running total after each send.

    Usage:
        acc = accumulator()
        next(acc)      # Initialize, returns 0
        acc.send(10)   # Returns 10
        acc.send(5)    # Returns 15
        acc.send(3)    # Returns 18
    """
    total = 0
    while True:
        # YOUR CODE HERE
        # value = yield total
        # total += value (if value is not None)
        pass


# Exercise 1.9: Generator pipeline

def pipeline(data, *functions):
    """
    Create a generator pipeline.
    Each function is a generator function that transforms data.

    pipeline([1,2,3], squares, evens_only)
    -> Pass through squares, then evens_only
    """
    result = data
    for func in functions:
        result = func(result)
    return result


# Let's create some pipeline stages
def add_one(iterable):
    """Add 1 to each item."""
    for item in iterable:
        yield item + 1


def double(iterable):
    """Double each item."""
    for item in iterable:
        yield item * 2


# Exercise 1.10: Generator expressions

# Create a generator expression for squares of numbers 1-10
square_gen = ???

# Create a generator expression for even numbers from the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_gen = ???

# Generator expression with transformation and filter
# Get squares of odd numbers only from range 1-10
odd_squares_gen = ???


# ============= TESTS (Don't modify below) =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1.1
    assert list(count_up_to(5)) == [1, 2, 3, 4, 5]
    assert list(countdown(5)) == [5, 4, 3, 2, 1]
    print("✓ Exercise 1.1 passed")

    # Test 1.2
    fibs = list(fibonacci_generator(100))
    assert fibs == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print("✓ Exercise 1.2 passed")

    # Test 1.3
    from itertools import islice
    counter = infinite_counter(10, 5)
    assert list(islice(counter, 5)) == [10, 15, 20, 25, 30]
    cycler = cycle([1, 2, 3])
    assert list(islice(cycler, 7)) == [1, 2, 3, 1, 2, 3, 1]
    print("✓ Exercise 1.3 passed")

    # Test 1.4
    assert list(evens_only([1, 2, 3, 4, 5, 6])) == [2, 4, 6]
    assert list(filter_by_predicate([1, 2, 3, 4], lambda x: x > 2)) == [3, 4]
    print("✓ Exercise 1.4 passed")

    # Test 1.5
    assert list(squares([1, 2, 3])) == [1, 4, 9]
    assert list(map_generator([1, 2, 3], lambda x: x * 10)) == [10, 20, 30]
    print("✓ Exercise 1.5 passed")

    # Test 1.6
    assert list(flatten([[1, 2], [3, 4], [5]])) == [1, 2, 3, 4, 5]
    assert list(chain([1, 2], [3, 4], [5, 6])) == [1, 2, 3, 4, 5, 6]
    print("✓ Exercise 1.6 passed")

    # Test 1.7 - Create a temp file for testing
    import tempfile
    import os
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("line 1\nline 2 with PATTERN\nline 3\nPATTERN here too\n")
        temp_path = f.name
    try:
        lines = list(read_large_file_lines(temp_path))
        assert lines == ["line 1", "line 2 with PATTERN", "line 3", "PATTERN here too"]
        matches = list(grep_file(temp_path, "pattern"))
        assert len(matches) == 2
    finally:
        os.unlink(temp_path)
    print("✓ Exercise 1.7 passed")

    # Test 1.8
    acc = accumulator()
    assert next(acc) == 0
    assert acc.send(10) == 10
    assert acc.send(5) == 15
    assert acc.send(3) == 18
    print("✓ Exercise 1.8 passed")

    # Test 1.9
    result = list(pipeline([1, 2, 3], add_one, double))
    assert result == [4, 6, 8]  # (1+1)*2, (2+1)*2, (3+1)*2
    print("✓ Exercise 1.9 passed")

    # Test 1.10
    assert list(square_gen) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert list(even_gen) == [2, 4, 6, 8, 10]
    assert list(odd_squares_gen) == [1, 9, 25, 49, 81]
    print("✓ Exercise 1.10 passed")

    print("\n🎉 All tests passed! Great job!")
