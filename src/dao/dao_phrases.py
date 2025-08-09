import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG)
# logging.getLogger(__name__)


def phrase_create(conn: sqlite3.Connection, phrase: str) -> None:
    try:
        cursor = conn.cursor()
        logging.debug(phrase)
        cursor.execute('''
                       INSERT INTO phrases (phrase)
                       VALUES (?)''', (phrase, ))
        conn.commit()
    except sqlite3.Error:
        raise


def phrase_read():
    ...


def phrase_update():
    ...


def phrase_delete():
    ...


if __name__ == '__main__':
    conn = sqlite3.connect('egproj.db')
    phrase_create(conn, 'teste de inserção')
    conn.close()
