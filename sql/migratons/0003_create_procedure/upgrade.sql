CREATE OR REPLACE PROCEDURE add_teacher(IN teacher_name VARCHAR, IN department VARCHAR, IN faculty_id INT)
LANGUAGE 'plpgsql'
AS $$
BEGIN
    INSERT INTO teachers (name, department, faculty_id) 
    VALUES (teacher_name, department, faculty_id);
END;
$$;


CREATE OR REPLACE PROCEDURE get_count_students_in_group(IN "group" INT, OUT student_count INT)
LANGUAGE 'plpgsql'
AS $$
BEGIN
    SELECT COUNT(*) INTO student_count 
    FROM students AS s 
    WHERE s.group_id = "group";
END;
$$;


CREATE OR REPLACE PROCEDURE get_student_info(INOUT s_id INT, OUT student_name VARCHAR, OUT student_dob DATE)
LANGUAGE 'plpgsql'
AS $$
BEGIN
    SELECT p.name, p.date_of_birth INTO student_name, student_dob 
    FROM profiles p 
    WHERE p.student_id = s_id;

    IF NOT FOUND THEN
        RAISE NOTICE 'Студент з таким ID не знайдений';
        s_id := NULL;
        student_name := NULL;
        student_dob := NULL;
    END IF;
END;
$$;