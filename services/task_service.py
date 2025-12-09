import os
from typing import Optional, List

from repositories.task_repository import TaskRepository
from repositories.project_repository import ProjectRepository
from exceptions.service_exceptions import TaskLimitReachedError
from models.task import Task

MAX_NUMBER_OF_TASK = int(os.getenv("MAX_NUMBER_OF_TASK", 10))


class TaskService:
    """
    Service layer for handling task-related business logic.
    """

    def __init__(self, task_repo: TaskRepository, project_repo: ProjectRepository) -> None:
        """
        Initialize TaskService.

        Args:
            task_repo: Repository for task database operations.
            project_repo: Repository for project-related queries.
        """
        self.task_repo = task_repo
        self.project_repo = project_repo

    # -----------------------------
    # CREATE
    # -----------------------------
    def create_task(
        self,
        project_id: str,
        title: str,
        description: Optional[str] = None,
        deadline: Optional[str] = None
    ) -> Task:
        """
        Create a new task inside a project.

        Args:
            project_id: The ID of the project the task belongs to.
            title: Task title.
            description: Task description (optional).
            deadline: Task deadline (optional).

        Returns:
            The created Task instance.

        Raises:
            TaskLimitReachedError: If project has reached its maximum task capacity.
        """
        project = self.project_repo.get_project_by_id(project_id)

        count = self.task_repo.count_tasks_for_project(project_id)
        if count >= MAX_NUMBER_OF_TASK:
            raise TaskLimitReachedError(
                f"Cannot create more than {MAX_NUMBER_OF_TASK} tasks in this project."
            )

        task = Task(
            title=title,
            description=description,
            deadline=deadline,
            project_id=project_id
        )
        return self.task_repo.create_task(task)

    # -----------------------------
    # READ
    # -----------------------------
    def get_task(self, task_id: str) -> Task:
        """
        Retrieve a task by ID.

        Args:
            task_id: The unique identifier of the task.

        Returns:
            The Task object.
        """
        return self.task_repo.get_task_by_id(task_id)

    def list_tasks(self, project_id: str) -> List[Task]:
        """
        List all tasks belonging to a project.

        Args:
            project_id: The project ID.

        Returns:
            A list of Task objects.
        """
        return self.task_repo.get_tasks_by_project_id(project_id)

    # -----------------------------
    # UPDATE
    # -----------------------------
    def update_task(
        self,
        task_id: str,
        title: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[str] = None,
        deadline: Optional[str] = None
    ) -> Task:
        """
        Update task fields.

        Args:
            task_id: Task ID.
            title: New title (optional).
            description: New description (optional).
            status: New task status (optional).
            deadline: New deadline (optional).

        Returns:
            Updated Task instance.
        """
        task = self.task_repo.get_task_by_id(task_id)

        if title is not None:
            task.title = title

        if description is not None:
            task.description = description

        if status is not None:
            task.status = status

        if deadline is not None:
            task.deadline = deadline

        return self.task_repo.update_task(task)

    def update_status(self, task_id: str, new_status: str) -> Task:
        """
        Update the status of a task.

        Args:
            task_id: The ID of the task.
            new_status: The new status to set.

        Returns:
            The updated Task instance.

        Raises:
            Exception: If the task does not exist.
        """
        task = self.task_repo.get_task_by_id(task_id)
        if not task:
            raise Exception(f"Task with ID '{task_id}' not found.")

        return self.task_repo.update_task_status(task, new_status)

    # -----------------------------
    # DELETE
    # -----------------------------
    def delete_task(self, task_id: str) -> None:
        """
        Delete a task by ID.

        Args:
            task_id: The ID of the task to delete.
        """
        task = self.task_repo.get_task_by_id(task_id)
        self.task_repo.delete_task(task)
