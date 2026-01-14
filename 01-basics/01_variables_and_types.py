"""
Exercise 1: Variables and Types
================================

In JavaScript, you declare variables with const, let, or var.
In Python, you just assign directly - no keyword needed.

JavaScript:
    const name = "Alice";
    let age = 30;
    var isActive = true;

Python:
    name = "Alice"
    age = 30
    is_active = True

Key differences:
- Python uses snake_case by convention (not camelCase)
- Boolean values are True/False (capitalized)
- None instead of null (no undefined)
- No semicolons needed

EXERCISES:
Complete each exercise below. Run this file with: python3 01_variables_and_types.py
"""


# Exercise 1.1: Create variables
# Create the following variables:
# - A string variable called 'greeting' with value "Hello, Python!"
# - An integer variable called 'year' with value 2026
# - A float variable called 'pi_value' with value 3.14159
# - A boolean variable called 'is_learning' with value True
# - A variable called 'nothing' with value None

# YOUR CODE HERE:
greeting = "Hello, Python!"  # Replace None with your answer
year = 2026
pi_value = 3.14159
is_learning = True
nothing = None


# Exercise 1.2: Type checking
# In JS you use typeof. In Python, use type() or isinstance()
#
# JavaScript: typeof "hello" === "string"
# Python: type("hello") == str  OR  isinstance("hello", str)
#
# When to use each:
# - type(x) returns the exact type of x (useful for exact matching)
# - isinstance(x, Type) returns True/False (works with inheritance, multiple types)

# Part A: Use type() to get the exact type of each value
# Example: type("hello") returns <class 'str'>, which equals str

hello_type = ???          # Use type() on "hello"
answer_type = ???         # Use type() on 42
pi_type = ???             # Use type() on 3.14
flag_type = ???           # Use type() on True
empty_type = ???          # Use type() on None

# Part B: Use isinstance() to check types (returns True or False)
# Example: isinstance("hello", str) returns True
# Bonus: isinstance(x, (type1, type2)) checks multiple types!

is_string = ???           # Is "hello" a str?
is_integer = ???          # Is 3.14 an int? (Hint: it's not!)
is_numeric = ???          # Is 42 either an int OR float? Use isinstance with tuple: (int, float)
is_none = ???             # Is None a NoneType? (Hint: use type(None) as the type to check)


# Exercise 1.3: Type conversion
# Convert between types using int(), float(), str(), bool()
#
# JavaScript: String(42), Number("42"), Boolean(1)
# Python: str(42), int("42"), bool(1)

number_string = "42"
# Convert number_string to an integer and store in 'converted_int'
converted_int = ???

float_number = 3.99
# Convert float_number to an integer (note: this truncates, doesn't round!)
truncated_int = ???

some_number = 0
# Convert some_number to a boolean (0 is falsy in Python too)
zero_as_bool = ???

non_zero = 42
# Convert non_zero to a boolean
nonzero_as_bool = ???


# Exercise 1.4: String operations
# Python strings are similar to JS but with some differences
#
# JavaScript: `Hello, ${name}!` (template literals)
# Python: f"Hello, {name}!" (f-strings, Python 3.6+)

name = "World"
# Create an f-string that says "Hello, World!" using the name variable
f_string_greeting = ???

# Python also supports these (older styles):
# "Hello, {}!".format(name)
# "Hello, %s!" % name

# Multi-line strings use triple quotes
# Create a multi-line string with three lines: "Line 1", "Line 2", "Line 3"
multi_line = ???


# Exercise 1.5: String methods
# Python strings have similar methods to JS

text = "  Hello, Python!  "

# Use .strip() to remove whitespace (like JS .trim())
stripped = ???

# Use .lower() to convert to lowercase
lowered = ???

# Use .replace() to replace "Python" with "JavaScript"
replaced = ???

# Use .split(", ") to split into a list (like JS .split())
parts = "apple, banana, cherry"
split_list = ???


# ============= TESTS (Don't modify below) =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1.1
    assert greeting == "Hello, Python!", "greeting should be 'Hello, Python!'"
    assert year == 2026, "year should be 2026"
    assert pi_value == 3.14159, "pi_value should be 3.14159"
    assert is_learning == True, "is_learning should be True"
    assert nothing is None, "nothing should be None"
    print("✓ Exercise 1.1 passed")

    # Test 1.2 Part A - type()
    assert hello_type == str, "hello_type should be str (use type('hello'))"
    assert answer_type == int, "answer_type should be int (use type(42))"
    assert pi_type == float, "pi_type should be float (use type(3.14))"
    assert flag_type == bool, "flag_type should be bool (use type(True))"
    assert empty_type == type(None), "empty_type should be NoneType (use type(None))"
    # Test 1.2 Part B - isinstance()
    assert is_string == True, "is_string should be True (isinstance('hello', str))"
    assert is_integer == False, "is_integer should be False (3.14 is not an int!)"
    assert is_numeric == True, "is_numeric should be True (use isinstance(42, (int, float)))"
    assert is_none == True, "is_none should be True (isinstance(None, type(None)))"
    print("✓ Exercise 1.2 passed")

    # Test 1.3
    assert converted_int == 42, "converted_int should be 42"
    assert truncated_int == 3, "truncated_int should be 3 (truncated, not rounded)"
    assert zero_as_bool == False, "zero_as_bool should be False"
    assert nonzero_as_bool == True, "nonzero_as_bool should be True"
    print("✓ Exercise 1.3 passed")

    # Test 1.4
    assert f_string_greeting == "Hello, World!", "f_string_greeting should be 'Hello, World!'"
    assert "Line 1" in multi_line and "Line 2" in multi_line and "Line 3" in multi_line
    print("✓ Exercise 1.4 passed")

    # Test 1.5
    assert stripped == "Hello, Python!", "stripped should have no leading/trailing spaces"
    assert lowered == "  hello, python!  ", "lowered should be lowercase"
    assert replaced == "  Hello, JavaScript!  ", "replaced should have JavaScript"
    assert split_list == ["apple", "banana",
                          "cherry"], "split_list should be a list"
    print("✓ Exercise 1.5 passed")

    print("\n🎉 All tests passed! Great job!")
