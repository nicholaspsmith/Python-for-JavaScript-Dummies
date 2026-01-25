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


def single_number(nums: List[int]) -> int:
    """
    Find the number that appears only once (all others appear twice).

    Hint: XOR all numbers together. Pairs will cancel out (a ^ a = 0),
    leaving only the single number.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Basic case
    try:

        assert single_number([2, 2, 1]) == 1
        print("✓ Test 1 passed: Basic case")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        _tests_failed += 1

    # Test 2: Longer array
    try:

        assert single_number([4, 1, 2, 1, 2]) == 4
        print("✓ Test 2 passed: Longer array")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        _tests_failed += 1

    # Test 3: Single element
    try:

        assert single_number([1]) == 1
        print("✓ Test 3 passed: Single element")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        _tests_failed += 1

    # Test 4: Negative numbers
    try:

        assert single_number([-1, -1, -2]) == -2
        print("✓ Test 4 passed: Negative numbers")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        _tests_failed += 1

    # Test 5: Mixed positive and negative
    try:

        assert single_number([1, -1, 1]) == -1
        print("✓ Test 5 passed: Mixed positive and negative")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
