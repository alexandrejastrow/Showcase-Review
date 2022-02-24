from passlib.context import CryptContext

context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def password_hash_generate(password: str)-> str:
    return context.hash(password)

def verify_password(password: str, password_hash: str)->bool:
    return context.verify(password, password_hash)
