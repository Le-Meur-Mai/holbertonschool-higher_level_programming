-- Script that display two columns, name and score of the table 'second-table' order in score, when the score is equal or superior to 10

SELECT `score`, `name`
FROM second_table
WHERE `score` >= 10
ORDER BY `score` DESC;
