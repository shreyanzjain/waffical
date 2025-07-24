from datetime import timedelta, datetime

from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..data_conn import get_db
from ..models import user_model, auth_model
from ..services import auth_service


router = APIRouter()

base_url = "/auth"


@router.post(f"{base_url}/login", response_model=auth_model.Token,
             responses={
                 status.HTTP_401_UNAUTHORIZED: {
                     "description": "Error logging in"}})
async def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth_service.authenticate_user(
        db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=auth_service.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_service.create_access_token(
        data={"username": user.username, "id": user.id}, expires_delta=access_token_expires
    )
    return auth_model.Token(access_token=access_token, token_type="bearer")


@router.post(f"{base_url}/check")
async def auth_check(access_token: str):
    return auth_service.auth_middleware(auth_model.Token(access_token=access_token, token_type="bearer"))
