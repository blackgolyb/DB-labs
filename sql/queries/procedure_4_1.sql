DO $$
    DECLARE student_id INT = 2;
    DECLARE student_name VARCHAR;
    DECLARE student_dob DATE;
BEGIN
	CALL get_student_info(student_id, student_name, student_dob);
    CREATE TEMP TABLE tmp_task4 ON COMMIT DROP AS
        SELECT student_id, student_name, student_dob;
END $$;
