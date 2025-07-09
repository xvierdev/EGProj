import random
from database_color import creat_dataase_color,boot,completion,cursor
points = 9

def colors():
    global points
    while True:
        creat_dataase_color()
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
