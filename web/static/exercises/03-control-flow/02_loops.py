"""
Exercise 2: Loops
==================

Python loops are different from JavaScript in several ways.

FOR LOOPS:
JavaScript: for (let i = 0; i < 10; i++) or for (const item of array)
Python: for i in range(10) or for item in list

WHILE LOOPS:
Very similar in both languages.

Key differences:
- Python for loops iterate over iterables (no C-style for loops)
- range(n) generates 0 to n-1
- enumerate() gives you index and value
- zip() iterates multiple sequences together
- Python has for/else and while/else (unusual feature!)

EXERCISES:
Complete each exercise below. Run with: python3 02_loops.py
"""


# Exercise 2.1: Basic for loops with range()
# range(stop) -> 0, 1, 2, ..., stop-1
# range(start, stop) -> start, start+1, ..., stop-1
# range(start, stop, step) -> start, start+step, ...

def sum_to_n(n):
    """Return sum of numbers from 1 to n (inclusive)."""
    # Use range() and a for loop
    # YOUR CODE HERE
    pass


def sum_evens(start, end):
    """Return sum of even numbers from start to end (inclusive)."""
    # Hint: range(start, end+1, step) or check with %
    # YOUR CODE HERE
    pass


# Exercise 2.2: Iterating over collections

def sum_list(numbers):
    """Return sum of all numbers in list."""
    # for num in numbers: (don't use range!)
    # YOUR CODE HERE
    pass


def count_vowels(text):
    """Count vowels (a, e, i, o, u) in text (case insensitive)."""
    # for char in text:
    # YOUR CODE HERE
    pass


# Exercise 2.3: enumerate() - get index and value
# JavaScript: array.forEach((item, index) => ...)
# Python: for index, item in enumerate(array):

def find_index(items, target):
    """Return index of target in items, or -1 if not found."""
    # Use enumerate() instead of tracking index manually
    # YOUR CODE HERE
    pass


def add_line_numbers(lines):
    """
    Return list of lines with line numbers added.
    ["Hello", "World"] -> ["1: Hello", "2: World"]
    """
    # Hint: enumerate(lines, start=1) starts counting from 1
    # YOUR CODE HERE
    pass


# Exercise 2.4: zip() - iterate multiple sequences
# JavaScript: array1.map((item, i) => [item, array2[i]])
# Python: for item1, item2 in zip(list1, list2):

def combine_names(first_names, last_names):
    """
    Combine first and last names into full names.
    ["John", "Jane"], ["Doe", "Smith"] -> ["John Doe", "Jane Smith"]
    """
    # Use zip()
    # YOUR CODE HERE
    pass


def dot_product(vec1, vec2):
    """Calculate dot product of two vectors (lists of numbers)."""
    # Dot product: sum of products of corresponding elements
    # [1, 2, 3] · [4, 5, 6] = 1*4 + 2*5 + 3*6 = 32
    # YOUR CODE HERE
    pass


# Exercise 2.5: Dictionary iteration

def invert_dict(d):
    """
    Return a new dict with keys and values swapped.
    {"a": 1, "b": 2} -> {1: "a", 2: "b"}
    """
    # for key, value in d.items():
    # YOUR CODE HERE
    pass


def filter_dict(d, min_value):
    """Return new dict with only items where value >= min_value."""
    # YOUR CODE HERE
    pass


# Exercise 2.6: while loops

def countdown(n):
    """Return list counting down from n to 1."""
    # [5, 4, 3, 2, 1] for n=5
    # Use a while loop (could use range, but practice while)
    # YOUR CODE HERE
    pass


def collatz_steps(n):
    """
    Count steps to reach 1 using Collatz sequence.
    If n is even: n = n / 2
    If n is odd: n = 3n + 1
    Example: 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 (8 steps)
    """
    # YOUR CODE HERE
    pass


# Exercise 2.7: break and continue
# Same as JavaScript

def find_first_negative(numbers):
    """Return the first negative number, or None if none found."""
    # Use break when found
    # YOUR CODE HERE
    pass


def sum_until_negative(numbers):
    """Sum numbers until a negative is encountered (don't include it)."""
    # Use break
    # YOUR CODE HERE
    pass


def sum_positives(numbers):
    """Sum only positive numbers, skip negatives."""
    # Use continue to skip negatives
    # YOUR CODE HERE
    pass


# Exercise 2.8: for/else and while/else (Python unique!)
# The else block runs if the loop completes WITHOUT break
# Great for search patterns!

def find_prime_factor(n):
    """
    Return the smallest prime factor of n, or None if n is 1.
    Use for/else pattern.
    """
    for i in range(2, n):
        if n % i == 0:
            return i
    else:
        # This runs if we didn't break (no factor found)
        return n if n > 1 else None


def has_duplicate(items):
    """
    Return True if items has any duplicate, False otherwise.
    Try using for/else pattern (though set is easier).
    """
    # YOUR CODE HERE
    pass


# Exercise 2.9: Nested loops

def multiplication_table(n):
    """
    Return n x n multiplication table as list of lists.
    multiplication_table(3) -> [[1,2,3], [2,4,6], [3,6,9]]
    """
    # YOUR CODE HERE
    pass


def find_pair_with_sum(numbers, target):
    """
    Find two numbers that sum to target.
    Return tuple (num1, num2) or None if not found.
    """
    # Use nested loops (there are more efficient ways, but practice loops)
    # YOUR CODE HERE
    pass


# Exercise 2.10: Loop with else for validation

def all_positive(numbers):
    """
    Return True if all numbers are positive.
    Use for/else pattern.
    """
    # YOUR CODE HERE
    pass


# ============= TESTS (Don't modify below) =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 2.1
    assert sum_to_n(5) == 15  # 1+2+3+4+5
    assert sum_to_n(10) == 55
    assert sum_evens(1, 10) == 30  # 2+4+6+8+10
    assert sum_evens(2, 8) == 20  # 2+4+6+8
    print("✓ Exercise 2.1 passed")

    # Test 2.2
    assert sum_list([1, 2, 3, 4, 5]) == 15
    assert sum_list([]) == 0
    assert count_vowels("Hello World") == 3
    assert count_vowels("AEIOU") == 5
    print("✓ Exercise 2.2 passed")

    # Test 2.3
    assert find_index([10, 20, 30], 20) == 1
    assert find_index([10, 20, 30], 40) == -1
    assert add_line_numbers(["a", "b"]) == ["1: a", "2: b"]
    print("✓ Exercise 2.3 passed")

    # Test 2.4
    assert combine_names(["John", "Jane"], ["Doe", "Smith"]) == ["John Doe", "Jane Smith"]
    assert dot_product([1, 2, 3], [4, 5, 6]) == 32
    print("✓ Exercise 2.4 passed")

    # Test 2.5
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert filter_dict({"a": 1, "b": 5, "c": 3}, 3) == {"b": 5, "c": 3}
    print("✓ Exercise 2.5 passed")

    # Test 2.6
    assert countdown(5) == [5, 4, 3, 2, 1]
    assert collatz_steps(6) == 8
    assert collatz_steps(1) == 0
    print("✓ Exercise 2.6 passed")

    # Test 2.7
    assert find_first_negative([1, 2, -3, 4]) == -3
    assert find_first_negative([1, 2, 3]) is None
    assert sum_until_negative([1, 2, 3, -4, 5]) == 6
    assert sum_positives([1, -2, 3, -4, 5]) == 9
    print("✓ Exercise 2.7 passed")

    # Test 2.8
    assert find_prime_factor(15) == 3
    assert find_prime_factor(7) == 7
    assert has_duplicate([1, 2, 3, 2]) == True
    assert has_duplicate([1, 2, 3, 4]) == False
    print("✓ Exercise 2.8 passed")

    # Test 2.9
    assert multiplication_table(3) == [[1,2,3], [2,4,6], [3,6,9]]
    assert find_pair_with_sum([1, 2, 3, 4], 5) in [(1, 4), (2, 3)]
    assert find_pair_with_sum([1, 2, 3], 10) is None
    print("✓ Exercise 2.9 passed")

    # Test 2.10
    assert all_positive([1, 2, 3]) == True
    assert all_positive([1, -2, 3]) == False
    assert all_positive([]) == True
    print("✓ Exercise 2.10 passed")

    print("\n🎉 All tests passed! Great job!")
