"""
Search in Rotated Sorted Array
===============================

A sorted array has been rotated at some pivot unknown to you beforehand.
For example, [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].

Given the rotated array nums and a target value, return the index of target
if it is in nums, or -1 if it is not.

You must write an algorithm with O(log n) runtime complexity (binary search).

Example:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

    Input: nums = [1], target = 0
    Output: -1

JS to Python Tips:
-----------------
- Integer division: `mid = (left + right) // 2` (double slash!).
  In JS you'd use `Math.floor((left + right) / 2)`.
- Python allows chained comparisons: `left <= target < nums[mid]` instead of
  `left <= target && target < nums[mid]`. This is unique to Python!
- `while left <= right:` same as JS.

Modified Binary Search:
- Find mid element. One half is always sorted!
- Determine which half is sorted (compare nums[left] vs nums[mid]).
- Check if target is in the sorted half.
- If yes, search that half; if no, search the other half.

Key insight: In a rotated sorted array, at least one half is always properly sorted.
"""

from typing import List


'''HINTS
{
  "hint1": "def search(nums: List[int], target: int) -> int:\\n    # Use binary search with left, right, mid pointers\\n    left, right = 0, len(nums) - 1\\n    while left <= right:\\n        mid = (left + right) // 2\\n        # Your logic here\\n    return -1",
  "hint2": "Pseudocode:\\n1) Initialize left = 0, right = len(nums) - 1\\n2) While left <= right:\\n   a) Calculate mid = (left + right) // 2\\n   b) If nums[mid] == target, return mid\\n   c) Check if left half is sorted: nums[left] <= nums[mid]\\n      - If target is in sorted left half (nums[left] <= target < nums[mid]), search left: right = mid - 1\\n      - Else search right: left = mid + 1\\n   d) Else right half is sorted:\\n      - If target is in sorted right half (nums[mid] < target <= nums[right]), search right: left = mid + 1\\n      - Else search left: right = mid - 1\\n3) Return -1 if not found",
  "solution": "def search(nums: List[int], target: int) -> int:\\n    left, right = 0, len(nums) - 1\\n    \\n    while left <= right:\\n        mid = (left + right) // 2\\n        \\n        if nums[mid] == target:\\n            return mid\\n        \\n        # Check if left half is sorted\\n        if nums[left] <= nums[mid]:\\n            # Target is in the sorted left half\\n            if nums[left] <= target < nums[mid]:\\n                right = mid - 1\\n            else:\\n                left = mid + 1\\n        else:\\n            # Right half is sorted\\n            # Target is in the sorted right half\\n            if nums[mid] < target <= nums[right]:\\n                left = mid + 1\\n            else:\\n                right = mid - 1\\n    \\n    return -1"
}
HINTS'''


def search(nums: List[int], target: int) -> int:
    """Search for target in rotated sorted array."""
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Target in rotated part
    try:
        _t1_input = {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 0}
        _t1_expected = 4
        result = search([4, 5, 6, 7, 0, 1, 2], 0)
        assert result == _t1_expected
        print("✓ Test 1 passed: Target in rotated part")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{e}")
        _tests_failed += 1

    # Test 2: Target not found
    try:
        _t2_input = {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 3}
        _t2_expected = -1
        result = search([4, 5, 6, 7, 0, 1, 2], 3)
        assert result == _t2_expected
        print("✓ Test 2 passed: Target not found")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{e}")
        _tests_failed += 1

    # Test 3: Single element not found
    try:
        _t3_input = {"nums": [1], "target": 0}
        _t3_expected = -1
        result = search([1], 0)
        assert result == _t3_expected
        print("✓ Test 3 passed: Single element not found")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{e}")
        _tests_failed += 1

    # Test 4: Single element found
    try:
        _t4_input = {"nums": [1], "target": 1}
        _t4_expected = 0
        result = search([1], 1)
        assert result == _t4_expected
        print("✓ Test 4 passed: Single element found")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{e}")
        _tests_failed += 1

    # Test 5: Target in first half
    try:
        _t5_input = {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 5}
        _t5_expected = 1
        result = search([4, 5, 6, 7, 0, 1, 2], 5)
        assert result == _t5_expected
        print("✓ Test 5 passed: Target in first half")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|{e}")
        _tests_failed += 1

    # Test 6: Not rotated (edge case)
    try:
        _t6_input = {"nums": [1, 2, 3, 4, 5], "target": 3}
        _t6_expected = 2
        result = search([1, 2, 3, 4, 5], 3)
        assert result == _t6_expected
        print("✓ Test 6 passed: Not rotated (edge case)")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 6 failed: {e}")
        print(f"__TD__|{_t6_input}|{_t6_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 6 error: {e}")
        print(f"__TD__|{_t6_input}|{_t6_expected}|{e}")
        _tests_failed += 1

    # Test 7: Fully rotated (same as original)
    try:
        _t7_input = {"nums": [2, 1], "target": 1}
        _t7_expected = 1
        result = search([2, 1], 1)
        assert result == _t7_expected
        print("✓ Test 7 passed: Fully rotated (same as original)")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 7 failed: {e}")
        print(f"__TD__|{_t7_input}|{_t7_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 7 error: {e}")
        print(f"__TD__|{_t7_input}|{_t7_expected}|{e}")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
