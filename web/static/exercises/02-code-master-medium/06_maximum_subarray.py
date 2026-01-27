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


'''HINTS
{
  "hint1": "def max_subarray(nums: List[int]) -> int:\\n    # Track current_sum (running sum of current subarray)\\n    # Track max_sum (best sum seen so far)\\n    ...",
  "hint2": "# Pseudocode:\\n# 1. Initialize max_sum = nums[0], current_sum = 0\\n# 2. For each num in nums:\\n#    current_sum = max(num, current_sum + num)  # extend or start fresh\\n#    max_sum = max(max_sum, current_sum)  # update best\\n# 3. Return max_sum",
  "solution": "def max_subarray(nums: List[int]) -> int:\\n    max_sum = nums[0]\\n    current_sum = 0\\n    for num in nums:\\n        current_sum = max(num, current_sum + num)\\n        max_sum = max(max_sum, current_sum)\\n    return max_sum"
}
HINTS'''


def max_subarray(nums: List[int]) -> int:
    """Find the maximum sum of any contiguous subarray."""
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Mixed positives and negatives
    try:
        _t1_input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        _t1_expected = 6
        result = max_subarray(_t1_input)
        assert result == _t1_expected
        print("✓ Test 1 passed: Mixed positives and negatives")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|None")
        _tests_failed += 1

    # Test 2: Single element
    try:
        _t2_input = [1]
        _t2_expected = 1
        result = max_subarray(_t2_input)
        assert result == _t2_expected
        print("✓ Test 2 passed: Single element")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|None")
        _tests_failed += 1

    # Test 3: All positive
    try:
        _t3_input = [5, 4, -1, 7, 8]
        _t3_expected = 23
        result = max_subarray(_t3_input)
        assert result == _t3_expected
        print("✓ Test 3 passed: All positive")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|None")
        _tests_failed += 1

    # Test 4: All negative
    try:
        _t4_input = [-3, -2, -1, -4]
        _t4_expected = -1
        result = max_subarray(_t4_input)
        assert result == _t4_expected
        print("✓ Test 4 passed: All negative")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|None")
        _tests_failed += 1

    # Test 5: Single negative
    try:
        _t5_input = [-1]
        _t5_expected = -1
        result = max_subarray(_t5_input)
        assert result == _t5_expected
        print("✓ Test 5 passed: Single negative")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|None")
        _tests_failed += 1

    # Test 6: Zero included
    try:
        _t6_input = [-2, 0, -1]
        _t6_expected = 0
        result = max_subarray(_t6_input)
        assert result == _t6_expected
        print("✓ Test 6 passed: Zero included")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 6 failed: {e}")
        print(f"__TD__|{_t6_input}|{_t6_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 6 error: {e}")
        print(f"__TD__|{_t6_input}|{_t6_expected}|None")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
