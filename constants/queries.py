CREATE = "CREATE TABLE favorite(id INT, lectures TEXT, PRIMARY KEY (id))"
IF_DROP = "DROP TABLE IF EXISTS favorite"
INSERT = "INSERT INTO favorite(id, lectures) VALUES({0}, '{1}')"
DROP = "DROP TABLE favorite"
SELECT_ALL = "SELECT * FROM favorite"
SELECT_BY_ID = "SELECT lectures FROM favorite WHERE id = {0}"
UPDATE = "UPDATE favorite SET lectures = '{1}' WHERE id = {0}"
EXISTS = "SELECT EXISTS(SELECT id FROM favorite WHERE id = {0})"