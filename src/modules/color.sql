CREATE TABLE IF NOT EXISTS database_color (
    id INTEGER PRIMARY KEY auto_increment,
    color_english VARCHAR(50) UNIQUE NOT NULL,
    color_portuguese VARCHAR(50) NOT NULL
)