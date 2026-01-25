/*
Filter Groups with HAVING
=========================
Write a query to find departments with more than 1 employee.

HAVING filters groups after GROUP BY is applied.
Use HAVING (not WHERE) to filter based on aggregate values.

WHERE filters rows before grouping.
HAVING filters groups after grouping.

Expected output: Departments with employee count > 1.

Hint: GROUP BY ... HAVING COUNT(*) > n
*/

-- ============= SCHEMA =============
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL
);

-- ============= DATA =============
INSERT INTO employees (id, name, department) VALUES
(1, 'Alice', 'Engineering'),
(2, 'Bob', 'Marketing'),
(3, 'Charlie', 'Engineering'),
(4, 'Diana', 'HR'),
(5, 'Eve', 'Engineering');

-- ============= SOLUTION TEMPLATE =============
-- Write your query to find departments with > 1 employee:
SELECT

/*TESTS
{"type": "query_result", "expected": [["Engineering", 3]]}
TESTS*/
