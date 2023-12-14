--  lists all genres of the show Dexter
-- use SELECT statement
SELECT DISTINCT name
FROM tv_genres
JOIN tv_show_genres
JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id and tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title = 'Dexter'
ORDER BY name

