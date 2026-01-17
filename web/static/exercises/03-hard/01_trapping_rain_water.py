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


def trap(height: List[int]) -> int:
    """
    Calculate total trapped rain water.

    Hint: For each position, water trapped = min(max_left, max_right) - height[i].
    Use two pointers starting from both ends, tracking left_max and right_max.
    Move the pointer with the smaller max.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Standard example
    try:

        assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
        print("✓ Test 1 passed: Standard example")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        _tests_failed += 1

    # Test 2: Another example
    try:

        assert trap([4, 2, 0, 3, 2, 5]) == 9
        print("✓ Test 2 passed: Another example")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        _tests_failed += 1

    # Test 3: No water (ascending)
    try:

        assert trap([1, 2, 3, 4]) == 0
        print("✓ Test 3 passed: No water (ascending)")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        _tests_failed += 1

    # Test 4: No water (descending)
    try:

        assert trap([4, 3, 2, 1]) == 0
        print("✓ Test 4 passed: No water (descending)")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        _tests_failed += 1

    # Test 5: Empty
    try:

        assert trap([]) == 0
        print("✓ Test 5 passed: Empty")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        _tests_failed += 1

    # Test 6: Single/double elements
    try:

        assert trap([5, 4]) == 0
        print("✓ Test 6 passed: Single/double elements")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 6 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 6 error: {e}")
        _tests_failed += 1

    # Test 7: Valley
    try:

        assert trap([5, 0, 5]) == 5
        print("✓ Test 7 passed: Valley")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 7 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 7 error: {e}")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
