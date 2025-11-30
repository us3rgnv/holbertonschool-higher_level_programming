-- 15-comedy_only.sql
-- This script lists all shows that belong to the Comedy genre
-- Only one SELECT statement is used
-- Results are sorted by tv show title ascending

SELECT ts.title
FROM tv_shows ts
JOIN tv_show_genres tsg ON ts.id = tsg.tv_show_id
JOIN genres g ON tsg.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY ts.title ASC;
