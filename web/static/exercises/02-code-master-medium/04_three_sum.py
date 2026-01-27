"""
3Sum
=====

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

The solution set must not contain duplicate triplets.

Example:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

    Input: nums = [0,1,1]
    Output: [] (no triplets sum to 0)

    Input: nums = [0,0,0]
    Output: [[0,0,0]]

JS to Python Tips:
-----------------
- Sort in-place: `nums.sort()` (mutates list, returns None - NOT like JS!).
- Or create sorted copy: `sorted_nums = sorted(nums)`.
- Skip duplicates: `if i > 0 and nums[i] == nums[i-1]: continue`.
- Negative indexing: `nums[-1]` is last element.
- `while left < right:` same as JS.
- List literals: `[nums[i], nums[left], nums[right]]`.

Approach (O(n^2)):
1. Sort the array first.
2. For each element nums[i], use two pointers on the remaining elements.
3. Skip duplicates at each level to avoid duplicate triplets.
4. If sum < 0, move left pointer right. If sum > 0, move right pointer left.
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets that sum to zero.

    Hint: Sort first. For each i, use two pointers (left=i+1, right=end).
    Skip duplicates by checking if current == previous.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Normal case
    _t1_input = [-1, 0, 1, 2, -1, -4]
    _t1_expected = [[-1, -1, 2], [-1, 0, 1]]
    try:
        result = three_sum(_t1_input)
        assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in _t1_expected])
        print("✓ Test 1 passed: Normal case")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|N/A")
        _tests_failed += 1

    # Test 2: No solution
    _t2_input = [0, 1, 1]
    _t2_expected = []
    try:
        result = three_sum(_t2_input)
        assert result == _t2_expected
        print("✓ Test 2 passed: No solution")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|N/A")
        _tests_failed += 1

    # Test 3: All zeros
    _t3_input = [0, 0, 0]
    _t3_expected = [[0, 0, 0]]
    try:
        result = three_sum(_t3_input)
        assert result == _t3_expected
        print("✓ Test 3 passed: All zeros")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|N/A")
        _tests_failed += 1

    # Test 4: Empty/small input
    _t4_input = [0]
    _t4_expected = []
    try:
        result = three_sum(_t4_input)
        assert result == _t4_expected
        print("✓ Test 4 passed: Empty/small input")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|N/A")
        _tests_failed += 1

    # Test 5: Multiple triplets
    _t5_input = [-2, 0, 1, 1, 2]
    _t5_expected = [[-2, 0, 2], [-2, 1, 1]]
    try:
        result = three_sum(_t5_input)
        assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in _t5_expected])
        print("✓ Test 5 passed: Multiple triplets")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|N/A")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
