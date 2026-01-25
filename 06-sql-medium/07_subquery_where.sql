/*
Subquery in WHERE
=================
Write a query to find employees who earn more than the average salary.

A subquery is a query nested inside another query.
Subqueries in WHERE can be used for comparisons.

Expected output: Employees with salary above company average.

Hint: WHERE salary > (SELECT AVG(salary) FROM ...)
*/

-- ============= SCHEMA =============
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    salary INTEGER NOT NULL
);

-- ============= DATA =============
INSERT INTO employees (id, name, salary) VALUES
(1, 'Alice', 75000),
(2, 'Bob', 60000),
(3, 'Charlie', 80000),
(4, 'Diana', 55000),
(5, 'Eve', 70000);

-- ============= SOLUTION TEMPLATE =============
-- Write your query using a subquery:
-- (Average salary is 68000)
SELECT

/*TESTS
{"type": "query_result", "expected": [[1, "Alice", 75000], [3, "Charlie", 80000], [5, "Eve", 70000]]}
TESTS*/
