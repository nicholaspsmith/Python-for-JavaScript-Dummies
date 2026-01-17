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


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group anagrams together.

    Hint: Use a dict where key = sorted characters of word.
    defaultdict(list) makes this cleaner - just append to any key.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1: Normal case
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Sort for comparison
    result = [sorted(g) for g in result]
    result.sort()
    expected = [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    assert result == expected, f"Got {result}"
    print("✓ Test 1 passed: Grouped anagrams correctly")

    # Test 2: Empty string
    result = group_anagrams([""])
    assert result == [[""]], f"Got {result}"
    print("✓ Test 2 passed: Empty string")

    # Test 3: Single string
    result = group_anagrams(["a"])
    assert result == [["a"]], f"Got {result}"
    print("✓ Test 3 passed: Single string")

    # Test 4: No anagrams
    result = group_anagrams(["abc", "def", "ghi"])
    result = [sorted(g) for g in result]
    result.sort()
    assert result == [["abc"], ["def"], ["ghi"]]
    print("✓ Test 4 passed: No anagrams")

    # Test 5: All same word
    result = group_anagrams(["a", "a", "a"])
    assert sorted(result[0]) == ["a", "a", "a"]
    print("✓ Test 5 passed: All same word")

    print("\n🎉 All tests passed!")
