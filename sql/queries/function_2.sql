SELECT name
FROM groups
WHERE count_students_in_group(id) > 1;