"""
Exercise 3: Tuples and Sets
============================

Tuples and Sets are Python collections with no direct JavaScript equivalent.

TUPLES:
- Immutable lists (can't be changed after creation)
- Use parentheses: (1, 2, 3)
- Great for fixed data like coordinates, RGB values
- Can be dictionary keys (unlike lists)
- JavaScript equivalent: Object.freeze([1, 2, 3]) kind of

SETS:
- Unordered collection of unique values
- Use braces: {1, 2, 3}
- Like JavaScript Set: new Set([1, 2, 3])
- Great for removing duplicates, membership testing, set operations

EXERCISES:
Complete each exercise below. Run with: python3 03_tuples_sets.py
"""


# ============= TUPLES =============

# Exercise 3.1: Creating tuples

# Create a tuple called 'coordinates' with values (10, 20, 30)
coordinates = ???

# Create a single-element tuple (needs trailing comma!)
# Note: (1) is just parentheses, (1,) is a tuple
single = ???  # Should be a tuple containing just the number 42

# Create a tuple without parentheses (Python allows this)
# This is called "tuple packing"
point = ???  # Should be (5, 10) but without using parentheses


# Exercise 3.2: Tuple operations

rgb = (255, 128, 0)

# Access the first element (red)
red = ???

# Unpack the tuple into r, g, b variables
r, g, b = ???

# Tuples are immutable - this would raise TypeError:
# rgb[0] = 200  # Can't do this!

# But you can create a new tuple with different values
# Create new_rgb with red=200, keep green and blue
new_rgb = ???  # Should be (200, 128, 0)


# Exercise 3.3: Tuple as dictionary key
# Lists can't be dictionary keys, but tuples can!

# Create a dictionary that maps coordinate tuples to location names
locations = ???  # {(0, 0): "origin", (10, 20): "point A"}

# Access the location at (0, 0)
origin_name = ???


# Exercise 3.4: Named tuples (like lightweight classes)
# More readable than regular tuples
from collections import namedtuple

# Create a named tuple type called 'Person' with fields: name, age, city
Person = namedtuple('Person', ???)

# Create a Person instance
alice = Person(name="Alice", age=30, city="NYC")

# Access fields by name (more readable than alice[0])
alice_name = alice.name
alice_age = ???
alice_city = ???


# ============= SETS =============

# Exercise 3.5: Creating sets

# Create a set with values 1, 2, 3, 4, 5
numbers_set = ???

# Create a set from a list with duplicates (duplicates removed automatically)
# List: [1, 2, 2, 3, 3, 3, 4]
unique_numbers = ???  # Should be {1, 2, 3, 4}

# Create an empty set (note: {} creates an empty dict, not set!)
empty_set = ???


# Exercise 3.6: Set operations

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union: all elements from both sets
# JavaScript: new Set([...a, ...b])
union = ???  # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection: elements in both sets
intersection = ???  # {4, 5}

# Difference: elements in A but not in B
difference = ???  # {1, 2, 3}

# Symmetric difference: elements in either but not both
symmetric_diff = ???  # {1, 2, 3, 6, 7, 8}


# Exercise 3.7: Set methods

fruits_set = {"apple", "banana"}

# Add "cherry" to the set
???

# Try to add "apple" again (sets ignore duplicates)
???

# Remove "banana" from the set
???

# Check if "apple" is in the set
has_apple = ???

# After operations, fruits_set should be {"apple", "cherry"}


# Exercise 3.8: Practical set usage

# Remove duplicates from a list while preserving some order
# (Note: regular set doesn't preserve order)
items_with_dupes = ["b", "a", "b", "c", "a", "d", "c"]

# Use dict.fromkeys() to remove duplicates while preserving first-occurrence order
unique_ordered = ???  # Should be ["b", "a", "c", "d"]

# Find common elements between two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = ???  # Should be {4, 5} (use set intersection)


# Exercise 3.9: Set comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a set of squares of even numbers
# Should be {4, 16, 36, 64, 100}
even_squares = ???


# Exercise 3.10: Frozenset (immutable set)
# Like tuple is to list, frozenset is to set
# Can be used as dictionary keys

# Create a frozenset from {1, 2, 3}
frozen = ???

# Use frozensets as dictionary keys
permission_sets = {
    frozenset({"read"}): "viewer",
    frozenset({"read", "write"}): "editor",
    frozenset({"read", "write", "delete"}): "admin"
}

# Look up the role for {"read", "write"} permissions
editor_role = permission_sets[frozenset({"read", "write"})]


# ============= TESTS (Don't modify below) =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 3.1
    assert coordinates == (10, 20, 30), "coordinates should be (10, 20, 30)"
    assert single == (42,), "single should be (42,) - don't forget the comma!"
    assert point == (5, 10), "point should be (5, 10)"
    print("✓ Exercise 3.1 passed")

    # Test 3.2
    assert red == 255, "red should be 255"
    assert (r, g, b) == (255, 128, 0), "r, g, b should be unpacked correctly"
    assert new_rgb == (200, 128, 0), "new_rgb should be (200, 128, 0)"
    print("✓ Exercise 3.2 passed")

    # Test 3.3
    assert locations[(0, 0)] == "origin", "locations[(0, 0)] should be 'origin'"
    assert origin_name == "origin", "origin_name should be 'origin'"
    print("✓ Exercise 3.3 passed")

    # Test 3.4
    assert alice_age == 30, "alice_age should be 30"
    assert alice_city == "NYC", "alice_city should be 'NYC'"
    print("✓ Exercise 3.4 passed")

    # Test 3.5
    assert numbers_set == {1, 2, 3, 4, 5}, "numbers_set incorrect"
    assert unique_numbers == {1, 2, 3, 4}, "unique_numbers incorrect"
    assert empty_set == set() and isinstance(empty_set, set), "empty_set should be set()"
    print("✓ Exercise 3.5 passed")

    # Test 3.6
    assert union == {1, 2, 3, 4, 5, 6, 7, 8}, "union incorrect"
    assert intersection == {4, 5}, "intersection incorrect"
    assert difference == {1, 2, 3}, "difference incorrect"
    assert symmetric_diff == {1, 2, 3, 6, 7, 8}, "symmetric_diff incorrect"
    print("✓ Exercise 3.6 passed")

    # Test 3.7
    assert fruits_set == {"apple", "cherry"}, "fruits_set should be {'apple', 'cherry'}"
    assert has_apple == True, "has_apple should be True"
    print("✓ Exercise 3.7 passed")

    # Test 3.8
    assert unique_ordered == ["b", "a", "c", "d"], "unique_ordered incorrect"
    assert common == {4, 5}, "common should be {4, 5}"
    print("✓ Exercise 3.8 passed")

    # Test 3.9
    assert even_squares == {4, 16, 36, 64, 100}, "even_squares incorrect"
    print("✓ Exercise 3.9 passed")

    # Test 3.10
    assert frozen == frozenset({1, 2, 3}), "frozen incorrect"
    assert editor_role == "editor", "editor_role should be 'editor'"
    print("✓ Exercise 3.10 passed")

    print("\n🎉 All tests passed! Great job!")
