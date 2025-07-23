from sqlalchemy.orm import Session
from ..schema import user_schema
from ..models import user_model
from bcrypt import hashpw, gensalt

def get_user_by_username(db: Session, username: str):
    return db.query(user_schema.User).filter(user_schema.User.username == username).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(user_schema.User).filter(user_schema.User.id == user_id).first()

def create_user(db: Session, user: user_model.UserCreate):
    hashed_pwd = hashpw(password=user.password.encode(), 
                        salt=gensalt())
    db_user = user_schema.User(username=user.username, hashed_password=hashed_pwd)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user