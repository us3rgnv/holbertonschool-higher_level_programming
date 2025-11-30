-- 13-count_shows_by_genre.sql
-- This script lists all genres from hbtn_0d_tvshows and the number of shows linked to each
-- Columns: genre, number_of_shows
-- Do not display genres with no shows
-- Results are sorted by number_of_shows DESC
-- Only one SELECT statement is used

SELECT g.name AS genre, COUNT(tsg.tv_show_id) AS number_of_shows
FROM genres g
JOIN tv_show_genres tsg ON g.id = tsg.genre_id
GROUP BY g.id
ORDER BY number_of_shows DESC;
