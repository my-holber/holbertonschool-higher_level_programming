-- Выбираем столбцы 'score' и 'name' из таблицы 'second_table'
SELECT score, name
-- Извлекаем записи, где значение столбца 'score' больше или равно 10
FROM second_table
WHERE score >= 10
-- Сортируем результаты по столбцу 'score' в порядке убывания (наивысший балл первым)
ORDER BY score DESC; 
