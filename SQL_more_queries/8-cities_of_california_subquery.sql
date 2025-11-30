-- 8-cities_of_california_subquery.sql
-- This script lists all cities in California in the database hbtn_0d_usa
-- No JOIN is allowed, so we use a subquery to find California's id

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
