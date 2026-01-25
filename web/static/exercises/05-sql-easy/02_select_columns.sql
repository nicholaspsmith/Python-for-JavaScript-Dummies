/*
Select Specific Columns
=======================
Write a query to select only the name and department columns
from the employees table.

This demonstrates how to retrieve specific columns rather than
all columns from a table.

Expected output: Two columns (name, department) for all employees.

Hint: List the column names you want, separated by commas.
*/

-- ============= SCHEMA =============
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER NOT NULL,
    hire_date TEXT NOT NULL
);

-- ============= DATA =============
INSERT INTO employees (id, name, department, salary, hire_date) VALUES
(1, 'Alice', 'Engineering', 75000, '2020-01-15'),
(2, 'Bob', 'Marketing', 60000, '2019-06-01'),
(3, 'Charlie', 'Engineering', 80000, '2018-03-20'),
(4, 'Diana', 'HR', 55000, '2021-09-10');

-- ============= SOLUTION TEMPLATE =============
-- Write your query to select name and department:
SELECT

/*TESTS
{"type": "query_result", "expected": [["Alice", "Engineering"], ["Bob", "Marketing"], ["Charlie", "Engineering"], ["Diana", "HR"]]}
TESTS*/
