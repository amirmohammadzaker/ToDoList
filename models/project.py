from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from db.base import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(String(36), primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)

    # One-to-Many Relationship
    tasks = relationship("Task", back_populates="project", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Project id={self.id} name={self.name}>"
