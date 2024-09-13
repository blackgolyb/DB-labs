ALTER TABLE students
ADD COLUMN name VARCHAR(255),
ADD COLUMN date_of_birth DATE;

UPDATE students
SET
    name = profiles.name,
    date_of_birth = profiles.date_of_birth
FROM
    profiles
WHERE
    students.id = profiles.student_id;

ALTER TABLE students
ALTER COLUMN name SET NOT NULL,
ALTER COLUMN date_of_birth SET NOT NULL;

DROP TABLE profiles;