"""
Módulo: database_connection.py

Descrição:
    Este módulo gerencia a conexão com o banco de dados
    SQLite principal da aplicação, definido pela constante DBNAME.
    Ele fornece funções para estabelecer a conexão e garantir
    a criação da estrutura inicial necessária para os dados dos usuários.

Funções:
    - get_db_connection: Retorna um objeto de conexão com o banco de dados.
    - create_user_table: Cria a tabela de usuários se ela não existir.

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
import sqlite3
import logging

logging.getLogger(__name__)

_DBNAME = 'egproj.db'


def get_connection(dbname=_DBNAME) -> sqlite3.Connection:
    """
    Cria e retorna um objeto de conexão com o banco de dados SQLite.

    A conexão é configurada para que as linhas retornadas possam ser
    acessadas por nome de coluna (via `sqlite3.Row`).

    Args:
        dbname (str): Nome do banco de dados.

    Returns:
        sqlite3.Connection: Um objeto de conexão ativo com o banco de dados.

    Raises:
        sqlite3.Error: Se ocorrer um erro durante a conexão com o \
        banco de dados (ex: permissão negada, banco corrompido).
    """
    try:
        conn = sqlite3.connect(dbname)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        logging.debug(f'Retornando conexão com {dbname}')
        return conn
    except sqlite3.Error as e:
        logging.error(f"Erro ao conectar ao banco de dados '{dbname}': {e}")
        raise
