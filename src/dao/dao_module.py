import logging
import sqlite3
from typing import Optional
from connection_factory.database_connection import get_connection
from models.model_modules import Module


def dao_get_all_categories(conn: sqlite3.Connection):
    try:
        cursor = conn.cursor()
        cursor.execute(
            """SELECT category FROM categories""")
        return cursor.fetchall()
    except sqlite3.Error:
        logging.exception('Erro ao obter lista de palavras')


def dao_get_all_word(conn: sqlite3.Connection, category: str):
    try:
        cursor = conn.cursor()
        cursor.execute(
            """SELECT br_word, en_word
            FROM words WHERE category = ?
            """, (category,)
        )
        return cursor.fetchall()
    except sqlite3.Error:
        logging.exception('Erro ao obter palavra por categoria')


def dao_get_one_random_word(conn: sqlite3.Connection, category: str):
    try:
        cursor = conn.cursor()
        cursor.execute(
            """SELECT br_word, en_word
            FROM words
            WHERE category = ?
            ORDER BY RANDOM()
            LIMIT 1
            """, (category,)
        )
        return cursor.fetchone()
    except sqlite3.Error:
        logging.exception('Erro ao obter palavra por categoria')


# if __name__ == '__main__':
#     with sqlite3.connect('egproj.db') as conn:
#         words = dao_get_all_word_by_category(conn, 'verbs')
#         for word in words:
#             print(word)
#         # data = dao_get_all_categories(conn)
#         # print(type(data))
#         # for i in data:
#         #     print(i)
