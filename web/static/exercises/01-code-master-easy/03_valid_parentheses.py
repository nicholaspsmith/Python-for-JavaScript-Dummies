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

'''HINTS
{
  "hint1": "def is_valid(s: str) -> bool:\\n    stack = []\\n    mapping = {')': '(', ']': '[', '}': '{'}\\n    # Your code here\\n    ...",
  "hint2": "def is_valid(s: str) -> bool:\\n    # 1. Create empty stack and mapping dict (closing -> opening)\\n    # 2. For each char in s:\\n    #    3. If char is opening bracket, push to stack\\n    #    4. If char is closing bracket:\\n    #       - If stack empty or top doesn't match, return False\\n    #       - Otherwise pop from stack\\n    # 5. Return True if stack is empty, False otherwise\\n    ...",
  "solution": "def is_valid(s: str) -> bool:\\n    stack = []\\n    mapping = {')': '(', ']': '[', '}': '{'}\\n    \\n    for char in s:\\n        if char in mapping:\\n            # Closing bracket\\n            if not stack or stack[-1] != mapping[char]:\\n                return False\\n            stack.pop()\\n        else:\\n            # Opening bracket\\n            stack.append(char)\\n    \\n    return len(stack) == 0"
}
HINTS'''

def is_valid(s: str) -> bool:
    """Return True if the string has valid matching brackets."""
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Simple valid
    _t1_input = "s='()'"
    _t1_expected = True
    try:
        result = is_valid("()")
        assert result == _t1_expected, f"Expected {_t1_expected}, got {result}"
        print("✓ Test 1 passed: Simple valid")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|Error: {e}")
        _tests_failed += 1

    # Test 2: Multiple types
    _t2_input = "s='()[]{}'"
    _t2_expected = True
    try:
        result = is_valid("()[]{}")
        assert result == _t2_expected, f"Expected {_t2_expected}, got {result}"
        print("✓ Test 2 passed: Multiple types")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|Error: {e}")
        _tests_failed += 1

    # Test 3: Mismatched
    _t3_input = "s='(]'"
    _t3_expected = False
    try:
        result = is_valid("(]")
        assert result == _t3_expected, f"Expected {_t3_expected}, got {result}"
        print("✓ Test 3 passed: Mismatched")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|Error: {e}")
        _tests_failed += 1

    # Test 4: Wrong order
    _t4_input = "s='([)]'"
    _t4_expected = False
    try:
        result = is_valid("([)]")
        assert result == _t4_expected, f"Expected {_t4_expected}, got {result}"
        print("✓ Test 4 passed: Wrong order")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|Error: {e}")
        _tests_failed += 1

    # Test 5: Nested valid
    _t5_input = "s='{[]}'"
    _t5_expected = True
    try:
        result = is_valid("{[]}")
        assert result == _t5_expected, f"Expected {_t5_expected}, got {result}"
        print("✓ Test 5 passed: Nested valid")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|Error: {e}")
        _tests_failed += 1

    # Test 6: Empty string
    _t6_input = "s=''"
    _t6_expected = True
    try:
        result = is_valid("")
        assert result == _t6_expected, f"Expected {_t6_expected}, got {result}"
        print("✓ Test 6 passed: Empty string")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 6 failed: {e}")
        print(f"__TD__|{_t6_input}|{_t6_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 6 error: {e}")
        print(f"__TD__|{_t6_input}|{_t6_expected}|Error: {e}")
        _tests_failed += 1

    # Test 7: Only closing
    _t7_input = "s=']'"
    _t7_expected = False
    try:
        result = is_valid("]")
        assert result == _t7_expected, f"Expected {_t7_expected}, got {result}"
        print("✓ Test 7 passed: Only closing")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 7 failed: {e}")
        print(f"__TD__|{_t7_input}|{_t7_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 7 error: {e}")
        print(f"__TD__|{_t7_input}|{_t7_expected}|Error: {e}")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
