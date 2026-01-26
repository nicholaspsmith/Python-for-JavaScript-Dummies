/*
IN Operator
===========
Write a query to select employees who work in Engineering OR Marketing.

The IN operator lets you specify multiple values in a WHERE clause.
It's cleaner than writing multiple OR conditions.

WHERE column IN (value1, value2, ...) is equivalent to:
WHERE column = value1 OR column = value2 OR ...

Expected output: Employees in Engineering or Marketing departments.

Hint: WHERE column IN ('value1', 'value2')
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
(5, 'Eve', 'Sales', 58000);

-- ============= SOLUTION TEMPLATE =============
-- Write your query to get employees in Engineering or Marketing:
SELECT

/*TESTS
{"type": "query_result", "expected": [[1, "Alice", "Engineering", 75000], [2, "Bob", "Marketing", 60000], [3, "Charlie", "Engineering", 80000]], "ignoreOrder": true}
TESTS*/
