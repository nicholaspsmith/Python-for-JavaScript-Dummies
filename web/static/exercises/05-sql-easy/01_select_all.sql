/*
Select All Columns
==================
Write a query to select ALL columns from the employees table.

The employees table contains information about company employees
including their ID, name, department, and salary.

Expected output: All rows and columns from the employees table.

Hint: Use SELECT * to select all columns.
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
(4, 'Diana', 'HR', 55000);

-- ============= SOLUTION TEMPLATE =============
-- Write your query below:
SELECT

/*TESTS
{"type": "query_result", "expected": [[1, "Alice", "Engineering", 75000], [2, "Bob", "Marketing", 60000], [3, "Charlie", "Engineering", 80000], [4, "Diana", "HR", 55000]]}
TESTS*/
