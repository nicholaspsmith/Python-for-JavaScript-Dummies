/*
LIKE Pattern Matching
=====================
Write a query to find all employees whose name starts with 'A'.

LIKE performs pattern matching with wildcards:
- % matches any sequence of characters (including empty)
- _ matches exactly one character

Examples:
- 'A%' matches strings starting with A
- '%son' matches strings ending with son
- '%an%' matches strings containing an
- 'A_' matches two-character strings starting with A

Expected output: Employees whose name starts with 'A'.

Hint: WHERE column LIKE 'pattern'
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
(3, 'Amanda', 'Engineering', 80000),
(4, 'Diana', 'HR', 55000),
(5, 'Aaron', 'Sales', 70000);

-- ============= SOLUTION TEMPLATE =============
-- Write your query to find employees whose name starts with 'A':
SELECT

/*TESTS
{"type": "query_result", "expected": [[1, "Alice", "Engineering", 75000], [3, "Amanda", "Engineering", 80000], [5, "Aaron", "Sales", 70000]], "ignoreOrder": true}
TESTS*/
