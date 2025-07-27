from utils.terminal import clear
from getpass import getpass
from models.user import User
from services.user_service import update_password, delete_user_account


def user_account_menu(user: User):
    if user is None:
        raise ValueError('User cannot be None.')
    while True:
        print('Choose one option:')
        print()
        print('1 - choose password')
        print('2 - delete account')
        print('r - return to back menu')
        print()
        option = input('> ')

        if option in ('q', 'Q'):
            exit()

        match option:
            case '1':
                old_password = getpass('type old password: ')
                new_password = getpass('type new password: ')
                t_new_password = getpass('re-type new password: ')

                if new_password != t_new_password:
                    raise ValueError('Passwords must match!')

                update_password(user, old_password, new_password)
            case '2':
                password = getpass('current password: ')
                delete_user_account(user, password)
                exit()
            case 'r':
                clear()
                break
