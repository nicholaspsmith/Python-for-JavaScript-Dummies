"""
3Sum
=====

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

The solution set must not contain duplicate triplets.

Example:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

    Input: nums = [0,1,1]
    Output: [] (no triplets sum to 0)

    Input: nums = [0,0,0]
    Output: [[0,0,0]]

JS to Python Tips:
-----------------
- Sort in-place: `nums.sort()` (mutates list, returns None - NOT like JS!).
- Or create sorted copy: `sorted_nums = sorted(nums)`.
- Skip duplicates: `if i > 0 and nums[i] == nums[i-1]: continue`.
- Negative indexing: `nums[-1]` is last element.
- `while left < right:` same as JS.
- List literals: `[nums[i], nums[left], nums[right]]`.

Approach (O(n^2)):
1. Sort the array first.
2. For each element nums[i], use two pointers on the remaining elements.
3. Skip duplicates at each level to avoid duplicate triplets.
4. If sum < 0, move left pointer right. If sum > 0, move right pointer left.
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets that sum to zero.

    Hint: Sort first. For each i, use two pointers (left=i+1, right=end).
    Skip duplicates by checking if current == previous.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1: Normal case
    result = three_sum([-1, 0, 1, 2, -1, -4])
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])
    print("✓ Test 1 passed: [-1,0,1,2,-1,-4]")

    # Test 2: No solution
    assert three_sum([0, 1, 1]) == []
    print("✓ Test 2 passed: No triplet sums to 0")

    # Test 3: All zeros
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    print("✓ Test 3 passed: [0,0,0]")

    # Test 4: Empty/small input
    assert three_sum([]) == []
    assert three_sum([0]) == []
    print("✓ Test 4 passed: Edge cases")

    # Test 5: Multiple triplets
    result = three_sum([-2, 0, 1, 1, 2])
    expected = [[-2, 0, 2], [-2, 1, 1]]
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])
    print("✓ Test 5 passed: Multiple triplets")

    print("\n🎉 All tests passed!")
