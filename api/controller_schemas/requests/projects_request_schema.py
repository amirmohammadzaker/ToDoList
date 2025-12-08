# TODOLIST/api/controller_schemas/requests/projects_request_schema.py
from pydantic import BaseModel
from typing import Optional

class ProjectCreateRequest(BaseModel):
    name: str
    description: Optional[str] = None

class ProjectUpdateRequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
