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


'''HINTS
{
  "hint1": "def longest_common_prefix(strs: List[str]) -> str:\\n    # Handle empty list edge case\\n    if not strs:\\n        return ''\\n    # Start with first string as prefix\\n    prefix = strs[0]\\n    # Your code here: shrink prefix for each string\\n    ...",
  "hint2": "# Pseudocode:\\n# 1) Handle empty list - return ''\\n# 2) Start with first string as the prefix\\n# 3) For each string in the list:\\n#    - While the string doesn't start with prefix:\\n#      - Remove last character from prefix\\n#      - If prefix is empty, return ''\\n# 4) Return the prefix",
  "solution": "def longest_common_prefix(strs: List[str]) -> str:\\n    if not strs:\\n        return ''\\n    prefix = strs[0]\\n    for s in strs[1:]:\\n        while not s.startswith(prefix):\\n            prefix = prefix[:-1]\\n            if not prefix:\\n                return ''\\n    return prefix"
}
HINTS'''


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
    _t1_input = "strs=['flower','flow','flight']"
    _t1_expected = "fl"
    try:
        result = longest_common_prefix(["flower", "flow", "flight"])
        assert result == _t1_expected, f"Expected {_t1_expected}, got {result}"
        print("✓ Test 1 passed: Has common prefix")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|Error: {e}")
        _tests_failed += 1

    # Test 2: No common prefix
    _t2_input = "strs=['dog','racecar','car']"
    _t2_expected = ""
    try:
        result = longest_common_prefix(["dog", "racecar", "car"])
        assert result == _t2_expected, f"Expected {_t2_expected}, got {result}"
        print("✓ Test 2 passed: No common prefix")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|Error: {e}")
        _tests_failed += 1

    # Test 3: All same
    _t3_input = "strs=['test','test','test']"
    _t3_expected = "test"
    try:
        result = longest_common_prefix(["test", "test", "test"])
        assert result == _t3_expected, f"Expected {_t3_expected}, got {result}"
        print("✓ Test 3 passed: All same")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|Error: {e}")
        _tests_failed += 1

    # Test 4: Single string
    _t4_input = "strs=['single']"
    _t4_expected = "single"
    try:
        result = longest_common_prefix(["single"])
        assert result == _t4_expected, f"Expected {_t4_expected}, got {result}"
        print("✓ Test 4 passed: Single string")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|Error: {e}")
        _tests_failed += 1

    # Test 5: Empty string in list
    _t5_input = "strs=['','b']"
    _t5_expected = ""
    try:
        result = longest_common_prefix(["", "b"])
        assert result == _t5_expected, f"Expected {_t5_expected}, got {result}"
        print("✓ Test 5 passed: Empty string in list")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|Error: {e}")
        _tests_failed += 1

    # Test 6: Empty list
    _t6_input = "strs=[]"
    _t6_expected = ""
    try:
        result = longest_common_prefix([])
        assert result == _t6_expected, f"Expected {_t6_expected}, got {result}"
        print("✓ Test 6 passed: Empty list")
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
