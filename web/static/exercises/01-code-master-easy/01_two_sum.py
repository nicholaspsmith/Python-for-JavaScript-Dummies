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

'''HINTS
{
  "hint1": "from typing import List\n\n\ndef two_sum(nums: List[int], target: int) -> List[int]:\n    seen = {}  # Store number -> index mapping\n    ...",
  "hint2": "from typing import List\n\n\ndef two_sum(nums: List[int], target: int) -> List[int]:\n    # 1. Create empty dict to store seen numbers\n    # 2. Loop through nums with enumerate(nums)\n    # 3. Calculate complement = target - num\n    # 4. If complement in seen dict, return [seen[complement], i]\n    # 5. Otherwise, store seen[num] = i\n    ...",
  "solution": "from typing import List\n\n\ndef two_sum(nums: List[int], target: int) -> List[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        complement = target - num\n        if complement in seen:\n            return [seen[complement], i]\n        seen[num] = i\n    return []"
}
HINTS'''


def two_sum(nums: List[int], target: int) -> List[int]:
    """Return indices of two numbers that add up to target."""
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Basic case
    _t1_input = "nums=[2, 7, 11, 15], target=9"
    _t1_expected = [0, 1]
    try:
        result = two_sum([2, 7, 11, 15], 9)
        assert sorted(result) == _t1_expected, f"Expected {_t1_expected}, got {result}"
        print("✓ Test 1 passed: Basic two sum")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|Error: {e}")
        _tests_failed += 1

    # Test 2: Target at end
    _t2_input = "nums=[3, 2, 4], target=6"
    _t2_expected = [1, 2]
    try:
        result = two_sum([3, 2, 4], 6)
        assert sorted(result) == _t2_expected, f"Expected {_t2_expected}, got {result}"
        print("✓ Test 2 passed: Target at end of array")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|Error: {e}")
        _tests_failed += 1

    # Test 3: Same numbers
    _t3_input = "nums=[3, 3], target=6"
    _t3_expected = [0, 1]
    try:
        result = two_sum([3, 3], 6)
        assert sorted(result) == _t3_expected, f"Expected {_t3_expected}, got {result}"
        print("✓ Test 3 passed: Duplicate numbers")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|Error: {e}")
        _tests_failed += 1

    # Test 4: Negative numbers
    _t4_input = "nums=[-1, -2, -3, -4, -5], target=-8"
    _t4_expected = [2, 4]
    try:
        result = two_sum([-1, -2, -3, -4, -5], -8)
        assert sorted(result) == _t4_expected, f"Expected {_t4_expected}, got {result}"
        print("✓ Test 4 passed: Negative numbers")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|Error: {e}")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
