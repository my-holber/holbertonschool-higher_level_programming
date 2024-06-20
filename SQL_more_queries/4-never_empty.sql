--скрипт, который создает таблицу id_not_null на вашем сервере MySQL.
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256)
);
