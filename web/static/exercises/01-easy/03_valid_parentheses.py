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
    print("Running tests...")

    # Test 1: Simple valid
    assert is_valid("()") == True, "() should be valid"
    print("✓ Exercise 1.1 passed: Simple parentheses")

    # Test 2: Multiple types
    assert is_valid("()[]{}") == True, "()[]{} should be valid"
    print("✓ Exercise 1.2 passed: Multiple bracket types")

    # Test 3: Mismatched
    assert is_valid("(]") == False, "(] should be invalid"
    print("✓ Exercise 1.3 passed: Mismatched brackets")

    # Test 4: Wrong order
    assert is_valid("([)]") == False, "([)] should be invalid"
    print("✓ Exercise 1.4 passed: Wrong nesting order")

    # Test 5: Nested valid
    assert is_valid("{[]}") == True, "{[]} should be valid"
    print("✓ Exercise 1.5 passed: Properly nested")

    # Test 6: Empty string
    assert is_valid("") == True, "Empty string should be valid"
    print("✓ Exercise 1.6 passed: Empty string")

    # Test 7: Only closing
    assert is_valid("]") == False, "Single closing should be invalid"
    print("✓ Exercise 1.7 passed: Unmatched closing bracket")

    print("\n🎉 All tests passed!")
