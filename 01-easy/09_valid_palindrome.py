"""
Valid Palindrome
=================

A phrase is a palindrome if, after converting all uppercase letters to lowercase
and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string s, return True if it is a palindrome, or False otherwise.

Example:
    Input: s = "A man, a plan, a canal: Panama"
    Output: True ("amanaplanacanalpanama" is a palindrome)

    Input: s = "race a car"
    Output: False

    Input: s = " "
    Output: True (empty string after removing non-alphanumeric)

JS to Python Tips:
-----------------
- `str.lower()` like JS `str.toLowerCase()`.
- `str.isalnum()` checks if char is alphanumeric (no JS equivalent - you'd use regex).
- `char.isalpha()` checks if alphabetic, `char.isdigit()` checks if numeric.
- String building: You CAN use `+=` on strings, but list + join is more efficient:
  `''.join([char for char in s if char.isalnum()])` - this is a list comprehension!
- Two-pointer approach: `left, right = 0, len(s) - 1`.
- Python's `while left < right:` is same as JS.

List comprehension is the Pythonic way to filter and transform:
`[expression for item in iterable if condition]`
"""


def is_palindrome(s: str) -> bool:
    """
    Return True if s is a valid palindrome (ignoring case and non-alphanumeric chars).

    Hint: Either clean the string first with a list comprehension,
    or use two pointers that skip non-alphanumeric characters.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Classic palindrome
    try:

        assert is_palindrome("A man, a plan, a canal: Panama") == True
        print("✓ Test 1 passed: Classic palindrome")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        _tests_failed += 1

    # Test 2: Not a palindrome
    try:

        assert is_palindrome("race a car") == False
        print("✓ Test 2 passed: Not a palindrome")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        _tests_failed += 1

    # Test 3: Empty/whitespace
    try:

        assert is_palindrome(" ") == True
        print("✓ Test 3 passed: Empty/whitespace")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        _tests_failed += 1

    # Test 4: Single character
    try:

        assert is_palindrome("a") == True
        print("✓ Test 4 passed: Single character")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        _tests_failed += 1

    # Test 5: Numbers included
    try:

        assert is_palindrome("0P") == False
        print("✓ Test 5 passed: Numbers included")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        _tests_failed += 1

    # Test 6: Numeric palindrome
    try:

        assert is_palindrome("12321") == True
        print("✓ Test 6 passed: Numeric palindrome")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 6 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 6 error: {e}")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
