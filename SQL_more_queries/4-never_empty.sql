-- Скрипт для создания таблицы id_not_null на вашем сервере MySQL.
CREATE TABLE IF NOT EXISTS id_not_null(
        id INT DEFAULT 1,  -- Поле id с значением по умолчанию 1
        name VARCHAR(256)  -- Поле name типа VARCHAR с максимальной длиной 256 символов
);
