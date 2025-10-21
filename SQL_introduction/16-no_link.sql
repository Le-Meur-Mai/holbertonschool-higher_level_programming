-- Script that lists all records of the table second_table of the database, except when there are an empty name
SELECT `score`, `name`
FROM second_table
WHERE `name` != ""
ORDER BY `score` DESC;
