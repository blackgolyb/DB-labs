SELECT
    g.name AS group_name
    ,p.name AS student_name
FROM students AS s
JOIN groups AS g
    ON g.id = s.group_id
JOIN profiles AS p
    ON p.student_id = s.id
ORDER BY g.name ASC;