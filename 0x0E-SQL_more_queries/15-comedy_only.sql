--  lists all Comedy shows in the database hbtn_0d_tvshows
-- select only comedy shows
SELECT title
FROM tv_shows
JOIN tv_show_genres
JOIN tv_genres
ON tv_shows.id = tv_show_genres.show_id and tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title

