/*
UNION and UNION ALL
===================
Write a query to combine all customer names and supplier names into one list.
Include duplicates (a name appearing in both tables should appear twice).

UNION combines results from multiple SELECT statements:
- UNION removes duplicates (slower, checks each row)
- UNION ALL keeps duplicates (faster, no duplicate check)

Rules:
1. Same number of columns in each SELECT
2. Columns must have compatible data types
3. Column names come from the first SELECT

Expected output: All names from both tables, with duplicates.

Hint: SELECT ... UNION ALL SELECT ...
*/

-- ============= SCHEMA =============
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL
);

CREATE TABLE suppliers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    country TEXT NOT NULL
);

-- ============= DATA =============
INSERT INTO customers (id, name, city) VALUES
(1, 'Alice', 'New York'),
(2, 'Bob', 'Chicago'),
(3, 'Charlie', 'Boston');

INSERT INTO suppliers (id, name, country) VALUES
(1, 'Bob', 'USA'),
(2, 'Diana', 'Canada'),
(3, 'Eve', 'UK');

-- ============= SOLUTION TEMPLATE =============
-- Write your query to combine all names (keep duplicates):
SELECT

/*TESTS
{"type": "query_result", "expected": [["Alice"], ["Bob"], ["Charlie"], ["Bob"], ["Diana"], ["Eve"]]}
TESTS*/
