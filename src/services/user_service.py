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
from dao.user_dao import get_user_by_login, verify_user_name, insert_user


def create_user(user_login: str, user_name: str, password: str) -> Optional[User]:
    """
    Cria um novo usuário, validando login, nome e senha
    e armazenando-a "hashed".

    Args:
        user_login (str): Login único do usuário.
        user_name (str): Nome de exibição do usuário.
        password (str): Senha em texto puro.

    Returns:
        Optional[User]: Objeto do usuário recém-criado, ou None
        em caso de falha (se não levantar exceção).

    Raises:
        ValueError: Se o login já existe, nome inválido, ou senha
        não atende aos requisitos.
    """
    if verify_user_name(user_login):
        print(
            "Já existe um usuário com esse login. Por favor, escolha outro."
        )

    if len(password) < 6:
        print("A senha precisa ter no mínimo 6 caracteres.")

    if " " in password:
        print("A senha não pode conter espaços.")

    if len(user_name) < 3:
        print("O nome de usuário precisa ter no mínimo 3 caracteres.")

    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    user = User(
        user_id=0,  # ID will be assigned by the database
        user_login=user_login,
        user_name=user_name,
        password=hashed_password.decode("utf-8"),
    )
    insert_user(user.user_name, user.user_login, user.password)
    return user


def authenticate_user(user_login: str, password: str) -> Optional[User]:
    """
    Autentica um usuário verificando o login e a senha.

    Args:
        user_login (str): Login do usuário.
        password (str): Senha em texto puro para autenticação.

    Returns:
        User: Objeto do usuário recém-criado.

    Raises:
        ValueError: Se o usuário não for encontrado ou a senha for inválida.
    """
    user = get_user_by_login(user_login)
    if user is None:
        print("Usuário não encontrado. Verifique seu login.")
        return None

    elif bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
        print(f"{user.user_name} autenticado com sucesso!")
        return user
    else:
        print("Senha inválida. Por favor, tente novamente.")
        return None


def guest_user() -> User:
    user = User(0, "guest", "guest user", "")
    return user
