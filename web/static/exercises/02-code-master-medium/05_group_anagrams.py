"""
Group Anagrams
===============

Given an array of strings, group the anagrams together.
An anagram is a word formed by rearranging the letters of another word.

Example:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    Input: strs = [""]
    Output: [[""]]

    Input: strs = ["a"]
    Output: [["a"]]

JS to Python Tips:
-----------------
- `collections.defaultdict(list)` auto-creates empty list for missing keys.
  No need for `if key not in dict: dict[key] = []` pattern from JS.
- `''.join(sorted(s))` sorts string characters and rejoins them.
  This is your anagram signature! "eat" -> "aet", "tea" -> "aet".
- Tuple as dict key: `tuple(sorted(s))` is hashable (lists are not!).
- `dict.values()` returns a view object. Use `list(dict.values())` to get list.

Approach:
- Anagrams have the same sorted characters.
- Use sorted string (or character count tuple) as dictionary key.
- Group all words with same key together.
- Return all groups.

Alternative key: Character count tuple. Faster for long strings but more complex.
"""

from typing import List
from collections import defaultdict


'''HINTS
{
  "hint1": "def group_anagrams(strs: List[str]) -> List[List[str]]\\n\\nUse the sorted string as a key in a dictionary. All anagrams will have the same sorted key.",
  "hint2": "Pseudocode:\\n1) Create a defaultdict(list) to store groups\\n2) For each string in strs, sort it to get the key\\n3) Append the original string to groups[key]\\n4) Return list(groups.values())",
  "solution": "def group_anagrams(strs: List[str]) -> List[List[str]]:\\n    groups = defaultdict(list)\\n    for s in strs:\\n        key = ''.join(sorted(s))\\n        groups[key].append(s)\\n    return list(groups.values())"
}
HINTS'''


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Group anagrams together."""
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Normal case
    _t1_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    _t1_expected = [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    try:
        result = group_anagrams(_t1_input)
        result = [sorted(g) for g in result]
        result.sort()
        assert result == _t1_expected, f"Got {result}"
        print("✓ Test 1 passed: Normal case")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|None")
        _tests_failed += 1

    # Test 2: Empty string
    _t2_input = [""]
    _t2_expected = [[""]]
    try:
        result = group_anagrams(_t2_input)
        assert result == _t2_expected, f"Got {result}"
        print("✓ Test 2 passed: Empty string")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|None")
        _tests_failed += 1

    # Test 3: Single string
    _t3_input = ["a"]
    _t3_expected = [["a"]]
    try:
        result = group_anagrams(_t3_input)
        assert result == _t3_expected, f"Got {result}"
        print("✓ Test 3 passed: Single string")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|None")
        _tests_failed += 1

    # Test 4: No anagrams
    _t4_input = ["abc", "def", "ghi"]
    _t4_expected = [["abc"], ["def"], ["ghi"]]
    try:
        result = group_anagrams(_t4_input)
        result = [sorted(g) for g in result]
        result.sort()
        assert result == _t4_expected
        print("✓ Test 4 passed: No anagrams")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|None")
        _tests_failed += 1

    # Test 5: All same word
    _t5_input = ["a", "a", "a"]
    _t5_expected = ["a", "a", "a"]
    try:
        result = group_anagrams(_t5_input)
        assert sorted(result[0]) == _t5_expected
        print("✓ Test 5 passed: All same word")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|None")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
