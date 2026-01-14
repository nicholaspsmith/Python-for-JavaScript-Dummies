"""
Exercise 1: Conditionals
=========================

Python conditionals are similar to JavaScript but with different syntax.

JavaScript:
    if (condition) {
        // code
    } else if (other) {
        // code
    } else {
        // code
    }

Python:
    if condition:
        # code
    elif other:
        # code
    else:
        # code

Key differences:
- No parentheses required around condition
- Colon after condition
- Indentation instead of braces
- 'elif' instead of 'else if'
- 'and', 'or', 'not' instead of &&, ||, !

EXERCISES:
Complete each exercise below. Run with: python3 01_conditionals.py
"""


# Exercise 1.1: Basic if/elif/else

def get_grade(score):
    """
    Return letter grade based on score:
    90-100: "A"
    80-89: "B"
    70-79: "C"
    60-69: "D"
    Below 60: "F"
    """
    # YOUR CODE HERE
    pass


# Exercise 1.2: Truthiness
# Python has similar falsy values to JavaScript, but not identical
# Falsy in Python: False, None, 0, 0.0, "", [], {}, set()
# Note: In JS, [] and {} are truthy!

def is_truthy(value):
    """Return True if value is truthy, False if falsy."""
    # Hint: Use bool() or just 'if value'
    # YOUR CODE HERE
    pass


# Exercise 1.3: Ternary operator
# JavaScript: condition ? valueIfTrue : valueIfFalse
# Python: valueIfTrue if condition else valueIfFalse

def absolute_value(n):
    """Return absolute value using Python's ternary operator."""
    # YOUR CODE HERE (use ternary, not abs())
    pass


# Exercise 1.4: Multiple conditions

def can_vote(age, is_citizen, is_registered):
    """
    Return True if person can vote:
    - Must be 18 or older AND
    - Must be a citizen AND
    - Must be registered
    """
    # Use 'and' instead of &&
    # YOUR CODE HERE
    pass


def can_enter_club(age, has_id, is_vip):
    """
    Return True if person can enter club:
    - Must be 21+ with ID OR
    - Must be VIP (any age)
    """
    # Use 'or' instead of ||
    # YOUR CODE HERE
    pass


# Exercise 1.5: Chained comparisons
# Python allows: 0 < x < 10 (instead of 0 < x && x < 10)

def is_valid_percentage(value):
    """Return True if value is between 0 and 100 (inclusive)."""
    # Use chained comparison: 0 <= value <= 100
    # YOUR CODE HERE
    pass


def is_between(value, low, high):
    """Return True if low < value < high (exclusive on both ends)."""
    # YOUR CODE HERE
    pass


# Exercise 1.6: Match statement (Python 3.10+)
# Like JavaScript switch, but more powerful (structural pattern matching)
#
# JavaScript:
#   switch (status) {
#     case 200: return "OK";
#     default: return "Unknown";
#   }
#
# Python:
#   match status:
#       case 200:
#           return "OK"
#       case _:
#           return "Unknown"

def http_status_message(code):
    """
    Return message for HTTP status code using match statement:
    200 -> "OK"
    201 -> "Created"
    400 -> "Bad Request"
    401 -> "Unauthorized"
    404 -> "Not Found"
    500 -> "Internal Server Error"
    anything else -> "Unknown Status"
    """
    # YOUR CODE HERE (use match/case)
    pass


# Exercise 1.7: Pattern matching with match (advanced)

def describe_point(point):
    """
    Describe a point tuple using pattern matching:
    (0, 0) -> "origin"
    (0, y) -> "on y-axis"
    (x, 0) -> "on x-axis"
    (x, y) where x == y -> "on diagonal"
    (x, y) -> "point at (x, y)"
    """
    match point:
        case (0, 0):
            return "origin"
        # YOUR CODE HERE - add more cases
        case _:
            return f"point at {point}"


# Exercise 1.8: Guard clauses (early return pattern)
# Clean up nested conditionals using early returns

def process_user(user):
    """
    Process user dict and return status message.
    - If user is None, return "No user provided"
    - If user has no 'name' key, return "Invalid user: no name"
    - If user's name is empty string, return "Invalid user: empty name"
    - If user is not active (active key is False), return "User is inactive"
    - Otherwise return "Processing: {name}"

    Use guard clauses (early returns) instead of nested if/else.
    """
    # YOUR CODE HERE
    pass


# ============= TESTS (Don't modify below) =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1.1
    assert get_grade(95) == "A"
    assert get_grade(85) == "B"
    assert get_grade(75) == "C"
    assert get_grade(65) == "D"
    assert get_grade(55) == "F"
    assert get_grade(90) == "A"
    assert get_grade(80) == "B"
    print("✓ Exercise 1.1 passed")

    # Test 1.2
    assert is_truthy(1) == True
    assert is_truthy("hello") == True
    assert is_truthy([1, 2, 3]) == True
    assert is_truthy(0) == False
    assert is_truthy("") == False
    assert is_truthy([]) == False
    assert is_truthy(None) == False
    print("✓ Exercise 1.2 passed")

    # Test 1.3
    assert absolute_value(5) == 5
    assert absolute_value(-5) == 5
    assert absolute_value(0) == 0
    print("✓ Exercise 1.3 passed")

    # Test 1.4
    assert can_vote(18, True, True) == True
    assert can_vote(17, True, True) == False
    assert can_vote(18, False, True) == False
    assert can_vote(18, True, False) == False
    assert can_enter_club(21, True, False) == True
    assert can_enter_club(18, True, True) == True  # VIP
    assert can_enter_club(18, True, False) == False
    assert can_enter_club(21, False, False) == False
    print("✓ Exercise 1.4 passed")

    # Test 1.5
    assert is_valid_percentage(0) == True
    assert is_valid_percentage(100) == True
    assert is_valid_percentage(50) == True
    assert is_valid_percentage(-1) == False
    assert is_valid_percentage(101) == False
    assert is_between(5, 0, 10) == True
    assert is_between(0, 0, 10) == False  # exclusive
    assert is_between(10, 0, 10) == False  # exclusive
    print("✓ Exercise 1.5 passed")

    # Test 1.6
    assert http_status_message(200) == "OK"
    assert http_status_message(201) == "Created"
    assert http_status_message(404) == "Not Found"
    assert http_status_message(500) == "Internal Server Error"
    assert http_status_message(999) == "Unknown Status"
    print("✓ Exercise 1.6 passed")

    # Test 1.7
    assert describe_point((0, 0)) == "origin"
    assert describe_point((0, 5)) == "on y-axis"
    assert describe_point((5, 0)) == "on x-axis"
    assert describe_point((5, 5)) == "on diagonal"
    assert describe_point((3, 7)) == "point at (3, 7)"
    print("✓ Exercise 1.7 passed")

    # Test 1.8
    assert process_user(None) == "No user provided"
    assert process_user({}) == "Invalid user: no name"
    assert process_user({"name": ""}) == "Invalid user: empty name"
    assert process_user({"name": "Alice", "active": False}) == "User is inactive"
    assert process_user({"name": "Alice", "active": True}) == "Processing: Alice"
    print("✓ Exercise 1.8 passed")

    print("\n🎉 All tests passed! Great job!")
