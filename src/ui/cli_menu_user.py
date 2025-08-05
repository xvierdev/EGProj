# external imports
from getpass import getpass
from rich import print

# project imports
from utils.util_cli import quit  # , clear
from models.model_user import User
from services.service_user import update_password, delete_user_account


def user_account_menu(user: User):
    if user is None:
        raise ValueError('User cannot be None.')
    # clear()
    while True:
        print('[orange1]Summary')
        print()
        print(f'[yellow]User name: {user.user_name}')
        print(f'[yellow]Login: {user.user_login}')
        print(f'[yellow]Created at: {user.created_at}')
        print('\n[orange1]Choose one option:\n')
        print('1 > Choose your password :key:')
        print('2 > Delete your account :toilet:')
        print('R > Return to back menu :wine_glass:')
        print('Q > Quit :zzz:')
        option = input('\n> ').strip().upper()[0]

        match option:
            case '1':
                try:
                    old_password = getpass('Type old password: ')
                    new_password = getpass('Type new password: ')
                    t_new_password = getpass('Re-type new password: ')

                    if new_password != t_new_password:
                        raise ValueError('Passwords must match!')

                    result = update_password(user, old_password, new_password)
                    if result is True:
                        print('Senha alterada com sucesso!')
                    else:
                        print('Erro ao alterar a senha.')
                except ValueError as e:
                    print(f'Erro: {e}')
            case '2':
                password = getpass('Current password: ')
                delete_user_account(user, password)
                quit()
            case 'R':
                # clear()
                break
            case 'Q':
                quit()
