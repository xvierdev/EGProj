#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
    1.0.0

Licença:
    MIT License
    Copyright (c) 2025 ProStudents Ltda.
"""
import sqlite3

DBNAME = 'egproj.db'


def get_db_connection() -> sqlite3.Connection:
    """
    Cria e retorna um objeto de conexão com o banco de dados SQLite.

    A conexão é configurada para que as linhas retornadas possam ser
    acessadas por nome de coluna (via `sqlite3.Row`).

    Retorna:
        sqlite3.Connection: Um objeto de conexão ativo com o banco de dados.

    Levanta:
        sqlite3.Error: Se ocorrer um erro durante a conexão com o
        banco de dados.
    """
    try:
        conn = sqlite3.connect(DBNAME)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados '{DBNAME}': {e}")
        raise


def create_user_table():
    """
    Cria a tabela 'users' no banco de dados se ela ainda não existir.

    A tabela inclui colunas para ID (chave primária autoincrementada),
    login (texto único e não nulo), nome (texto não nulo),
    senha (hash, texto não nulo)
    e data de criação (DATETIME com timestamp padrão).
    """
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    login TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao criar/verificar a tabela 'users': {e}")
        raise
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao manipular a tabela 'users': {e}")
        raise


try:
    create_user_table()
except Exception as e:
    print(f"Não foi possível inicializar as tabelas. Erro: {e}")
