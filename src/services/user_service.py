import bcrypt
from models.user import User
from dao.user_dao import (
    get_user_by_login,
    verify_user_name,
    insert_user
)


def create_user(user_login, user_name, password):
    """Create a new user with a hashed password."""
    if verify_user_name(user_login):
        raise ValueError("User already exists with this login.")
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user = User(
        user_id=0,  # ID will be assigned by the database
        user_login=user_login,
        user_name=user_name,
        password=hashed_password.decode('utf-8')
    )
    insert_user(user.user_name, user.user_login, user.password)
    return user


def authenticate_user(user_login, password):
    """Authenticate a user by checking the login and password."""
    user = get_user_by_login(user_login)
    if user is None:
        raise ValueError("User not found.")

    if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return user
    else:
        raise ValueError("Invalid password.")
