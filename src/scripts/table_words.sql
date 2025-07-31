-- tabela de definição das categorias de palavras
CREATE TABLE IF NOT EXISTS categories (
    category VARCHAR(50) PRIMARY KEY
);

-- tabela de definição das palavras
CREATE TABLE IF NOT EXISTS words (
    br_word VARCHAR(80),
    en_word VARCHAR(80),
    category VARCHAR(50),
    FOREIGN KEY (category) REFERENCES categories (name)
);