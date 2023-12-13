-- creates the table unique_id on your MySQL server
-- id of the table defaults to 1 and is unique
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));

