import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG)
# logging.getLogger(__name__)


def phrase_create(conn: sqlite3.Connection, phrase: str) -> None:
    try:
        logging.debug(f'inserir {phrase=}')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO phrases (phrase)
            VALUES (?)''', (phrase, ))
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f'Erro ao inserir frase: {e}')
        raise


def phrase_read(conn: sqlite3.Connection, id: int) -> str | None:
    try:
        logging.debug(f'consulta por {id=}')
        cursor = conn.cursor()
        cursor.execute(
            '''
            SELECT phrase FROM phrases
            WHERE id = (?)''', (id, ))
        result = cursor.fetchone()
        if result is not None:
            return result[0]
    except sqlite3.Error as e:
        logging.error(f'Erro ao obter frase: {e}')
        raise
    except Exception as e:
        logging.error(f'Erro inesperado ao obter {id=}: {e}')
        raise


def phrase_update(conn: sqlite3.Connection, id: int, phrase: str):
    try:
        logging.debug(f'atualizar {id=} com {phrase=}')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE phrases SET phrase = ?
            WHERE id = ?''', (id, phrase))
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f'Erro ao atualizar frase por {id=}: {e}')
        raise
    except Exception as e:
        logging.error(f'Erro inesperado ao atualizar {id=}: {e}')
        raise


def phrase_delete(conn: sqlite3.Connection, id: int) -> bool:
    try:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM phrases WHERE id = ?''', (id,))
        conn.commit()
        if cursor.rowcount > 0:
            return True
        else:
            return False
    except sqlite3.Error as e:
        logging.error(f'Erro ao deletar frase: {e}')
        raise
    except Exception as e:
        logging.error(f'Erro inesperado ao deletar {id=}: {e}')
        raise


if __name__ == '__main__':
    conn = sqlite3.connect('egproj.db')
    phrase_create(conn, 'teste de inserção')
    result = phrase_read(conn, 1)
    print(result)
    result = phrase_update(conn, 1, 'tralalelo tralala')
    print(result)
    for i in range(200):
        print(i, phrase_delete(conn, i))
    conn.close()
