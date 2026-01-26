/*
EXISTS Subquery
===============
Write a query to find departments that have at least one employee.

EXISTS checks if a subquery returns any rows:
- Returns TRUE if subquery has 1+ rows
- Returns FALSE if subquery is empty
- Often more efficient than IN for large datasets

NOT EXISTS finds rows where the subquery returns nothing.

EXISTS vs IN:
- EXISTS stops at first match (can be faster)
- IN loads all subquery results into memory
- EXISTS can reference outer query columns (correlated)

Expected output: Department names that have employees.

Hint: WHERE EXISTS (SELECT 1 FROM ... WHERE ...)
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
(3, 'HR'),
(4, 'Legal');

INSERT INTO employees (id, name, department_id) VALUES
(1, 'Alice', 1),
(2, 'Bob', 2),
(3, 'Charlie', 1);

-- ============= SOLUTION TEMPLATE =============
-- Write your query to find departments with at least one employee:
SELECT

/*TESTS
{"type": "query_result", "expected": [["Engineering"], ["Marketing"]], "ignoreOrder": true}
TESTS*/
