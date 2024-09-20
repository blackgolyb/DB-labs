CREATE OR REPLACE FUNCTION count_students_in_group("group" INT)
RETURNS INT
LANGUAGE 'plpgsql'
AS $$
DECLARE
    student_count INT;
BEGIN
    SELECT COUNT(s.id) INTO student_count
    FROM students AS s
    WHERE s.group_id = "group";
    
    RETURN student_count;
END;
$$;


CREATE OR REPLACE FUNCTION count_students_in_faculty(faculty INT)
RETURNS INT
LANGUAGE 'plpgsql'
AS $$
DECLARE
    total_students INT;
BEGIN
    SELECT COUNT(s.id) INTO total_students
    FROM students AS s
    JOIN groups AS g ON s.group_id = g.id
    WHERE g.faculty_id = faculty;
    
    RETURN total_students;
END;
$$;
