from typing import List, Optional
from datetime import date
from sqlalchemy.orm import Session
from models.task import Task as TaskModel


class TaskRepository:
    """
    Repository class for handling Task database operations.
    Provides CRUD functionality and additional task queries.
    """

    def __init__(self, db_session: Session) -> None:
        """
        Initialize TaskRepository.

        Args:
            db_session: SQLAlchemy database session.
        """
        self.db_session = db_session

    # -----------------------------
    # CREATE
    # -----------------------------
    def create_task(self, task: TaskModel) -> TaskModel:
        """
        Add a new task to the database.

        Args:
            task: The Task instance to insert.

        Returns:
            The created Task instance.
        """
        self.db_session.add(task)
        self.db_session.commit()
        self.db_session.refresh(task)
        return task

    # -----------------------------
    # READ
    # -----------------------------
    def get_task_by_id(self, task_id: str) -> Optional[TaskModel]:
        """
        Retrieve a task by its ID.

        Args:
            task_id: Unique task identifier.

        Returns:
            The matching Task instance, or None if not found.
        """
        return (
            self.db_session.query(TaskModel)
            .filter(TaskModel.id == task_id)
            .first()
        )

    def get_tasks_by_project_id(self, project_id: str) -> List[TaskModel]:
        """
        Retrieve all tasks belonging to a specific project.

        Args:
            project_id: The project identifier.

        Returns:
            A list of Task instances.
        """
        return (
            self.db_session.query(TaskModel)
            .filter(TaskModel.project_id == project_id)
            .all()
        )

    def count_tasks_for_project(self, project_id: str) -> int:
        """
        Count how many tasks exist in a given project.

        Args:
            project_id: The project identifier.

        Returns:
            The number of tasks in the project.
        """
        return (
            self.db_session.query(TaskModel)
            .filter(TaskModel.project_id == project_id)
            .count()
        )

    def list_all_overdue(self) -> List[TaskModel]:
        """
        Retrieve all overdue tasks that are not marked as done.

        Returns:
            A list of overdue Task instances.
        """
        today = date.today()
        return (
            self.db_session.query(TaskModel)
            .filter(
                TaskModel.deadline < today,
                TaskModel.status != "done"
            )
            .all()
        )

    # -----------------------------
    # UPDATE
    # -----------------------------
    def update_task(self, task: TaskModel) -> TaskModel:
        """
        Update an existing task.

        Args:
            task: The Task instance with updated values.

        Returns:
            The updated Task instance.
        """
        self.db_session.commit()
        self.db_session.refresh(task)
        return task

    def update_task_status(self, task: TaskModel, new_status: str) -> TaskModel:
        """
        Update only the status field of a task.

        Args:
            task: Task instance to update.
            new_status: The new status value.

        Returns:
            Updated Task instance.
        """
        task.status = new_status
        self.db_session.commit()
        self.db_session.refresh(task)
        return task

    # -----------------------------
    # DELETE
    # -----------------------------
    def delete_task(self, task: TaskModel) -> None:
        """
        Delete a task from the database.

        Args:
            task: Task instance to remove.
        """
        self.db_session.delete(task)
        self.db_session.commit()
