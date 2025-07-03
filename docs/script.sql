CREATE DATABASE EnglishTerminal;
USE EnglishTerminal;

CREATE TABLE
  User (
    id INT PRIMARY KEY auto_increment,
    name VARCHAR(100) NOT NULL,
    login VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
  );

INSERT INTO user (name, login, password) VALUES ('joão', 'jao', 'jao123');