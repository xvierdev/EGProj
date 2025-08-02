from datetime import datetime
from typing import Optional


class User:
    """
    Representa um usuário no sistema de aprendizado de inglês.

    Esta classe encapsula as informações básicas de um usuário, como
    ID, login, nome, senha (espera-se que seja um hash) e a data de criação
    do registro do usuário.

    Atributos:
        user_id (int): O identificador único para o usuário.
        user_login (str): O nome de usuário único usado para login.
        user_name (str): O nome de exibição do usuário.
        password (str): O hash da senha do usuário.
        created_at (datetime): O timestamp de quando o usuário foi criado.
    """

    def __init__(
        self,
        user_id: Optional[int],
        user_login: str,
        user_name: str,
        password: str,
        created_at: Optional[datetime] = None
    ):
        self.user_id = user_id
        self.user_login = user_login
        self.user_name = user_name
        self.password = password
        self.created_at = created_at

    def display_info(self) -> str:
        """
        Retorna uma string formatada com as informações do usuário
        para exibição.

        Esta string inclui o nome do usuário, seu login e a data de criação
        do registro, no formato padrão de string de data/hora (ISO 8601).

        Retorna:
            str: Uma string contendo as informações formatadas do usuário.
        """
        return (
            f"User: {self.user_name} "
            f"Login: {self.user_login} "
            f"Created at: {self.created_at}"
        )

    @classmethod
    def create_guest_user(cls):
        """
        Cria e retorna uma nova instância de usuário convidado (guest user).

        Este método de classe inicializa um objeto 'User' com valores
        padrão predefinidos para um usuário convidado, sendo útil para
        sessões que não exigem autenticação completa.

        Retorna:
            User: Uma nova instância da classe 'User' configurada
            como usuário convidado.
        """
        return cls(0, "guest", "gues user", "guest_pass")
