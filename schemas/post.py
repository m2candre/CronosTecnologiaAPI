from datetime import datetime
from pydantic import BaseModel

class Post(BaseModel):
    id: int | None = None
    author_id: int
    title: str
    body: str
    #created_at: datetime | None = None
    #updated_at: datetime | None = None
    #published_at: datetime | None = None
    
    
