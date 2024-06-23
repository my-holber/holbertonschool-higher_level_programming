kk-- Города Калифорнии
-- Выбрать города, где state_id соответствует имени "California"
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;

