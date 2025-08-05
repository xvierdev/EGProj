# external imports
import logging
from rich import print

# project imports
from ui.cli_menu_user import user_account_menu
from utils.util_cli import quit  # , clear
from models.model_user import User
from modules.core import core
from modules.phrases.interrogation import interrogquest
# from modules import number


logging.getLogger(__name__)


def main_menu(user: User, funcs: dict[str, str]):
    """
    Mostra o menu principal do jogador após autenticação ou entrada
    como usuário convidado, contém as opções para treinar o inglês ou
    gerenciar a própria conta de usuário.
    """
    if user is None:
        msg_err = 'usuário inválido'
        logging.error(msg_err)
        raise ValueError(msg_err)
    user_name = user.user_name
    print(
        f'[orange1]{user_name}[/orange1], [yellow]welcome to the English App!')
    print('Press [cyan] Ctrl + C[/cyan] to [red]exit[/red] at any time.')
    try:
        while True:
            print()
            print(f'[black on white]{'Menu':^22}')
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
                        # clear()
                        print('Invalid choice. Please try again.')
                case '1':
                    core('weekdays')
                case '2':
                    print('temporary disabled.')  # TODO: implementar isto
                    # core(number.NumberTest())
                case '3':
                    core('colors')
                case '4':
                    core('geometric forms')
                case '5':
                    print('temporary disabled.')  # TODO: implementar isto
                    # core(pronouns.PronounsTest())
                case '6':
                    core('months')
                case '7':
                    interrogquest()
                case 'Q':
                    quit()
                case _:
                    # clear()
                    print('Invalid choice. Please try again.')
    except KeyboardInterrupt:
        logging.info('programa finalizado pelo usuário')
        print('\nExiting the program :zzz:')
