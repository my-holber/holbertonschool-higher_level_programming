-- Создание базы данных
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Создание таблицы
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,  -- Поле id с уникальным автоинкрементным значением, не может быть NULL, и является первичным ключом
    name VARCHAR(256) NOT NULL  -- Поле name типа VARCHAR с максимальной длиной 256 символов, не может быть NULL
);
