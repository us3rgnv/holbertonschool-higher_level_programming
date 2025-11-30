-- 16-no_link.sql
-- This script lists all records from second_table where name is not empty
-- It displays score and name in this order
-- Records are ordered by score descending

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
