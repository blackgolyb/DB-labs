SELECT 
    group_id AS id
    ,COUNT(*) AS students
FROM
    students
GROUP BY group_id
