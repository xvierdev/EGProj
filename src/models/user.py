from datetime import datetime


class User:
    def __init__(self, user_id, user_login, user_name, password, created_at=None):
        self.user_id = user_id
        self.user_login = user_login
        self.user_name = user_name
        self.password = password
        self.created_at = created_at if created_at else datetime.now()

    def display_info(self):
        return f"User: {self.user_name} Login: {self.user_login} Created at: {self.created_at}"

    @classmethod
    def create_guest_user(cls):
        """
        Create a guest user with default values.
        This method returns a User instance with predefined values for a guest user.
        """
        return cls("0", "guest", "gues user", "guest_pass")


if __name__ == "__main__":
    # Exemplo de uso
    user = User("1", "john_doe", "John Doe", "securepassword")
    print(user.display_info())

    guest_user = User.create_guest_user()
    print(guest_user.display_info())
