from bcrypt import gensalt,hashpw



def hash_password(password: str) -> bytes:
    return  hashpw(password= password.encode(),salt= gensalt())

def checkpwd() -> bool:
    pass

