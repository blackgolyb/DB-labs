CREATE TABLE
    ects (
        id SERIAL PRIMARY KEY,
        name VARCHAR(2) NOT NULL,
        lower INT NOT NULL,
        upper INT NOT NULL
    );

INSERT INTO ects (name, lower, upper) VALUES
('A', 90, 100),
('B', 82, 89),
('C', 75, 81),
('D', 64, 74),
('E', 60, 63),
('FX', 35, 59),
('F', 1, 34);

CREATE VIEW grades_with_ects AS 
SELECT
    g.*,
    e.name AS ects
FROM grades AS g
LEFT JOIN ects AS e
    ON g.grade BETWEEN e.lower AND e.upper;


CREATE VIEW best_grades AS
SELECT *
FROM grades_with_ects
WHERE ects = 'A'
ORDER BY grade DESC;


CREATE VIEW students_info AS
SELECT
    s.id AS id,
    p.name AS name,
    p.address AS address,
    p.phone_number AS phone_number,
    p.date_of_birth AS date_of_birth,
    DATE_PART('year',AGE(p.date_of_birth))::INT AS age,
    g.name AS group,
    g.course AS course
FROM students AS s
JOIN profiles AS p
    ON p.student_id = s.id
JOIN groups AS g
    ON g.id = s.group_id
ORDER BY g.course, g.name

