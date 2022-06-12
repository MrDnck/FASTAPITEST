from typing import Optional
from pydantic import BaseModel

class USER(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str