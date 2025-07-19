CREATE DATABASE EnglishTerminal;

USE EnglishTerminal;

CREATE TABLE user (
  id INT PRIMARY KEY auto_increment, -- Unique identifier for each user
  name VARCHAR(100) NOT NULL, -- User's name
  login VARCHAR(100) NOT NULL UNIQUE, -- Unique login for the user
  password VARCHAR(100) NOT NULL,  -- User's password
  createtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the user was created
);

CREATE TABLE module (
  module_id INT PRIMARY KEY auto_increment,
  record_user_id INT,
  description TEXT,
  count_total_acess INT NOT NULL DEFAULT 0,
  module_name TEXT NOT NULL,
  record_value INT DEFAULT 0,
  record_datetime TIMESTAMP,
  FOREIGN KEY record_user_id REFERENCES user (id)
);

CREATE TABLE score (
  user_id INT NOT NULL,
  module_id INT NOT NULL,
  total_score INT NOT NULL DEFAULT 0,
  count_access INT NOT NULL DEFAULT 1,
  record INT DEFAULT 0,
  FOREIGN KEY user_id REFERENCES user (id),
  FOREIGN KEY module_id REFERENCES module (module_id)
);

INSERT INTO
  user (name, login, password)
VALUES
  ('joão', 'jao', 'jao123');