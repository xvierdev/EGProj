CREATE DATABASE EnglishTerminal;

USE EnglishTerminal;

CREATE TABLE User (
  id INT PRIMARY KEY auto_increment, -- Unique identifier for each user
  name VARCHAR(100) NOT NULL, -- User's name
  login VARCHAR(100) NOT NULL UNIQUE, -- Unique login for the user
  password VARCHAR(100) NOT NULL,  -- User's password
  createtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the user was created
);

INSERT INTO
  user (name, login, password)
VALUES
  ('joão', 'jao', 'jao123');