class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display_info(self):
        return f"User: {self.username}"

    @classmethod
    def create_guest_user(cls):
        """
        Método de fábrica para criar um usuário convidado padrão.
        """
        return cls("guest", "guest_pass")
