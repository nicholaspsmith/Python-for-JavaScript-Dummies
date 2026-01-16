"""
Two Sum
========

Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`.

You may assume each input has exactly one solution, and you may not use
the same element twice. Return the answer in any order.

Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]  # Because nums[0] + nums[1] == 9

JS to Python Tips:
-----------------
- In JS you might use a Map() or object for O(1) lookup. In Python, use a dict.
- Python's `enumerate(list)` is like JS's `array.entries()` - it gives you (index, value) pairs.
- Instead of `for (let i = 0; i < arr.length; i++)`, Python uses `for i, num in enumerate(nums)`.
- Dict access: `my_dict.get(key)` returns None if missing (vs JS undefined).
  Or use `key in my_dict` to check existence (like JS `key in obj`).

The optimal solution uses a hash map (dict) for O(n) time complexity.
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Return indices of two numbers that add up to target.

    Hint: As you iterate, store each number's index in a dict.
    For each number, check if (target - num) exists in your dict.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1: Basic case
    result = two_sum([2, 7, 11, 15], 9)
    assert sorted(result) == [0, 1], f"Expected [0, 1], got {result}"
    print("✓ Exercise 1.1 passed: Basic two sum")

    # Test 2: Target at end
    result = two_sum([3, 2, 4], 6)
    assert sorted(result) == [1, 2], f"Expected [1, 2], got {result}"
    print("✓ Exercise 1.2 passed: Target at end of array")

    # Test 3: Same numbers
    result = two_sum([3, 3], 6)
    assert sorted(result) == [0, 1], f"Expected [0, 1], got {result}"
    print("✓ Exercise 1.3 passed: Duplicate numbers")

    # Test 4: Negative numbers
    result = two_sum([-1, -2, -3, -4, -5], -8)
    assert sorted(result) == [2, 4], f"Expected [2, 4], got {result}"
    print("✓ Exercise 1.4 passed: Negative numbers")

    print("\n🎉 All tests passed!")
