--Un script qui crée la table unique_id sur votre serveur MySQL.
CREATE TABLE IF NOT EXISTS unique_id (
	id INT default 1 UNIQUE,
	name VARCHAR(256)
) ENGINE=INNODB;
