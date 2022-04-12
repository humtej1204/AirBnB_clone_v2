-- Creating the new DataBase
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creating a new USER
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- Giving privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
