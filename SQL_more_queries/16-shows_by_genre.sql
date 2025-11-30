-- 16-shows_by_genre.sql
-- This script lists all shows and their genres
-- If a show has no genre, display NULL in the genre column
-- Results sorted by show title and genre name ascending
-- Only one SELECT statement is used

SELECT ts.title, g.name
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg ON ts.id = tsg.tv_show_id
LEFT JOIN genres g ON tsg.genre_id = g.id
ORDER BY ts.title ASC, g.name ASC;
