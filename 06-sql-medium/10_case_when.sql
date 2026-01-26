/*
CASE WHEN
=========
Write a query to categorize employees by salary level:
- 'High' if salary >= 70000
- 'Medium' if salary >= 55000
- 'Low' otherwise

CASE provides conditional logic in SQL (like if/else):

CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ELSE default_result
END

Conditions are evaluated in order; first match wins.

Expected output: employee name, salary, and salary_level.

Hint: SELECT name, salary, CASE WHEN ... END AS salary_level
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
(4, 'Diana', 'HR', 50000),
(5, 'Eve', 'Sales', 55000);

-- ============= SOLUTION TEMPLATE =============
-- Write your query to categorize employees by salary level:
SELECT

/*TESTS
{"type": "query_result", "expected": [["Alice", 75000, "High"], ["Bob", 60000, "Medium"], ["Charlie", 80000, "High"], ["Diana", 50000, "Low"], ["Eve", 55000, "Medium"]], "ignoreOrder": true}
TESTS*/
