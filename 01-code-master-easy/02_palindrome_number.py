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

'''HINTS
{
  "hint1": "def is_palindrome(x: int) -> bool:\\n    # Convert number to string and use slicing to reverse\\n    s = str(x)\\n    # Use [::-1] to reverse the string\\n    ...",
  "hint2": "def is_palindrome(x: int) -> bool:\\n    # Step 1: Handle negative numbers (they can't be palindromes)\\n    # if x < 0: return False\\n    \\n    # Step 2: Convert integer to string\\n    # s = str(x)\\n    \\n    # Step 3: Compare string with its reverse using [::-1]\\n    # return s == s[::-1]\\n    ...",
  "solution": "def is_palindrome(x: int) -> bool:\\n    if x < 0:\\n        return False\\n    return str(x) == str(x)[::-1]"
}
HINTS'''


def is_palindrome(x: int) -> bool:
    """Return True if x is a palindrome integer."""
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Positive palindrome
    _t1_input = "x=121"
    _t1_expected = True
    try:
        result = is_palindrome(121)
        assert result == _t1_expected, f"Expected {_t1_expected}, got {result}"
        print("✓ Test 1 passed: Positive palindrome")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|Error: {e}")
        _tests_failed += 1

    # Test 2: Negative number
    _t2_input = "x=-121"
    _t2_expected = False
    try:
        result = is_palindrome(-121)
        assert result == _t2_expected, f"Expected {_t2_expected}, got {result}"
        print("✓ Test 2 passed: Negative number")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|Error: {e}")
        _tests_failed += 1

    # Test 3: Ends with zero
    _t3_input = "x=10"
    _t3_expected = False
    try:
        result = is_palindrome(10)
        assert result == _t3_expected, f"Expected {_t3_expected}, got {result}"
        print("✓ Test 3 passed: Ends with zero")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|Error: {e}")
        _tests_failed += 1

    # Test 4: Single digit
    _t4_input = "x=7"
    _t4_expected = True
    try:
        result = is_palindrome(7)
        assert result == _t4_expected, f"Expected {_t4_expected}, got {result}"
        print("✓ Test 4 passed: Single digit")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|Error: {e}")
        _tests_failed += 1

    # Test 5: Zero
    _t5_input = "x=0"
    _t5_expected = True
    try:
        result = is_palindrome(0)
        assert result == _t5_expected, f"Expected {_t5_expected}, got {result}"
        print("✓ Test 5 passed: Zero")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|Error: {e}")
        _tests_failed += 1

    # Test 6: Large palindrome
    _t6_input = "x=12321"
    _t6_expected = True
    try:
        result = is_palindrome(12321)
        assert result == _t6_expected, f"Expected {_t6_expected}, got {result}"
        print("✓ Test 6 passed: Large palindrome")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 6 failed: {e}")
        print(f"__TD__|{_t6_input}|{_t6_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 6 error: {e}")
        print(f"__TD__|{_t6_input}|{_t6_expected}|Error: {e}")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
