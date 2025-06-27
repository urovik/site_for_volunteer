import os
from dotenv import load_dotenv

load_dotenv()


class DBSettings():
    def __init__(self):
        self.db_host: str = os.getenv('host')
        self.db_name: str = os.getenv('db_name')
        self.db_pass: str = os.getenv('password_db')
        self.db_user: str = os.getenv('user_db')


class JWTConfig():
     def __init__(self):
        self.secret_key: str = os.getenv('private_key')
        self.secret_public_key: str = os.getenv('public_key')
        self.algorithm: str = os.getenv('algorithm')
        self.expire: int = int(os.getenv('expire_minutes'))

jwt_config = JWTConfig()







