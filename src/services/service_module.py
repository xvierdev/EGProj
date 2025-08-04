import logging
from typing import Optional

from connection_factory.database_connection import get_connection as _get_conn
from dao.dao_module import (
    dao_get_one_random_word as _get_random_word
)


logging.getLogger(__name__)

# logging.basicConfig(level=logging.DEBUG)


class Vocabulary:
    def __init__(self, category: str):
        logging.debug(f'{category=}')
        if category is None:
            raise ValueError('Categoria não pode ser nula')
        elif category == '':
            raise TypeError('Categoria não pode ser vazio')
        self.category = category

    def get_random_words(self) -> Optional[list[str]]:
        """
        Obtém uma lista com uma palavra aleatória em português e sua traduação
        para o inglês.

        Returns:
            Optional[list[str]]: Uma lista contendo a palavra em português e a
            palavra em inglês ou None caso a categoria não exista.
        """
        with _get_conn() as conn:
            word = _get_random_word(conn, self.category)
            if word is None:
                return None
            return [word['br_word'], word['en_word']]
