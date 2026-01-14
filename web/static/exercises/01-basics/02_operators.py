"""
Exercise 2: Operators
======================

Python operators are similar to JavaScript with a few key differences.

Key differences from JavaScript:
- No === (Python == doesn't do type coercion)
- 'and', 'or', 'not' instead of &&, ||, !
- ** for exponentiation (not Math.pow())
- // for integer division
- 'in' for membership testing
- 'is' for identity comparison

EXERCISES:
Complete each exercise below. Run with: python3 02_operators.py
"""


# Exercise 2.1: Arithmetic operators
# Most are the same as JS: +, -, *, /
# New ones: ** (power), // (integer division), % (modulo)

# Calculate 2 to the power of 10 using **
power_result = ???

# Divide 17 by 5 using regular division (should give 3.4)
regular_division = ???

# Divide 17 by 5 using integer division // (should give 3)
integer_division = ???

# Get the remainder of 17 divided by 5 using %
remainder = ???


# Exercise 2.2: Comparison operators
# Python uses == for equality (no ===, Python doesn't coerce types)
#
# JavaScript: 5 == "5" is true, 5 === "5" is false
# Python: 5 == "5" is False (no coercion!)

# Check if 10 is equal to 10.0 (different types, same value)
int_float_equal = ???  # True or False?

# Check if "5" is equal to 5
string_int_equal = ???  # True or False?

# Check if 10 is not equal to 5
not_equal = ???  # Use !=


# Exercise 2.3: Logical operators
# JavaScript: && || !
# Python: and, or, not

a = True
b = False

# Use 'and' - both must be True
and_result = ???  # a and b

# Use 'or' - at least one must be True
or_result = ???  # a or b

# Use 'not' - negate the value
not_result = ???  # not a


# Exercise 2.4: Identity vs Equality
# == checks if values are equal
# 'is' checks if they're the same object in memory
#
# JavaScript equivalent: === checks both value and type
# Python 'is' is stricter - checks actual object identity

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# Are list1 and list2 equal in value?
equal_value = ???  # Use ==

# Are list1 and list2 the same object?
same_object_1_2 = ???  # Use 'is'

# Are list1 and list3 the same object?
same_object_1_3 = ???  # Use 'is'

# Important: Always use 'is' when comparing to None
value = None
is_none = ???  # value is None


# Exercise 2.5: Membership operator 'in'
# Python has a handy 'in' operator (like JS .includes())
#
# JavaScript: [1,2,3].includes(2) // true
# Python: 2 in [1,2,3]  # True

numbers = [1, 2, 3, 4, 5]

# Check if 3 is in numbers
three_in_list = ???

# Check if 10 is NOT in numbers (use 'not in')
ten_not_in_list = ???

# 'in' also works with strings
message = "Hello, Python!"

# Check if "Python" is in message
python_in_message = ???

# 'in' works with dictionaries (checks keys)
person = {"name": "Alice", "age": 30}

# Check if "name" is a key in person
name_in_dict = ???

# Check if "Alice" is a key in person (it's a value, not a key!)
alice_in_dict = ???


# Exercise 2.6: Walrus operator := (Python 3.8+)
# Assigns and returns a value in one expression
# No direct JS equivalent (closest is assignment in conditions, which is discouraged)

# Example: if (n := len(some_list)) > 5:
# This assigns len(some_list) to n AND checks if n > 5

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use the walrus operator to assign len(data) to 'length' and check if > 5
# Complete this expression:
if (length := ???) > 5:
    result_walrus = f"List has {length} items"
else:
    result_walrus = "List is short"


# ============= TESTS (Don't modify below) =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 2.1
    assert power_result == 1024, "2 ** 10 should be 1024"
    assert regular_division == 3.4, "17 / 5 should be 3.4"
    assert integer_division == 3, "17 // 5 should be 3"
    assert remainder == 2, "17 % 5 should be 2"
    print("✓ Exercise 2.1 passed")

    # Test 2.2
    assert int_float_equal == True, "10 == 10.0 should be True"
    assert string_int_equal == False, "'5' == 5 should be False in Python"
    assert not_equal == True, "10 != 5 should be True"
    print("✓ Exercise 2.2 passed")

    # Test 2.3
    assert and_result == False, "True and False should be False"
    assert or_result == True, "True or False should be True"
    assert not_result == False, "not True should be False"
    print("✓ Exercise 2.3 passed")

    # Test 2.4
    assert equal_value == True, "[1,2,3] == [1,2,3] should be True"
    assert same_object_1_2 == False, "list1 is list2 should be False"
    assert same_object_1_3 == True, "list1 is list3 should be True"
    assert is_none == True, "None is None should be True"
    print("✓ Exercise 2.4 passed")

    # Test 2.5
    assert three_in_list == True, "3 in [1,2,3,4,5] should be True"
    assert ten_not_in_list == True, "10 not in [1,2,3,4,5] should be True"
    assert python_in_message == True, "'Python' in message should be True"
    assert name_in_dict == True, "'name' in person should be True"
    assert alice_in_dict == False, "'Alice' is a value, not a key"
    print("✓ Exercise 2.5 passed")

    # Test 2.6
    assert length == 10, "length should be 10"
    assert "10 items" in result_walrus, "result should mention 10 items"
    print("✓ Exercise 2.6 passed")

    print("\n🎉 All tests passed! Great job!")
