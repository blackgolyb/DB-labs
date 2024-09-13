SELECT
    f.name AS faculty
    ,AVG(g.grade) AS average_grade
FROM faculties AS f
LEFT JOIN teachers AS t
    ON t.faculty_id = f.id
LEFT JOIN grades AS g
    ON g.teacher_id = t.id
GROUP BY f.id
ORDER BY AVG(g.grade) ASC;