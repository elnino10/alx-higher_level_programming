-- lists all cities contained in the database hbtn_0d_usa
-- SELECT all cities in DB
SELECT cities.id, cities.name, states.name
FROM states NATURAL JOIN cities
ORDER BY cities.id

