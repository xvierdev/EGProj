from pathlib import Path
import sqlite3
from ui import cli_initial_menu, cli_main_menu
import logging

logging.basicConfig(
    # references https://docs.python.org/3/howto/logging.html
    filename='debug.log',
    format='%(asctime)s - %(levelname)s - %(filename)s - %(message)s',
    level=logging.DEBUG,
    encoding='utf-8'
)

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
    logging.info('aplicação inciada.')
    current_user = cli_initial_menu.user_menu()
    cli_main_menu.main_menu(current_user, funcs)


if __name__ == '__main__':
    main()
