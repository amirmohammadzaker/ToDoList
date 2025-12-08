# TODOLIST/api/controller_schemas/responses/projects_response_schema.py
from pydantic import BaseModel
from typing import Optional

class ProjectResponse(BaseModel):
    id: str
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True  # برای تبدیل خودکار ORM objects به Pydantic
