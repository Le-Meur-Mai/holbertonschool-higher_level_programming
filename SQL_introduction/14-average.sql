-- Return the score average of all the data in second_table
ALTER TABLE second_table
ADD COLUMN average FLOAT;
@average_score = (SELECT AVG(`score`) FROM second_table);
UPDATE second_table
SET `average` = @average_score
