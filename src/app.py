from modules import weekdays, number, colors, geomtest, pronouns, months
from colorama import Fore, Back, Style, init
from core import core

init(autoreset=True)

funcs = {
    "1": "Weekdays",
    "2": "Numbers",
    "3": "Colors",
    "4": "Geometry",
    "5": "Pronouns",
    "6": "Months",
    "q": "Quit"
}


def main_menu():
    """Display a simple menu to the user and handle their choices.F
    This function provides a menu with options to show weekdays or
    exit the program.
    It runs in a loop until the user chooses to exit.
    """
    print(Fore.YELLOW + "Welcome to the English App!")
    print(f"Press {Fore.CYAN} Ctrl + C",
          f"{Fore.RESET} to {Style.BRIGHT} exit",
          f"{Style.RESET_ALL} at any time.")
    try:
        while True:
            print()
            print(f"{Fore.BLACK}{Back.WHITE}    Menu    ")

            for key, value in funcs.items():
                print(f"{key}. {value}")
            choice = input("Enter your choice: ")

            match choice:
                case '1':
                    core(weekdays.WeekdaysTest())
                case '2':
                    core(number.NumberTest())
                case '3':
                    colors.colors()
                case '4':
                    core(geomtest.GeometryTest())
                case '5':
                    core(pronouns.PronounsTest())
                case '6':
                    core(months.MonthsTest())
                case 'q':
                    print(f"{Fore.YELLOW}{Back.BLACK}Goodbye ...")
                    break
                case _:
                    print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nExiting the program.")


if __name__ == "__main__":
    main_menu()
