-- lists all records of the table second_table of the database
SELECT score, name, COUNT(*) AS number  
FROM second_table
WHERE score IS NOT NULL AND name IS NOT NULL 
GROUP BY score, name
ORDER BY number DESC; 