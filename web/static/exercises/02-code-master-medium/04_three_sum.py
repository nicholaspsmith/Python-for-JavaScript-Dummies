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


'''HINTS
{
  "hint1": "def three_sum(nums: List[int]) -> List[List[int]]:\\n    # Sort the array first: nums.sort()\\n    # Use two pointers for the inner loop: left = i + 1, right = len(nums) - 1",
  "hint2": "# Pseudocode:\\n# 1) Sort the array: nums.sort()\\n# 2) For each index i from 0 to len(nums)-3:\\n#    - Skip if nums[i] == nums[i-1] (avoid duplicates)\\n#    - Set left = i + 1, right = len(nums) - 1\\n#    - While left < right:\\n#      - Calculate total = nums[i] + nums[left] + nums[right]\\n#      - If total < 0: move left pointer right (left += 1)\\n#      - If total > 0: move right pointer left (right -= 1)\\n#      - If total == 0: add triplet, skip duplicates, move both pointers",
  "solution": "def three_sum(nums: List[int]) -> List[List[int]]:\\n    result = []\\n    nums.sort()\\n    \\n    for i in range(len(nums) - 2):\\n        # Skip duplicates for i\\n        if i > 0 and nums[i] == nums[i - 1]:\\n            continue\\n        \\n        left, right = i + 1, len(nums) - 1\\n        \\n        while left < right:\\n            total = nums[i] + nums[left] + nums[right]\\n            \\n            if total < 0:\\n                left += 1\\n            elif total > 0:\\n                right -= 1\\n            else:\\n                result.append([nums[i], nums[left], nums[right]])\\n                # Skip duplicates for left\\n                while left < right and nums[left] == nums[left + 1]:\\n                    left += 1\\n                # Skip duplicates for right\\n                while left < right and nums[right] == nums[right - 1]:\\n                    right -= 1\\n                left += 1\\n                right -= 1\\n    \\n    return result"
}
HINTS'''


def three_sum(nums: List[int]) -> List[List[int]]:
    """Find all unique triplets that sum to zero."""
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
