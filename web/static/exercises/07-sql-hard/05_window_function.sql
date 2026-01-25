/*
Window Functions
================
Write a query to rank employees by salary within their department.

Window functions perform calculations across a set of rows
related to the current row, without collapsing rows like GROUP BY.

RANK() gives each row a ranking, with gaps for ties.
PARTITION BY defines the window (group) for the function.

Expected output: name, department, salary, rank within department

Hint: RANK() OVER (PARTITION BY ... ORDER BY ...)
*/

-- ============= SCHEMA =============
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER NOT NULL
);

-- ============= DATA =============
INSERT INTO employees (id, name, department, salary) VALUES
(1, 'Alice', 'Engineering', 80000),
(2, 'Bob', 'Engineering', 70000),
(3, 'Charlie', 'Engineering', 80000),
(4, 'Diana', 'Marketing', 65000),
(5, 'Eve', 'Marketing', 55000);

-- ============= SOLUTION TEMPLATE =============
-- Write your window function query:
SELECT

/*TESTS
{"type": "query_result", "expected": [["Alice", "Engineering", 80000, 1], ["Charlie", "Engineering", 80000, 1], ["Bob", "Engineering", 70000, 3], ["Diana", "Marketing", 65000, 1], ["Eve", "Marketing", 55000, 2]], "ignoreOrder": true}
TESTS*/
