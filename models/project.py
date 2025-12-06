from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from db.base import Base
import uuid

class ProjectError(Exception):
    """Custom exception for project-related errors in projects."""
    pass
class Project(Base):
    __tablename__ = "projects"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4())[:6])
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)

    # One-to-Many Relationship
    tasks = relationship("Task", back_populates="project", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Project id={self.id} name={self.name}>"
