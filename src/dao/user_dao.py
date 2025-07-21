#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo: user_dao.py

Descrição:
    Este módulo oferece funções para acesso a dados (DAO) para gerenciar
    usuários em um banco de dados SQLite. Ele abstrai as operações de
    persistência e recuperação de dados da tabela 'users'.

Funções:
    - insert_user: Insere um novo usuário no banco de dados.
    - get_user_by_id: Recupera um usuário pelo seu ID.
    - verify_user_login_exists: Verifica se um login de usuário já existe.
    - get_user_by_login: Recupera um usuário pelo seu login.

Autor:
    Wesley Xavier <wesley.xvier@gmail.com>

Criado em:
    2025-07-17

Versão:
    1.0.0

Licença:
    MIT License
    Copyright (c) 2025 ProStudents Ltda.
"""
import sqlite3
from datetime import datetime
from typing import Optional
from models.user import User

from connection_factory.database_connection import (
    get_db_connection as get_connection
)


def insert_user(user_name: str, user_login: str, user_password: str):
    """Insere um novo usuário na tabela 'users'.

    Args:
        user_login (str): O login único do usuário.
        user_name (str): O nome de exibição do usuário.
        hashed_password (str): O hash da senha do usuário.

    Retorna:
        int: O ID (chave primária) do usuário recém-inserido.

    Levanta:
        sqlite3.IntegrityError: Se o 'user_login' já existir
        (UNIQUE violation).
        sqlite3.Error: Para outros erros de banco de dados.
        Exception: Para erros inesperados.
    """
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (name, login, password)
                VALUES (?, ?, ?)
            ''', (user_name, user_login, user_password))
            conn.commit()
            return cursor.lastrowid
    except sqlite3.IntegrityError as e:
        print(f'Erro de integridade (login duplicado): {e}')
        raise
    except sqlite3.Error as e:
        print(f'Ocorreu um erro SQL ao inserir o usuário: {e}')
        raise
    except Exception as e:
        print(f'Ocorreu um erro inesperado ao inserir o usuário: {e}')
        raise


def get_user_by_id(user_id: int) -> Optional[User]:
    """Recupera um usuário pelo seu ID do banco de dados.

    Args:
        user_id (int): O ID único do usuário a ser recuperado.

    Retorna:
        Optional[User]: Um objeto User se encontrado, caso contrário None.

    Levanta:
        sqlite3.Error: Se ocorrer um erro no banco de dados durante a operação.
        Exception: Para erros inesperados.
    """
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, name, login, password, created_at
                FROM users
                WHERE id = ? """, (user_id,))
            temp_info = cursor.fetchone()
            if temp_info is None:
                return None
            user = User(
                user_id=temp_info['user_id'],
                user_login=temp_info['user_login'],
                user_name=temp_info['user_name'],
                password=temp_info['password'],
                created_at=datetime.strptime(
                    temp_info['created_at'], '%Y-%m-%d %H:%M:%S')
            )
            return user

    except sqlite3.Error as e:
        print(f'Ocorreu um erro SQL ao recuperar o usuário por ID: {e}')
        raise
    except Exception as e:
        print(f'Ocorreu um erro inesperado ao recuperar o usuário por ID: {e}')
        raise


def verify_user_name(user_login: str) -> bool:
    """Verifica se um usuário com o login especificado já existe.

    Args:
        user_login (str): O login do usuário a ser verificado.

    Retorna:
        bool: True se o usuário existir, False caso contrário.

    Levanta:
        sqlite3.Error: Se ocorrer um erro no banco de dados durante a operação.
        Exception: Para erros inesperados.
    """
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, name, login, password, created_at
                FROM users
                WHERE login = ? """, (user_login,))
            user_exists = cursor.fetchone() is not None
            return user_exists
    except sqlite3.Error as e:
        print(f'Ocorreu um erro SQL ao verificar a existência do usuário: {e}')
        raise
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')
        raise


def get_user_by_login(user_login: str):
    """Recupera um usuário pelo seu login do banco de dados.

    Args:
        user_login (str): O login do usuário a ser recuperado.

    Retorna:
        Optional[User]: Um objeto User se encontrado, caso contrário None.

    Levanta:
        sqlite3.Error: Se ocorrer um erro no banco de dados durante a operação.
        Exception: Para erros inesperados.
    """
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, name, login, password, created_at
                FROM users
                WHERE login = ? """, (user_login,))
            temp_info = cursor.fetchone()
            if temp_info is None:
                return None
            return User(
                user_id=temp_info['id'],
                user_name=temp_info['name'],
                user_login=temp_info['login'],
                password=temp_info['password'],
                created_at=datetime.strptime(
                    temp_info['created_at'], '%Y-%m-%d %H:%M:%S')
            )
    except sqlite3.Error as e:
        print(f'Ocorreu um erro SQL ao recuperar o usuário por login: {e}')
        raise
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')
        raise
