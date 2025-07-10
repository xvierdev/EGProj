import random
from modules.database_color import creat_database_color, boot, completion, get_cursor

points = 9


def colors():
    global points
    while True:
        creat_database_color()
        completion()
        boot()
        print("╔═════════════════════════════════╗")
        print("║          jogo das cores         ║")
        print("╚═════════════════════════════════╝")
        print("(q) quit, (1) start game, (2) view score")
        menu = input("Choose your option: ")
        if menu == "q":
            break

        elif menu == "1":
            print("How does the game work?\n"
                  "A color will appear in English, and you must type "
                  "its Portuguese translation.\nThe game will begin now!")
            while True:
                get_cursor().execute(
                    "SELECT color_english,"
                    "color_Portuguese FROM database_color")
                color_r = get_cursor().fetchall()
                random_colors = random.choice(color_r)
                color_english, color_portuguese = random_colors
                print("What is the translation of this color:", color_english)
                response = str(input("> "))
                if response.lower().strip() == color_portuguese.lower():
                    print("Correct! +1 point.")
                    points += 1
                    print("Current points:", points)
                    if points == 10:
                        print("Congratulations! You've completed the quiz!")
                        break
                else:
                    points -= 1
                    print('Incorrect answer!')
                    print(f'Correct answer: {color_portuguese}')

        elif menu == "2":
            print("How does it work?")
            print("Every time you get a question right, you earn a point.")
            print("Every time you get a question wrong, you lose a point.")
            print("Current score:", points)


if __name__ == "__main__":
    colors()
