from models.user import User
from colorama import Fore, Back, Style, init
from ui.cli_user_manager import user_account_menu
from modules import (
    number,
    pronouns,
)
from modules.core import core
from modules.phrases.interrogation import interrogquest
from utils.terminal import clear, quit


init(autoreset=True)


def main_menu(user: User, funcs: dict[str, str]):
    """Mostra o menu principal do jogador após autenticação ou entrada
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

            for key, value in funcs.items():
                print(f'{key} -> {value}')
            choice = input('\n> ').strip().upper()

            match choice:
                case '0':
                    user_account_menu(user)
                case '1':
                    # core(weekdays.WeekdaysTest())
                    ...
                case '2':
                    core(number.NumberTest())
                case '3':
                    # colors.colors()
                    ...
                case '4':
                    # core(geomtest.GeometryTest())
                    ...
                case '5':
                    core(pronouns.PronounsTest())
                case '6':
                    # core(months.MonthsTest())
                    ...
                case '7':
                    interrogquest()
                case 'Q':
                    quit()
                case _:
                    clear()
                    print('Invalid choice. Please try again.')
    except KeyboardInterrupt:
        print('\nExiting the program.')
