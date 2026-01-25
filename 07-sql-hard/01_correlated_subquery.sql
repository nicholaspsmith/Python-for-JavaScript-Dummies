/*
Correlated Subquery
===================
Write a query to find employees who earn more than the average
salary of their own department.

A correlated subquery references the outer query, executing once
for each row in the outer query.

Expected output: Employees earning above their department's average.

Hint: The inner query references the outer query's row.
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
(3, 'Charlie', 'Engineering', 75000),
(4, 'Diana', 'Marketing', 65000),
(5, 'Eve', 'Marketing', 55000);

-- ============= SOLUTION TEMPLATE =============
-- Write your correlated subquery:
-- (Eng avg: 75000, Marketing avg: 60000)
SELECT

/*TESTS
{"type": "query_result", "expected": [[1, "Alice", "Engineering", 80000], [4, "Diana", "Marketing", 65000]]}
TESTS*/
