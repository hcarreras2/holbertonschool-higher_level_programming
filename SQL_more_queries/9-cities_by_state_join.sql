-- Script to list all cities with their states in "hbtn_0d_usa" database
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
