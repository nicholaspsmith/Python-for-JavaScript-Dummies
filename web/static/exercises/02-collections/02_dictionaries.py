"""
Exercise 2: Dictionaries
=========================

Python dictionaries are like JavaScript objects - key-value stores.

JavaScript: const obj = { name: "Alice", age: 30 };
Python: obj = {"name": "Alice", "age": 30}

Key differences:
- Keys must be quoted (no shorthand like JS)
- Use dict["key"] or dict.get("key") to access (not dict.key)
- Keys can be any hashable type (strings, numbers, tuples)
- Dictionaries are ordered (Python 3.7+)

EXERCISES:
Complete each exercise below. Run with: python3 02_dictionaries.py
"""


# Exercise 2.1: Creating and accessing dictionaries

# Create a dictionary called 'person' with:
# - name: "Alice"
# - age: 30
# - city: "New York"
person = ???

# Access 'name' using bracket notation
name = ???

# Access 'age' using .get() method
age = ???

# Try to access 'country' using .get() with default value "Unknown"
# (This is safer than bracket notation - won't raise KeyError)
country = ???


# Exercise 2.2: Modifying dictionaries

user = {"username": "alice", "email": "alice@example.com"}

# Add a new key 'role' with value "admin"
???

# Update 'email' to "alice@newdomain.com"
???

# Remove 'username' and store its value (like delete in JS, but returns value)
removed_username = ???  # Use .pop()

# After these operations, user should have: email, role


# Exercise 2.3: Dictionary methods

inventory = {"apples": 10, "bananas": 5, "oranges": 8}

# Get all keys as a list
keys = ???  # Use list() to convert dict_keys to list

# Get all values as a list
values = ???

# Get all key-value pairs as a list of tuples
items = ???  # Each item is (key, value)

# Check if 'apples' is a key
has_apples = ???  # Use 'in' operator


# Exercise 2.4: Dictionary iteration
# In JS: Object.entries(obj).forEach(([key, value]) => ...)
# In Python: for key, value in dict.items():

scores = {"math": 90, "science": 85, "english": 88}

# Create a list of formatted strings: ["math: 90", "science: 85", "english: 88"]
# Hint: Use a for loop or list comprehension
formatted_scores = ???


# Exercise 2.5: Merging dictionaries
# JavaScript: { ...obj1, ...obj2 }
# Python: {**dict1, **dict2} or dict1 | dict2 (Python 3.9+)

defaults = {"theme": "light", "language": "en", "timezone": "UTC"}
user_prefs = {"theme": "dark", "language": "es"}

# Merge dictionaries (user_prefs should override defaults)
# Result: {"theme": "dark", "language": "es", "timezone": "UTC"}
merged = ???


# Exercise 2.6: Dictionary comprehension
# Like JS: Object.fromEntries(arr.map(([k, v]) => [k, v * 2]))
# Python: {k: v * 2 for k, v in dict.items()}

prices = {"apple": 1.0, "banana": 0.5, "orange": 0.75}

# Create a new dict with prices doubled
doubled_prices = ???

# Create a dict of only items with price >= 0.75
expensive = ???


# Exercise 2.7: Nested dictionaries

company = {
    "name": "TechCorp",
    "employees": {
        "alice": {"role": "developer", "salary": 80000},
        "bob": {"role": "designer", "salary": 70000}
    }
}

# Get Alice's role
alice_role = ???

# Get Bob's salary
bob_salary = ???

# Add a new employee "charlie" with role "manager" and salary 90000
???


# Exercise 2.8: .get() vs .setdefault() vs defaultdict
# Three ways to handle missing keys:
# 1. .get(key, default) - returns default but doesn't modify dict
# 2. .setdefault(key, default) - returns value AND inserts default if missing
# 3. defaultdict(factory) - automatically creates default values

# Part A: Use .get() to safely access with defaults
# .get() returns the default but DOESN'T modify the dictionary
config = {"theme": "dark", "language": "en"}

# Get 'theme' value, or "light" if missing
theme_value = ???  # Use config.get()

# Get 'timeout' value, or 30 if missing (config won't be modified)
timeout_value = ???  # Use config.get()

# Verify: 'timeout' should NOT be in config after using .get()


# Part B: Use .setdefault() to get-or-create
# .setdefault() returns the value AND inserts the default if key was missing
user_settings = {"name": "Alice"}

# Get 'name' value using setdefault (key exists, so just returns value)
name_from_setdefault = ???  # Use user_settings.setdefault()

# Get 'role' value using setdefault with default "guest"
# This WILL add 'role' to the dict since it's missing
role_from_setdefault = ???  # Use user_settings.setdefault()

# After this, user_settings should have both 'name' and 'role' keys


# Part C: Use .setdefault() for grouping pattern
# Group words by their first letter: {"a": ["apple", "apricot"], "b": ["banana"], ...}
words_to_group = ["apple", "banana", "apricot", "blueberry", "cherry"]
grouped_words = {}

for word in words_to_group:
    first_letter = word[0]
    # Use setdefault to get-or-create the list, then append
    ???  # grouped_words.setdefault(first_letter, []).append(word)


# Part D: Count words using .get() pattern (alternative to setdefault)
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = {}

for word in words:
    # Use .get() with default 0, then add 1
    word_count[word] = ???  # word_count.get(word, 0) + 1

# word_count should be {"apple": 3, "banana": 2, "cherry": 1}


# ============= TESTS (Don't modify below) =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 2.1
    assert person == {"name": "Alice", "age": 30, "city": "New York"}
    assert name == "Alice"
    assert age == 30
    assert country == "Unknown"
    print("✓ Exercise 2.1 passed")

    # Test 2.2
    assert "role" in user and user["role"] == "admin"
    assert user["email"] == "alice@newdomain.com"
    assert removed_username == "alice"
    assert "username" not in user
    print("✓ Exercise 2.2 passed")

    # Test 2.3
    assert set(keys) == {"apples", "bananas", "oranges"}
    assert sorted(values) == [5, 8, 10]
    assert len(items) == 3
    assert has_apples == True
    print("✓ Exercise 2.3 passed")

    # Test 2.4
    assert set(formatted_scores) == {"math: 90", "science: 85", "english: 88"}
    print("✓ Exercise 2.4 passed")

    # Test 2.5
    assert merged == {"theme": "dark", "language": "es", "timezone": "UTC"}
    print("✓ Exercise 2.5 passed")

    # Test 2.6
    assert doubled_prices == {"apple": 2.0, "banana": 1.0, "orange": 1.5}
    assert expensive == {"apple": 1.0, "orange": 0.75}
    print("✓ Exercise 2.6 passed")

    # Test 2.7
    assert alice_role == "developer"
    assert bob_salary == 70000
    assert company["employees"]["charlie"] == {"role": "manager", "salary": 90000}
    print("✓ Exercise 2.7 passed")

    # Test 2.8 Part A - .get()
    assert theme_value == "dark", "theme_value should be 'dark'"
    assert timeout_value == 30, "timeout_value should be 30 (default)"
    assert "timeout" not in config, ".get() should NOT modify the dictionary"
    # Test 2.8 Part B - .setdefault()
    assert name_from_setdefault == "Alice", "setdefault returns existing value"
    assert role_from_setdefault == "guest", "setdefault returns default for missing key"
    assert user_settings.get("role") == "guest", "setdefault SHOULD add key to dict"
    # Test 2.8 Part C - grouping with setdefault
    assert grouped_words == {"a": ["apple", "apricot"], "b": ["banana", "blueberry"], "c": ["cherry"]}
    # Test 2.8 Part D - counting with .get()
    assert word_count == {"apple": 3, "banana": 2, "cherry": 1}
    print("✓ Exercise 2.8 passed")

    print("\n🎉 All tests passed! Great job!")
