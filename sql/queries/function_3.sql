SELECT
    f.id,
    f.name,
    count_students_in_faculty(f.id) AS students_count,
    COUNT(g.id) AS groups_count
FROM faculties AS f
JOIN groups AS g ON g.faculty_id = f.id
GROUP BY f.id, f.name
HAVING count_students_in_faculty(f.id) > 2;