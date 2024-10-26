-- List the number of records for each score in second_table
-- Display the score and the count of records with the label 'number'
SELECT score, COUNT(*) AS number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;
