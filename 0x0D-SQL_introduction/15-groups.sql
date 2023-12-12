-- lists the number of records with the same score in the table second_table
-- use the SELECT command
SELECT score,  count(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;

