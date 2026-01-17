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
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Standard example
    try:
        result = max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
        assert result == [3, 3, 5, 5, 6, 7], f"Got {result}"
        print("✓ Test 1 passed: Standard example")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        _tests_failed += 1

    # Test 2: Single element
    try:
        result = max_sliding_window([1], 1)
        assert result == [1], f"Got {result}"
        print("✓ Test 2 passed: Single element")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        _tests_failed += 1

    # Test 3: Window size equals array
    try:
        result = max_sliding_window([1, 3, 2], 3)
        assert result == [3], f"Got {result}"
        print("✓ Test 3 passed: Window size equals array")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        _tests_failed += 1

    # Test 4: Descending array
    try:
        result = max_sliding_window([9, 8, 7, 6, 5], 2)
        assert result == [9, 8, 7, 6], f"Got {result}"
        print("✓ Test 4 passed: Descending array")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        _tests_failed += 1

    # Test 5: Ascending array
    try:
        result = max_sliding_window([1, 2, 3, 4, 5], 2)
        assert result == [2, 3, 4, 5], f"Got {result}"
        print("✓ Test 5 passed: Ascending array")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        _tests_failed += 1

    # Test 6: All same
    try:
        result = max_sliding_window([5, 5, 5, 5], 2)
        assert result == [5, 5, 5], f"Got {result}"
        print("✓ Test 6 passed: All same")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 6 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 6 error: {e}")
        _tests_failed += 1

    # Test 7: Negative numbers
    try:
        result = max_sliding_window([-1, -2, -3, -4], 2)
        assert result == [-1, -2, -3], f"Got {result}"
        print("✓ Test 7 passed: Negative numbers")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 7 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 7 error: {e}")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
