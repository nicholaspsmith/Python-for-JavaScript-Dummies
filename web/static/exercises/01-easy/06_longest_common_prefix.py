"""
Longest Common Prefix
======================

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example:
    Input: strs = ["flower", "flow", "flight"]
    Output: "fl"

    Input: strs = ["dog", "racecar", "car"]
    Output: "" (no common prefix)

JS to Python Tips:
-----------------
- `min()` and `max()` work on strings! They compare lexicographically.
  This is a clever trick: compare only min and max strings since any common
  prefix must be shared by the lexicographically smallest and largest strings.
- String slicing: `s[:i]` gets first i characters (like JS `s.slice(0, i)`).
- `zip(str1, str2)` pairs up characters: zip("abc", "abd") -> [('a','a'), ('b','b'), ('c','d')].
- Empty list check: `if not strs:` returns True for empty list.
- `enumerate(iterable)` gives you index and value together.

Multiple approaches work:
1. Horizontal scan: compare first two, then result with third, etc.
2. Vertical scan: compare character by character across all strings.
3. Min/max trick: only compare the smallest and largest strings.
"""

from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    """
    Find the longest common prefix among all strings.

    Hint: Try comparing min(strs) and max(strs) character by character.
    The common prefix of these two is the answer!
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Has common prefix
    try:

        assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
        print("✓ Test 1 passed: Has common prefix")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        _tests_failed += 1

    # Test 2: No common prefix
    try:

        assert longest_common_prefix(["dog", "racecar", "car"]) == ""
        print("✓ Test 2 passed: No common prefix")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        _tests_failed += 1

    # Test 3: All same
    try:

        assert longest_common_prefix(["test", "test", "test"]) == "test"
        print("✓ Test 3 passed: All same")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        _tests_failed += 1

    # Test 4: Single string
    try:

        assert longest_common_prefix(["single"]) == "single"
        print("✓ Test 4 passed: Single string")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        _tests_failed += 1

    # Test 5: Empty string in list
    try:

        assert longest_common_prefix(["", "b"]) == ""
        print("✓ Test 5 passed: Empty string in list")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        _tests_failed += 1

    # Test 6: Empty list
    try:

        assert longest_common_prefix([]) == ""
        print("✓ Test 6 passed: Empty list")
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
