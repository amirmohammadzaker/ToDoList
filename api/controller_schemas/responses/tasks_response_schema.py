# TODOLIST/api/controller_schemas/responses/task_response_schema.py
from pydantic import BaseModel
from typing import Optional

class TaskResponse(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    status: str
    deadline: Optional[str] = None
    project_id: str

    class Config:
        orm_mode = True
