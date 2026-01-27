"""
Single Number
==============

Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.

You must implement a solution with O(n) time complexity and O(1) extra space.

Example:
    Input: nums = [2,2,1]
    Output: 1

    Input: nums = [4,1,2,1,2]
    Output: 4

    Input: nums = [1]
    Output: 1

JS to Python Tips:
-----------------
- XOR operator is `^` (same as JS): `a ^ b`.
- XOR properties: a ^ a = 0, a ^ 0 = a, and XOR is commutative/associative.
- This means: 2 ^ 2 ^ 1 = 0 ^ 1 = 1. All pairs cancel out!
- Python's reduce: `from functools import reduce` then `reduce(lambda a, b: a ^ b, nums)`.
- Or just loop: `result = 0; for n in nums: result ^= n`
- Augmented assignment: `result ^= n` is like JS `result ^= n`.

The XOR trick is elegant:
- XORing a number with itself gives 0
- XORing with 0 gives the number back
- So XOR all numbers together: pairs cancel, single remains!
"""

from typing import List


'''HINTS
{
  "hint1": "def single_number(nums: List[int]) -> int:\\n\\nUse the XOR operator (^) which has the property that a ^ a = 0 and a ^ 0 = a. When you XOR all numbers together, duplicates cancel out.",
  "hint2": "1. Initialize result = 0\\n2. Loop through each number in nums\\n3. XOR the current number with result: result ^= num\\n4. After all numbers are processed, result contains the single number (duplicates canceled out)",
  "solution": "def single_number(nums: List[int]) -> int:\\n    result = 0\\n    for num in nums:\\n        result ^= num\\n    return result\\n\\n# Alternative using reduce:\\n# from functools import reduce\\n# def single_number(nums: List[int]) -> int:\\n#     return reduce(lambda a, b: a ^ b, nums)"
}
HINTS'''


def single_number(nums: List[int]) -> int:
    """Find the number that appears only once (all others appear twice)."""
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Basic case
    _t1_input = "nums=[2,2,1]"
    _t1_expected = 1
    try:
        result = single_number([2, 2, 1])
        assert result == _t1_expected, f"Expected {_t1_expected}, got {result}"
        print("✓ Test 1 passed: Basic case")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|Error: {e}")
        _tests_failed += 1

    # Test 2: Longer array
    _t2_input = "nums=[4,1,2,1,2]"
    _t2_expected = 4
    try:
        result = single_number([4, 1, 2, 1, 2])
        assert result == _t2_expected, f"Expected {_t2_expected}, got {result}"
        print("✓ Test 2 passed: Longer array")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|Error: {e}")
        _tests_failed += 1

    # Test 3: Single element
    _t3_input = "nums=[1]"
    _t3_expected = 1
    try:
        result = single_number([1])
        assert result == _t3_expected, f"Expected {_t3_expected}, got {result}"
        print("✓ Test 3 passed: Single element")
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
    _t4_input = "nums=[-1,-1,-2]"
    _t4_expected = -2
    try:
        result = single_number([-1, -1, -2])
        assert result == _t4_expected, f"Expected {_t4_expected}, got {result}"
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

    # Test 5: Mixed positive and negative
    _t5_input = "nums=[1,-1,1]"
    _t5_expected = -1
    try:
        result = single_number([1, -1, 1])
        assert result == _t5_expected, f"Expected {_t5_expected}, got {result}"
        print("✓ Test 5 passed: Mixed positive and negative")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|Error: {e}")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
