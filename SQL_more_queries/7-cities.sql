-- Таблица штатов
-- Создание базы данных
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Создание таблицы городов
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,  -- Поле id с уникальным автоинкрементным значением, не может быть NULL, и является первичным ключом
    state_id INT NOT NULL,                             -- Поле state_id типа INT, не может быть NULL
    name VARCHAR(256) NOT NULL,                        -- Поле name типа VARCHAR с максимальной длиной 256 символов, не может быть NULL
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)  -- Внешний ключ, связывающий state_id с полем id таблицы hbtn_0d_usa.states
);
