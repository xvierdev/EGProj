from pathlib import Path
import sqlite3
from ui import cli_initial_menu, cli_main_menu
from connection_factory.create_tables import (
    create_tables_by_script,
    get_sql_script_content
)


_SCRIPT = (Path(__file__).parent / 'scripts' / 'main_tables.sql').resolve()


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
    try:
        script_path = get_sql_script_content(_SCRIPT)
        create_tables_by_script(script_path)
        current_user = cli_initial_menu.user_menu()
        cli_main_menu.main_menu(current_user, funcs)
    except (FileNotFoundError, sqlite3.Error) as e:
        print(f'Erro ao criar tabelas: {e}')


if __name__ == '__main__':
    main()
    # ...
