-- Creating a new database for testing operators
CREATE DATABASE oprators_test;

-- Using the created database
USE oprators_test;

-- Creating a sample table to demonstrate operators
CREATE TABLE items (
    item_id INT PRIMARY KEY,
    price DECIMAL(10, 2),
    name VARCHAR(50)
);

-- Inserting data into the sample table
INSERT INTO items (item_id, price, name) VALUES
(1, 25.00, 'pen'),
(2, 50.00, 'notebook'),
(3, 75.00, 'backpack');

-- Arithmetic Operators
-- Adding values
SELECT price + 5.00 AS addition_result FROM items;

-- Subtracting values
SELECT price - 5.00 AS subtraction_result FROM items;

-- Multiplying values
SELECT price * 2 AS multiplication_result FROM items;

-- Dividing values
SELECT price / 2 AS division_result FROM items;

-- Modulus operation
SELECT price % 3 AS modulus_result FROM items;

-- Comparison Operators
-- Equal to
SELECT price = 50.00 AS is_equal FROM items;

-- Not equal to
SELECT price != 50.00 AS is_not_equal FROM items;

-- Greater than
SELECT price > 30.00 AS is_greater FROM items;

-- Less than
SELECT price < 60.00 AS is_less FROM items;

-- Greater than or equal to
SELECT price >= 50.00 AS is_greater_or_equal FROM items;

-- Less than or equal to
SELECT price <= 50.00 AS is_less_or_equal FROM items;

-- Logical Operators
-- AND operator
SELECT (price > 20.00 AND price < 70.00) AS and_result FROM items;

-- OR operator
SELECT (price < 30.00 OR price > 60.00) AS or_result FROM items;

-- NOT operator
SELECT NOT (price = 50.00) AS not_result FROM items;

-- Bitwise Operators (using constants for clarity)
-- AND operation
SELECT 12 & 5 AS bitwise_and;

-- OR operation
SELECT 12 | 5 AS bitwise_or;

-- XOR operation
SELECT 12 ^ 5 AS bitwise_xor;

-- NOT operation
SELECT ~12 AS bitwise_not;

-- Left shift operation
SELECT 12 << 2 AS left_shift;

-- Right shift operation
SELECT 12 >> 2 AS right_shift;

-- String Concatenation
-- Concatenating two strings
SELECT 'Hello' || ' SQL' AS concatenated_string;

-- IN Operator
-- Checking if a price is in a list
SELECT price IN (25.00, 50.00, 75.00) AS in_list FROM items;

-- Checking if a name is in a list
SELECT name IN ('pen', 'notebook', 'eraser') AS name_in_list FROM items;

-- BETWEEN Operator
-- Checking if a price is between two numbers
SELECT price BETWEEN 30.00 AND 70.00 AS between_prices FROM items;

-- Checking if a name is between two strings
SELECT name BETWEEN 'a' AND 'm' AS between_strings FROM items;

-- LIKE Operator
-- Matching patterns
SELECT name LIKE 'p%' AS starts_with_p FROM items;
SELECT name LIKE '%k' AS ends_with_k FROM items;
SELECT name LIKE 'n_t%' AS pattern_match FROM items;

-- IS NULL Operator
-- Creating a sample table with NULL values to demonstrate IS NULL and IS NOT NULL
CREATE TABLE inventory (
    item_id INT PRIMARY KEY,
    quantity INT
);

-- Inserting data into the inventory table
INSERT INTO inventory (item_id, quantity) VALUES
(1, 10),
(2, NULL);

-- Checking for NULL values
SELECT quantity IS NULL AS is_null FROM inventory;
SELECT quantity IS NOT NULL AS is_not_null FROM inventory;

-- Clean up: Dropping the created database
DROP DATABASE oprators_test;
