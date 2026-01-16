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
    print("Running tests...")

    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]

    # Test 1: Word exists
    assert exist(board, "ABCCED") == True
    print("✓ Exercise 2.1 passed: Found 'ABCCED'")

    # Test 2: Another valid word
    assert exist(board, "SEE") == True
    print("✓ Exercise 2.2 passed: Found 'SEE'")

    # Test 3: Can't reuse cell
    assert exist(board, "ABCB") == False
    print("✓ Exercise 2.3 passed: 'ABCB' fails (can't reuse)")

    # Test 4: Single cell
    assert exist([["A"]], "A") == True
    print("✓ Exercise 2.4 passed: Single cell match")

    # Test 5: Word not in grid
    assert exist(board, "XYZ") == False
    print("✓ Exercise 2.5 passed: Word not found")

    # Test 6: Word longer than grid
    assert exist([["A"]], "AB") == False
    print("✓ Exercise 2.6 passed: Word too long")

    print("\n🎉 All tests passed!")
