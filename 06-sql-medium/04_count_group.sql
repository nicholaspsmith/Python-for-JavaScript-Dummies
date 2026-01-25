/*
Count and Group By
==================
Write a query to count the number of employees in each department.

GROUP BY groups rows with the same values, allowing aggregate
functions like COUNT() to work on each group.

Expected output: department name and employee count.

Hint: SELECT column, COUNT(*) FROM ... GROUP BY column
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
(4, 'Diana', 3),
(5, 'Eve', 1);

-- ============= SOLUTION TEMPLATE =============
-- Write your query to count employees per department:
SELECT

/*TESTS
{"type": "query_result", "expected": [["Engineering", 3], ["HR", 1], ["Marketing", 1]], "ignoreOrder": true}
TESTS*/
