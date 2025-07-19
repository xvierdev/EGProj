import sqlite3
from typing import Optional
from connection_factory.database_connection import get_db_connection
from models.module import Module


def insert_module(module: Module):
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """ INSERT INTO module (module_name, description)
                    VALUES (?, ?)""",
                (module.module_name, module.description),
            )
            conn.commit()
    except sqlite3.Error as e:
        print(f"Erro de conexão com banco de dados: {e}")
        raise


def get_module(module_name: str) -> Optional[Module]:
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT
                    module_id,
                    module_name,
                    description,
                    count_total_access,
                    record_user_id,
                    record_value,
                    record_datetime
                FROM
                    module
                WHERE
                    module_name = ?""",
                (module_name,),
            )
            result = cursor.fetchone()
            if not result:
                return None
            module = Module(
                module_id=result["module_id"],
                module_name=result["module_name"],
                description=result["description"],
                count_total_access=result["count_total_access"],
                record_user_id=result["record_user_id"],
                record_value=result["record_value"],
                record_datetime=result["record_datetime"],
            )
            return module
    except sqlite3.Error as e:
        print(f"Erro de conexão com banco de dados: {e}")
        raise


def update_module(): ...


def delete_module(module_name: str):
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
            DELETE FROM module WHERE module_name = ?
            """, (module_name,)

            )
    except sqlite3.Error as e:
        print(f'Erro ao remover modulo: {e}')
        raise
