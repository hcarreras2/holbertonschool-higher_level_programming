-- A script that creates the database hbtn_0d_usa and the table cities.
CREATE DATABASE IF NOT EXIST hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXIST states(
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
);
