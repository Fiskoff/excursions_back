from jwt import encode, decode
from bcrypt import gensalt, hashpw, checkpw
from app.certs.config_keys import auth_jwt

def encode_jwt(payload: dict, private_key: str = auth_jwt.private_key, algorithm: str = auth_jwt.algorithm) -> str:
    encoded = encode(payload, private_key, algorithm=algorithm)
    return encoded

def decode_jwt(token: str | bytes, public_key: str = auth_jwt.public_key, algorithm: str = auth_jwt.algorithm) -> dict:
    decoded = decode(token, public_key, algorithms=[algorithm])
    return decoded

def hash_password(password: str) -> bytes:
    salt = gensalt()
    password_bytes: bytes = password.encode()
    return hashpw(password_bytes, salt)

def validate_password(password: str, hashed_password: bytes) -> bool:
    return checkpw(password.encode(), hashed_password)
