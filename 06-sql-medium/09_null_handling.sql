/*
NULL Handling
=============
Write a query to list all employees with their manager's name.
If an employee has no manager (NULL), show 'No Manager' instead.

NULL represents missing or unknown data. Key concepts:
- IS NULL / IS NOT NULL to check for NULL (not = NULL!)
- COALESCE(a, b, c) returns the first non-NULL value
- IFNULL(a, b) returns b if a is NULL (SQLite-specific)

NULL comparisons are tricky: NULL = NULL is NULL, not TRUE!

Expected output: employee name and manager name (or 'No Manager').

Hint: Use COALESCE(column, 'default') or LEFT JOIN with COALESCE
*/

-- ============= SCHEMA =============
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    manager_id INTEGER,
    FOREIGN KEY (manager_id) REFERENCES employees(id)
);

-- ============= DATA =============
INSERT INTO employees (id, name, manager_id) VALUES
(1, 'Alice', NULL),
(2, 'Bob', 1),
(3, 'Charlie', 1),
(4, 'Diana', 2);

-- ============= SOLUTION TEMPLATE =============
-- Write your query to show employee and manager name (or 'No Manager'):
SELECT

/*TESTS
{"type": "query_result", "expected": [["Alice", "No Manager"], ["Bob", "Alice"], ["Charlie", "Alice"], ["Diana", "Bob"]], "ignoreOrder": true}
TESTS*/
