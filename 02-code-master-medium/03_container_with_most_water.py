"""
Container With Most Water
==========================

Given n non-negative integers representing heights of vertical lines,
find two lines that together with the x-axis form a container that holds the most water.

The container's area = min(height[i], height[j]) * (j - i)

Example:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: Lines at index 1 (height 8) and index 8 (height 7)
                 form a container of area = min(8,7) * (8-1) = 7 * 7 = 49

    Input: height = [1,1]
    Output: 1

JS to Python Tips:
-----------------
- Two pointers: `left, right = 0, len(height) - 1` (tuple unpacking).
- `min(a, b)` and `max(a, b)` are built-in (no Math object).
- Area calculation: `area = min(height[left], height[right]) * (right - left)`.
- Move the pointer with smaller height inward (greedy choice).

Why move the smaller pointer?
- Width will definitely decrease.
- Only chance for more area is if we find a taller line.
- Moving the taller one can only make things worse (we're limited by the shorter side).

O(n) time, O(1) space with two pointers.
"""

from typing import List


'''HINTS
{
  "hint1": "def max_area(height: List[int]) -> int:\\n    # Use two pointers starting from both ends of the array\\n    # left = 0, right = len(height) - 1",
  "hint2": "# Pseudocode:\\n# 1. Initialize left = 0, right = len(height) - 1, max_area = 0\\n# 2. While left < right:\\n#    a. Calculate area = min(height[left], height[right]) * (right - left)\\n#    b. Update max_area if current area is larger\\n#    c. Move the pointer with the smaller height inward\\n# 3. Return max_area",
  "solution": "def max_area(height: List[int]) -> int:\\n    left, right = 0, len(height) - 1\\n    max_area = 0\\n    \\n    while left < right:\\n        width = right - left\\n        h = min(height[left], height[right])\\n        area = width * h\\n        max_area = max(max_area, area)\\n        \\n        if height[left] < height[right]:\\n            left += 1\\n        else:\\n            right -= 1\\n    \\n    return max_area"
}
HINTS'''


def max_area(height: List[int]) -> int:
    """
    Find the maximum water container area.

    Hint: Two pointers starting from both ends.
    Calculate area, then move the pointer with the shorter height.
    Track maximum area found.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Example case
    try:
        _t1_input = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        _t1_expected = 49
        result = max_area(_t1_input)
        assert result == _t1_expected
        print("✓ Test 1 passed: Example case")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{e}")
        _tests_failed += 1

    # Test 2: Two elements
    try:
        _t2_input = [1, 1]
        _t2_expected = 1
        result = max_area(_t2_input)
        assert result == _t2_expected
        print("✓ Test 2 passed: Two elements")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{e}")
        _tests_failed += 1

    # Test 3: Decreasing heights
    try:
        _t3_input = [4, 3, 2, 1, 4]
        _t3_expected = 16
        result = max_area(_t3_input)
        assert result == _t3_expected
        print("✓ Test 3 passed: Decreasing heights")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{e}")
        _tests_failed += 1

    # Test 4: All same height
    try:
        _t4_input = [5, 5, 5, 5]
        _t4_expected = 15
        result = max_area(_t4_input)
        assert result == _t4_expected
        print("✓ Test 4 passed: All same height")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{e}")
        _tests_failed += 1

    # Test 5: Two different heights
    try:
        _t5_input = [1, 2]
        _t5_expected = 1
        result = max_area(_t5_input)
        assert result == _t5_expected
        print("✓ Test 5 passed: Two different heights")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|{e}")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
