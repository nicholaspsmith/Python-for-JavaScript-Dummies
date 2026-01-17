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
    print("Running tests...")

    # Test 1: Some overlap
    result = merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    assert result == [[1, 6], [8, 10], [15, 18]], f"Got {result}"
    print("✓ Test 1 passed: Merged overlapping intervals")

    # Test 2: Touching intervals
    result = merge([[1, 4], [4, 5]])
    assert result == [[1, 5]], f"Got {result}"
    print("✓ Test 2 passed: Touching intervals merge")

    # Test 3: No overlap
    result = merge([[1, 2], [3, 4], [5, 6]])
    assert result == [[1, 2], [3, 4], [5, 6]], f"Got {result}"
    print("✓ Test 3 passed: No overlap")

    # Test 4: Single interval
    result = merge([[1, 5]])
    assert result == [[1, 5]], f"Got {result}"
    print("✓ Test 4 passed: Single interval")

    # Test 5: All merge into one
    result = merge([[1, 4], [2, 5], [3, 6]])
    assert result == [[1, 6]], f"Got {result}"
    print("✓ Test 5 passed: All merge into one")

    # Test 6: Unsorted input
    result = merge([[3, 4], [1, 2], [2, 3]])
    assert result == [[1, 4]], f"Got {result}"
    print("✓ Test 6 passed: Handles unsorted input")

    print("\n🎉 All tests passed!")
