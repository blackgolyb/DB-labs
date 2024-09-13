SELECT
    f.name AS faculty
    ,AVG(g.grade) as average_grade
FROM grades AS g
RIGHT JOIN students AS s
    ON s.id = g.student_id
RIGHT JOIN groups AS gr
    ON gr.id = s.group_id
RIGHT JOIN faculties AS f
    ON f.id = gr.faculty_id
GROUP BY f.id
ORDER BY AVG(g.grade) ASC;