from pydantic import BaseModel


class UserAuthReq(BaseModel):
    username: str
    password: str


class UserAuthRes(BaseModel):
    token: str
