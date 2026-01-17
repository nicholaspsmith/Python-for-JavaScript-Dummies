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
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Basic case
    try:
        result = two_sum([2, 7, 11, 15], 9)
        assert sorted(result) == [0, 1], f"Expected [0, 1], got {result}"
        print("✓ Test 1 passed: Basic two sum")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        _tests_failed += 1

    # Test 2: Target at end
    try:
        result = two_sum([3, 2, 4], 6)
        assert sorted(result) == [1, 2], f"Expected [1, 2], got {result}"
        print("✓ Test 2 passed: Target at end of array")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        _tests_failed += 1

    # Test 3: Same numbers
    try:
        result = two_sum([3, 3], 6)
        assert sorted(result) == [0, 1], f"Expected [0, 1], got {result}"
        print("✓ Test 3 passed: Duplicate numbers")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        _tests_failed += 1

    # Test 4: Negative numbers
    try:
        result = two_sum([-1, -2, -3, -4, -5], -8)
        assert sorted(result) == [2, 4], f"Expected [2, 4], got {result}"
        print("✓ Test 4 passed: Negative numbers")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
