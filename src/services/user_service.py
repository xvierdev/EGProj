"""
Módulo de Autenticação e Gestão de Usuários

Contém funções para criar novos usuários, autenticar
usuários existentes e permitir a entrada como convidado.
Ele integra-se com a camada de acesso a dados (DAO)
para interagir com o banco de dados e utiliza a biblioteca
bcrypt para o "hashing" seguro de senhas.

Funções:
    - create_user: Cria e valida um novo usuário.
    - authenticate_user: Autentica um usuário existente.
    - guest_user: retorna um objeto User como guest user.

Dependências:
    - bcrypt: Para "hashing" de senhas.
    - models.user.User: Modelo de dados para o objeto User.
    - dao.user_dao: Módulo de acesso a dados para operações de usuário.

Autores:
    Wesley Xavier <wesley.xvier@gmail.com>

Criado em:
    2025-07-17

Versão:
    1.0.0

Licença:
    MIT License
    Copyright (c) 2025 ProStudents Ltda.
"""

import bcrypt
from typing import Optional
from models.user import User
from dao.user_dao import (
    get_user_by_login,
    verify_user_login_exists,
    insert_user,
    update_password as password_update,
    delete_user
)


def create_user(user_name: str, user_login: str,
                password: str) -> Optional[User]:
    """
    Cria um novo usuário, validando login, nome e senha
    e armazenando-a "hashed".

    Args:
        user_name (str): Nome de exibição do usuário.
        user_login (str): Login único do usuário.
        password (str): Senha em texto puro.

    Returns:
        Optional[User]: Objeto do usuário recém-criado, ou None em caso de
        falha (login já existe, nome inválido, senha não atende aos
        requisitos), ou se ocorrer um erro interno.
    """
    error = False
    if verify_user_login_exists(user_login):
        print(
            "Já existe um usuário com esse login. Por favor, escolha outro."
        )
        error = True

    if len(password) < 6:
        print("A senha precisa ter no mínimo 6 caracteres.")
        error = True

    if " " in password:
        print("A senha não pode conter espaços.")
        error = True

    if len(user_name) < 3:
        print("O nome de usuário precisa ter no mínimo 3 caracteres.")
        error = True

    if len(user_login) < 3:
        print('O login precisa ter no mínimo 3 caracteres.')
        error = True

    if error:
        return None

    try:
        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )
        hashed_password_decoded = hashed_password.decode("utf-8")
        user_id = insert_user(user_name, user_login, hashed_password_decoded)
        if user_id is not None:
            user = User(
                user_id=user_id,
                user_login=user_login,
                user_name=user_name,
                password=hashed_password_decoded,
            )
            return user
    except Exception as Erro:
        print(f'Ocorreu um erro na criação do user: {Erro}')


def authenticate_user(user_login: str, password: str) -> Optional[User]:
    """
    Autentica um usuário verificando o login e a senha.

    Args:
        user_login (str): Login do usuário.
        password (str): Senha em texto puro para autenticação.

    Returns:
        User: Objeto do usuário recém-criado.
    """
    user = get_user_by_login(user_login)
    if user is None:
        print("Usuário não encontrado. Verifique seu login.")
        return None

    elif _check_password(user, password):
        print(f"{user.user_name} autenticado com sucesso!")
        return user
    else:
        print("Senha inválida. Por favor, tente novamente.")
        return None


def guest_user() -> User:
    user = User(None, "guest", "guest user", "")
    return user


def update_password(user: User, old_password: str, new_password: str):
    try:
        if user.user_id is not None:
            if _check_password(user, old_password):
                hashed_password = bcrypt.hashpw(
                    new_password.encode("utf-8"),
                    bcrypt.gensalt()
                )
                hashed_password_decoded = hashed_password.decode('utf-8')
                result = password_update(user.user_id, hashed_password_decoded)
                if result:
                    print('Password atualizado.')
                    user.password = hashed_password_decoded
                else:
                    print('Erro ao atualizar password.')
            else:
                print('Erro: Senha incorreta.')
        else:
            print('Erro: Id do usuário é nula.')
    except ValueError as e:
        print(f'Erro {e}')


def _check_password(user: User, password: str):
    if user is None:
        raise ValueError('User não pode ser None.')
    if password is None:
        raise ValueError('Password não pode ser None.')
    password_encode = password.encode('utf-8')
    user_password_encode = user.password.encode('utf-8')
    return bcrypt.checkpw(password_encode, user_password_encode)


def delete_user_account(user: User, password: str):
    if user.user_id is not None:
        if _check_password(user, password):
            if delete_user(user.user_id):
                print('Usuário removido com sucesso.')
            else:
                print('Não foi possível remover usuário.')
        else:
            print('Senha inválida.')
