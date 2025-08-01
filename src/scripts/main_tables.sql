-- Cria a tabela de armazenamento de usuários
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  login TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de armazenamento de módulos
CREATE TABLE IF NOT EXISTS module (
  module_id INTEGER PRIMARY KEY AUTOINCREMENT,
  module_name TEXT UNIQUE NOT NULL,
  description TEXT,
  count_total_access INTEGER NOT NULL DEFAULT 0,
  record_user_id INTEGER,
  record_value INTEGER DEFAULT 0,
  record_datetime TIMESTAMP,
  FOREIGN KEY (record_user_id) REFERENCES user (id)
);

-- Tabela de armazenamento dos scores do usuário.
CREATE TABLE IF NOT EXISTS score (
  user_id INTEGER NOT NULL,
  module_id INTEGER NOT NULL,
  total_score INTEGER NOT NULL DEFAULT 0,
  count_access INTEGER NOT NULL DEFAULT 1,
  record INTEGER DEFAULT 0,
  FOREIGN KEY (user_id) REFERENCES user (id),
  FOREIGN KEY (module_id) REFERENCES module (module_id)
);

-- Tabela de definição das categorias de palavras.
CREATE TABLE IF NOT EXISTS categories (category VARCHAR(50) PRIMARY KEY);

-- Tabela de definição da estrutura das palavras.
CREATE TABLE IF NOT EXISTS words (
  br_word VARCHAR(80),
  en_word VARCHAR(80),
  category VARCHAR(50),
  FOREIGN KEY (category) REFERENCES categories (name)
);