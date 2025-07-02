import weekdays

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
            print("2. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                weekdays.weekdays()
            elif choice == '2':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nExiting the program.")
if __name__ == "__main__":
    main_menu()