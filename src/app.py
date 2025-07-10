from modules import weekdays, number, colors, geomtest, pronouns, months

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
    print("Welcome to the English App!")
    print("Press Ctrl+C to exit at any time.")
    try:
        while True:
            print("\nMenu:")

            for key, value in funcs.items():
                print(f"{key}. {value}")
            choice = input("Enter your choice: ")
            
            match choice:
                case '1':
                    weekdays.weekdays()
                case '2':
                    number.numbers()
                case '3':
                    colors.colors()
                case '4':
                    geomtest.geomtest()
                case '5':
                    pronouns.pronouns_test()
                case '6':
                    months.start()
                case 'q':
                    print("Goodbye")
                    break
                case _:
                    print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nExiting the program.")


if __name__ == "__main__":
    main_menu()
