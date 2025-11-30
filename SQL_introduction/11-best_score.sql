-- 11-best_score.sql
-- This script lists all records from second_table with score >= 10
-- It displays score and name in this order and orders by score descending

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
