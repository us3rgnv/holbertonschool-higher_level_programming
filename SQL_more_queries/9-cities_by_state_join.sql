-- 9-cities_by_state_join.sql
-- This script lists all cities of the database hbtn_0d_usa
-- Each record displays: cities.id - cities.name - states.name
-- Results are sorted by cities.id ascending
-- Only one SELECT statement is used

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
