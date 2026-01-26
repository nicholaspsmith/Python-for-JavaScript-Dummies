/*
ROW_NUMBER Window Function
==========================
Write a query to number each employee within their department by salary (highest first).

ROW_NUMBER() assigns a unique sequential number to each row.
Unlike RANK(), it never has gaps or ties - each row gets a distinct number.

Syntax: ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)
- PARTITION BY: restarts numbering for each group
- ORDER BY: determines the numbering order

ROW_NUMBER vs RANK vs DENSE_RANK:
- ROW_NUMBER: 1, 2, 3, 4 (always unique)
- RANK: 1, 1, 3, 4 (ties get same rank, next rank skipped)
- DENSE_RANK: 1, 1, 2, 3 (ties get same rank, no gaps)

Expected output: name, department, salary, row_num

Hint: ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC)
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
(5, 'Eve', 'Marketing', 60000);

-- ============= SOLUTION TEMPLATE =============
-- Write your ROW_NUMBER query:
SELECT

/*TESTS
{"type": "query_result", "expected": [["Alice", "Engineering", 80000, 1], ["Charlie", "Engineering", 75000, 2], ["Bob", "Engineering", 70000, 3], ["Diana", "Marketing", 65000, 1], ["Eve", "Marketing", 60000, 2]]}
TESTS*/
