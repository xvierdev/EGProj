import sqlite3
from pathlib import Path
from connection_factory.database_connection import get_db_connection as connect


def create_table_words(script: str):
    try:
        with connect() as conn:
            cursor = conn.cursor()
            cursor.executescript(script)
            conn.commit()

    except sqlite3.Error as e:
        raise e


def get_script(path: Path) -> str:
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()
