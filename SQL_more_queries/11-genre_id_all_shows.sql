-- 11-genre_id_all_shows.sql
-- This script lists all shows in hbtn_0d_tvshows
-- Each record displays: tv_shows.title - tv_show_genres.genre_id
-- Shows without a genre must display NULL
-- Results are sorted by tv_shows.title ASC and tv_show_genres.genre_id ASC
-- Only one SELECT statement is used

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
