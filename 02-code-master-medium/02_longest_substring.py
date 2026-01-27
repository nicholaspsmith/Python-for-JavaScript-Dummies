"""
Longest Substring Without Repeating Characters
================================================

Given a string s, find the length of the longest substring without repeating characters.

Example:
    Input: s = "abcabcbb"
    Output: 3 (The answer is "abc")

    Input: s = "bbbbb"
    Output: 1 (The answer is "b")

    Input: s = "pwwkew"
    Output: 3 (The answer is "wke")

JS to Python Tips:
-----------------
- `set()` is like JS `Set` - O(1) add/remove/lookup.
- Set operations: `seen.add(x)`, `seen.remove(x)`, `x in seen`.
- `seen.discard(x)` removes if present (no error if missing).
- `max(a, b)` instead of `Math.max(a, b)`.
- Sliding window: expand right, shrink left when duplicate found.

Sliding Window Pattern:
- Use two pointers: left (start of window) and right (expanding).
- Use a set to track characters in current window.
- When you find a duplicate, shrink from left until it's removed.
- Track the maximum window size seen.

Dict alternative: Store char -> index for O(1) jump to after duplicate.
"""


def length_of_longest_substring(s: str) -> int:
    """
    Find length of longest substring without repeating characters.

    Hint: Sliding window with a set. Expand right, when duplicate found,
    shrink left until duplicate is removed. Track max length.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Normal case
    _t1_input = "s='abcabcbb'"
    _t1_expected = 3
    try:
        result = length_of_longest_substring("abcabcbb")
        assert result == _t1_expected, f"Expected {_t1_expected}, got {result}"
        print("✓ Test 1 passed: Normal case")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|Error: {e}")
        _tests_failed += 1

    # Test 2: All same
    _t2_input = "s='bbbbb'"
    _t2_expected = 1
    try:
        result = length_of_longest_substring("bbbbb")
        assert result == _t2_expected, f"Expected {_t2_expected}, got {result}"
        print("✓ Test 2 passed: All same")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|Error: {e}")
        _tests_failed += 1

    # Test 3: Repeat in middle
    _t3_input = "s='pwwkew'"
    _t3_expected = 3
    try:
        result = length_of_longest_substring("pwwkew")
        assert result == _t3_expected, f"Expected {_t3_expected}, got {result}"
        print("✓ Test 3 passed: Repeat in middle")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|Error: {e}")
        _tests_failed += 1

    # Test 4: Empty string
    _t4_input = "s=''"
    _t4_expected = 0
    try:
        result = length_of_longest_substring("")
        assert result == _t4_expected, f"Expected {_t4_expected}, got {result}"
        print("✓ Test 4 passed: Empty string")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|Error: {e}")
        _tests_failed += 1

    # Test 5: Single char
    _t5_input = "s='a'"
    _t5_expected = 1
    try:
        result = length_of_longest_substring("a")
        assert result == _t5_expected, f"Expected {_t5_expected}, got {result}"
        print("✓ Test 5 passed: Single char")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|Error: {e}")
        _tests_failed += 1

    # Test 6: All unique
    _t6_input = "s='abcdef'"
    _t6_expected = 6
    try:
        result = length_of_longest_substring("abcdef")
        assert result == _t6_expected, f"Expected {_t6_expected}, got {result}"
        print("✓ Test 6 passed: All unique")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 6 failed: {e}")
        print(f"__TD__|{_t6_input}|{_t6_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 6 error: {e}")
        print(f"__TD__|{_t6_input}|{_t6_expected}|Error: {e}")
        _tests_failed += 1

    # Test 7: Space character
    _t7_input = "s='a b c'"
    _t7_expected = 3
    try:
        result = length_of_longest_substring("a b c")
        assert result == _t7_expected, f"Expected {_t7_expected}, got {result}"
        print("✓ Test 7 passed: Space character")
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
