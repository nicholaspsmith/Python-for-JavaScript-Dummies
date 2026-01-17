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


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge overlapping intervals.

    Hint: Sort by start time. For each interval, check if it overlaps
    with the last merged interval. If yes, extend; if no, add new.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Some overlap
    try:
        result = merge([[1, 3], [2, 6], [8, 10], [15, 18]])
        assert result == [[1, 6], [8, 10], [15, 18]], f"Got {result}"
        print("✓ Test 1 passed: Some overlap")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        _tests_failed += 1

    # Test 2: Touching intervals
    try:
        result = merge([[1, 4], [4, 5]])
        assert result == [[1, 5]], f"Got {result}"
        print("✓ Test 2 passed: Touching intervals")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        _tests_failed += 1

    # Test 3: No overlap
    try:
        result = merge([[1, 2], [3, 4], [5, 6]])
        assert result == [[1, 2], [3, 4], [5, 6]], f"Got {result}"
        print("✓ Test 3 passed: No overlap")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        _tests_failed += 1

    # Test 4: Single interval
    try:
        result = merge([[1, 5]])
        assert result == [[1, 5]], f"Got {result}"
        print("✓ Test 4 passed: Single interval")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        _tests_failed += 1

    # Test 5: All merge into one
    try:
        result = merge([[1, 4], [2, 5], [3, 6]])
        assert result == [[1, 6]], f"Got {result}"
        print("✓ Test 5 passed: All merge into one")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        _tests_failed += 1

    # Test 6: Unsorted input
    try:
        result = merge([[3, 4], [1, 2], [2, 3]])
        assert result == [[1, 4]], f"Got {result}"
        print("✓ Test 6 passed: Unsorted input")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 6 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 6 error: {e}")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
