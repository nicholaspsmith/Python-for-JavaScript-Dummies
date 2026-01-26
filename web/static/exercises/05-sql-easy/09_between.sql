/*
BETWEEN Operator
================
Write a query to select employees with salaries between 60000 and 75000 (inclusive).

BETWEEN filters values within a range (inclusive of both endpoints).
It's cleaner than writing: column >= low AND column <= high

Works with numbers, dates, and text (alphabetically).

Expected output: Employees with salary from 60000 to 75000.

Hint: WHERE column BETWEEN low AND high
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
(5, 'Eve', 'Sales', 70000);

-- ============= SOLUTION TEMPLATE =============
-- Write your query to get employees with salary between 60000 and 75000:
SELECT

/*TESTS
{"type": "query_result", "expected": [[1, "Alice", "Engineering", 75000], [2, "Bob", "Marketing", 60000], [5, "Eve", "Sales", 70000]], "ignoreOrder": true}
TESTS*/
