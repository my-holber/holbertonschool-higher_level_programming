-- Список всех шоу без связанного жанра
SELECT tv_shows.title, tv_show_genres.genre_id
-- Выбираем названия шоу и идентификаторы жанров
FROM tv_shows
-- Присоединяем таблицы tv_shows и tv_show_genres по id к show_id, используя LEFT JOIN для включения всех записей из tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Фильтруем только записи, где жанр отсутствует (NULL)
WHERE tv_show_genres.genre_id IS NULL
-- Сортируем результаты по названию шоу (возрастанию) и жанру (возрастанию)
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
