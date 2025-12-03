from datetime import datetime
import uuid
from typing import Optional


class TaskError(Exception):
    """Custom exception class for task-related errors."""
    pass


class Task:
    """
    Represents a task within a project.

    Attributes:
        id (str): Unique short ID for the task.
        title (str): Title of the task.
        description (str): Description of the task.
        status (str): Current status of the task ("todo", "doing", "done").
        deadline (Optional[str]): Optional deadline in YYYY-MM-DD format.
    """

    VALID_STATUSES = {"todo", "doing", "done"}

    def __init__(
        self,
        title: str,
        description: str,
        status: str = "todo",
        deadline: Optional[str] = None,
    ):
        """
        Initialize a new task.

        Args:
            title (str): Task title.
            description (str): Task description.
            status (str, optional): Task status. Defaults to "todo".
            deadline (Optional[str], optional): Deadline in YYYY-MM-DD format. Defaults to None.

        Raises:
            TaskError: If title/description exceeds limits, status invalid, or deadline format invalid.
        """
        if len(title.split()) > 30:
            raise TaskError("Task title cannot exceed 30 words.")

        if len(description.split()) > 150:
            raise TaskError("Task description cannot exceed 150 words.")

        if status not in Task.VALID_STATUSES:
            raise TaskError(
                f"Invalid status '{status}'. Must be one of {Task.VALID_STATUSES}."
            )

        if deadline:
            try:
                datetime.strptime(deadline, "%Y-%m-%d")
            except ValueError:
                raise TaskError("Deadline must be a valid date in YYYY-MM-DD format.")

        self.id: str = str(uuid.uuid4())[:6]  # Short unique ID
        self.title: str = title
        self.description: str = description
        self.status: str = status
        self.deadline: Optional[str] = deadline

    def update_title(self, new_title: str) -> None:
        if len(new_title.split()) > 30:
            raise TaskError("Task title cannot exceed 30 words.")
        self.title = new_title

    def update_description(self, new_description: str) -> None:
        if len(new_description.split()) > 150:
            raise TaskError("Task description cannot exceed 150 words.")
        self.description = new_description

    def update_status(self, new_status: str) -> None:
        if new_status not in Task.VALID_STATUSES:
            raise TaskError(
                f"Invalid status '{new_status}'. Must be one of {Task.VALID_STATUSES}."
            )
        self.status = new_status

    def update_deadline(self, new_deadline: Optional[str]) -> None:
        if new_deadline:
            try:
                datetime.strptime(new_deadline, "%Y-%m-%d")
            except ValueError:
                raise TaskError("Deadline must be a valid date in YYYY-MM-DD format.")
        self.deadline = new_deadline

    def __repr__(self) -> str:
        return f"<Task id={self.id} title={self.title} status={self.status}>"
