# external imports
from statistics import geometric_mean
from colorama import Fore, Back, Style, init

# internal imports
from ui.cli_menu_user import user_account_menu
from utils.util_cli import clear, quit
from models.model_user import User
from modules.core import core
from modules.phrases.interrogation import interrogquest
from modules import (
    number,
    pronouns,
)


init(autoreset=True)


def main_menu(user: User, funcs: dict[str, str]):
    """
    Mostra o menu principal do jogador após autenticação ou entrada
    como usuário convidado, contém as opções para treinar o inglês ou
    gerenciar a própria conta de usuário.
    """
    if user is None:
        print('User is not valid.')
        return
    user_name = user.user_name
    print(f'{Fore.YELLOW}{user_name}, welcome to the English App!')
    print(
        f'Press {Fore.CYAN} Ctrl + C',
        f'{Fore.RESET} to {Style.BRIGHT} exit',
        f'{Style.RESET_ALL} at any time.',
    )
    try:
        while True:
            print()
            print(f'{Fore.BLACK}{Back.WHITE}{'Menu':^22}')
            guestUser = user.user_id is None
            for key, value in funcs.items():
                if guestUser:
                    if key == '0':
                        continue
                print(f'{key} -> {value}')
            choice = input('\n> ').strip().upper()

            match choice:
                case '0':
                    if not guestUser:
                        user_account_menu(user)
                    else:
                        clear()
                        print('Invalid choice. Please try again.')
                case '1':
                    core('weekdays')
                case '2':
                    core(number.NumberTest())
                case '3':
                    core('colors')
                case '4':
                    core('geometric forms')
                case '5':
                    print('temporary disabled.')
                    # core(pronouns.PronounsTest())
                    ...
                case '6':
                    core('months')
                case '7':
                    interrogquest()
                case 'Q':
                    quit()
                case _:
                    clear()
                    print('Invalid choice. Please try again.')
    except KeyboardInterrupt:
        print('\nExiting the program.')
