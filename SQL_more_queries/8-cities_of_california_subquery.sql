-- Cities of California
-- Select cities where state_id corresponds to the name "California"
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California') 
ORDER BY id ASC;

