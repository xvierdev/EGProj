import sqlite3
conexao = sqlite3.connect('database_color.db')
cursor = conexao.cursor()
def creat_dataase_color():
    global conexao, cursor
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS database_color (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        color_english TEXT,
        color_Portuguese TEXT)""")
    conexao.commit()

def boot():
    colors_english = ["Black", "White", "Red", "Blue", "Yellow",
                    "Green", "Orange", "Pink", "Purple", "Brown", "Gray"]
    colors_portuguese = ["Preto", "Branco", "Vermelho", "Azul",
                        "Amarelo", "Verde", "Laranja", "Rosa",
                        "Roxo", "Marrom", "Cinza"]
    for colors_e, colors_p in zip(colors_english, colors_portuguese):
        cursor.execute(
            '''INSERT INTO database_color (color_english,color_Portuguese)
            VALUES (?,?)''', (colors_e, colors_p))
        conexao.commit()


def completion():
    cursor.execute("DELETE FROM database_color")
    conexao.commit()
