"""
Trapping Rain Water
====================

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

Example:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6 (the elevation map can trap 6 units of rain water)

    Visual:
            █
        █   ██ █
      █ ██ ██████
    0,1,0,2,1,0,1,3,2,1,2,1

    Input: height = [4,2,0,3,2,5]
    Output: 9

JS to Python Tips:
-----------------
- `max()` works on iterables: `max(height[:i+1])` finds max of subarray.
- List comprehension with `min/max`: `[min(a, b) for a, b in zip(left, right)]`.
- `zip()` pairs up elements from multiple iterables (like JS you'd manually iterate).
- Two-pointer approach works great here.
- Prefix max arrays: `left_max[i] = max of height[0..i]`.

Multiple approaches:

1. Brute Force O(n^2): For each position, find max left and max right, water = min - height.

2. DP/Prefix arrays O(n): Precompute left_max and right_max arrays.
   Water at i = min(left_max[i], right_max[i]) - height[i].

3. Two Pointers O(n), O(1) space: Track left_max and right_max as you go.
   Move the pointer with smaller max value.

The key insight: water at any position = min(max_left, max_right) - height[i].
"""

from typing import List


'''HINTS
{
  "hint1": "def trap(height: List[int]) -> int:\\n    # Use two pointers from both ends\\n    # Track left_max and right_max as you iterate\\n    left, right = 0, len(height) - 1\\n    left_max, right_max = 0, 0",
  "hint2": "# Pseudocode:\\n# 1. Initialize two pointers: left = 0, right = len(height) - 1\\n# 2. Track left_max and right_max, both starting at 0\\n# 3. While left < right:\\n#    - Update left_max = max(left_max, height[left])\\n#    - Update right_max = max(right_max, height[right])\\n#    - If left_max < right_max: water += left_max - height[left], move left++\\n#    - Else: water += right_max - height[right], move right--\\n# 4. Return total water",
  "solution": "def trap(height: List[int]) -> int:\\n    if not height:\\n        return 0\\n    \\n    left, right = 0, len(height) - 1\\n    left_max, right_max = 0, 0\\n    water = 0\\n    \\n    while left < right:\\n        left_max = max(left_max, height[left])\\n        right_max = max(right_max, height[right])\\n        \\n        if left_max < right_max:\\n            water += left_max - height[left]\\n            left += 1\\n        else:\\n            water += right_max - height[right]\\n            right -= 1\\n    \\n    return water"
}
HINTS'''


def trap(height: List[int]) -> int:
    """Calculate total trapped rain water."""
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Standard example
    try:
        _t1_input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        _t1_expected = 6
        result = trap(_t1_input)
        assert result == _t1_expected
        print("✓ Test 1 passed: Standard example")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|None")
        _tests_failed += 1

    # Test 2: Another example
    try:
        _t2_input = [4, 2, 0, 3, 2, 5]
        _t2_expected = 9
        result = trap(_t2_input)
        assert result == _t2_expected
        print("✓ Test 2 passed: Another example")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|None")
        _tests_failed += 1

    # Test 3: No water (ascending)
    try:
        _t3_input = [1, 2, 3, 4]
        _t3_expected = 0
        result = trap(_t3_input)
        assert result == _t3_expected
        print("✓ Test 3 passed: No water (ascending)")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|None")
        _tests_failed += 1

    # Test 4: No water (descending)
    try:
        _t4_input = [4, 3, 2, 1]
        _t4_expected = 0
        result = trap(_t4_input)
        assert result == _t4_expected
        print("✓ Test 4 passed: No water (descending)")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|None")
        _tests_failed += 1

    # Test 5: Empty
    try:
        _t5_input = []
        _t5_expected = 0
        result = trap(_t5_input)
        assert result == _t5_expected
        print("✓ Test 5 passed: Empty")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|None")
        _tests_failed += 1

    # Test 6: Single/double elements
    try:
        _t6_input = [5, 4]
        _t6_expected = 0
        result = trap(_t6_input)
        assert result == _t6_expected
        print("✓ Test 6 passed: Single/double elements")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 6 failed: {e}")
        print(f"__TD__|{_t6_input}|{_t6_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 6 error: {e}")
        print(f"__TD__|{_t6_input}|{_t6_expected}|None")
        _tests_failed += 1

    # Test 7: Valley
    try:
        _t7_input = [5, 0, 5]
        _t7_expected = 5
        result = trap(_t7_input)
        assert result == _t7_expected
        print("✓ Test 7 passed: Valley")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 7 failed: {e}")
        print(f"__TD__|{_t7_input}|{_t7_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 7 error: {e}")
        print(f"__TD__|{_t7_input}|{_t7_expected}|None")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
