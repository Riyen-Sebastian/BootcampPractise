-- GROUP BY
-- GROUP BY clause groups rows with the same values into summary rows.

-- A) GROUP BY using HAVING
SELECT cname, COUNT(*) AS Number
FROM customer
GROUP BY cname
HAVING Number >= 1;

-- B) GROUP BY using CONCAT
SELECT location, GROUP_CONCAT(DISTINCT pname) AS product_names
FROM products
GROUP BY location;

-- C) GROUP BY with aggregate functions like COUNT, MAX, MIN, AVG, SUM
SELECT location, AVG(price) AS avg_price
FROM products
GROUP BY location;

-- ORDER BY
-- ORDER BY clause is used to sort the result set.

-- A) Basic ORDER BY
SELECT pname, price
FROM products
ORDER BY price;

-- B) Ascending Order
SELECT pid, pname, price
FROM products
ORDER BY price ASC;

-- C) Descending Order
SELECT cid, cname, age
FROM customer
ORDER BY age DESC;

-- HAVING BY
-- HAVING clause filters groups based on a condition after grouping.

-- A) Products with stock level < 10
SELECT pid, pname, stock
FROM products
GROUP BY pid, pname, stock
HAVING stock < 10;

-- B) Locations with total stock > 50
SELECT location, SUM(stock) AS total_stock
FROM products
GROUP BY location
HAVING SUM(stock) > 50;

-- QUESTIONS AND ANSWERS

-- GROUP BY:
-- 1) Total stock of products for each location
SELECT location, SUM(stock) AS total_stock 
FROM products 
GROUP BY location;

-- 2) Number of products in each price range
SELECT CASE 
 WHEN price BETWEEN 0 AND 10000 THEN '0-10000' 
 WHEN price BETWEEN 10001 AND 20000 THEN '10000-20000'
 WHEN price BETWEEN 20001 AND 50000 THEN '20000-50000' 
 ELSE '50000+' 
 END AS price_range, COUNT(*) AS product_count
FROM products 
GROUP BY price_range;

-- 3) Average age of customers grouped by their location
SELECT SUBSTRING(addr, 1, 3) AS location, AVG(age) AS avg_age 
FROM customer 
GROUP BY location;

-- ORDER BY:
-- 1) Retrieve all products ordered by their price in descending order
SELECT * 
FROM products 
ORDER BY price DESC;

-- 2) Retrieve all customers ordered by their age in ascending order
SELECT * 
FROM customer 
ORDER BY age ASC;

-- 3) Retrieve all orders ordered by amount in descending order and then by customer name
SELECT o.oid, c.cname, o.amt 
FROM orders o 
JOIN customer c ON o.cid = c.cid 
ORDER BY o.amt DESC, c.cname ASC;

-- HAVING:
-- 1) Locations where total stock of products is greater than 20
SELECT location, SUM(stock) AS total_stock 
FROM products 
GROUP BY location 
HAVING SUM(stock) > 20;

-- 2) Customers who have placed orders with a total amount greater than 10000
SELECT c.cid, c.cname, SUM(o.amt) AS total_amount 
FROM customer c 
JOIN orders o ON c.cid = o.cid 
GROUP BY c.cid, c.cname 
HAVING SUM(o.amt) > 10000;

-- 3) Products with stock level between 10 and 20 located in Mumbai
SELECT p.pid, p.pname, p.stock 
FROM products p 
WHERE p.location = 'Mumbai' 
GROUP BY p.pid, p.pname, p.stock 
HAVING p.stock BETWEEN 10 AND 20;