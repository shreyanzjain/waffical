from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from ..data_conn import get_db
from ..models import user_model, auth_model
from ..services import auth_service

router = APIRouter()

base_url = "/auth"


@router.post(f"{base_url}/login", response_model=auth_model.LoginOutcome,
             responses={
                 status.HTTP_403_FORBIDDEN: {
                     "description": "Error logging in"}})
async def login_user(user_info: auth_model.Login, db: Session = Depends(get_db)):
    if (auth_service.login_user(db, user_info)):
        return auth_model.LoginOutcome(code=200, message="Successfully logged in")
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Error logging in")
