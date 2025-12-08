from pydantic import BaseModel
from typing import Optional
from datetime import date

class TaskResponse(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    status: str
    deadline: Optional[date] = None   
    project_id: str

    class Config:
        orm_mode = True
