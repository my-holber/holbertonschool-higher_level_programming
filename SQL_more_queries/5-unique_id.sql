k-- Создание таблицы
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,  -- Поле id с значением по умолчанию 1 и уникальным индексом
    name VARCHAR(256)         -- Поле name типа VARCHAR с максимальной длиной 256 символов
);

