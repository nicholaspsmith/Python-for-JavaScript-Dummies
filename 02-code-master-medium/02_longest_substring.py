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
    try:

        assert length_of_longest_substring("abcabcbb") == 3
        print("✓ Test 1 passed: Normal case")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        _tests_failed += 1

    # Test 2: All same
    try:

        assert length_of_longest_substring("bbbbb") == 1
        print("✓ Test 2 passed: All same")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        _tests_failed += 1

    # Test 3: Repeat in middle
    try:

        assert length_of_longest_substring("pwwkew") == 3
        print("✓ Test 3 passed: Repeat in middle")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        _tests_failed += 1

    # Test 4: Empty string
    try:

        assert length_of_longest_substring("") == 0
        print("✓ Test 4 passed: Empty string")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        _tests_failed += 1

    # Test 5: Single char
    try:

        assert length_of_longest_substring("a") == 1
        print("✓ Test 5 passed: Single char")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        _tests_failed += 1

    # Test 6: All unique
    try:

        assert length_of_longest_substring("abcdef") == 6
        print("✓ Test 6 passed: All unique")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 6 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 6 error: {e}")
        _tests_failed += 1

    # Test 7: Space character
    try:

        assert length_of_longest_substring("a b c") == 3
        print("✓ Test 7 passed: Space character")
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
