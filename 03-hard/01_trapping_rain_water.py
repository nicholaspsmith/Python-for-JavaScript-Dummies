"""
Trapping Rain Water
====================

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

Example:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6 (the elevation map can trap 6 units of rain water)

    Visual:
            █
        █   ██ █
      █ ██ ██████
    0,1,0,2,1,0,1,3,2,1,2,1

    Input: height = [4,2,0,3,2,5]
    Output: 9

JS to Python Tips:
-----------------
- `max()` works on iterables: `max(height[:i+1])` finds max of subarray.
- List comprehension with `min/max`: `[min(a, b) for a, b in zip(left, right)]`.
- `zip()` pairs up elements from multiple iterables (like JS you'd manually iterate).
- Two-pointer approach works great here.
- Prefix max arrays: `left_max[i] = max of height[0..i]`.

Multiple approaches:

1. Brute Force O(n^2): For each position, find max left and max right, water = min - height.

2. DP/Prefix arrays O(n): Precompute left_max and right_max arrays.
   Water at i = min(left_max[i], right_max[i]) - height[i].

3. Two Pointers O(n), O(1) space: Track left_max and right_max as you go.
   Move the pointer with smaller max value.

The key insight: water at any position = min(max_left, max_right) - height[i].
"""

from typing import List


def trap(height: List[int]) -> int:
    """
    Calculate total trapped rain water.

    Hint: For each position, water trapped = min(max_left, max_right) - height[i].
    Use two pointers starting from both ends, tracking left_max and right_max.
    Move the pointer with the smaller max.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1: Standard example
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    print("✓ Test 1 passed: [0,1,0,2,1,0,1,3,2,1,2,1] -> 6")

    # Test 2: Another example
    assert trap([4, 2, 0, 3, 2, 5]) == 9
    print("✓ Test 2 passed: [4,2,0,3,2,5] -> 9")

    # Test 3: No water (ascending)
    assert trap([1, 2, 3, 4]) == 0
    print("✓ Test 3 passed: Ascending -> 0")

    # Test 4: No water (descending)
    assert trap([4, 3, 2, 1]) == 0
    print("✓ Test 4 passed: Descending -> 0")

    # Test 5: Empty
    assert trap([]) == 0
    print("✓ Test 5 passed: Empty -> 0")

    # Test 6: Single/double elements
    assert trap([5]) == 0
    assert trap([5, 4]) == 0
    print("✓ Test 6 passed: Too few elements")

    # Test 7: Valley
    assert trap([5, 0, 5]) == 5
    print("✓ Test 7 passed: Simple valley")

    print("\n🎉 All tests passed!")
