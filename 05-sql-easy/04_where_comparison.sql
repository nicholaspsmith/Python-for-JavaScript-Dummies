/*
Filter with WHERE (Comparison)
==============================
Write a query to find all employees with a salary greater than 65000.

You can use comparison operators in WHERE clauses:
- > greater than
- < less than
- >= greater than or equal
- <= less than or equal

Expected output: All employees earning more than 65000.

Hint: WHERE column_name > value
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
-- Write your query to find employees earning > 65000:
SELECT * FROM employees

/*TESTS
{"type": "query_result", "expected": [[1, "Alice", "Engineering", 75000], [3, "Charlie", "Engineering", 80000], [5, "Eve", "Engineering", 70000]]}
TESTS*/
