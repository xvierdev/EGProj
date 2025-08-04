import logging
import sqlite3


logging.getLogger(__name__)


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
        logging.exception('Erro ao obter as palavras')


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
        logging.exception('Erro ao obter uma palavra aleatória')
