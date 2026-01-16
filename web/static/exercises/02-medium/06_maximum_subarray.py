"""
Maximum Subarray (Kadane's Algorithm)
======================================

Given an integer array nums, find the subarray with the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6 (subarray [4,-1,2,1] has the largest sum)

    Input: nums = [1]
    Output: 1

    Input: nums = [5,4,-1,7,8]
    Output: 23 (entire array)

JS to Python Tips:
-----------------
- `float('-inf')` is negative infinity (like JS `-Infinity`).
- `max(a, b)` built-in function (no Math.max needed).
- Kadane's algorithm: at each position, decide: extend current subarray or start fresh?
- `current_sum = max(num, current_sum + num)` - the key insight!

Kadane's Algorithm:
- At each position i, we have a choice:
  1. Add nums[i] to the current subarray (current_sum + nums[i])
  2. Start a new subarray at nums[i] (just nums[i])
- We pick whichever is larger: `current_sum = max(nums[i], current_sum + nums[i])`
- Track the maximum sum seen across all positions.

This is a classic DP problem with O(n) time, O(1) space.
"""

from typing import List


def max_subarray(nums: List[int]) -> int:
    """
    Find the maximum sum of any contiguous subarray.

    Hint: Kadane's algorithm. Track current_sum and max_sum.
    At each element: current_sum = max(num, current_sum + num)
    This decides whether to extend or start fresh.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1: Mixed positives and negatives
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    print("✓ Exercise 2.1 passed: [-2,1,-3,4,-1,2,1,-5,4] -> 6")

    # Test 2: Single element
    assert max_subarray([1]) == 1
    print("✓ Exercise 2.2 passed: Single element")

    # Test 3: All positive
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    print("✓ Exercise 2.3 passed: All positive")

    # Test 4: All negative
    assert max_subarray([-3, -2, -1, -4]) == -1
    print("✓ Exercise 2.4 passed: All negative -> pick least negative")

    # Test 5: Single negative
    assert max_subarray([-1]) == -1
    print("✓ Exercise 2.5 passed: Single negative")

    # Test 6: Zero included
    assert max_subarray([-2, 0, -1]) == 0
    print("✓ Exercise 2.6 passed: Zero as best option")

    print("\n🎉 All tests passed!")
