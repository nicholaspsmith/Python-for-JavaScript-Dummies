/*
Select Distinct
===============
Write a query to get all unique departments from the employees table.

DISTINCT removes duplicate values from your result set.
It's useful when you want to see what unique values exist in a column.

Expected output: A list of unique department names.

Hint: SELECT DISTINCT column FROM table
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
(1, 'Alice', 'Engineering', 75000),
(2, 'Bob', 'Marketing', 60000),
(3, 'Charlie', 'Engineering', 80000),
(4, 'Diana', 'HR', 55000),
(5, 'Eve', 'Marketing', 65000),
(6, 'Frank', 'Engineering', 70000);

-- ============= SOLUTION TEMPLATE =============
-- Write your query to get unique departments:
SELECT

/*TESTS
{"type": "query_result", "expected": [["Engineering"], ["HR"], ["Marketing"]], "ignoreOrder": true}
TESTS*/
