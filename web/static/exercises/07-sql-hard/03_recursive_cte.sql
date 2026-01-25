/*
Recursive CTE
=============
Write a recursive CTE to generate numbers from 1 to 5.

Recursive CTEs reference themselves to build results iteratively.
Structure:
1. Base case (anchor)
2. UNION ALL
3. Recursive case

Expected output: Numbers 1 through 5.

Hint: WITH RECURSIVE cte AS (base UNION ALL recursive WHERE condition)
*/

-- ============= SCHEMA =============
-- No tables needed for this exercise

-- ============= DATA =============
-- No data needed

-- ============= SOLUTION TEMPLATE =============
-- Write your recursive CTE:
WITH RECURSIVE

/*TESTS
{"type": "query_result", "expected": [[1], [2], [3], [4], [5]]}
TESTS*/
