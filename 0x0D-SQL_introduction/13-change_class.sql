--  a script that removes all records with a score <= 5 in the table second_table


DELETE FROM `second_table`
FROM `score`, `name`
WHERE `score` <= 5
ORDER BY `score`;