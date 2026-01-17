"""
Valid Parentheses
==================

Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

A string is valid if:
1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example:
    Input: s = "()"      Output: True
    Input: s = "()[]{}"  Output: True
    Input: s = "(]"      Output: False
    Input: s = "([)]"    Output: False
    Input: s = "{[]}"    Output: True

JS to Python Tips:
-----------------
- Use a list as a stack: `stack.append(x)` to push, `stack.pop()` to pop.
  In JS you'd use `array.push()` and `array.pop()` - Python's append is the equivalent of push.
- Check if stack is empty: `if not stack:` or `if len(stack) == 0:`.
  The Pythonic way is `if not stack:` since empty lists are falsy.
- Dict for bracket matching: `pairs = {'(': ')', '[': ']', '{': '}'}`.
- Iterate string directly: `for char in s:` (no need for index).

This is a classic stack problem - push opening brackets, pop and match closing ones.
"""


def is_valid(s: str) -> bool:
    """
    Return True if the string has valid matching brackets.

    Hint: Use a stack (list). Push opening brackets.
    When you see a closing bracket, pop and check if it matches.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Simple valid
    try:

        assert is_valid("()") == True, "() should be valid"
        print("✓ Test 1 passed: Simple valid")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        _tests_failed += 1

    # Test 2: Multiple types
    try:

        assert is_valid("()[]{}") == True, "()[]{} should be valid"
        print("✓ Test 2 passed: Multiple types")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        _tests_failed += 1

    # Test 3: Mismatched
    try:

        assert is_valid("(]") == False, "(] should be invalid"
        print("✓ Test 3 passed: Mismatched")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        _tests_failed += 1

    # Test 4: Wrong order
    try:

        assert is_valid("([)]") == False, "([)] should be invalid"
        print("✓ Test 4 passed: Wrong order")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        _tests_failed += 1

    # Test 5: Nested valid
    try:

        assert is_valid("{[]}") == True, "{[]} should be valid"
        print("✓ Test 5 passed: Nested valid")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        _tests_failed += 1

    # Test 6: Empty string
    try:

        assert is_valid("") == True, "Empty string should be valid"
        print("✓ Test 6 passed: Empty string")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 6 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 6 error: {e}")
        _tests_failed += 1

    # Test 7: Only closing
    try:

        assert is_valid("]") == False, "Single closing should be invalid"
        print("✓ Test 7 passed: Only closing")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 7 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 7 error: {e}")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
