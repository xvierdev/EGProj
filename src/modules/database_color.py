import sqlite3


def get_connection():
    """Establish a connection to the SQLite database."""
    return sqlite3.connect('database_color.db')


def creat_database_color():
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS database_color (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        simple_color_english TEXT,
        simple_color_Portuguese TEXT,
        advanced_color_english TEXT,
        advanced_color_Portuguese TEX
        )""")
    conexao.commit()


def boot():
    simple_colors_english = [
        "black", "white", "red", "blue", "yellow",
        "green", "orange", "pink", "purple", "brown", "gray"
    ]
    simple_colors_portuguese = [
        "preto", "branco", "vermelho", "azul", "amarelo",
        "verde", "laranja", "rosa", "roxo", "marrom", "cinza"
    ]
    advanced_colors_english = [
        "cyan", "magenta", "turquoise", "violet", "beige",
        "gold", "silver", "burgundy", "salmon", "lavender", "olive"
    ]
    advanced_colors_portuguese = [
        "ciano", "magenta", "turquesa", "violeta", "bege",
        "dourado", "prateado", "bordô", "salmão", "lavanda", "oliva"
    ]
    for (
        simple_colors_e,
        simple_colors_p,
        advanced_colors_e,
        advanced_colors_p
    ) in zip(
        simple_colors_english,
        simple_colors_portuguese,
        advanced_colors_english,
        advanced_colors_portuguese
    ):
        conexao = get_connection()
        cursor = conexao.cursor()
        cursor.execute(
            (
                'INSERT INTO database_color '
                '(simple_color_english, simple_color_Portuguese, '
                'advanced_color_english, advanced_color_portuguese) '
                'VALUES (?,?,?,?)'
            ),
            (
                simple_colors_e,
                simple_colors_p,
                advanced_colors_e,
                advanced_colors_p
            )
        )
        conexao.commit()
        conexao.close()


def completion():
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM DATABASE_COLOR WHERE id > 0")
    conexao.commit()
    conexao.close()
