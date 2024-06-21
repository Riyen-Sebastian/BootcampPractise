-- Using a 'school' database

USE school;

-- Creaating delimiter for procedure and function creation
DELIMITER //

-- 1. Simple procedure to get all students
CREATE PROCEDURE get_all_students()
BEGIN
    SELECT * FROM students;
END //

-- 2. Function to count students in a specific grade
CREATE FUNCTION count_students_in_grade(grade INT)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE student_count INT;
    SELECT COUNT(*) INTO student_count
    FROM students
    WHERE student_grade = grade;
    RETURN student_count;
END //

-- 3. Procedure with IN parameter to get students by grade
CREATE PROCEDURE get_students_by_grade(IN grade INT)
BEGIN
    SELECT * FROM students WHERE student_grade = grade;
END //

-- 4. Procedure with OUT parameter to get the average age of students
CREATE PROCEDURE get_average_age(OUT avg_age DECIMAL(5,2))
BEGIN
    SELECT AVG(age) INTO avg_age FROM students;
END //

-- 5. Simple cursor to print student names
CREATE PROCEDURE print_student_names()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE student_name VARCHAR(100);
    DECLARE name_cursor CURSOR FOR SELECT student_name FROM students;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN name_cursor;

    name_loop: LOOP
        FETCH name_cursor INTO student_name;
        IF done THEN
            LEAVE name_loop;
        END IF;
        SELECT CONCAT('Student: ', student_name) AS student_info;
    END LOOP;

    CLOSE name_cursor;
END //

-- Resettinf delimiter
DELIMITER ;

-- To Execute the procedures and function

-- To Call procedure to get all students
CALL get_all_students();

-- To Use function to count students in grade 10
SELECT count_students_in_grade(10) AS students_in_grade_10;

-- To Call procedure to get students in grade 9
CALL get_students_by_grade(9);

-- To Call procedure to get average age
CALL get_average_age(@avg_student_age);
SELECT @avg_student_age AS average_student_age;

-- To Call procedure to print student names
CALL print_student_names();