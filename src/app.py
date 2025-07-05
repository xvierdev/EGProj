from modules import weekdays, number, colors, geomtest

funcs = {
   "1": "Show weekdays",
   "2": "Show numbers",
   "3": "Show colors",
   "4": "Show geometry",
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
            if choice == '1':
                weekdays.weekdays()
            elif choice == '2':
                number.numbers()
            elif choice == '3':
                colors.colors()
            elif choice == '4':
                geomtest.geomtest()
            elif choice == 'q':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nExiting the program.")


if __name__ == "__main__":
    main_menu()
