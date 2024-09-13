CREATE TABLE
    profiles (
        id SERIAL PRIMARY KEY,
        student_id INT UNIQUE REFERENCES students (id) ON DELETE CASCADE,
        name VARCHAR(255) NOT NULL,
        date_of_birth DATE NOT NULL,
        address VARCHAR(255),
        phone_number VARCHAR(15)
    );

INSERT INTO
    profiles (student_id, name, date_of_birth)
SELECT
    id,
    name,
    date_of_birth
FROM
    students;

ALTER TABLE students
DROP COLUMN name,
DROP COLUMN date_of_birth;