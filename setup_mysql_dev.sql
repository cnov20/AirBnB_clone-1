-- Script sets up a MYSQL server
-- Sets usage and permissions for database and user
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
GRANT ALL ON *.* TO hbnb_dev_db;
