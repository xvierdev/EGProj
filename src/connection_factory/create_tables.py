import sqlite3
import logging
from pathlib import Path
from connection_factory.database_connection import get_connection as connect

logging.getLogger(__name__)


def create_tables_by_script(content: str):
    """
    Executa um script SQL para criar tabelas no banco de dados.

    Args:
        content (str):
        Uma string contendo um ou mais comandos SQL para a criação de tabelas.

    Raises:
        sqlite3.Error: Possíveis erros na execussão do script fornecido.
    """

    if content == '':
        raise ValueError("Content is empty")

    try:
        with connect() as conn:
            cursor = conn.cursor()
            cursor.executescript(content)
            conn.commit()
            logging.debug('Script executado com sucesso.')

    except sqlite3.Error:
        logging.exception('Ocorreu um erro ao executar o script.')
        raise


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
        msg = f'Arquivo não encontrado: {path}. Nome inválido?'
        logging.error(msg)
        raise FileNotFoundError(msg)

    try:
        with open(path, encoding='utf-8') as file:
            logging.debug('Script encontrado f{path}')
            return file.read()
    except IOError as e:
        logging.error(f'Erro de IO: {e}')
        raise
