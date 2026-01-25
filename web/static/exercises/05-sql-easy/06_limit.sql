/*
Limit Results
=============
Write a query to get the top 3 highest-paid employees.

LIMIT restricts the number of rows returned.
Combine with ORDER BY to get "top N" results.

Expected output: The 3 employees with highest salaries.

Hint: ORDER BY ... DESC LIMIT n
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
(5, 'Eve', 'Sales', 72000);

-- ============= SOLUTION TEMPLATE =============
-- Write your query to get top 3 earners:
SELECT * FROM employees

/*TESTS
{"type": "query_result", "expected": [[3, "Charlie", "Engineering", 80000], [1, "Alice", "Engineering", 75000], [5, "Eve", "Sales", 72000]]}
TESTS*/
