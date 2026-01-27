"""
Merge Intervals
================

Given an array of intervals where intervals[i] = [start_i, end_i],
merge all overlapping intervals and return an array of non-overlapping intervals.

Example:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: [1,3] and [2,6] overlap, merge to [1,6]

    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: [1,4] and [4,5] are touching, merge to [1,5]

JS to Python Tips:
-----------------
- Sort by first element: `intervals.sort(key=lambda x: x[0])`.
  The `key` parameter is like JS `sort((a, b) => a[0] - b[0])`.
- Or `intervals.sort()` works too since tuples/lists compare element by element.
- `result[-1]` gets last element of list (negative indexing!).
- Unpacking: `start, end = interval` extracts both values.
- List append: `result.append([start, end])`.

Approach:
1. Sort intervals by start time.
2. For each interval:
   - If it overlaps with previous (start <= prev_end), merge by extending end.
   - Otherwise, add it as a new interval.
3. Two intervals overlap if current.start <= previous.end.
"""

from typing import List


'''HINTS
{
  "hint1": "def merge(intervals: List[List[int]]) -> List[List[int]]:\\n    intervals.sort(key=lambda x: x[0])\\n    result = [intervals[0]]",
  "hint2": "1) Sort intervals by start: intervals.sort(key=lambda x: x[0])\\n2) Initialize result with first interval: result = [intervals[0]]\\n3) For each interval in intervals[1:]:\\n   - If current start <= result[-1][1], merge: result[-1][1] = max(result[-1][1], current end)\\n   - Else append current interval to result\\n4) Return result",
  "solution": "def merge(intervals: List[List[int]]) -> List[List[int]]:\\n    if not intervals:\\n        return []\\n    intervals.sort(key=lambda x: x[0])\\n    result = [intervals[0]]\\n    for start, end in intervals[1:]:\\n        if start <= result[-1][1]:\\n            result[-1][1] = max(result[-1][1], end)\\n        else:\\n            result.append([start, end])\\n    return result"
}
HINTS'''


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """Merge overlapping intervals."""
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Some overlap
    _t1_input = [[1, 3], [2, 6], [8, 10], [15, 18]]
    _t1_expected = [[1, 6], [8, 10], [15, 18]]
    try:
        result = merge(_t1_input)
        assert result == _t1_expected, f"Got {result}"
        print("✓ Test 1 passed: Some overlap")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|None")
        _tests_failed += 1

    # Test 2: Touching intervals
    _t2_input = [[1, 4], [4, 5]]
    _t2_expected = [[1, 5]]
    try:
        result = merge(_t2_input)
        assert result == _t2_expected, f"Got {result}"
        print("✓ Test 2 passed: Touching intervals")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|None")
        _tests_failed += 1

    # Test 3: No overlap
    _t3_input = [[1, 2], [3, 4], [5, 6]]
    _t3_expected = [[1, 2], [3, 4], [5, 6]]
    try:
        result = merge(_t3_input)
        assert result == _t3_expected, f"Got {result}"
        print("✓ Test 3 passed: No overlap")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|None")
        _tests_failed += 1

    # Test 4: Single interval
    _t4_input = [[1, 5]]
    _t4_expected = [[1, 5]]
    try:
        result = merge(_t4_input)
        assert result == _t4_expected, f"Got {result}"
        print("✓ Test 4 passed: Single interval")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|None")
        _tests_failed += 1

    # Test 5: All merge into one
    _t5_input = [[1, 4], [2, 5], [3, 6]]
    _t5_expected = [[1, 6]]
    try:
        result = merge(_t5_input)
        assert result == _t5_expected, f"Got {result}"
        print("✓ Test 5 passed: All merge into one")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|None")
        _tests_failed += 1

    # Test 6: Unsorted input
    _t6_input = [[3, 4], [1, 2], [2, 3]]
    _t6_expected = [[1, 4]]
    try:
        result = merge(_t6_input)
        assert result == _t6_expected, f"Got {result}"
        print("✓ Test 6 passed: Unsorted input")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 6 failed: {e}")
        print(f"__TD__|{_t6_input}|{_t6_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 6 error: {e}")
        print(f"__TD__|{_t6_input}|{_t6_expected}|None")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
