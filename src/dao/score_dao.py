#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nome do arquivo: score_dao.py

Descrição:
    Este módulo fornece funções de acesso a dados para gerenciar pontuações
    em um banco de dados SQLite.

Funções:
    - create_scores_table: Cria a tabela de pontuações, se ela não existir.
    - insert_score: Insere uma nova pontuação na tabela de pontuações.
    - get_scores: Recupera pontuações para um usuário e módulo específicos.
    - update_score: Atualiza a pontuação para um usuário e módulo específicos.
    - delete_score: Exclui a pontuação para um usuário e módulo específicos.
    - initialize_database: Inicializa o banco de dados e cria a tabela de
      pontuações.

Autor:
    Wesley Xavier <wesley.xvier@gmail.com>

Criado em:
    2025-07-16

Versão:
    1.0.0

Licença:
    Licença MIT
    Copyright (c) 2025 ProStudents Ltda.
"""
import sqlite3
from connection_factory.database_connection import (
    get_db_connection as _get_connection
)

TABLE_NAME = 'scores'


def create_scores_table():
    """Create the scores table if it does not exist."""
    conn = _get_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    module_id INTEGER NOT NULL,
                    score INTEGER DEFAULT 0,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while creating the table: {e}")
        finally:
            conn.close()
    else:
        print("Failed to create a database connection.")


def insert_score(user_id, module_id, score):
    """Insert a new score into the scores table."""
    conn = _get_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(f'''
                INSERT INTO {TABLE_NAME} (user_id, module_id, score)
                VALUES (?, ?, ?)
            ''', (user_id, module_id, score))
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while inserting the score: {e}")
        finally:
            conn.close()
    else:
        print("Failed to create a database connection.")


def get_scores(user_id, module_id):
    """Retrieve scores for a specific user and module."""
    conn = _get_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(f'''
                SELECT * FROM {TABLE_NAME}
                WHERE user_id = ? AND module_id = ?
            ''', (user_id, module_id))
            scores = cursor.fetchall()
            return scores
        except sqlite3.Error as e:
            print(f"An error occurred while retrieving scores: {e}")
            return []
        finally:
            conn.close()
    else:
        print("Failed to create a database connection.")
        return []


def update_score(user_id, module_id, score):
    """Update the score for a specific user and module."""
    conn = _get_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(f'''
                UPDATE {TABLE_NAME}
                SET score = ?
                WHERE user_id = ? AND module_id = ?
            ''', (score, user_id, module_id))
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while updating the score: {e}")
        finally:
            conn.close()
    else:
        print("Failed to create a database connection.")


def delete_score(user_id, module_id):
    """Delete the score for a specific user and module."""
    conn = _get_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(f'''
                DELETE FROM {TABLE_NAME}
                WHERE user_id = ? AND module_id = ?
            ''', (user_id, module_id))
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while deleting the score: {e}")
        finally:
            conn.close()
    else:
        print("Failed to create a database connection.")


def initialize_database():
    """Initialize the database and create the scores table."""
    create_scores_table()
