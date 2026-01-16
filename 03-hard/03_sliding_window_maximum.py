"""
Sliding Window Maximum
=======================

You are given an array of integers nums and a window size k.
Return the maximum value in each sliding window of size k as it moves
from left to right.

Example:
    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]

    Window positions:              Max:
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7

    Input: nums = [1], k = 1
    Output: [1]

JS to Python Tips:
-----------------
- `collections.deque` is a double-ended queue with O(1) append/pop at both ends.
  In JS you'd use an array, but shift() is O(n). Python's deque is efficient.
- `deque.append(x)` adds to right, `deque.appendleft(x)` adds to left.
- `deque.pop()` removes from right, `deque.popleft()` removes from left.
- `deque[0]` peeks at left (front), `deque[-1]` peeks at right (back).
- Store indices in the deque, not values (so you can check if index is in window).

Monotonic Deque O(n):
- Maintain a deque of indices where values are in decreasing order.
- For each new element:
  1. Remove indices outside the current window from front.
  2. Remove indices of smaller elements from back (they'll never be max).
  3. Add current index to back.
  4. Front of deque is always the max for current window.

This is O(n) because each element is added and removed at most once.
"""

from typing import List
from collections import deque


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """
    Return the maximum in each sliding window of size k.

    Hint: Use a monotonic deque storing indices.
    Keep it decreasing: when adding a new element, pop smaller elements from back.
    The front is always the max. Remove front if it's outside the window.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1: Standard example
    result = max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
    assert result == [3, 3, 5, 5, 6, 7], f"Got {result}"
    print("✓ Exercise 3.1 passed: Standard sliding window")

    # Test 2: Single element
    result = max_sliding_window([1], 1)
    assert result == [1], f"Got {result}"
    print("✓ Exercise 3.2 passed: Single element")

    # Test 3: Window size equals array
    result = max_sliding_window([1, 3, 2], 3)
    assert result == [3], f"Got {result}"
    print("✓ Exercise 3.3 passed: Window equals array size")

    # Test 4: Descending array
    result = max_sliding_window([9, 8, 7, 6, 5], 2)
    assert result == [9, 8, 7, 6], f"Got {result}"
    print("✓ Exercise 3.4 passed: Descending array")

    # Test 5: Ascending array
    result = max_sliding_window([1, 2, 3, 4, 5], 2)
    assert result == [2, 3, 4, 5], f"Got {result}"
    print("✓ Exercise 3.5 passed: Ascending array")

    # Test 6: All same
    result = max_sliding_window([5, 5, 5, 5], 2)
    assert result == [5, 5, 5], f"Got {result}"
    print("✓ Exercise 3.6 passed: All same values")

    # Test 7: Negative numbers
    result = max_sliding_window([-1, -2, -3, -4], 2)
    assert result == [-1, -2, -3], f"Got {result}"
    print("✓ Exercise 3.7 passed: Negative numbers")

    print("\n🎉 All tests passed!")
