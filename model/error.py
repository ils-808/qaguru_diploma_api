from typing import List

from pydantic import BaseModel, RootModel


class ErrorRes(BaseModel):
    reason: str
