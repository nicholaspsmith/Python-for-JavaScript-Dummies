"""
Container With Most Water
==========================

Given n non-negative integers representing heights of vertical lines,
find two lines that together with the x-axis form a container that holds the most water.

The container's area = min(height[i], height[j]) * (j - i)

Example:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: Lines at index 1 (height 8) and index 8 (height 7)
                 form a container of area = min(8,7) * (8-1) = 7 * 7 = 49

    Input: height = [1,1]
    Output: 1

JS to Python Tips:
-----------------
- Two pointers: `left, right = 0, len(height) - 1` (tuple unpacking).
- `min(a, b)` and `max(a, b)` are built-in (no Math object).
- Area calculation: `area = min(height[left], height[right]) * (right - left)`.
- Move the pointer with smaller height inward (greedy choice).

Why move the smaller pointer?
- Width will definitely decrease.
- Only chance for more area is if we find a taller line.
- Moving the taller one can only make things worse (we're limited by the shorter side).

O(n) time, O(1) space with two pointers.
"""

from typing import List


def max_area(height: List[int]) -> int:
    """
    Find the maximum water container area.

    Hint: Two pointers starting from both ends.
    Calculate area, then move the pointer with the shorter height.
    Track maximum area found.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1: Example case
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    print("✓ Test 1 passed: [1,8,6,2,5,4,8,3,7] -> 49")

    # Test 2: Two elements
    assert max_area([1, 1]) == 1
    print("✓ Test 2 passed: [1,1] -> 1")

    # Test 3: Decreasing heights
    assert max_area([4, 3, 2, 1, 4]) == 16
    print("✓ Test 3 passed: [4,3,2,1,4] -> 16")

    # Test 4: All same height
    assert max_area([5, 5, 5, 5]) == 15
    print("✓ Test 4 passed: All same height")

    # Test 5: Two different heights
    assert max_area([1, 2]) == 1
    print("✓ Test 5 passed: [1,2] -> 1")

    print("\n🎉 All tests passed!")
