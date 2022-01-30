from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int | None = None
    name: str
    email: str
    password: str
    is_admin: bool | None = None
    #created_at: datetime | None = None
