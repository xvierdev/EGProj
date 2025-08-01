"""
Módulo: user_dao.py

Descrição:
    Este módulo oferece funções para acesso a dados (DAO) para gerenciar \
    usuários em um banco de dados SQLite. Ele abstrai as operações de \
    persistência e recuperação de dados da tabela 'users'.

Funções:
    - insert_user: Insere um novo usuário no banco de dados.
    - get_user_by_id: Recupera um usuário pelo seu ID.
    - verify_user_login_exists: Verifica se um login de usuário já existe.
    - get_user_by_login: Recupera um usuário pelo seu login.
    - update_password: Atualiza a senha de um usuário existente.

Autor:
    Wesley Xavier <wesley.xvier@gmail.com>

Criado em:
    2025-07-17

Versão:
    1.0.1

Licença:
    MIT License
    Copyright (c) 2025 ProStudents Ltda.
"""
from ast import Tuple
import logging
import sqlite3
from datetime import datetime
from typing import Optional
from models.user import User
from connection_factory.database_connection import (
    get_db_connection as _get_connection
)

_USER_TABLE = 'users'

logging.getLogger(__name__)


def dao_insert_user(conn: sqlite3.Connection, user_name: str, user_login: str,
                    user_password: str) -> Optional[int]:
    """
    Insere um novo usuário na table users.

    Args:
        conn (sqlite3.Connection): O objeto de conexão com o DB.
        user_name (str): O nome de exibição do usuário.
        user_login (str): O login único do usuário.
        user_password (str): O hash da senha do usuário.

    Returns:
        int: O ID (chave primária) do usuário recém-inserido.

    Raises:
        sqlite3.IntegrityError: Se o 'user_login' já existir \
        (UNIQUE constraint violation).
        sqlite3.Error: Para outros erros gerais de banco de dados.
        Exception: Para erros inesperados não relacionados ao SQLite.
    """
    try:
        cursor = conn.cursor()
        cursor.execute(
            f"""INSERT INTO {_USER_TABLE} (name, login, password)
                VALUES (?, ?, ?)""",
            (user_name, user_login, user_password)
        )
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        conn.rollback()
        logging.exception(
            f'Erro de integridade ao inserir usuário. Login: {user_login}')
        raise
    except sqlite3.Error:
        conn.rollback()
        logging.exception('Erro de banco de dados ao inserir usuário')
        raise
    except Exception:
        conn.rollback()
        logging.exception('Erro inesperado ao inserir usuário')
        raise


def dao_get_user_by_id(conn: sqlite3.Connection,
                       user_id: int) -> Optional[Tuple]:
    """
    Recupera um usuário pelo seu ID do banco de dados.

    Args:
        conn (sqlite3.Connection): O objeto de conexão com o DB.
        user_id (int): O ID único do usuário a ser recuperado.

    Returns:
        Optional[User]: Um objeto User se encontrado, caso contrário None.

    Exceptions:
        sqlite3.Error: Se ocorrer um erro no banco de dados durante a operação.
        Exception: Para erros inesperados não relacionados ao SQLite.
    """
    try:
        cursor = conn.cursor()
        cursor.execute(
            f"""SELECT id, name, login, password, created_at
                FROM {_USER_TABLE}
                WHERE id = ? """,
            (user_id,)
        )
        return cursor.fetchone()

        # TODO: move this to services level.
        # created_at_str = temp_info['created_at']
        # created_at_dt = datetime.strptime(
        #     created_at_str, '%Y-%m-%d %H:%M:%S')

        # user = User(
        #     user_id=temp_info['id'],
        #     user_login=temp_info['login'],
        #     user_name=temp_info['name'],
        #     password=temp_info['password'],
        #     created_at=created_at_dt
        # )
        # return user

    except sqlite3.Error:
        logging.exception(f'Ocorreu um erro ao consultar usuário {user_id}')
        raise
    except Exception:
        logging.exception(f'Erro inesperado ao consultar usuário {user_id}')
        raise


def dao_verify_user_login_exists(conn: sqlite3.Connection,
                                 user_login: str) -> bool:
    """
    Verifica se um usuário com o login especificado já existe.

    Args:
        conn (sqlite3.Connection): O objeto de conexão com o DB.
        user_login (str): O login do usuário a ser verificado.

    Returns:
        bool: True se o usuário existir, False caso contrário.

    Raises:
        sqlite3.Error: Se ocorrer um erro no banco de dados durante a operação.
        Exception: Para erros inesperados não relacionados ao SQLite.
    """
    try:
        with _get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"""SELECT id FROM {_USER_TABLE}
                WHERE login = ? """,
                (user_login,)
            )
            user_exists = cursor.fetchone() is not None
            return user_exists
    except sqlite3.Error as e:
        logging.exception(f'Ocorreu um erro na consultar {user_login=}')
        raise e
    except Exception as e:
        logging.exception(f'Erro inexperado na consulta {user_login=}')
        raise e


def get_user_by_login(user_login: str) -> Optional[User]:
    """Recupera um usuário pelo seu login do banco de dados.

    Args:
        user_login (str): O login do usuário a ser recuperado.

    Returns:
        Optional[User]: Um objeto User se encontrado, caso contrário None.

    Raises:
        sqlite3.Error: Se ocorrer um erro no banco de dados durante a operação.
        Exception: Para erros inesperados não relacionados ao SQLite.
    """
    try:
        with _get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                f""" SELECT id, name, login, password, created_at
                FROM {_USER_TABLE}
                WHERE login = ? """,
                (user_login,)
            )
            temp_info = cursor.fetchone()
            if temp_info is None:
                return None

            created_at_str = temp_info['created_at']
            created_at_dt = datetime.strptime(
                created_at_str, '%Y-%m-%d %H:%M:%S')

            return User(
                user_id=temp_info['id'],
                user_name=temp_info['name'],
                user_login=temp_info['login'],
                password=temp_info['password'],
                created_at=created_at_dt
            )
    except sqlite3.Error as e:
        # print(f'Ocorreu um erro SQL ao recuperar o usuário por login: {e}')
        raise e
    except Exception as e:
        # print(
        #     f'Ocorreu um erro inesperado ao recuperar '
        #     f'o usuário por login: {e}'
        # )
        raise e


def update_password(user_id: int, new_password_hash: str) -> bool:
    """Atualiza a senha (hash) de um usuário existente no banco de dados.

    Args:
        user_id (int): O ID único do usuário cuja senha será atualizada.
        new_password_hash (str): O novo hash da senha a ser armazenado.

    Returns:
        bool: True se a senha foi atualizada com sucesso, \
        False se o usuário não foi encontrado ou a senha não foi alterada.

    Raises:
        sqlite3.Error: Se ocorrer um erro no banco de dados durante a operação.
        Exception: Para outros erros inesperados não relacionados ao SQLite.
    """
    try:
        with _get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"""UPDATE {_USER_TABLE}
                SET password = ?
                WHERE id = ? """,
                (new_password_hash, user_id)
            )
            conn.commit()
            return cursor.rowcount > 0
    except sqlite3.Error as e:
        raise e
    except Exception as e:
        raise e


def delete_user(user_id: int) -> bool:
    """Remove um usuário do banco de dados.
    Args:
        user_id (int): O id do usuário a ser removido.

    Returns:
        bool: True se o usuário for removido com sucesso,
        False se o usuário não for encontrado ou não for removido.

    Raises:
        sqlite3.Error: Se ocorrer um erro no banco de dados.
        Exception: Se ocorrer um erro inesperado.
    """
    try:
        with _get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"""DELETE FROM {_USER_TABLE} WHERE id = ?""",
                (user_id,)
            )
            return cursor.rowcount > 0
    except sqlite3.Error as e:
        raise e
    except Exception as e:
        raise e
