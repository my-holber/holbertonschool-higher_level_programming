-- Выбираем столбцы 'score' и 'name' из таблицы 'second_table'
SELECT score, name
-- Из базы данных 'hbtn_0c_0', конкретно из таблицы 'second_table'
FROM second_table
-- Сортируем результаты по столбцу 'score' в порядке убывания (наивысший балл первым)
ORDER BY score DESC;
