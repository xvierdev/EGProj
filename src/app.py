from modules import weekdays, number, colors


def main_menu():
    """Display a simple menu to the user and handle their choices.

    This function provides a menu with options to show weekdays or exit the program.
    It runs in a loop until the user chooses to exit.
    """
    print("Welcome to the English App!")
    print("Press Ctrl+C to exit at any time.")
    try:
        while True:
            print("\nMenu:")
            print("1. Show weekdays")
            print("2. Show numbers")
            print("3. Show colors")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                weekdays.weekdays()
            elif choice == '2':
                number.numbers()
            elif choice == '3':
                colors.colors()
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nExiting the program.")
if __name__ == "__main__":
    main_menu()