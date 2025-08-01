import random
from colorama import Fore, Back, Style, init
from modules.database_color import (
    creat_database_color,
    boot,
    completion,
    get_connection,
)

init(autoreset=True)


def level(points):
    global levels
    levels = 0
    if points >= 0:
        levels = 1
    if points >= 10:
        levels = 2
    if points >= 20:
        levels = 3


def random_simple_color():
    global simples_color_english, simple_color_portuguese
    cursor = get_connection().cursor()
    cursor.execute(
        "SELECT simple_color_english ,"
        "simple_color_Portuguese FROM database_color")
    color_r = cursor.fetchall()
    simple_random_colors = random.choice(color_r)
    simples_color_english, simple_color_portuguese = simple_random_colors


def random_advanced_color():
    global advanced_color_english, advanced_color_portuguese
    cursor = get_connection().cursor()
    cursor.execute(
        "SELECT advanced_color_english ,"
        "advanced_color_Portuguese FROM database_color")
    color_r = cursor.fetchall()
    advaanced_random_colors = random.choice(color_r)
    advanced_color_english, advanced_color_portuguese = advaanced_random_colors


def colors():
    global points
    points = 0
    print("Welcome to the Colors Quiz!")
    print("Press Ctrl+C to exit at any time.")
    print("You can quit at any time by typing 'q'.")
    while True:
        creat_database_color()
        completion()
        boot()
        level(points)
        print("╔═════════════════════════════════╗")
        print("║            color game           ║")
        print("╚═════════════════════════════════╝")
        print("(q) quit, (1) start game, (2) tutorial")
        menu = input("Choose your option: ")
        if menu == "q":
            break

        elif menu == "1":
            if levels == 1:
                while True:
                    random_simple_color()
                    print("What is the translation of this color:",
                          simples_color_english)
                    response = str(input("> "))
                    if response.lower().strip() == simple_color_portuguese:
                        print("Correct! +1 point.")
                        points += 1
                        print("Current points:", points)
                        if not ask_play_again():
                            break

                        if points == 10:
                            print("Congratulations! You've level up!")
                            break
                    else:
                        points -= 1
                        print('Incorrect answer!')
                        print(f'Correct answer: {simple_color_portuguese}')

            elif levels == 2:
                while True:
                    random_advanced_color()
                    print("What is the translation of this color:",
                          advanced_color_english)
                    response = str(input("> "))
                    if response.strip().lower() == advanced_color_portuguese:
                        print("Correct! +1 point.")
                        points += 1
                        print("Current points:", points)
                        if points == 20:
                            print("Congratulations! You've level up!")
                            break
                    else:
                        points -= 1
                        print('Incorrect answer!')
                        print(f'Correct answer: {advanced_color_portuguese}')
                    if not ask_play_again():
                        break

            elif levels == 3:
                while True:
                    random_simple_color()
                    random_advanced_color()
                    print("What is the translation of this color:",
                          simples_color_english, advanced_color_english)
                    response_simple = str(input("first color> "))
                    response_advanced = str(input("second color> "))
                    if (
                        response_simple.strip().lower() ==
                        simple_color_portuguese
                    ):
                        if (
                            response_advanced.strip().lower() ==
                            advanced_color_portuguese
                        ):
                            print("Correct! +1 point.")
                            points += 1
                            print("Current points:", points)
                            if points == 30:
                                print("Congratulations! You've level up!")
                                break

                    if (
                        response_simple.lower() != simple_color_portuguese or
                        response_advanced.lower() != advanced_color_portuguese
                    ):
                        points -= 1
                        print('Incorrect answer!')
                        print(
                            f'Correct answer: {simple_color_portuguese}, '
                            f'{advanced_color_portuguese}'
                        )

                    if not ask_play_again():
                        break

        elif menu == "2":
            while True:
                print(f"{Fore.YELLOW}{Back.BLACK}How does it work?")
                print("Every time you get a question right, you earn a point.")
                print("Every time you get a question wrong, you lose a point.")
                print("Levels, every ten points you go up one level")
                print("start with level 1 simple colors")
                print("10 points level 2 advanced colors")
                print("20 points Level 3 Simple and Advanced colors")
                print(
                    f"Current score: {Style.BRIGHT}{points}{Style.RESET_ALL} "
                    f"your level: {Style.BRIGHT}{levels}{Style.RESET_ALL}"
                )
                if not ask_play_again():
                    break


def ask_play_again():
    """
    Pergunta ao usuário se ele quer continuar o jogo.

    Solicita ao usuário para digitar 'y' para sim ou 'n' para não.
    Qualquer entrada diferente de 'n' é interpretada como 'sim'.

    Returns:
        bool: False se o usuário digitar 'n', True caso contrário.
    """
    play_again = input('Continue (y/n): ')
    if play_again == 'n':
        return False
    else:
        return True


if __name__ == "__main__":
    colors()
