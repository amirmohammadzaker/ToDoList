from pydantic import BaseModel
from typing import Optional


class ProjectCreateRequest(BaseModel):
    """
    Request schema for creating a new project.

    Attributes:
        name: Name of the project (required).
        description: Optional description of the project.
    """
    name: str
    description: Optional[str] = None


class ProjectUpdateRequest(BaseModel):
    """
    Request schema for updating an existing project.

    Attributes:
        name: New name of the project (optional).
        description: New description of the project (optional).
    """
    name: Optional[str] = None
    description: Optional[str] = None
