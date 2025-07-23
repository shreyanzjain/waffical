from sqlalchemy.orm import Session
from ..models import auth_model
from . import user_service
from bcrypt import checkpw


def login_user(db: Session, user: auth_model.Login):
    db_user = user_service.get_user_by_username(Session, user.username)
    if (checkpw(user.password, db_user.hashed_password)):
        return True
    else:
        return False
