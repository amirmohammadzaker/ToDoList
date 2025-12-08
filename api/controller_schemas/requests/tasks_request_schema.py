# TODOLIST/api/controller_schemas/requests/task_request_schema.py
from pydantic import BaseModel
from typing import Optional

class TaskCreateRequest(BaseModel):
    title: str
    description: Optional[str] = None
    deadline: Optional[str] = None  # YYYY-MM-DD

class TaskUpdateRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None  # todo/doing/done
    deadline: Optional[str] = None

class TaskStatusUpdateRequest(BaseModel):
    status: str  # todo/doing/done
