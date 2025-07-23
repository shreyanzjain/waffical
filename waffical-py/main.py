from fastapi import FastAPI
from sqlalchemy.orm import Session
from .data_conn import SessionLocal, engine, get_db, Base
from . import schema
from .api import user_endpoint, auth_endpoint

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_endpoint.router)
app.include_router(auth_endpoint.router)


@app.get("/")
async def read_root():
    return "Hello"
