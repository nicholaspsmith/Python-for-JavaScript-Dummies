"""
Search in Rotated Sorted Array
===============================

A sorted array has been rotated at some pivot unknown to you beforehand.
For example, [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].

Given the rotated array nums and a target value, return the index of target
if it is in nums, or -1 if it is not.

You must write an algorithm with O(log n) runtime complexity (binary search).

Example:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

    Input: nums = [1], target = 0
    Output: -1

JS to Python Tips:
-----------------
- Integer division: `mid = (left + right) // 2` (double slash!).
  In JS you'd use `Math.floor((left + right) / 2)`.
- Python allows chained comparisons: `left <= target < nums[mid]` instead of
  `left <= target && target < nums[mid]`. This is unique to Python!
- `while left <= right:` same as JS.

Modified Binary Search:
- Find mid element. One half is always sorted!
- Determine which half is sorted (compare nums[left] vs nums[mid]).
- Check if target is in the sorted half.
- If yes, search that half; if no, search the other half.

Key insight: In a rotated sorted array, at least one half is always properly sorted.
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    """
    Search for target in rotated sorted array. Return index or -1.

    Hint: Binary search with modification. At each step, determine which
    half is sorted. Then check if target falls in the sorted range.
    Use Python's chained comparisons: `left <= target < right`.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1: Target in rotated part
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    print("✓ Exercise 2.1 passed: Found 0 at index 4")

    # Test 2: Target not found
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    print("✓ Exercise 2.2 passed: 3 not found")

    # Test 3: Single element not found
    assert search([1], 0) == -1
    print("✓ Exercise 2.3 passed: Single element, not found")

    # Test 4: Single element found
    assert search([1], 1) == 0
    print("✓ Exercise 2.4 passed: Single element, found")

    # Test 5: Target in first half
    assert search([4, 5, 6, 7, 0, 1, 2], 5) == 1
    print("✓ Exercise 2.5 passed: Found 5 in first half")

    # Test 6: Not rotated (edge case)
    assert search([1, 2, 3, 4, 5], 3) == 2
    print("✓ Exercise 2.6 passed: Non-rotated array")

    # Test 7: Fully rotated (same as original)
    assert search([2, 1], 1) == 1
    print("✓ Exercise 2.7 passed: Two elements rotated")

    print("\n🎉 All tests passed!")
