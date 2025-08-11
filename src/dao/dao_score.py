import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG)
# logging.getLogger(__name__)


def dao_create_score(conn: sqlite3.Connection, id: int,
                     module_id: int, score: int):
    try:
        logging.debug(f'{id=}, {score=}')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO score (user_id,
                       module_id, score,
                       count_access,
                       record) VALUES (?, ?, ?, ?, ?)""",
                       (id, module_id, score, 1, score))
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f'Erro ao criar score {id=}: {e}')
        raise
    except Exception as e:
        logging.error(f'Ocorreu um erro inesperado ao criar score {id=}: {e=}')
        raise


def dao_read_score(conn: sqlite3.Connection, id: int):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT user_id, module_id, score, count_access, record
            FROM score WHERE user_id = ?""", (id,))
        data = cursor.fetchall()
        return data
    except sqlite3.Error as e:
        logging.error(f'Erro ao consultar score {id=}: {e}')
        raise
    except Exception as e:
        logging.error(
            f'Ocorreu um erro inesperado ao consultar score {id=}: {e=}')
        raise


def dao_update_score():
    pass


def dao_delete_score():
    pass


if __name__ == '__main__':
    conn = sqlite3.connect('egproj.db')
    conn.row_factory = sqlite3.Row
    # dao_create_score(conn, 1, 1, 111)
    # dao_create_score(conn, 1, 2, 333)
    data = dao_read_score(conn, 1)
    for line in data:
        print(dict(line))
    conn.close()
