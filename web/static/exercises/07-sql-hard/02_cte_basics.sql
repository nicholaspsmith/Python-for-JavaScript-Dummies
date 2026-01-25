/*
Common Table Expression (CTE)
=============================
Write a query using a CTE to find the highest-paid employee
in each department, then list those employees.

CTEs (WITH clause) create temporary named result sets that can
be referenced in the main query, improving readability.

Expected output: The top earner from each department.

Hint: WITH cte_name AS (SELECT ...) SELECT ... FROM cte_name
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
(3, 'Charlie', 'Marketing', 65000),
(4, 'Diana', 'Marketing', 55000),
(5, 'Eve', 'HR', 60000);

-- ============= SOLUTION TEMPLATE =============
-- Write your CTE query:
WITH

/*TESTS
{"type": "query_result", "expected": [["Alice", "Engineering", 80000], ["Charlie", "Marketing", 65000], ["Eve", "HR", 60000]], "ignoreOrder": true}
TESTS*/
