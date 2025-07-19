-- CREATE DATABASE egproj;
-- USE egproj;

-- tabela de armazenamento dos usuários
CREATE TABLE
  user (
    id INTEGER PRIMARY KEY auto_increment, -- Unique identifier for each user
    name VARCHAR(100) NOT NULL, -- User's name
    login VARCHAR(100) NOT NULL UNIQUE, -- Unique login for the user
    password VARCHAR(100) NOT NULL, -- User's password
    createtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the user was created
  );

-- tabela de armazenamento de referencia aos módulos
CREATE TABLE
  module (
    module_id INTEGER PRIMARY KEY AUTOINCREMENT,
    module_name TEXT UNIQUE NOT NULL,
    description TEXT,
    count_total_access INTEGER NOT NULL DEFAULT 0,
    record_user_id INTEGER,
    record_value INTEGER DEFAULT 0,
    record_datetime TIMESTAMP,
    FOREIGN KEY (record_user_id) REFERENCES user (id)
  );

-- tabela de armazenamento dos scores
CREATE TABLE
  score (
    user_id INTEGER NOT NULL,
    module_id INTEGER NOT NULL,
    total_score INTEGER NOT NULL DEFAULT 0,
    count_access INTEGER NOT NULL DEFAULT 1,
    record INTEGER DEFAULT 0,
    FOREIGN KEY user_id REFERENCES user (id),
    FOREIGN KEY module_id REFERENCES module (module_id)
  );