"""
Palindrome Number
==================

Given an integer `x`, return `True` if `x` is a palindrome, and `False` otherwise.

A palindrome reads the same backward as forward.

Example:
    Input: x = 121
    Output: True (121 reads as 121 backwards)

    Input: x = -121
    Output: False (reads as 121- backwards)

    Input: x = 10
    Output: False (reads as 01 backwards)

JS to Python Tips:
-----------------
- String conversion: Python uses `str(num)` instead of `num.toString()` or `String(num)`.
- String reversal: Python has no built-in reverse for strings, but you can use slicing: `s[::-1]`.
  This slice syntax means [start:stop:step] where -1 step goes backwards.
- Boolean values are `True` and `False` (capitalized), not `true` and `false`.
- Negative check: `x < 0` works the same way.

Challenge: Can you solve it without converting to a string?
"""


def is_palindrome(x: int) -> bool:
    """
    Return True if x is a palindrome integer.

    Hint: Negative numbers are never palindromes.
    Think about how to reverse a number mathematically, or use string slicing.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Positive palindrome
    try:

        assert is_palindrome(121) == True, "121 should be a palindrome"
        print("✓ Test 1 passed: Positive palindrome")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        _tests_failed += 1

    # Test 2: Negative number
    try:

        assert is_palindrome(-121) == False, "-121 should not be a palindrome"
        print("✓ Test 2 passed: Negative number")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        _tests_failed += 1

    # Test 3: Ends with zero
    try:

        assert is_palindrome(10) == False, "10 should not be a palindrome"
        print("✓ Test 3 passed: Ends with zero")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        _tests_failed += 1

    # Test 4: Single digit
    try:

        assert is_palindrome(7) == True, "Single digits are palindromes"
        print("✓ Test 4 passed: Single digit")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        _tests_failed += 1

    # Test 5: Zero
    try:

        assert is_palindrome(0) == True, "0 is a palindrome"
        print("✓ Test 5 passed: Zero")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        _tests_failed += 1

    # Test 6: Large palindrome
    try:

        assert is_palindrome(12321) == True, "12321 is a palindrome"
        print("✓ Test 6 passed: Large palindrome")
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
