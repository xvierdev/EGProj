from utils.terminal import clear, quit
from models.user import User
from services.user_service import create_user, authenticate_user, guest_user
from getpass import getpass


def user_menu() -> User:
    '''Menu inicial do usuário para criação de conta, login ou entrar
    como usuário convidado, isto ficará em loop até que seja obtido
    um usuário válido (novo, autenticado ou convidado.)

    Returns:
        User: retorna o objeto do tipo User que representa o usuário atual.
    '''
    user = None
    clear()
    print('Welcome to the English App in Command Line Interface!')
    while True:
        print('\nChoose your option:\n')
        print('1 -> Login\n2 -> Create new account\n3 -> Guest user\nQ -> Quit\n')
        option = input('> ').strip().upper()[0]
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
            clear()
            return user
