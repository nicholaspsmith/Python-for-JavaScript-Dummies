"""
Majority Element
=================

Given an array `nums` of size n, return the majority element.

The majority element is the element that appears more than n/2 times.
You may assume the majority element always exists in the array.

Example:
    Input: nums = [3,2,3]
    Output: 3

    Input: nums = [2,2,1,1,1,2,2]
    Output: 2

JS to Python Tips:
-----------------
- `collections.Counter` is like a specialized dict for counting (no JS equivalent).
  Usage: `from collections import Counter; counts = Counter(nums)`
  Then `counts.most_common(1)` returns [(element, count)] for the most frequent.
- Dict comprehension: `{x: nums.count(x) for x in set(nums)}` (but O(n^2)!).
- Boyer-Moore Voting Algorithm works in O(n) time, O(1) space - no extra data structures!
- `//` is integer division: `len(nums) // 2` (JS uses `Math.floor(len / 2)`).

Boyer-Moore Algorithm:
- Keep a candidate and a count.
- When count is 0, pick current element as new candidate.
- If current equals candidate, increment count; else decrement.
- The majority element will survive because it has more than n/2 occurrences.
"""

from typing import List


def majority_element(nums: List[int]) -> int:
    """
    Find the element that appears more than n/2 times.

    Hint: Use Boyer-Moore Voting: maintain a candidate and count.
    When count hits 0, switch candidate. The majority will always win.

    Or simpler: use collections.Counter and find the most common.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1: Simple majority
    assert majority_element([3, 2, 3]) == 3
    print("✓ Test 1 passed: [3,2,3] -> 3")

    # Test 2: Longer array
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
    print("✓ Test 2 passed: [2,2,1,1,1,2,2] -> 2")

    # Test 3: Single element
    assert majority_element([1]) == 1
    print("✓ Test 3 passed: Single element")

    # Test 4: All same
    assert majority_element([5, 5, 5]) == 5
    print("✓ Test 4 passed: All same elements")

    # Test 5: Two elements
    assert majority_element([1, 1]) == 1
    print("✓ Test 5 passed: Two same elements")

    # Test 6: Large majority
    assert majority_element([1, 1, 1, 1, 2]) == 1
    print("✓ Test 6 passed: Clear majority")

    print("\n🎉 All tests passed!")
