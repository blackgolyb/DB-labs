SELECT
    p.name AS student
    ,sub.name AS subject
    ,g.grade AS grade
FROM students AS s
JOIN profiles AS p
    ON p.student_id = s.id
CROSS JOIN subjects as sub
LEFT JOIN grades AS g
    ON g.student_id = s.id
    AND g.subject_id = sub.id
ORDER BY s.id, sub.name;
