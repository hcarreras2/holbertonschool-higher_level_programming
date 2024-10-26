-- Create the second_table if it does not already exist
CREATE TABLE IF NOT EXISTS second_table (
    id INT PRIMARY KEY,       -- Define the id column as INT and set it as the primary key
    name VARCHAR(256),       -- Define the name column as VARCHAR with a maximum length of 256 characters
    score INT                -- Define the score column as INT
);

-- Insert multiple rows into second_table
INSERT INTO second_table (id, name, score) VALUES 
(1, 'John', 10),          -- Insert the first record
(2, 'Alex', 3),           -- Insert the second record
(3, 'Bob', 14),           -- Insert the third record
(4, 'George', 8);         -- Insert the fourth record