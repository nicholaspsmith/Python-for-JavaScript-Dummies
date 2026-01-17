"""
Remove Duplicates from Sorted Array
=====================================

Given a sorted array `nums`, remove the duplicates in-place such that each
element appears only once and returns the new length.

Do not allocate extra space for another array - modify the input array in-place
with O(1) extra memory.

The relative order of elements should be kept the same. The first k elements
of nums should hold the final result (it doesn't matter what you leave beyond k).

Example:
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]

    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

JS to Python Tips:
-----------------
- In-place modification works the same: `nums[i] = value` modifies the list.
- Two-pointer technique: one pointer for reading, one for writing.
- Unlike JS, Python lists are always mutable (no frozen arrays by default).
- `len(nums)` instead of `nums.length`.
- Edge case: `if not nums:` checks for empty list.

The key insight: since the array is sorted, duplicates are adjacent.
Use a "write pointer" that only advances when you find a new unique value.
"""

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """
    Remove duplicates in-place and return the new length.

    Hint: Use two pointers - one to track where to write (k),
    one to iterate through the array.
    When you find a new number different from nums[k-1], write it at nums[k].
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1: Basic case
    nums = [1, 1, 2]
    k = remove_duplicates(nums)
    assert k == 2, f"Expected length 2, got {k}"
    assert nums[:k] == [1, 2], f"Expected [1,2], got {nums[:k]}"
    print("✓ Test 1 passed: [1,1,2] -> [1,2]")

    # Test 2: Longer array
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(nums)
    assert k == 5, f"Expected length 5, got {k}"
    assert nums[:k] == [0, 1, 2, 3, 4], f"Expected [0,1,2,3,4], got {nums[:k]}"
    print("✓ Test 2 passed: Longer array with multiple duplicates")

    # Test 3: No duplicates
    nums = [1, 2, 3]
    k = remove_duplicates(nums)
    assert k == 3, f"Expected length 3, got {k}"
    assert nums[:k] == [1, 2, 3], f"Expected [1,2,3], got {nums[:k]}"
    print("✓ Test 3 passed: No duplicates")

    # Test 4: All duplicates
    nums = [5, 5, 5, 5]
    k = remove_duplicates(nums)
    assert k == 1, f"Expected length 1, got {k}"
    assert nums[:k] == [5], f"Expected [5], got {nums[:k]}"
    print("✓ Test 4 passed: All same values")

    # Test 5: Empty array
    nums = []
    k = remove_duplicates(nums)
    assert k == 0, f"Expected length 0, got {k}"
    print("✓ Test 5 passed: Empty array")

    print("\n🎉 All tests passed!")
