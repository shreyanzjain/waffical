from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from ..data_conn import get_db
from ..models import user_model
from ..services import user_service

router = APIRouter()


@router.post("/users", response_model=user_model.User,
             responses={
                 status.HTTP_400_BAD_REQUEST: {
                     "description": "Bad Request: User already exists"}
             })
async def create_user_endpoint(user: user_model.UserCreate, db: Session = Depends(get_db)):
    if (user_service.get_user_by_username(db, user.username)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"User {user.username} already exists")
    return user_service.create_user(db, user)
