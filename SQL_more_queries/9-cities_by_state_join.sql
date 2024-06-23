-- Вывести список всех городов с соответствующими названиями штатов
SELECT cities.id, cities.name, states.name
FROM cities, states
-- Соединяем таблицы cities и states по идентификатору штата (state_id)
WHERE cities.state_id = states.id
-- Упорядочиваем результаты по идентификатору города по возрастанию
ORDER BY cities.id ASC;
