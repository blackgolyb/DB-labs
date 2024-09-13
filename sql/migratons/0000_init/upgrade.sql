CREATE TABLE
    faculties (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    );

CREATE TABLE
    groups (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        course INT CHECK (
            course >= 1
            AND course <= 4
        ),
        faculty_id INT REFERENCES faculties (id)
    );

CREATE TABLE
    teachers (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        department VARCHAR(255) NOT NULL,
        faculty_id INT REFERENCES faculties (id)
    );

CREATE TABLE
    subjects (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL);

CREATE TABLE
    students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        date_of_birth DATE NOT NULL,
        group_id INT REFERENCES groups (id)
    );

CREATE TABLE
    grades (
        id SERIAL PRIMARY KEY,
        student_id INT REFERENCES students (id),
        subject_id INT REFERENCES subjects (id),
        teacher_id INT REFERENCES teachers (id),
        grade INT CHECK (
            grade >= 1
            AND grade <= 100
        )
    );
