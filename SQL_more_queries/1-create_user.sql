-- Создание пользователя
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Предоставление всех привилегий
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Сброс привилегий
FLUSH PRIVILEGES;
