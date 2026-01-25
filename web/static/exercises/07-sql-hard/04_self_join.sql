/*
Self Join
=========
Write a query to find pairs of employees in the same department
(employee pairs, not an employee with themselves).

A self join joins a table with itself using different aliases.
Useful for comparing rows within the same table.

Expected output: employee1_name, employee2_name, department
(Only show each pair once, where employee1 < employee2)

Hint: JOIN the table to itself with different aliases.
*/

-- ============= SCHEMA =============
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL
);

-- ============= DATA =============
INSERT INTO employees (id, name, department) VALUES
(1, 'Alice', 'Engineering'),
(2, 'Bob', 'Engineering'),
(3, 'Charlie', 'Engineering'),
(4, 'Diana', 'Marketing'),
(5, 'Eve', 'Marketing');

-- ============= SOLUTION TEMPLATE =============
-- Write your self-join query:
-- (Use e1.name < e2.name to avoid duplicates and self-pairs)
SELECT

/*TESTS
{"type": "query_result", "expected": [["Alice", "Bob", "Engineering"], ["Alice", "Charlie", "Engineering"], ["Bob", "Charlie", "Engineering"], ["Diana", "Eve", "Marketing"]], "ignoreOrder": true}
TESTS*/
