/*
Sort Results with ORDER BY
==========================
Write a query to select all employees ordered by salary
from highest to lowest (descending order).

ORDER BY sorts your results:
- ASC for ascending (default)
- DESC for descending

Expected output: All employees sorted by salary descending.

Hint: ORDER BY column_name DESC
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
-- Write your query to sort by salary descending:
SELECT * FROM employees

/*TESTS
{"type": "query_result", "expected": [[3, "Charlie", "Engineering", 80000], [1, "Alice", "Engineering", 75000], [2, "Bob", "Marketing", 60000], [4, "Diana", "HR", 55000]]}
TESTS*/
