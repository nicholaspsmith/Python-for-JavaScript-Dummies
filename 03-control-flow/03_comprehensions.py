"""
Exercise 3: Comprehensions
===========================

Comprehensions are Python's elegant way to create collections.
They're more Pythonic than map/filter and often more readable.

JavaScript equivalents:
- List comprehension: array.map(...).filter(...)
- Dict comprehension: Object.fromEntries(...)
- Set comprehension: new Set(array.map(...))

Basic syntax:
- List: [expression for item in iterable if condition]
- Dict: {key: value for item in iterable if condition}
- Set: {expression for item in iterable if condition}
- Generator: (expression for item in iterable if condition)

EXERCISES:
Complete each exercise below. Run with: python3 03_comprehensions.py
"""


# Exercise 3.1: Basic list comprehensions

# Create a list of squares from 1 to 10: [1, 4, 9, 16, ..., 100]
# JavaScript: [...Array(10)].map((_, i) => (i+1)**2)
squares = ???


# Create a list of even numbers from 1 to 20: [2, 4, 6, ..., 20]
# JavaScript: [...Array(20)].map((_, i) => i+1).filter(n => n % 2 === 0)
evens = ???


# Convert list of strings to uppercase: ["HELLO", "WORLD"]
words = ["hello", "world"]
upper_words = ???


# Exercise 3.2: List comprehension with condition (filter)

numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

# Get only positive numbers: [1, 3, 5, 7, 9]
positives = ???

# Get only negative numbers as absolute values: [2, 4, 6, 8, 10]
abs_negatives = ???

# Get numbers greater than 0 and less than 5: [1, 3]
small_positives = ???


# Exercise 3.3: Comprehension with transformation and filter

# Get squares of even numbers only
# [4, 16, 36, 64, 100] (squares of 2, 4, 6, 8, 10)
even_squares = ???


# Get lengths of words with more than 3 characters
words_list = ["hi", "hello", "hey", "howdy", "yo", "greetings"]
long_word_lengths = ???  # [5, 5, 9] (lengths of "hello", "howdy", "greetings")


# Exercise 3.4: Nested comprehensions

# Flatten a 2D list: [[1,2], [3,4], [5,6]] -> [1, 2, 3, 4, 5, 6]
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = ???  # [item for row in matrix for item in row]


# Create a 3x3 matrix of zeros
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
zeros_matrix = ???


# Create multiplication table rows
# [[1,2,3,4,5], [2,4,6,8,10], [3,6,9,12,15]]
mult_rows = ???  # 3x5 multiplication table


# Exercise 3.5: Dictionary comprehensions

# Create dict mapping numbers to their squares: {1: 1, 2: 4, 3: 9, ...}
num_to_square = ???  # for numbers 1-5


# Invert a dictionary: {"a": 1, "b": 2} -> {1: "a", 2: "b"}
original = {"a": 1, "b": 2, "c": 3}
inverted = ???


# Create dict from two lists using zip
keys = ["name", "age", "city"]
values = ["Alice", 30, "NYC"]
person_dict = ???


# Filter dictionary: keep only items where value > 50
scores = {"Alice": 85, "Bob": 42, "Charlie": 91, "Diana": 38}
passing = ???  # {"Alice": 85, "Charlie": 91}


# Exercise 3.6: Set comprehensions

# Get unique first letters from words
words_set = ["apple", "apricot", "banana", "blueberry", "cherry"]
first_letters = ???  # {'a', 'b', 'c'}


# Get all unique vowels in a string
text = "Hello World, How Are You?"
unique_vowels = ???  # Should be a set of vowels found


# Exercise 3.7: Generator expressions
# Like list comprehensions but with () - lazy evaluation
# More memory efficient for large sequences

# Create a generator of squares (use parentheses, not brackets)
square_gen = ???  # (x**2 for x in range(1, 6))

# Sum of squares using generator (more efficient than list)
sum_of_squares = sum(???)  # sum(x**2 for x in range(1, 11))


# Exercise 3.8: Comprehension with multiple conditions

# Get numbers divisible by both 2 and 3 (i.e., by 6)
divisible_by_6 = ???  # from range(1, 31), should be [6, 12, 18, 24, 30]


# FizzBuzz using comprehension!
# For numbers 1-15: "Fizz" if divisible by 3, "Buzz" if by 5,
# "FizzBuzz" if by both, else the number as string
fizzbuzz = [
    ???
    for n in range(1, 16)
]
# Should be: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]


# Exercise 3.9: Walrus operator in comprehensions (Python 3.8+)
# Useful when you need to compute something once and use multiple times

# Get lengths of words only if length > 3, but also include the length
# [(word, length), ...] for words where length > 3
sample_words = ["hi", "hello", "hey", "magnificent", "yo"]
long_with_length = ???
# Hint: [(word, length) for word in sample_words if (length := len(word)) > 3]
# Should be: [("hello", 5), ("magnificent", 11)]


# Exercise 3.10: Complex comprehension practice

# Parse "key=value" strings into dictionary
# ["name=Alice", "age=30"] -> {"name": "Alice", "age": "30"}
pairs = ["name=Alice", "age=30", "city=NYC"]
parsed = ???


# Group by first letter: {"a": ["apple", "avocado"], "b": ["banana"], ...}
# This is tricky! You might need to use set comprehension first
fruits = ["apple", "avocado", "banana", "blueberry", "cherry", "coconut"]
# Hint: First get unique first letters, then filter fruits for each
grouped = ???


# ============= TESTS (Don't modify below) =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 3.1
    assert squares == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert evens == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    assert upper_words == ["HELLO", "WORLD"]
    print("✓ Exercise 3.1 passed")

    # Test 3.2
    assert positives == [1, 3, 5, 7, 9]
    assert abs_negatives == [2, 4, 6, 8, 10]
    assert small_positives == [1, 3]
    print("✓ Exercise 3.2 passed")

    # Test 3.3
    assert even_squares == [4, 16, 36, 64, 100]
    assert long_word_lengths == [5, 5, 9]
    print("✓ Exercise 3.3 passed")

    # Test 3.4
    assert flattened == [1, 2, 3, 4, 5, 6]
    assert zeros_matrix == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert mult_rows == [[1,2,3,4,5], [2,4,6,8,10], [3,6,9,12,15]]
    print("✓ Exercise 3.4 passed")

    # Test 3.5
    assert num_to_square == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    assert inverted == {1: "a", 2: "b", 3: "c"}
    assert person_dict == {"name": "Alice", "age": 30, "city": "NYC"}
    assert passing == {"Alice": 85, "Charlie": 91}
    print("✓ Exercise 3.5 passed")

    # Test 3.6
    assert first_letters == {"a", "b", "c"}
    assert unique_vowels == {"e", "o", "a", "u"} or unique_vowels == {"E", "o", "A", "e", "O", "a", "U", "u"}  # case may vary
    print("✓ Exercise 3.6 passed")

    # Test 3.7
    import types
    assert isinstance(square_gen, types.GeneratorType), "square_gen should be a generator"
    assert sum_of_squares == 385  # 1+4+9+...+100
    print("✓ Exercise 3.7 passed")

    # Test 3.8
    assert divisible_by_6 == [6, 12, 18, 24, 30]
    assert fizzbuzz == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    print("✓ Exercise 3.8 passed")

    # Test 3.9
    assert long_with_length == [("hello", 5), ("magnificent", 11)]
    print("✓ Exercise 3.9 passed")

    # Test 3.10
    assert parsed == {"name": "Alice", "age": "30", "city": "NYC"}
    assert grouped == {"a": ["apple", "avocado"], "b": ["banana", "blueberry"], "c": ["cherry", "coconut"]}
    print("✓ Exercise 3.10 passed")

    print("\n🎉 All tests passed! Great job!")
