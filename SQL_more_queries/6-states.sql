-- A script that creates the database hbtn_0d_usa and the table cities.
CREATE DATABASE IF NOT EXIST hbtn_0d_usa;
CREATE TABLE IF NOT EXIST cities(
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
    );
