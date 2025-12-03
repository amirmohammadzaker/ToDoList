import uuid
from datetime import datetime
from typing import List

from models.task import Task, TaskError


class ProjectError(Exception):
    """Custom exception class for project-related errors."""
    pass


class Project:
    """
    Represents a project containing multiple tasks.

    Attributes:
        id (str): Unique short ID for the project.
        name (str): Name of the project.
        description (str): Description of the project.
        tasks (List[Task]): List of tasks in the project.
    """

    def __init__(self, name: str, description: str):
        """
        Initialize a new project.

        Args:
            name (str): Name of the project.
            description (str): Description of the project.
        """
        self.id: str = str(uuid.uuid4())[:6]  # First 6 characters of UUID as short ID
        self.name: str = name
        self.description: str = description
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """
        Add a task to the project.

        Args:
            task (Task): Task instance to add.
        """
        self.tasks.append(task)

    def update_task_status(self, task_id: str, new_status: str) -> None:
        """
        Update the status of a task in the project.

        Args:
            task_id (str): ID of the task to update.
            new_status (str): New status ("todo", "doing", or "done").

        Raises:
            TaskError: If task not found.
        """
        for task in self.tasks:
            if task.id == task_id:
                task.status = new_status
                return
        raise TaskError(f"Task with id '{task_id}' not found in project '{self.name}'.")

    def edit_task(
        self,
        task_id: str,
        title: str = None,
        description: str = None,
        status: str = None,
        deadline: str = None,
    ) -> None:
        """
        Edit a task's details.

        Args:
            task_id (str): ID of the task to edit.
            title (str, optional): New title.
            description (str, optional): New description.
            status (str, optional): New status.
            deadline (str, optional): New deadline in YYYY-MM-DD format.

        Raises:
            TaskError: If task not found or deadline invalid.
        """
        for task in self.tasks:
            if task.id == task_id:
                if title is not None:
                    task.title = title
                if description is not None:
                    task.description = description
                if status is not None:
                    task.status = status
                if deadline is not None:
                    try:
                        datetime.strptime(deadline, "%Y-%m-%d")
                    except ValueError:
                        raise TaskError("Deadline must be a valid date in YYYY-MM-DD format.")
                    task.deadline = deadline
                return
        raise TaskError(f"Task with id '{task_id}' not found in project '{self.name}'.")

    def delete_task(self, task_id: str) -> None:
        """
        Delete a task from the project.

        Args:
            task_id (str): ID of the task to delete.

        Raises:
            TaskError: If task not found.
        """
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return
        raise TaskError(f"Task with id '{task_id}' not found in project '{self.name}'.")

    def update_name(self, new_name: str) -> None:
        """
        Update the project's name.

        Args:
            new_name (str): New name for the project.
        """
        self.name = new_name

    def update_description(self, new_description: str) -> None:
        """
        Update the project's description.

        Args:
            new_description (str): New description.
        """
        self.description = new_description

    def list_tasks(self) -> List[Task]:
        """
        Return the list of tasks in the project.

        Returns:
            List[Task]: All tasks in the project.
        """
        return self.tasks

    def __repr__(self) -> str:
        """Return a concise string representation of the project."""
        return f"<Project id={self.id} name={self.name} tasks={len(self.tasks)}>"
