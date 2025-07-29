from ui import cli_initial_menu, cli_main_menu
from connection_factory import database_connection

database_connection.create_user_table()

funcs = {
    '0': 'Manage Account',
    '1': 'Weekdays',
    '2': 'Numbers',
    '3': 'Colors',
    '4': 'Geometry',
    '5': 'Pronouns',
    '6': 'Months',
    '7': 'Interrogative forms',
    'Q': 'Quit',
}


def main():
    """
    Ponto de entrada da aplicação, função principal de chamada dos menus.
    """
    current_user = cli_initial_menu.user_menu()
    cli_main_menu.main_menu(current_user, funcs)


if __name__ == '__main__':
    main()
