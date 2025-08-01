"""
Módulo: user_dao.py

Descrição:
    Este módulo oferece funções para acesso a dados (DAO) para gerenciar \
    usuários em um banco de dados SQLite. Ele abstrai as operações de \
    persistência e recuperação de dados da tabela 'users'.

Funções:
    - dao_create_user: Insere um novo usuário no banco de dados.
    - dao_read_user: Recupera um usuário pelo seu ID.
    - dao_read_user_by_login: Recupear um usuário pelo login.
    - dao_update_user: Atualiza o nome e a senha de um usuário existente.
    - dao_delete_user: Remove um usuário identificado por user_id.

Autor:
    Wesley Xavier <wesley.xvier@gmail.com>

Criado em:
    2025-07-17

Versão:
    1.0.2

Licença:
    MIT License
    Copyright (c) 2025 ProStudents Ltda.
"""
import logging
import sqlite3
from typing import Optional
from models.user import User


_USER_TABLE = 'users'

logging.getLogger(__name__)


def dao_create_user(conn: sqlite3.Connection, user_name: str, user_login: str,
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
        conn.commit()
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        conn.rollback()
        logging.exception(
            f'Erro de integridade ao inserir usuário "{user_login=}"')
        raise
    except sqlite3.Error:
        conn.rollback()
        logging.exception('Erro de banco de dados ao inserir usuário')
        raise
    except Exception:
        conn.rollback()
        logging.exception('Erro inesperado ao inserir usuário')
        raise


def dao_read_user(conn: sqlite3.Connection,
                  user_id: int) -> Optional[dict[str, str]]:
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

        result = cursor.fetchone()
        if result is not None:
            return dict(result)
        return None

    except sqlite3.Error:
        logging.exception(f'Ocorreu um erro ao consultar usuário "{user_id}"')
        raise
    except Exception:
        logging.exception(f'Erro inesperado ao consultar usuário "{user_id}"')
        raise


def dao_read_user_by_login(conn: sqlite3.Connection,
                           user_login: str) -> Optional[dict[str, str]]:
    """
    Recupera o usuário pelo login.
    """
    try:
        cursor = conn.cursor()
        cursor.execute(
            f"""SELECT id, name, login, password, created_at
                FROM {_USER_TABLE}
                WHERE login = ?""",
            (user_login,)
        )
        result = cursor.fetchone()
        if result is not None:
            return dict(result)
        return None
    except sqlite3.Error:
        logging.exception(f'Erro ao buscar usuário por login: {user_login}')
        raise


def dao_update_user(conn: sqlite3.Connection, user_id: int, user_name: str,
                    password: str) -> bool:
    """
    Atualiza a senha (hash) de um usuário existente no banco de dados.

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
        cursor = conn.cursor()
        cursor.execute(
            f"""UPDATE {_USER_TABLE}
                SET name = ?, password = ?
                WHERE id = ? """,
            (user_name, password, user_id)
        )
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        logging.exception(f'Ocorreu um erro na atualizar "{user_id=}"')
        raise e
    except Exception as e:
        logging.exception(f'Erro inexperado ao atualizar "{user_id=}"')
        raise e


def dao_delete_user(conn: sqlite3.Connection, user_id: int) -> bool:
    """
    Remove um usuário do banco de dados.

    Args:
        conn (sqlite3.Connection): O objeto de conexão com o DB.
        user_id (int): O id do usuário a ser removido.

    Returns:
        bool: True se o usuário for removido com sucesso,
        False se o usuário não for encontrado ou não for removido.

    Raises:
        sqlite3.Error: Se ocorrer um erro no banco de dados.
        Exception: Se ocorrer um erro inesperado.
    """
    try:
        cursor = conn.cursor()
        cursor.execute(
            f"""DELETE FROM {_USER_TABLE} WHERE id = ?""",
            (user_id,)
        )
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        conn.rollback()
        logging.exception(f'Ocorreu um erro ao remover "{user_id=}"')
        raise e
    except Exception as e:
        conn.rollback()
        logging.exception(f'Erro inexperado ao remover "{user_id=}"')
        raise e
