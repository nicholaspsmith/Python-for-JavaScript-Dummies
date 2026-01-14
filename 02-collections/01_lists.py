"""
Exercise 1: Lists
==================

Python lists are like JavaScript arrays - ordered, mutable collections.

JavaScript: const arr = [1, 2, 3];
Python: arr = [1, 2, 3]

Key differences:
- Python uses negative indexing: arr[-1] is the last element
- Slicing syntax: arr[start:end:step]
- Different method names (append vs push, etc.)

EXERCISES:
Complete each exercise below. Run with: python3 01_lists.py
"""


# Exercise 1.1: Creating and accessing lists
# Python lists can hold mixed types (like JS arrays)

# Create a list called 'mixed' with: 1, "two", 3.0, True, None
mixed = ???

# Get the first element
first = ???

# Get the last element using negative indexing (not len()-1)
last = ???

# Get the second-to-last element
second_to_last = ???


# Exercise 1.2: Slicing
# Python has powerful slicing: list[start:end:step]
# - start is inclusive, end is exclusive
# - omit start to start from beginning
# - omit end to go to the end
# - step is optional (default 1)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements from index 2 to 5 (exclusive), should be [2, 3, 4]
slice_1 = ???

# Get first 3 elements [0, 1, 2]
slice_2 = ???

# Get last 3 elements [7, 8, 9]
slice_3 = ???

# Get every other element [0, 2, 4, 6, 8]
every_other = ???

# Reverse the list using slicing [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
reversed_list = ???


# Exercise 1.3: List methods
# JavaScript -> Python method mapping:
# push() -> append()
# pop() -> pop()
# shift() -> pop(0)
# unshift() -> insert(0, item)
# splice() -> no direct equivalent, use slicing
# indexOf() -> index()
# includes() -> 'in' operator

fruits = ["apple", "banana"]

# Add "cherry" to the end (like push)
???

# Add "apricot" to the beginning (like unshift)
???

# Remove and return the last element (like pop)
removed_last = ???

# Remove and return the first element (like shift)
removed_first = ???

# After these operations, fruits should be ["banana"]


# Exercise 1.4: List operations

list_a = [1, 2, 3]
list_b = [4, 5, 6]

# Concatenate lists (like [...a, ...b] in JS)
concatenated = ???  # Should be [1, 2, 3, 4, 5, 6]

# Repeat a list (no JS equivalent)
repeated = ???  # [1, 2, 3] repeated 3 times = [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Get length of a list
length = ???

# Check if 2 is in list_a
contains_two = ???


# Exercise 1.5: List unpacking (like JS destructuring)
#
# JavaScript: const [first, second, ...rest] = arr;
# Python: first, second, *rest = arr

coordinates = [10, 20, 30, 40, 50]

# Unpack first two elements and collect rest
# x should be 10, y should be 20, remaining should be [30, 40, 50]
x, y, *remaining = ???

# Unpack first and last, ignore middle
# first_coord should be 10, last_coord should be 50
first_coord, *_, last_coord = ???


# Exercise 1.6: List sorting
# Python has in-place sort() and returns-new-list sorted()

unsorted = [3, 1, 4, 1, 5, 9, 2, 6]

# Create a NEW sorted list (original unchanged) - use sorted()
sorted_new = ???

# Sort in place (modifies original) - use .sort()
to_sort = [3, 1, 4, 1, 5, 9, 2, 6]
???  # Sort to_sort in place

# Sort in reverse order
reverse_sorted = ???  # Use sorted() with reverse=True


# ============= TESTS (Don't modify below) =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1.1
    assert mixed == [1, "two", 3.0, True, None], "mixed list is incorrect"
    assert first == 1, "first should be 1"
    assert last == None, "last should be None"
    assert second_to_last == True, "second_to_last should be True"
    print("✓ Exercise 1.1 passed")

    # Test 1.2
    assert slice_1 == [2, 3, 4], "slice_1 should be [2, 3, 4]"
    assert slice_2 == [0, 1, 2], "slice_2 should be [0, 1, 2]"
    assert slice_3 == [7, 8, 9], "slice_3 should be [7, 8, 9]"
    assert every_other == [0, 2, 4, 6, 8], "every_other should be [0, 2, 4, 6, 8]"
    assert reversed_list == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], "reversed_list incorrect"
    print("✓ Exercise 1.2 passed")

    # Test 1.3
    assert fruits == ["banana"], "fruits should be ['banana'] after operations"
    assert removed_last == "cherry", "removed_last should be 'cherry'"
    assert removed_first == "apricot", "removed_first should be 'apricot'"
    print("✓ Exercise 1.3 passed")

    # Test 1.4
    assert concatenated == [1, 2, 3, 4, 5, 6], "concatenated incorrect"
    assert repeated == [1, 2, 3, 1, 2, 3, 1, 2, 3], "repeated incorrect"
    assert length == 3, "length should be 3"
    assert contains_two == True, "contains_two should be True"
    print("✓ Exercise 1.4 passed")

    # Test 1.5
    assert x == 10, "x should be 10"
    assert y == 20, "y should be 20"
    assert remaining == [30, 40, 50], "remaining should be [30, 40, 50]"
    assert first_coord == 10, "first_coord should be 10"
    assert last_coord == 50, "last_coord should be 50"
    print("✓ Exercise 1.5 passed")

    # Test 1.6
    assert sorted_new == [1, 1, 2, 3, 4, 5, 6, 9], "sorted_new incorrect"
    assert to_sort == [1, 1, 2, 3, 4, 5, 6, 9], "to_sort should be sorted in place"
    assert reverse_sorted == [9, 6, 5, 4, 3, 2, 1, 1], "reverse_sorted incorrect"
    print("✓ Exercise 1.6 passed")

    print("\n🎉 All tests passed! Great job!")
