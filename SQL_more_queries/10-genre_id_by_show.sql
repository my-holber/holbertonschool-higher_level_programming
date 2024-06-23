-- Идентификаторы жанров по шоу
-- Выборка и соединение таблиц

-- Выбираем названия шоу и идентификаторы жанров
SELECT tv_shows.title, tv_show_genres.genre_id
-- Объединяем таблицы tv_shows и tv_show_genres по show_id и id соответственно
FROM tv_shows
JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
-- Сортируем результаты по названию шоу и идентификатору жанра
ORDER BY tv_shows.title, tv_show_genres.genre_id;
