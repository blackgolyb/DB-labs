DO $$
    DECLARE ctn INT;
BEGIN
	CALL get_count_students_in_group(1, ctn);
    CREATE TEMP TABLE tmp_ctn ON COMMIT DROP AS
        SELECT ctn AS "Students counts";
END $$;
