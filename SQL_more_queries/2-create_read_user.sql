-- Пользователь только для чтения
-- Создание базы данных
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Создание пользователя
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Предоставление привилегий
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
