"""
Word Search
============

Given an m x n grid of characters and a string word, return True if word exists
in the grid. The word can be constructed from letters of adjacent cells
(horizontally or vertically neighboring). Each cell may only be used once.

Example:
    Input: board = [["A","B","C","E"],
                    ["S","F","C","S"],
                    ["A","D","E","E"]], word = "ABCCED"
    Output: True

    Input: board = same, word = "SEE"
    Output: True

    Input: board = same, word = "ABCB"
    Output: False (can't reuse 'B')

JS to Python Tips:
-----------------
- Backtracking pattern: try a path, mark visited, recurse, unmark if fails.
- Mark visited by temporarily modifying: `board[r][c] = '#'` (Python strings
  in lists are mutable at the list level).
- Tuple for directions: `directions = [(0,1), (1,0), (0,-1), (-1,0)]`.
- Boundary check: `0 <= new_row < rows and 0 <= new_col < cols`.
  Note: Python allows chained comparisons!
- `any()` and `all()` are Pythonic: `any(dfs(...) for dr, dc in directions)`.
  Returns True if any element is True.

Backtracking:
1. Try starting from each cell.
2. For each cell, try to build the word character by character.
3. Mark current cell as visited (to avoid reuse).
4. Explore all 4 directions.
5. Backtrack (unmark) if path doesn't work.
"""

from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    """
    Return True if word can be found in the grid using adjacent cells.

    Hint: Use DFS/backtracking. For each starting position, try to match
    the word character by character. Mark cells as visited by changing
    them temporarily (e.g., to '#'), then restore after backtracking.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Shared test board
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]

    # Test 1: Word exists
    try:
        _t1_input = (board, "ABCCED")
        _t1_expected = True
        result = exist(board, "ABCCED")
        assert result == _t1_expected
        print("✓ Test 1 passed: Word exists")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{e}")
        _tests_failed += 1

    # Test 2: Another valid word
    try:
        _t2_input = (board, "SEE")
        _t2_expected = True
        result = exist(board, "SEE")
        assert result == _t2_expected
        print("✓ Test 2 passed: Another valid word")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{e}")
        _tests_failed += 1

    # Test 3: Can't reuse cell
    try:
        _t3_input = (board, "ABCB")
        _t3_expected = False
        result = exist(board, "ABCB")
        assert result == _t3_expected
        print("✓ Test 3 passed: Can't reuse cell")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{e}")
        _tests_failed += 1

    # Test 4: Single cell
    try:
        _t4_input = ([["A"]], "A")
        _t4_expected = True
        result = exist([["A"]], "A")
        assert result == _t4_expected
        print("✓ Test 4 passed: Single cell")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{e}")
        _tests_failed += 1

    # Test 5: Word not in grid
    try:
        _t5_input = (board, "XYZ")
        _t5_expected = False
        result = exist(board, "XYZ")
        assert result == _t5_expected
        print("✓ Test 5 passed: Word not in grid")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|{e}")
        _tests_failed += 1

    # Test 6: Word longer than grid
    try:
        _t6_input = ([["A"]], "AB")
        _t6_expected = False
        result = exist([["A"]], "AB")
        assert result == _t6_expected
        print("✓ Test 6 passed: Word longer than grid")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 6 failed: {e}")
        print(f"__TD__|{_t6_input}|{_t6_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 6 error: {e}")
        print(f"__TD__|{_t6_input}|{_t6_expected}|{e}")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
