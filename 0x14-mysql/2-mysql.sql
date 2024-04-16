-- create a database with one table and one row in that table
  DROP DATABASE IF EXISTS tyrell_corp;
CREATE DATABASE tyrell_corp;

CREATE TABLE tyrell_corp.nexus6 (
    id   INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

INSERT
  INTO tyrell_corp.nexus6
       (name)
 VALUE ('Leon');

GRANT SELECT
   ON tyrell_corp.nexus6
   TO 'holberton_user'@'localhost';
