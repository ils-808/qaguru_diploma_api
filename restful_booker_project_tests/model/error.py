from pydantic import BaseModel


class ErrorRes(BaseModel):
    reason: str
