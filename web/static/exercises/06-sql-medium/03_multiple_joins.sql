/*
Multiple Joins
==============
Write a query to get employee names, department names, and their
manager's name for each employee.

You can chain multiple JOINs to combine data from 3+ tables.

Tables:
- employees (id, name, department_id, manager_id)
- departments (id, name)

Expected output: employee_name, department_name, manager_name

Hint: Join employees to departments, then employees to itself for managers.
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
    manager_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(id),
    FOREIGN KEY (manager_id) REFERENCES employees(id)
);

-- ============= DATA =============
INSERT INTO departments (id, name) VALUES
(1, 'Engineering'),
(2, 'Marketing');

INSERT INTO employees (id, name, department_id, manager_id) VALUES
(1, 'Alice', 1, NULL),
(2, 'Bob', 2, NULL),
(3, 'Charlie', 1, 1),
(4, 'Diana', 2, 2);

-- ============= SOLUTION TEMPLATE =============
-- Write your query with multiple joins:
-- (Use LEFT JOIN for manager since some employees have no manager)
SELECT

/*TESTS
{"type": "query_result", "expected": [["Alice", "Engineering", null], ["Bob", "Marketing", null], ["Charlie", "Engineering", "Alice"], ["Diana", "Marketing", "Bob"]]}
TESTS*/
