"""
Remove Duplicates from Sorted Array
=====================================

Given a sorted array `nums`, remove the duplicates in-place such that each
element appears only once and returns the new length.

Do not allocate extra space for another array - modify the input array in-place
with O(1) extra memory.

The relative order of elements should be kept the same. The first k elements
of nums should hold the final result (it doesn't matter what you leave beyond k).

Example:
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]

    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

JS to Python Tips:
-----------------
- In-place modification works the same: `nums[i] = value` modifies the list.
- Two-pointer technique: one pointer for reading, one for writing.
- Unlike JS, Python lists are always mutable (no frozen arrays by default).
- `len(nums)` instead of `nums.length`.
- Edge case: `if not nums:` checks for empty list.

The key insight: since the array is sorted, duplicates are adjacent.
Use a "write pointer" that only advances when you find a new unique value.
"""

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """
    Remove duplicates in-place and return the new length.

    Hint: Use two pointers - one to track where to write (k),
    one to iterate through the array.
    When you find a new number different from nums[k-1], write it at nums[k].
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Basic case
    _t1_input = "nums=[1,1,2]"
    _t1_expected = [1, 2]
    try:
        nums = [1, 1, 2]
        k = remove_duplicates(nums)
        result = nums[:k]
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
    _t2_input = "nums=[0,0,1,1,1,2,2,3,3,4]"
    _t2_expected = [0, 1, 2, 3, 4]
    try:
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = remove_duplicates(nums)
        result = nums[:k]
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

    # Test 3: No duplicates
    _t3_input = "nums=[1,2,3]"
    _t3_expected = [1, 2, 3]
    try:
        nums = [1, 2, 3]
        k = remove_duplicates(nums)
        result = nums[:k]
        assert result == _t3_expected, f"Expected {_t3_expected}, got {result}"
        print("✓ Test 3 passed: No duplicates")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|Error: {e}")
        _tests_failed += 1

    # Test 4: All duplicates
    _t4_input = "nums=[5,5,5,5]"
    _t4_expected = [5]
    try:
        nums = [5, 5, 5, 5]
        k = remove_duplicates(nums)
        result = nums[:k]
        assert result == _t4_expected, f"Expected {_t4_expected}, got {result}"
        print("✓ Test 4 passed: All duplicates")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|Error: {e}")
        _tests_failed += 1

    # Test 5: Empty array
    _t5_input = "nums=[]"
    _t5_expected = 0
    try:
        nums = []
        k = remove_duplicates(nums)
        result = k
        assert result == _t5_expected, f"Expected {_t5_expected}, got {result}"
        print("✓ Test 5 passed: Empty array")
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
