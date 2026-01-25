"""
Spiral Matrix
==============

Given an m x n matrix, return all elements in spiral order.

Spiral order: Start top-left, go right, then down, then left, then up,
and repeat inward until all elements are visited.

Example:
    Input: [[1,2,3],
            [4,5,6],
            [7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

    Input: [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

JS to Python Tips:
-----------------
- 2D array access: `matrix[row][col]` (same as JS).
- Empty check: `if not matrix or not matrix[0]:`.
- `len(matrix)` for rows, `len(matrix[0])` for columns.
- Use boundary variables: top, bottom, left, right.
- `range(left, right + 1)` for inclusive iteration.
- `range(right, left - 1, -1)` for reverse iteration (step = -1).

Approach:
- Maintain four boundaries: top, bottom, left, right.
- Traverse in order: right across top row, down right column,
  left across bottom row, up left column.
- After each direction, shrink the corresponding boundary.
- Continue until boundaries cross.
"""

from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    Return matrix elements in spiral order.

    Hint: Use four boundaries (top, bottom, left, right).
    Go right, then down, then left, then up.
    After each direction, shrink that boundary and check if done.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: 3x3 matrix
    try:
        result = spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        assert result == [1, 2, 3, 6, 9, 8, 7, 4, 5], f"Got {result}"
        print("✓ Test 1 passed: 3x3 matrix")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        _tests_failed += 1

    # Test 2: 3x4 matrix
    try:
        result = spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        assert result == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], f"Got {result}"
        print("✓ Test 2 passed: 3x4 matrix")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        _tests_failed += 1

    # Test 3: Single row
    try:
        result = spiral_order([[1, 2, 3]])
        assert result == [1, 2, 3], f"Got {result}"
        print("✓ Test 3 passed: Single row")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        _tests_failed += 1

    # Test 4: Single column
    try:
        result = spiral_order([[1], [2], [3]])
        assert result == [1, 2, 3], f"Got {result}"
        print("✓ Test 4 passed: Single column")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        _tests_failed += 1

    # Test 5: Single element
    try:
        result = spiral_order([[1]])
        assert result == [1], f"Got {result}"
        print("✓ Test 5 passed: Single element")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        _tests_failed += 1

    # Test 6: Empty matrix
    try:
        result = spiral_order([])
        assert result == [], f"Got {result}"
        print("✓ Test 6 passed: Empty matrix")
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
