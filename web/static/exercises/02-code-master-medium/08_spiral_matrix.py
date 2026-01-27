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


'''HINTS
{
  "hint1": "def spiral_order(matrix: List[List[int]]) -> List[int]:\\n    # Track four boundaries: top, bottom, left, right\\n    # Initialize: top=0, bottom=len(matrix)-1, left=0, right=len(matrix[0])-1\\n    # Result list to collect elements",
  "hint2": "# Pseudocode:\\n# 1) Handle empty matrix edge case\\n# 2) Initialize boundaries: top=0, bottom=rows-1, left=0, right=cols-1\\n# 3) While top <= bottom and left <= right:\\n#    a) Go RIGHT: iterate col from left to right, add matrix[top][col], then top += 1\\n#    b) Go DOWN: iterate row from top to bottom, add matrix[row][right], then right -= 1\\n#    c) Go LEFT (if top <= bottom): iterate col from right to left, add matrix[bottom][col], then bottom -= 1\\n#    d) Go UP (if left <= right): iterate row from bottom to top, add matrix[row][left], then left += 1\\n# 4) Return result list",
  "solution": "def spiral_order(matrix: List[List[int]]) -> List[int]:\\n    if not matrix or not matrix[0]:\\n        return []\\n    \\n    result = []\\n    top, bottom = 0, len(matrix) - 1\\n    left, right = 0, len(matrix[0]) - 1\\n    \\n    while top <= bottom and left <= right:\\n        # Go right across top row\\n        for col in range(left, right + 1):\\n            result.append(matrix[top][col])\\n        top += 1\\n        \\n        # Go down right column\\n        for row in range(top, bottom + 1):\\n            result.append(matrix[row][right])\\n        right -= 1\\n        \\n        # Go left across bottom row (if rows remain)\\n        if top <= bottom:\\n            for col in range(right, left - 1, -1):\\n                result.append(matrix[bottom][col])\\n            bottom -= 1\\n        \\n        # Go up left column (if columns remain)\\n        if left <= right:\\n            for row in range(bottom, top - 1, -1):\\n                result.append(matrix[row][left])\\n            left += 1\\n    \\n    return result"
}
HINTS'''


def spiral_order(matrix: List[List[int]]) -> List[int]:
    """Return matrix elements in spiral order."""
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: 3x3 matrix
    _t1_input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    _t1_expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    try:
        result = spiral_order(_t1_input)
        assert result == _t1_expected, f"Got {result}"
        print("✓ Test 1 passed: 3x3 matrix")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{result}")
        _tests_failed += 1

    # Test 2: 3x4 matrix
    _t2_input = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    _t2_expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    try:
        result = spiral_order(_t2_input)
        assert result == _t2_expected, f"Got {result}"
        print("✓ Test 2 passed: 3x4 matrix")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{result}")
        _tests_failed += 1

    # Test 3: Single row
    _t3_input = [[1, 2, 3]]
    _t3_expected = [1, 2, 3]
    try:
        result = spiral_order(_t3_input)
        assert result == _t3_expected, f"Got {result}"
        print("✓ Test 3 passed: Single row")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{result}")
        _tests_failed += 1

    # Test 4: Single column
    _t4_input = [[1], [2], [3]]
    _t4_expected = [1, 2, 3]
    try:
        result = spiral_order(_t4_input)
        assert result == _t4_expected, f"Got {result}"
        print("✓ Test 4 passed: Single column")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{result}")
        _tests_failed += 1

    # Test 5: Single element
    _t5_input = [[1]]
    _t5_expected = [1]
    try:
        result = spiral_order(_t5_input)
        assert result == _t5_expected, f"Got {result}"
        print("✓ Test 5 passed: Single element")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|{result}")
        _tests_failed += 1

    # Test 6: Empty matrix
    _t6_input = []
    _t6_expected = []
    try:
        result = spiral_order(_t6_input)
        assert result == _t6_expected, f"Got {result}"
        print("✓ Test 6 passed: Empty matrix")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 6 failed: {e}")
        print(f"__TD__|{_t6_input}|{_t6_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 6 error: {e}")
        print(f"__TD__|{_t6_input}|{_t6_expected}|{result}")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
