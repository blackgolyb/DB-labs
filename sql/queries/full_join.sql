WITH
StudentGrade AS (
    SELECT
        g.id AS grade_id
        ,g.grade AS grade
        ,g.subject_id AS subject_id
        ,p.name as student
    FROM students AS s
    JOIN profiles AS p
        ON p.student_id = s.id
    LEFT JOIN grades AS g
        ON s.id = g.student_id
),
TeacherGrade AS (
    SELECT
        g.id AS grade_id
        ,t.name as teacher
    FROM teachers AS t
    LEFT JOIN grades AS g
        ON t.id = g.teacher_id
)
SELECT
    s.grade
    ,sub.name AS subject
    ,s.student
    ,t.teacher
FROM StudentGrade AS s
FULL JOIN TeacherGrade AS t USING(grade_id)
LEFT JOIN subjects as sub
    ON s.subject_id = sub.id
ORDER BY sub.name, s.grade DESC, s.student