-- 10-top_score.sql
-- This script lists all records of second_table
-- It displays score and name (in this order) and orders by score descending

SELECT score, name
FROM second_table
ORDER BY score DESC;
