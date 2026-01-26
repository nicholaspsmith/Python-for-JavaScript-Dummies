/*
DENSE_RANK Window Function
==========================
Write a query to rank products by price within each category.
Products with the same price should have the same rank, with no gaps.

DENSE_RANK() assigns ranks with no gaps between rank values.
When there's a tie, the next rank continues from the tied rank + 1.

Comparison with same data [100, 100, 80, 70]:
- ROW_NUMBER: 1, 2, 3, 4 (arbitrary tiebreaker)
- RANK:       1, 1, 3, 4 (tie at 1, skip 2)
- DENSE_RANK: 1, 1, 2, 3 (tie at 1, no skip)

Use DENSE_RANK when you want:
- Same rank for ties
- Consecutive rank numbers (no gaps)

Expected output: product_name, category, price, price_rank

Hint: DENSE_RANK() OVER (PARTITION BY category ORDER BY price DESC)
*/

-- ============= SCHEMA =============
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price INTEGER NOT NULL
);

-- ============= DATA =============
INSERT INTO products (id, name, category, price) VALUES
(1, 'Laptop', 'Electronics', 1000),
(2, 'Phone', 'Electronics', 800),
(3, 'Tablet', 'Electronics', 800),
(4, 'Desk', 'Furniture', 300),
(5, 'Chair', 'Furniture', 150),
(6, 'Lamp', 'Furniture', 50);

-- ============= SOLUTION TEMPLATE =============
-- Write your DENSE_RANK query:
SELECT

/*TESTS
{"type": "query_result", "expected": [["Laptop", "Electronics", 1000, 1], ["Phone", "Electronics", 800, 2], ["Tablet", "Electronics", 800, 2], ["Desk", "Furniture", 300, 1], ["Chair", "Furniture", 150, 2], ["Lamp", "Furniture", 50, 3]]}
TESTS*/
