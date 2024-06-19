-- Creating a new database for practice
CREATE DATABASE practice_db;
USE practice_db;

-- Creating tables
CREATE TABLE students (
   student_id INT PRIMARY KEY,
   student_name VARCHAR(50) NOT NULL,
   age INT,
   city VARCHAR(30)
);

CREATE TABLE courses (
   course_id INT PRIMARY KEY,
   course_name VARCHAR(50) NOT NULL,
   duration INT, -- in months
   fee INT
);

CREATE TABLE enrollments (
   enrollment_id INT PRIMARY KEY,
   student_id INT,
   course_id INT,
   enrollment_date DATE,
   FOREIGN KEY (student_id) REFERENCES students(student_id),
   FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Inserting sample data
INSERT INTO students (student_id, student_name, age, city)
VALUES
   (1, 'Ariel', 20, 'New York'),
   (2, 'Jake', 22, 'Los Angeles'),
   (3, 'Connor', 19, 'Hamburg'),
   (4, 'Ravi', 21, 'Houston'),
   (5, 'David ', 23, 'Singapore');

INSERT INTO courses (course_id, course_name, duration, fee)
VALUES
   (101, 'Computer Science', 4, 50000),
   (102, 'Business Administration', 2, 30000),
   (103, 'Liberal Arts', 3, 45000),
   (104, 'Mathematics', 6, 60000),
   (105, 'Politics', 2, 25000);

INSERT INTO enrollments (enrollment_id, student_id, course_id, enrollment_date)
VALUES
   (1, 1, 101, '2023-01-01'),
   (2, 2, 102, '2023-02-15'),
   (3, 3, 103, '2023-03-01'),
   (4, 4, 104, '2023-04-10'),
   (5, 5, 105, '2023-05-20');

-- INNER JOIN
-- Get the list of students enrolled in each course
SELECT s.student_name, c.course_name
FROM students s
INNER JOIN enrollments e ON s.student_id = e.student_id
INNER JOIN courses c ON e.course_id = c.course_id;

-- LEFT JOIN
-- Get the list of all students, including those not enrolled in any course
SELECT s.student_name, c.course_name
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
LEFT JOIN courses c ON e.course_id = c.course_id;

-- RIGHT JOIN
-- Get the list of all courses, including those with no enrollments
SELECT s.student_name, c.course_name
FROM students s
RIGHT JOIN enrollments e ON s.student_id = e.student_id
RIGHT JOIN courses c ON e.course_id = c.course_id;

-- SELF JOIN
-- Find students from the same city
SELECT s1.student_name AS student1, s2.student_name AS student2
FROM students s1
INNER JOIN students s2 ON s1.city = s2.city AND s1.student_id <> s2.student_id;

-- CROSS JOIN
-- Get all possible combinations of students and courses
SELECT s.student_name, c.course_name
FROM students s
CROSS JOIN courses c;