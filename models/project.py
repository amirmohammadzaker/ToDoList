import uuid
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from db.base import Base


class ProjectError(Exception):
    """
    Custom exception for project-related errors.
    """
    pass


class Project(Base):
    """
    SQLAlchemy model for the Project entity.

    Attributes:
        id: Unique identifier for the project (first 6 chars of UUID4 by default).
        name: Name of the project.
        description: Optional description of the project.
        tasks: One-to-many relationship with Task entity.
    """
    __tablename__ = "projects"

    id: str = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4())[:6])
    name: str = Column(String(100), nullable=False)
    description: str | None = Column(Text, nullable=True)

    tasks = relationship(
        "Task",
        back_populates="project",
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Project id={self.id} name={self.name}>"
