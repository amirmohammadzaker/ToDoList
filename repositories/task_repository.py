# app/repositories/task_repository.py

from typing import List, Optional
from datetime import date
from sqlalchemy.orm import Session
from models.task import Task as TaskModel

class TaskRepository:
    """Repository for Task entity, handles database CRUD operations."""

    def __init__(self, db_session: Session):
        self.db_session = db_session

    # -----------------------------
    # CREATE
    # -----------------------------
    def create_task(self, task: TaskModel) -> TaskModel:
        """Add a new task to the database."""
        self.db_session.add(task)
        self.db_session.commit()
        self.db_session.refresh(task)
        return task

    # -----------------------------
    # READ
    # -----------------------------
    def get_task_by_id(self, task_id: str) -> Optional[TaskModel]:
        """Retrieve a task by its ID."""
        return self.db_session.query(TaskModel).filter(TaskModel.id == task_id).first()

    def get_tasks_by_project_id(self, project_id: str) -> List[TaskModel]:
        """Retrieve all tasks for a given project."""
        return self.db_session.query(TaskModel).filter(TaskModel.project_id == project_id).all()

    def count_tasks_for_project(self, project_id: str) -> int:
        """Return the number of tasks in a given project."""
        return self.db_session.query(TaskModel).filter(TaskModel.project_id == project_id).count()

    def list_all_overdue(self) -> List[TaskModel]:
        """Return all tasks whose deadline has passed and are not yet done."""
        today = date.today()
        return self.db_session.query(TaskModel).filter(
            TaskModel.deadline < today,
            TaskModel.status != 'done'
        ).all()

    # -----------------------------
    # UPDATE
    # -----------------------------
    def update_task(self, task: TaskModel) -> TaskModel:
        """Update a task in the database."""
        self.db_session.commit()
        self.db_session.refresh(task)
        return task

    def update_task_status(self, task_id: str, new_status: str) -> None:
        """Update the status of a task by its ID."""
        task = self.get_task_by_id(task_id)
        if task:
            task.status = new_status
            self.db_session.commit()
            self.db_session.refresh(task)

    # -----------------------------
    # DELETE
    # -----------------------------
    def delete_task(self, task: TaskModel) -> None:
        """Delete a task from the database."""
        self.db_session.delete(task)
        self.db_session.commit()
