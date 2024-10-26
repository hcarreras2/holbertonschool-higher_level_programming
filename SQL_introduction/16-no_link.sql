-- List all records from second_table with a non-null name value
-- Display the score and name, sorted by score in descending order
SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL 
ORDER BY score DESC;
