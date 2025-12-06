from sqlalchemy import Column, String, Text, ForeignKey, Date
from sqlalchemy.orm import relationship
from db.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(String(36), primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(20), nullable=False, default="todo")
    deadline = Column(Date, nullable=True)

    project_id = Column(String(36), ForeignKey("projects.id"), nullable=False)
    project = relationship("Project", back_populates="tasks")

    def __repr__(self):
        return f"<Task id={self.id} title={self.title}>"
