from typing import Optional

import pypi_org.data.db_session as db_session
from pypi_org.data.users import User
from passlib.handlers.sha2_crypt import sha512_crypt as crypto


def get_user_count() -> int:
    session = db_session.create_session()
    return session.query(User).count()


def hash_text(text: str) -> str:
    hashed_text = crypto.encrypt(text, rounds=10000)
    return hashed_text


def verify_hash(hashed_text: str, plain_text: str) -> bool:
    return crypto.verify(plain_text, hashed_text)


def find_user_by_email(email: str) -> Optional[User]:
    session = db_session.create_session()
    return session.query(User).filter(User.email == email).first()


def create_user(name: str, email: str, password: str) -> Optional[User]:
    if find_user_by_email(email):
        return None
    u: User = User()
    u.email = email
    u.name = name
    u.hashed_password = hash_text(password)
    session = db_session.create_session()
    session.add(u)
    session.commit()
    return u


def login_user(email: str, password: str) -> Optional[User]:
    session = db_session.create_session()
    # hashed_pw:str=hash_text(password)
    user: User = session.query(User).filter(User.email == email).first()
    if not user:
        return None
    if verify_hash(user.hashed_password, password):
        return user
    else:
        return None


def find_user_by_id(id: int) -> Optional[User]:
    session = db_session.create_session()
    return session.query(User).filter(User.id == id).first()