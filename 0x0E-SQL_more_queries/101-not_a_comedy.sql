--  lists all shows without the genre Comedy in the database
-- select shows without comedy genre
SELECT DISTINCT tv_shows.title
FROM tv_shows
LEFT OUTER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT OUTER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title NOT IN (
	SELECT tv_shows.title
	FROM tv_shows
	LEFT OUTER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
	LEFT OUTER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
	WHERE tv_genres.name = 'Comedy')
ORDER BY tv_shows.title

