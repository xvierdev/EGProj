#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# external imports
import sqlite3
import logging
from pathlib import Path

# project imports
from ui import cli_menu_initial, cli_menu_main
from connection_factory.create_tables import (
    create_tables_by_script,
    get_sql_script_content
)

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='debug.log',
    encoding='utf-8',
    level=logging.DEBUG
)


_SCRIPT = (Path(__file__).parent / 'scripts' / 'main_tables.sql').resolve()


funcs = {
    '0': 'Manage Account :key:',
    '1': 'Weekdays',
    '2': 'Numbers',
    '3': 'Colors',
    '4': 'Geometry',
    '5': 'Pronouns',
    '6': 'Months',
    '7': 'Interrogative forms :glowing_star:',
    'Q': 'Quit',
}


def main():
    """
    Ponto de entrada da aplicação, função principal de chamada dos menus.
    """
    try:
        logging.debug('abrindo script sql')
        script_path = get_sql_script_content(_SCRIPT)
        logging.debug('criando tabelas do aplicativo')
        create_tables_by_script(script_path)
        logging.debug('inciando menu de login')
        current_user = cli_menu_initial.user_menu()
        logging.debug('entrando na aplicação principal')
        cli_menu_main.main_menu(current_user, funcs)
    except (FileNotFoundError, sqlite3.Error) as e:
        msg_err = f'Erro ao criar tabelas: {e}'
        logging.error(msg_err)
        print(f'Erro ao criar tabelas: {msg_err}')
    except KeyboardInterrupt:
        logging.info('finalizado pelo usuário')
        print('bye...')


if __name__ == '__main__':
    main()
    # ...
