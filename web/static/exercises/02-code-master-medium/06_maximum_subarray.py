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
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Mixed positives and negatives
    try:

        assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
        print("✓ Test 1 passed: Mixed positives and negatives")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        _tests_failed += 1

    # Test 2: Single element
    try:

        assert max_subarray([1]) == 1
        print("✓ Test 2 passed: Single element")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        _tests_failed += 1

    # Test 3: All positive
    try:

        assert max_subarray([5, 4, -1, 7, 8]) == 23
        print("✓ Test 3 passed: All positive")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        _tests_failed += 1

    # Test 4: All negative
    try:

        assert max_subarray([-3, -2, -1, -4]) == -1
        print("✓ Test 4 passed: All negative")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        _tests_failed += 1

    # Test 5: Single negative
    try:

        assert max_subarray([-1]) == -1
        print("✓ Test 5 passed: Single negative")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        _tests_failed += 1

    # Test 6: Zero included
    try:

        assert max_subarray([-2, 0, -1]) == 0
        print("✓ Test 6 passed: Zero included")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 6 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 6 error: {e}")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
