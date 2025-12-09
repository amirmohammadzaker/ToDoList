from pydantic import BaseModel
from typing import Optional


class ProjectResponse(BaseModel):
    """
    Response schema for a project.

    Attributes:
        id: Unique identifier of the project.
        name: Name of the project.
        description: Optional description of the project.
    """
    id: str
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True
        """
        Enable ORM mode for automatic conversion from ORM models to Pydantic models.
        """
