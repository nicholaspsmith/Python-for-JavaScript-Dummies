"""
Single Number
==============

Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.

You must implement a solution with O(n) time complexity and O(1) extra space.

Example:
    Input: nums = [2,2,1]
    Output: 1

    Input: nums = [4,1,2,1,2]
    Output: 4

    Input: nums = [1]
    Output: 1

JS to Python Tips:
-----------------
- XOR operator is `^` (same as JS): `a ^ b`.
- XOR properties: a ^ a = 0, a ^ 0 = a, and XOR is commutative/associative.
- This means: 2 ^ 2 ^ 1 = 0 ^ 1 = 1. All pairs cancel out!
- Python's reduce: `from functools import reduce` then `reduce(lambda a, b: a ^ b, nums)`.
- Or just loop: `result = 0; for n in nums: result ^= n`
- Augmented assignment: `result ^= n` is like JS `result ^= n`.

The XOR trick is elegant:
- XORing a number with itself gives 0
- XORing with 0 gives the number back
- So XOR all numbers together: pairs cancel, single remains!
"""

from typing import List


def single_number(nums: List[int]) -> int:
    """
    Find the number that appears only once (all others appear twice).

    Hint: XOR all numbers together. Pairs will cancel out (a ^ a = 0),
    leaving only the single number.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1: Basic case
    assert single_number([2, 2, 1]) == 1
    print("✓ Test 1 passed: [2,2,1] -> 1")

    # Test 2: Longer array
    assert single_number([4, 1, 2, 1, 2]) == 4
    print("✓ Test 2 passed: [4,1,2,1,2] -> 4")

    # Test 3: Single element
    assert single_number([1]) == 1
    print("✓ Test 3 passed: Single element")

    # Test 4: Negative numbers
    assert single_number([-1, -1, -2]) == -2
    print("✓ Test 4 passed: Negative numbers")

    # Test 5: Mixed positive and negative
    assert single_number([1, -1, 1]) == -1
    print("✓ Test 5 passed: Mixed positive/negative")

    print("\n🎉 All tests passed!")
