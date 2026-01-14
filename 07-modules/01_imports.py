"""
Exercise 1: Imports and Modules
================================

Python's import system is different from JavaScript's ES modules.

JavaScript:
    import defaultExport from 'module';
    import { named } from 'module';
    import * as all from 'module';

Python:
    import module
    from module import something
    from module import *  # Avoid this!
    import module as alias

Key differences:
- Python has no default exports
- Import paths use dots: from package.subpackage import module
- __init__.py makes a directory a package
- Relative imports: from . import sibling, from .. import parent

EXERCISES:
Complete each exercise below. Run with: python3 01_imports.py
"""


# Exercise 1.1: Basic imports
# Import the entire math module
import math

# Use math.sqrt() to calculate square root of 16
sqrt_result = ???

# Use math.pi to get pi
pi_value = ???

# Use math.floor() and math.ceil() on 3.7
floor_result = ???
ceil_result = ???


# Exercise 1.2: Named imports
# Import specific items from modules
from math import sqrt, pi, floor, ceil

# Now you can use them directly without 'math.' prefix
direct_sqrt = sqrt(25)
direct_pi = pi


# Exercise 1.3: Import with alias
# JavaScript: import * as math from 'math';
# Python: import math as m

import random as rnd

# Use rnd.randint(1, 10) to get a random number between 1 and 10
# (We can't test randomness, so just make sure it runs)
random_number = rnd.randint(1, 10)


# Exercise 1.4: Common standard library modules
# Python has a rich standard library - "batteries included"

# datetime - for dates and times
from datetime import datetime, date, timedelta

# Get current date
today = ???  # Use date.today()

# Get current datetime
now = ???  # Use datetime.now()

# Create a date for January 1, 2024
new_year = ???  # Use date(year, month, day)


# collections - useful data structures
from collections import Counter, defaultdict, namedtuple

# Count occurrences in a list
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_counts = ???  # Use Counter(words)

# defaultdict with default value
scores = defaultdict(int)  # Default value is 0
scores["alice"] += 10
scores["bob"] += 5
# scores["charlie"] automatically becomes 0 when accessed


# json - JSON encoding/decoding
import json

data = {"name": "Alice", "age": 30}
# Convert dict to JSON string
json_string = ???  # Use json.dumps(data)

# Convert JSON string back to dict
parsed_data = ???  # Use json.loads(json_string)


# os and os.path / pathlib - file system operations
import os
from pathlib import Path

# Get current working directory
cwd = ???  # Use os.getcwd() or Path.cwd()

# Check if a path exists
home_exists = os.path.exists(os.path.expanduser("~"))


# Exercise 1.5: Understanding __name__
# __name__ is "__main__" when the script is run directly
# __name__ is the module name when imported

# This is why we use:
# if __name__ == "__main__":
#     # Code here only runs when script is executed directly
#     # Not when imported as a module


# Exercise 1.6: Creating and using your own module
# In real projects, you'd have multiple .py files

# Let's simulate a module structure:
# mypackage/
#   __init__.py
#   utils.py
#   models.py

# For this exercise, we'll define a simple "module" as a class
class MockModule:
    """Simulates a module with utility functions."""

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


# Imagine this is imported: from mypackage import utils
utils = MockModule()

# Use the "module"
add_result = utils.add(5, 3)
mult_result = utils.multiply(4, 7)


# Exercise 1.7: Conditional imports
# Sometimes you want different behavior based on availability

def get_yaml_parser():
    """
    Try to import PyYAML, fall back to a mock if not available.
    This pattern is common for optional dependencies.
    """
    try:
        import yaml
        return yaml
    except ImportError:
        # Return a mock or alternative
        class MockYAML:
            @staticmethod
            def safe_load(s):
                return {"mock": True}
        return MockYAML()


# Exercise 1.8: Lazy imports
# Import only when needed (useful for expensive imports)

def process_image(path):
    """
    Only import PIL when actually processing images.
    This speeds up module loading if PIL isn't always needed.
    """
    # Import inside function - only happens when function is called
    try:
        from PIL import Image
        # Would process image here
        return "PIL available"
    except ImportError:
        return "PIL not available"


# ============= TESTS (Don't modify below) =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1.1
    assert sqrt_result == 4.0, f"sqrt_result should be 4.0, got {sqrt_result}"
    assert abs(pi_value - 3.14159) < 0.001, "pi_value should be ~3.14159"
    assert floor_result == 3, "floor_result should be 3"
    assert ceil_result == 4, "ceil_result should be 4"
    print("✓ Exercise 1.1 passed")

    # Test 1.2
    assert direct_sqrt == 5.0
    assert abs(direct_pi - 3.14159) < 0.001
    print("✓ Exercise 1.2 passed")

    # Test 1.3
    assert 1 <= random_number <= 10
    print("✓ Exercise 1.3 passed")

    # Test 1.4
    assert isinstance(today, date)
    assert isinstance(now, datetime)
    assert new_year == date(2024, 1, 1)
    assert word_counts["apple"] == 3
    assert json_string == '{"name": "Alice", "age": 30}'
    assert parsed_data == {"name": "Alice", "age": 30}
    assert isinstance(cwd, (str, Path))
    print("✓ Exercise 1.4 passed")

    # Test 1.5
    assert __name__ == "__main__", "This script should be run directly"
    print("✓ Exercise 1.5 passed")

    # Test 1.6
    assert add_result == 8
    assert mult_result == 28
    print("✓ Exercise 1.6 passed")

    # Test 1.7
    yaml_parser = get_yaml_parser()
    assert yaml_parser is not None
    print("✓ Exercise 1.7 passed")

    # Test 1.8
    result = process_image("test.jpg")
    assert result in ["PIL available", "PIL not available"]
    print("✓ Exercise 1.8 passed")

    print("\n🎉 All tests passed! Great job!")
