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
        title (str): Title of the task (max 30 words).
        description (str): Description of the task (max 150 words).
        status (str): Current status of the task ("todo", "doing", "done").
        deadline (Optional[str]): Optional deadline in YYYY-MM-DD format.

    Class Attributes:
        VALID_STATUSES (set): Set of valid statuses.
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
            title (str): Task title (max 30 words).
            description (str): Task description (max 150 words).
            status (str, optional): Task status. Defaults to "todo".
            deadline (Optional[str], optional): Deadline in YYYY-MM-DD format. Defaults to None.

        Raises:
            TaskError: If title or description exceeds limits, status is invalid, or deadline format is invalid.
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

        self.id: str = str(uuid.uuid4())[:6]  # First 6 characters of UUID as short ID
        self.title: str = title
        self.description: str = description
        self.status: str = status
        self.deadline: Optional[str] = deadline

    def __repr__(self) -> str:
        """
        Return a concise string representation of the task.

        Returns:
            str: String showing task id, title, and status.
        """
        return f"<Task id={self.id} title={self.title} status={self.status}>"
