SELECT
    name,
    count_students_in_group(id) AS total_students
FROM groups;