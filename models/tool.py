from typing import Optional
from pydantic import BaseModel

class TOOL(BaseModel):
    string: str
    user_id: Optional[str]
    type: str