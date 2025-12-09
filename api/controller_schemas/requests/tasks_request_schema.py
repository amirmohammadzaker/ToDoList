from pydantic import BaseModel
from typing import Optional


class TaskCreateRequest(BaseModel):
    """
    Request schema for creating a new task.

    Attributes:
        title: Title of the task (required).
        description: Optional description of the task.
        deadline: Optional deadline for the task in YYYY-MM-DD format.
    """
    title: str
    description: Optional[str] = None
    deadline: Optional[str] = None


class TaskUpdateRequest(BaseModel):
    """
    Request schema for updating an existing task.

    Attributes:
        title: New title of the task (optional).
        description: New description of the task (optional).
        status: New status of the task (optional). Allowed values: todo, doing, done.
        deadline: New deadline of the task in YYYY-MM-DD format (optional).
    """
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    deadline: Optional[str] = None


class TaskStatusUpdateRequest(BaseModel):
    """
    Request schema for updating the status of a task.

    Attributes:
        status: New status of the task. Allowed values: todo, doing, done.
    """
    status: str
