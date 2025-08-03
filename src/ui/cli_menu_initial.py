# external imports
from getpass import getpass

# internal imports
from models.model_user import User
from utils.util_cli import quit  # , clear
from services.service_user import create_user, authenticate_user, guest_user


def user_menu() -> User:
    """
    Menu inicial do usuário para criação de conta, login ou entrar
    como usuário convidado, isto ficará em loop até que seja obtido
    um usuário válido (novo, autenticado ou convidado.)

    Returns:
        User: retorna o objeto do tipo User que representa o usuário atual.
    """
    user = None
    # clear()
    print('Welcome to the English App in Command Line Interface!')
    while True:
        print('\nChoose your option:\n')
        print('\n1 -> Login\n2 -> Create new account',
              '\n3 -> Guest user\nQ -> Quit\n')
        option = None
        read_option = input('> ').strip().upper()
        if read_option is not None and len(read_option) > 0:
            option = read_option[0]
        # clear()
        if option == '1':
            login = input('User: ')
            password = getpass('Password: ')
            user = authenticate_user(login, password)
        elif option == '2':
            name = input('Your name: ')
            login = input('User login: ')
            password = getpass('Your password: ')
            user = create_user(name, login, password)
        elif option == '3':
            user = guest_user()
        elif option == 'Q':
            quit()
        else:
            print('Invalid option.')
        if user is not None:
            # clear()
            return user
