from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def get(user_id):
        # tbd
        pass

    @staticmethod
    def check_password(hash, password):
        return check_password_hash(hash, password)
