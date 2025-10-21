-- Script that return all the cities that are from California
SELECT * FROM `cities`
WHERE `state_id` = (SELECT `id` FROM `states` WHERE `name` = "California");
