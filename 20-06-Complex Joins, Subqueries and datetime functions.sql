-- Create a database and tables
CREATE DATABASE practice3;
USE practice3;

CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    price DECIMAL(10, 2),
    category VARCHAR(50)
);

CREATE TABLE orders (
    id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    order_date DATE
);

CREATE TABLE order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Insert sample data
INSERT INTO products (id, name, price, category) VALUES
    (1, 'Apple', 0.50, 'Fruit'),
    (2, 'Banana', 0.30, 'Fruit'),
    (3, 'Carrot', 0.40, 'Vegetable'),
    (4, 'Broccoli', 1.20, 'Vegetable'),
    (5, 'Milk', 2.50, 'Dairy');

INSERT INTO orders (id, customer_name, order_date) VALUES
    (1, 'Jay Williams', '2023-05-01'),
    (2, 'JJ Smith', '2023-05-02'),
    (3, 'Rachel Johnson', '2023-05-03'),
    (4, 'Emily Davis', '2023-05-04'),
    (5, 'David Wilson', '2023-05-05');

INSERT INTO order_items (order_id, product_id, quantity) VALUES
    (1, 1, 2),
    (1, 3, 3),
    (2, 2, 4),
    (2, 4, 1),
    (3, 1, 1),
    (3, 5, 2),
    (4, 3, 2),
    (4, 4, 3),
    (5, 2, 3),
    (5, 5, 1);

-- Subqueries
-- 1. Single-row subquery: Find the name of the product with the highest price.
SELECT name
FROM products
WHERE price = (
    SELECT MAX(price)
    FROM products
);

-- 2. Multi-row subquery: Find the names of customers who ordered fruits.
SELECT customer_name
FROM orders
WHERE id IN (
    SELECT order_id
    FROM order_items
    WHERE product_id IN (
        SELECT id
        FROM products
        WHERE category = 'Fruit'
    )
);

-- 3. Correlated subquery: Find the names of products whose price is higher than the average price of products in the same category.
SELECT name
FROM products p
WHERE price > (
    SELECT AVG(price)
    FROM products
    WHERE category = p.category
);

-- Joins
-- 4. Inner join with subquery: Retrieve the names of orders, customer names, product names, and quantities ordered.
SELECT o.id, o.customer_name, p.name, oi.quantity
FROM orders o
INNER JOIN order_items oi ON o.id = oi.order_id
INNER JOIN products p ON oi.product_id = p.id;

-- 5. Left join with aggregate function: Retrieve the names of all customers and the total amount they have spent on orders.
SELECT o.customer_name, COALESCE(SUM(oi.quantity * p.price), 0) AS total_spent
FROM orders o
LEFT JOIN order_items oi ON o.id = oi.order_id
LEFT JOIN products p ON oi.product_id = p.id
GROUP BY o.customer_name;

-- 6. Right join with date and time functions: Retrieve all order items and their corresponding order details, including the order date and current timestamp.
SELECT oi.id, o.customer_name, o.order_date, CURRENT_TIMESTAMP AS current_time
FROM order_items oi
RIGHT JOIN (
    SELECT id, customer_name, order_date, CURRENT_TIMESTAMP AS current_time
    FROM orders
) t ON oi.order_id = t.id;

-- Advanced functions
-- 7. RANK: Retrieves the names of products and their rank based on their price.
SELECT name, price, RANK() OVER (ORDER BY price DESC) AS price_rank
FROM products;

-- 8. DENSE_RANK: Retrieves the names of products and their dense rank based on their price.
SELECT name, price, DENSE_RANK() OVER (ORDER BY price DESC) AS dense_price_rank
FROM products;

-- 9. ROW_NUMBER: Retrieves the names of products and their row number based on their price.
SELECT name, price, ROW_NUMBER() OVER (ORDER BY price DESC) AS row_num
FROM products;

-- 10. CUME_DIST: Retrieves the names of products and the cumulative distribution of their price.
SELECT name, price, CUME_DIST() OVER (ORDER BY price) AS price_cume_dist
FROM products;

-- 11. LAG: Retrieves the names of products and their previous price.
SELECT name, price, LAG(price) OVER (ORDER BY price) AS previous_price
FROM products;

-- 12. LEAD: Retrieves the names of products and their next price.
SELECT name, price, LEAD(price) OVER (ORDER BY price) AS next_price
FROM products;