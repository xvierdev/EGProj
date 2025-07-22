from typing import Optional
from modules import weekdays, number, colors, geomtest, pronouns, months
from services.user_service import authenticate_user, create_user, guest_user
from getpass import getpass
from colorama import Fore, Back, Style, init
from core import core
from models.user import User
from os import system

init(autoreset=True)

funcs = {
    "1": "Weekdays",
    "2": "Numbers",
    "3": "Colors",
    "4": "Geometry",
    "5": "Pronouns",
    "6": "Months",
    "q": "Quit",
}


def user_menu() -> Optional[User]:
    user = None
    print("Welcome to the English Console App!")
    while True:
        print("Choose your option:")
        print("1 - Login | 2 - Create new account | 3 - Guest user | 4 - exit")
        option = input("> ")
        system('cls')  # TODO: view this option for portability
        if option == "1":
            login = input("user: ")
            password = getpass("password: ")
            user = authenticate_user(login, password)
        elif option == "2":
            name = input("Your name: ")
            login = input("User login: ")
            password = getpass("Your password: ")
            user = create_user(name, login, password)
        elif option == "3":
            user = guest_user()
        elif option == "4":
            exit()
        if user is not None:
            system('cls')
            return user


def main_menu(user: User):
    """Display a simple menu to the user and handle their choices.F
    This function provides a menu with options to show weekdays or
    exit the program.
    It runs in a loop until the user chooses to exit.
    """
    if user is None:
        print('User is not valid.')
        exit()
    user_name = user.user_name.capitalize()
    print(f"{Fore.YELLOW}{user_name}, welcome to the English App!")
    print(
        f"Press {Fore.CYAN} Ctrl + C",
        f"{Fore.RESET} to {Style.BRIGHT} exit",
        f"{Style.RESET_ALL} at any time.",
    )
    try:
        while True:
            print()
            print(f"{Fore.BLACK}{Back.WHITE}{'Menu':^12}")

            for key, value in funcs.items():
                print(f"{key}. {value}")
            choice = input("Enter your choice: ")

            match choice:
                case "1":
                    core(weekdays.WeekdaysTest())
                case "2":
                    core(number.NumberTest())
                case "3":
                    colors.colors()
                case "4":
                    core(geomtest.GeometryTest())
                case "5":
                    core(pronouns.PronounsTest())
                case "6":
                    core(months.MonthsTest())
                case "q":
                    print(f"{Fore.YELLOW}Goodbye ...")
                    break
                case _:
                    system('cls')
                    print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nExiting the program.")


if __name__ == "__main__":
    user = user_menu()
    if user is not None:
        main_menu(user)
