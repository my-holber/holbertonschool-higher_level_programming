-- Идентификаторы жанров по шоу
-- Выборка и объединение

-- Выбираем названия шоу и идентификаторы жанров
SELECT tv_shows.title, tv_show_genres.genre_id
-- Присоединяем таблицы tv_shows и tv_show_genres по show_id к id, используя LEFT JOIN для включения всех записей из tv_shows
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
-- Сортируем результаты по названию шоу и идентификатору жанра
ORDER BY tv_shows.title, tv_show_genres.genre_id;
