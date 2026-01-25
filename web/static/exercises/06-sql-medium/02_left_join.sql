/*
Left Join
=========
Write a query to get ALL employees with their department names,
including employees who don't have a department assigned.

LEFT JOIN returns all rows from the left table, and matching rows
from the right table. Non-matching rows get NULL values.

Expected output: All employees with department (or NULL if none).

Hint: LEFT JOIN keeps all rows from the first (left) table.
*/

-- ============= SCHEMA =============
CREATE TABLE departments (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

-- ============= DATA =============
INSERT INTO departments (id, name) VALUES
(1, 'Engineering'),
(2, 'Marketing');

INSERT INTO employees (id, name, department_id) VALUES
(1, 'Alice', 1),
(2, 'Bob', 2),
(3, 'Charlie', 1),
(4, 'Diana', NULL);

-- ============= SOLUTION TEMPLATE =============
-- Write your query using LEFT JOIN:
SELECT

/*TESTS
{"type": "query_result", "expected": [["Alice", "Engineering"], ["Bob", "Marketing"], ["Charlie", "Engineering"], ["Diana", null]]}
TESTS*/
