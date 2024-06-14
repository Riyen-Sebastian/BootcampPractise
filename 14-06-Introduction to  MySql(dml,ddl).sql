-- Creating a database
CREATE DATABASE school;

-- Using the created database
USE school;

-- Creating table 'students' with basic columns
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    address VARCHAR(100)
);

-- Creating table 'courses'
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50) NOT NULL,
    instructor VARCHAR(50)
);

-- Creating table 'enrollments' with foreign key references to 'students' and 'courses' tables
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    grade CHAR(1),
    FOREIGN KEY(student_id) REFERENCES students(student_id),
    FOREIGN KEY(course_id) REFERENCES courses(course_id)
);

-- Adding a column to 'students' table
ALTER TABLE students
ADD phone VARCHAR(15);

-- Deleting a column from 'students' table
ALTER TABLE students
DROP COLUMN phone;

-- Renaming a column in 'enrollments' table
ALTER TABLE enrollments
RENAME COLUMN grade TO final_grade;

-- Inserting data into 'students' table
INSERT INTO students (student_id, name, age, address) VALUES
(1, 'Alice Johnson', 20, '123 Main St'),
(2, 'Bob Smith', 22, '456 Maple Ave');

-- Inserting data into 'courses' table
INSERT INTO courses (course_id, course_name, instructor) VALUES
(101, 'Math 101', 'Dr. Adams'),
(102, 'History 101', 'Prof. Brown');

-- Inserting data into 'enrollments' table
INSERT INTO enrollments (enrollment_id, student_id, course_id, final_grade) VALUES
(1, 1, 101, 'A'),
(2, 2, 102, 'B');

-- Using SELECT statements with conditions
SELECT * FROM students WHERE age > 20;
SELECT * FROM courses WHERE instructor = 'Dr. Adams';
SELECT * FROM enrollments WHERE final_grade = 'A';

-- Updating records in 'students' table
UPDATE students
SET name = 'Alice Johnson', address = '789 Oak St'
WHERE student_id = 1;

-- Deleting records from 'enrollments' table
DELETE FROM enrollments WHERE enrollment_id = 2;

-- Using AND, OR, and NOT operators in SELECT queries
SELECT * FROM students WHERE age > 18 AND address LIKE '%St';
SELECT * FROM courses WHERE instructor = 'Prof. Brown' OR course_name = 'Math 101';
SELECT * FROM enrollments WHERE NOT (final_grade = 'C');

-- Creating a table with constraints
CREATE TABLE teachers (
    teacher_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL
);

-- Creating another table 
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL,
    head_id INT,
    FOREIGN KEY(head_id) REFERENCES teachers(teacher_id)
);

-- Inserting data into 'teachers' table while respecting constraints
INSERT INTO teachers (teacher_id, name, email)
VALUES (1, 'Dr. Adams', 'adams@example.com');


-- Using SELECT query with conditions
SELECT * 
FROM students 
WHERE age > 18;

-- Updating a record
UPDATE students
SET age = 21
WHERE student_id = 1;

-- Deleting records with a  condition
DELETE FROM students 
WHERE age < 20;
