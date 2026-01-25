/*
Filter with WHERE (Equality)
============================
Write a query to find all employees in the Engineering department.

The WHERE clause filters rows based on a condition.
Use = for exact matches.

Expected output: All employees where department equals 'Engineering'.

Hint: WHERE column_name = 'value'
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
(5, 'Eve', 'Engineering', 70000);

-- ============= SOLUTION TEMPLATE =============
-- Write your query to find Engineering employees:
SELECT * FROM employees

/*TESTS
{"type": "query_result", "expected": [[1, "Alice", "Engineering", 75000], [3, "Charlie", "Engineering", 80000], [5, "Eve", "Engineering", 70000]]}
TESTS*/
