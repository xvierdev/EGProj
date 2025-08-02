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
    1.0.1

Licença:
    MIT License
    Copyright (c) 2025 ProStudents Ltda.
"""

from datetime import datetime
import sqlite3
import bcrypt
from typing import Optional
from models.model_user import User
from connection_factory.database_connection import get_connection
from dao.user_dao import (
    dao_create_user as _create_user,
    dao_read_user_by_login as _read_user_login,
    dao_update_user as _update_user,
    dao_delete_user as _delete_user
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
    try:
        with get_connection() as conn:
            error = False
            if _read_user_login(conn, user_login) is not None:
                print("Já existe um usuário com esse login.")
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

            hashed_password = bcrypt.hashpw(
                password.encode('utf-8'),
                bcrypt.gensalt()
            )
            hashed_password_decoded = hashed_password.decode('utf-8')
            user_id = _create_user(
                conn,
                user_name,
                user_login,
                hashed_password_decoded
            )
            if user_id is not None:
                user = _read_user_login(conn, user_login)
                if user is not None:
                    return _make_user(user)
                return None
    except sqlite3.IntegrityError as e:
        print(f'Ja existe um usuário com o "{user_login=}": {e}')
    except sqlite3.Error as e:
        print(f'Ocorreu um erro de SQL ao inserir "{user_login=}": {e}')
    except Exception as e:
        print(f'Ocorreu um inesperado na criação de "{user_login=}": {e}')


def authenticate_user(user_login: str, password: str) -> Optional[User]:
    """
    Autentica um usuário verificando o login e a senha.

    Args:
        user_login (str): Login do usuário.
        password (str): Senha em texto puro para autenticação.

    Returns:
        Optional[User]: Objeto do usuário recém-criado ou None
        em caso alguma falha.
    """
    try:
        with get_connection() as conn:
            data_user = _read_user_login(conn, user_login)
            if data_user is None:
                print("Usuário não encontrado. Verifique seu login.")
                return None

            user = _make_user(data_user)
            if _check_password(user, password):
                print(f"{user.user_name} autenticado com sucesso!")
                return user
            else:
                print("Senha inválida. Por favor, tente novamente.")
                return None
    except sqlite3.Error as e:
        print(f'Ocorreu um erro de SQL ao consultar usuário: {e}')
    except ValueError as e:
        print(f'Erro ao verificar a senha do usuário: {e}')
    except Exception as e:
        print(f'Ocorreu um erro inesperado ao consultar usuário: {e}')


def guest_user() -> User:
    """
    Retorna um usuário convidado com informações genéricas.

    Returns:
        User: um objeto do tipo User que representa o usuário convidado.
    """
    user = User(None, 'guest', 'guest user', '')
    return user


def update_password(user: User, old_password: str, new_password: str):
    """
    Atualiza a senha do usuário.

    Args:
        user (User): Objeto que representa o usuário.
        old_password (str): Senha atual.
        new_password (str): Nova senha.

    Returns:
        bool: True caso a senha seja alterada e False caso contrário.

    """
    try:
        with get_connection() as conn:
            if user.user_id is not None:
                if _check_password(user, old_password):
                    new_password_encoded = new_password.encode('utf-8')
                    hashed_password = bcrypt.hashpw(
                        new_password_encoded,
                        bcrypt.gensalt()
                    )
                    hashed_password_decoded = hashed_password.decode('utf-8')
                    result = _update_user(
                        conn,
                        user.user_id,
                        user.user_name,
                        hashed_password_decoded
                    )
                    if result:
                        user.password = hashed_password_decoded
                        return True
                    else:
                        return False
                else:
                    raise ValueError('Senha incorreta.')
            else:
                print(f'Erro: id nula para o usuário "{user.user_name}"')
    except sqlite3.Error as e:
        print(f'Ocorreu um erro de SQL ao atualizar a senha: {e}')
    except ValueError as e:
        print(f'Erro {e}')
    except Exception as e:
        print(f'Ocorreu um erro inesperado ao atualizar a senha: {e}')


def _check_password(user: User, password: str) -> bool:
    """
    Médoto interno para checar se a senha do usuário é válida.

    Args:
        user (User): O objeto que representa o usuário.
        password (str): A senha a ser verificada.

    Raises:
        ValueError: Caso o valor de user ou password seja None.

    Returns:
        bool: True caso a senha esteja correta, False caso contrário.
    """
    if user is None:
        raise ValueError('User não pode ser None.')
    if password is None:
        raise ValueError('Password não pode ser None.')
    password_encode = password.encode('utf-8')
    user_password_encode = user.password.encode('utf-8')
    return bcrypt.checkpw(password_encode, user_password_encode)


def delete_user_account(user: User, password: str):
    """
    Remove a conta do usuário do banco de dados.

    Args:
        user (User): O objeto que representa o usuário.
        password (str): A senha atual do usuário.
    """
    try:
        with get_connection() as conn:
            if user.user_id is not None:
                if _check_password(user, password):
                    if _delete_user(conn, user.user_id):
                        print('Usuário removido com sucesso.')
                else:
                    print('Senha inválida.')
    except sqlite3.Error as e:
        print(f'Ocorreu um erro de SQL ao tentar remover usuário: {e}')
    except ValueError as e:
        print(f'Ocorreu um erro inesperado ao tentar remover o usuário {e}')


def _make_user(data: dict[str, str]) -> User:
    # TODO: validate data before return User
    id_user = data.get('id')
    user_id = int(id_user) if id_user is not None else None

    return User(
        user_id=user_id,
        user_name=data.get('name', ''),
        user_login=data.get('login', ''),
        password=data.get('password', ''),
        created_at=datetime.strptime(
            data['created_at'], '%Y-%m-%d %H:%M:%S'
        ),
    )
