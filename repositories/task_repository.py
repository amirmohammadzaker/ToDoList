# app/repositories/task_repository.py
from typing import List, Optional
from sqlalchemy.orm import Session
from models.task import Task as TaskModel

class TaskRepository:
    """Repository for Task entity, handles database CRUD operations."""

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_task(self, task: TaskModel) -> TaskModel:
        """Add a new task to the database."""
        self.db_session.add(task)
        self.db_session.commit()
        self.db_session.refresh(task)
        return task

    def get_task_by_id(self, task_id: str) -> Optional[TaskModel]:
        """Retrieve a task by its ID."""
        return self.db_session.query(TaskModel).filter(TaskModel.id == task_id).first()

    def get_tasks_by_project_id(self, project_id: str) -> List[TaskModel]:
        """Retrieve all tasks for a given project."""
        return self.db_session.query(TaskModel).filter(TaskModel.project_id == project_id).all()

    def update_task(self, task: TaskModel) -> TaskModel:
        """Update a task in the database."""
        self.db_session.commit()
        self.db_session.refresh(task)
        return task

    def delete_task(self, task: TaskModel) -> None:
        """Delete a task from the database."""
        self.db_session.delete(task)
        self.db_session.commit()
