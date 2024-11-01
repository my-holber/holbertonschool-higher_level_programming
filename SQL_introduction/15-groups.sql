-- lists the number of records with the same score
SELECT second_table COUNT(*) AS number
FROM second_table
GROUP BY score;
ORDER BY number DESC;