-- ANOMALIES

-- Insertion Anomaly
CREATE TABLE Customers (
    cid INT PRIMARY KEY,
    cname VARCHAR(50) NOT NULL
);

CREATE TABLE Products (
    pid INT PRIMARY KEY,
    pname VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Orders (
    oid INT PRIMARY KEY,
    cid INT,
    pid INT,
    quantity INT,
    FOREIGN KEY (cid) REFERENCES Customers(cid),
    FOREIGN KEY (pid) REFERENCES Products(pid)
);

-- Trying to insert an order for a non-existing customer (Insertion Anomaly)
INSERT INTO Orders (oid, cid, pid, quantity)
VALUES (1, 999, 1, 2); -- This will fail due to the foreign key constraint



-- Deletion Anomaly
INSERT INTO Customers (cid, cname) VALUES (1, 'John Doe');
INSERT INTO Products (pid, pname, price) VALUES (1, 'Laptop', 999.99);
INSERT INTO Orders (oid, cid, pid, quantity) VALUES (1, 1, 1, 1);

-- Deleting a product that has existing orders (Deletion Anomaly)
DELETE FROM Products WHERE pid = 1; -- This will fail due to the foreign key constraint



-- Update Anomaly
INSERT INTO Products (pid, pname, price) VALUES (2, 'Smartphone', 499.99);
INSERT INTO Orders (oid, cid, pid, quantity) VALUES (2, 1, 2, 1);

-- Updating the price of a product without updating existing orders (Update Anomaly)
UPDATE Products SET price = 549.99 WHERE pid = 2;
-- The order with oid = 2 will still have the old price

-- CANDIDATE KEYS
-- pid, cid, and oid are candidate keys in their respective tables




-- PRIMARY KEY
-- Creating a table with a primary key
CREATE TABLE Employees (
    eid INT PRIMARY KEY,
    ename VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL
);

-- Adding a primary key to an existing table
CREATE TABLE Departments (
    did INT,
    dname VARCHAR(50) NOT NULL
);

ALTER TABLE Departments ADD PRIMARY KEY (did);

-- Removing a primary key from a table
ALTER TABLE Departments DROP PRIMARY KEY;


-- FOREIGN KEY
-- Creating a table with a foreign key
CREATE TABLE EmployeeDepartments (
    eid INT,
    did INT,
    FOREIGN KEY (eid) REFERENCES Employees(eid),
    FOREIGN KEY (did) REFERENCES Departments(did)
);

-- Adding a foreign key to an existing table
ALTER TABLE EmployeeDepartments ADD FOREIGN KEY (did) REFERENCES Departments(did);

-- Removing a foreign key from a table
ALTER TABLE EmployeeDepartments DROP FOREIGN KEY EmployeeDepartments_ibfk_2;




-- NORMALIZATION
-- 1NF (First Normal Form)
CREATE TABLE OrderItems (
    order_id INT,
    items VARCHAR(100) -- Violates 1NF (multi-valued attribute)
);

-- Fixing 1NF violation
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT
);

CREATE TABLE OrderDetails (
    order_id INT,
    item VARCHAR(50),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);



-- 2NF (Second Normal Form)
CREATE TABLE StudentCourses (
    student_id INT,
    course_id INT,
    course_name VARCHAR(50), -- Violates 2NF (partial dependency on course_id)
    grade VARCHAR(2),
    PRIMARY KEY (student_id, course_id)
);

-- Fixing 2NF violation
CREATE TABLE Students (
    student_id INT PRIMARY KEY
);

CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50)
);

CREATE TABLE StudentGrades (
    student_id INT,
    course_id INT,
    grade VARCHAR(2),
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);




-- 3NF (Third Normal Form)
CREATE TABLE CustomerOrders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    customer_name VARCHAR(50), -- Violates 3NF (transitive dependency on customer_id)
    product_id INT,
    quantity INT
);

-- Fixing 3NF violation
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

