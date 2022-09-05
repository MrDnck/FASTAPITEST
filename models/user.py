from typing import Optional
from pydantic import BaseModel

class USER(BaseModel):
    name: str
    email: str
    password: str


class USERCREATE(BaseModel):
    email: str
    password: str
    replypassword: str

class USERCHECK(BaseModel):
    email: str
    password: str