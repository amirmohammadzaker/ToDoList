import uuid
from sqlalchemy import Column, String, Text, ForeignKey, Date
from sqlalchemy.orm import relationship
from db.base import Base


class Task(Base):
    """
    SQLAlchemy model for the Task entity.

    Attributes:
        id: Unique identifier for the task (first 6 chars of UUID4 by default).
        title: Title of the task.
        description: Optional description of the task.
        status: Task status, default is 'todo'.
        deadline: Optional deadline date for the task.
        project_id: Foreign key referencing the related project.
        project: Relationship to the Project entity.
    """
    __tablename__ = "tasks"

    id: str = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4())[:6])
    title: str = Column(String(100), nullable=False)
    description: str | None = Column(Text, nullable=True)
    status: str = Column(String(20), nullable=False, default="todo")
    deadline: Date | None = Column(Date, nullable=True)

    project_id: str = Column(String(36), ForeignKey("projects.id"), nullable=False)
    project = relationship("Project", back_populates="tasks")

    def __repr__(self) -> str:
        return f"<Task id={self.id} title={self.title}>"
