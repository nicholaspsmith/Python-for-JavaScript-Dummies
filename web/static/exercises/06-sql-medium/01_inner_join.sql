/*
Inner Join
==========
Write a query to get employee names along with their department names.

INNER JOIN combines rows from two tables where the join condition is met.
Only matching rows from both tables are included.

Tables:
- employees (id, name, department_id)
- departments (id, name)

Expected output: Employee name and department name for each employee.

Hint: SELECT ... FROM table1 INNER JOIN table2 ON table1.col = table2.col
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
(2, 'Marketing'),
(3, 'HR');

INSERT INTO employees (id, name, department_id) VALUES
(1, 'Alice', 1),
(2, 'Bob', 2),
(3, 'Charlie', 1),
(4, 'Diana', 3);

-- ============= SOLUTION TEMPLATE =============
-- Write your query to join employees with departments:
SELECT

/*TESTS
{"type": "query_result", "expected": [["Alice", "Engineering"], ["Bob", "Marketing"], ["Charlie", "Engineering"], ["Diana", "HR"]]}
TESTS*/
