import sqlite3
from pathlib import Path
from connection_factory.database_connection import get_connection as connect


def create_tables_by_script(content: str):
    """
    Executa um script SQL para criar tabelas no banco de dados.

    Args:
        content (str): Uma string contendo um ou mais comandos SQL
                      para a criação de tabelas.

    Raises:
        e: Possíveis erros na execussão do script fornecido.
    """

    if content == '':
        raise ValueError("Content is empty")

    try:
        with connect() as conn:
            cursor = conn.cursor()
            cursor.executescript(content)
            conn.commit()

    except sqlite3.Error as e:
        raise e


def get_sql_script_content(path: Path) -> str:
    """
    Lê o conteúdo de um arquivo SQL e o retorna como uma string.

    Args:
        path (Path): O caminho completo para o arquivo SQL.

    Returns:
        str: O conteúdo do arquivo lido.

    Raises:
        FileNotFoundError:
            Se o arquivo no caminho especificado não for encontrado.
        IOError:
            Se ocorrer um erro de leitura do arquivo.
    """

    if not path.is_file():
        raise FileNotFoundError(f"Arquivo não encontrado no caminho: {path}")

    try:
        with open(path, encoding='utf-8') as file:
            return file.read()
    except IOError as e:
        raise e
