-- 12-no_genre.sql
-- This script lists all shows in hbtn_0d_tvshows without a genre linked
-- Each record displays: tv_shows.title - tv_show_genres.genre_id (NULL)
-- Results are sorted by tv_shows.title ASC
-- Only one SELECT statement is used

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;
