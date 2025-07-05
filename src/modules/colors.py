import sqlite3
import random
points = 0
conexao = sqlite3.connect('database_color.db')
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS database_color (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color_english TEXT,
    color_Portuguese TEXT)""")


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


def colors():
    global points
    while True:
        completion()
        boot()
        print("╔═════════════════════════════════╗")
        print("║          jogo das cores         ║")
        print("╚═════════════════════════════════╝")
        print("(q)sair,(1)iniciar, (2)pontuação")
        menu = input("selecione um opção :")
        if menu == "q":
            break

        elif menu == "1":
            print("How does the game work?\n"
                  "a window will appear in English and you must type "
                  "your translation into Portuguese\nthe game will start")
            while True:
                cursor.execute(
                    "SELECT color_english,"
                    "color_Portuguese FROM database_color")
                color_r = cursor.fetchall()
                random_colors = random.choice(color_r)
                color_english, color_portuguese = random_colors
                print("qual a tradução dessa cor:", color_english)
                response = str(input(">"))
                if response.lower().strip() == color_portuguese.lower():
                    print("correto +1 ponto")
                    points += 1
                    print("pontos :", points)
                    if points == 10:
                        print("!parabems! voçe completou esse quiz ")
                        break
                else:
                    points -= 1
                    print('Resposta incorreta!')
                    print(f'A resposta era: {color_portuguese}')

        elif menu == "2":
            print("How does it work?")
            print("Every time you get a question right you earn a point")
            print("Every time you get a question wrong you lose a point")
            print("Current score is:", points)


if __name__ == "__main__":
    colors()
