--  a script that removes all records with a score <= 5 in the table second_table

DROP TABLE `second_table`
FROM `score`, `name`
WHERE `score` <= 5
