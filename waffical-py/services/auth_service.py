from sqlalchemy.orm import Session
from ..models import auth_model, user_model
from . import user_service
from ..schema import user_schema
from bcrypt import checkpw
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional


# Replace with a strong, randomly generated secret key
SECRET_KEY = "YOUR_SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def authenticate_user(db: Session, username: str, password: str) -> Optional[user_model.User]:
    user = user_service.get_user_by_username(db, username)
    if not user:
        return None
    if not checkpw(password.encode('utf-8'), user.hashed_password):
        return None
    else:
        return user_model.User(username=user.username, id=user.id)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def auth_middleware(token: auth_model.Token) -> bool:
        try:
            user_data = jwt.decode(token.access_token, SECRET_KEY, algorithms=ALGORITHM)
            return user_data
        except Exception as e:
            return False