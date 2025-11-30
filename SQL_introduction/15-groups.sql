-- 15-groups.sql
-- This script lists the number of records with the same score in second_table
-- The result displays the score and the number of records labeled as 'number'
-- The list is sorted by the number of records descending

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
