/*
Aggregate Functions
===================
Write a query to get the average salary and total salary cost
for each department.

Common aggregate functions:
- SUM() - total of values
- AVG() - average of values
- MIN() - minimum value
- MAX() - maximum value
- COUNT() - number of rows

Expected output: department, average_salary, total_salary

Hint: Use ROUND() to round the average to 2 decimal places.
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
-- Write your query for avg and sum per department:
SELECT

/*TESTS
{"type": "query_result", "expected": [["Engineering", 75000.0, 225000], ["HR", 55000.0, 55000], ["Marketing", 60000.0, 60000]], "ignoreOrder": true}
TESTS*/
