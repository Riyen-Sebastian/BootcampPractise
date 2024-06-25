-- Create database
CREATE DATABASE bookstore;

USE bookstore;

-- Create tables
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    book_id INT,
    quantity INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

-- Insert sample data
INSERT INTO books VALUES (1, 'The Great Gatsby', 15.99, 50);
INSERT INTO books VALUES (2, 'To Kill a Mockingbird', 12.99, 30);
INSERT INTO customers VALUES (1, 'John Doe', 'john@example.com');
INSERT INTO customers VALUES (2, 'Jane Smith', 'jane@example.com');

-- TCL Commands practice
START TRANSACTION;

INSERT INTO orders (order_id, customer_id, book_id, quantity) VALUES (1, 1, 1, 2);
UPDATE books SET stock = stock - 2 WHERE book_id = 1;

SAVEPOINT order_placed;

INSERT INTO orders (order_id, customer_id, book_id, quantity) VALUES (2, 2, 2, 1);
UPDATE books SET stock = stock - 1 WHERE book_id = 2;

-- Uncomment the following line to practice ROLLBACK TO SAVEPOINT
-- ROLLBACK TO order_placed;

COMMIT;

-- Triggers practice
DELIMITER //

CREATE TRIGGER update_stock_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE books
    SET stock = stock - NEW.quantity
    WHERE book_id = NEW.book_id;
END //

CREATE TRIGGER check_stock_before_order
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    DECLARE available_stock INT;
    SELECT stock INTO available_stock FROM books WHERE book_id = NEW.book_id;
    IF available_stock < NEW.quantity THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Insufficient stock for this book';
    END IF;
END //

DELIMITER ;

-- Test triggers
INSERT INTO orders (order_id, customer_id, book_id, quantity) VALUES (3, 1, 2, 5);

-- Views practice
CREATE VIEW customer_order_summary AS
SELECT c.customer_id, c.name, COUNT(o.order_id) AS total_orders, SUM(b.price * o.quantity) AS total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
LEFT JOIN books b ON o.book_id = b.book_id
GROUP BY c.customer_id, c.name;

-- Query the view
SELECT * FROM customer_order_summary;

-- Create or replace view
CREATE OR REPLACE VIEW books_low_stock AS
SELECT book_id, title, stock
FROM books
WHERE stock < 10;

-- Drop view
DROP VIEW IF EXISTS books_low_stock;