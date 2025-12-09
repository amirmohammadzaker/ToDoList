from pydantic import BaseModel
from typing import Optional
from datetime import date


class TaskResponse(BaseModel):
    """
    Response schema for a task.

    Attributes:
        id: Unique identifier of the task.
        title: Title of the task.
        description: Optional description of the task.
        status: Current status of the task (todo, doing, done).
        deadline: Optional deadline for the task.
        project_id: ID of the project this task belongs to.
    """
    id: str
    title: str
    description: Optional[str] = None
    status: str
    deadline: Optional[date] = None
    project_id: str

    class Config:
        orm_mode = True
        """
        Enable ORM mode for automatic conversion from ORM models to Pydantic models.
        """
