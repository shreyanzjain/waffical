from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str


class LoginOutcome(BaseModel):
    code: int
    message: str
