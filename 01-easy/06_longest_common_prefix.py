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
    print("Running tests...")

    # Test 1: Has common prefix
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    print("✓ Exercise 1.1 passed: Common prefix 'fl'")

    # Test 2: No common prefix
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
    print("✓ Exercise 1.2 passed: No common prefix")

    # Test 3: All same
    assert longest_common_prefix(["test", "test", "test"]) == "test"
    print("✓ Exercise 1.3 passed: All strings identical")

    # Test 4: Single string
    assert longest_common_prefix(["single"]) == "single"
    print("✓ Exercise 1.4 passed: Single string")

    # Test 5: Empty string in list
    assert longest_common_prefix(["", "b"]) == ""
    print("✓ Exercise 1.5 passed: Empty string in list")

    # Test 6: Empty list
    assert longest_common_prefix([]) == ""
    print("✓ Exercise 1.6 passed: Empty list")

    print("\n🎉 All tests passed!")
