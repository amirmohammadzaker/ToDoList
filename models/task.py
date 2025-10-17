from datetime import datetime
import uuid

class TaskError(Exception):
    pass

class Task:
    VALID_STATUSES = {"todo", "doing", "done"}

    def __init__(self, title: str, description: str, status: str = "todo", deadline: str = None):
        
        if len(title.split()) > 30:
            raise TaskError("Task title cannot exceed 30 words.")
        
        
        if len(description.split()) > 150:
            raise TaskError("Task description cannot exceed 150 words.")

        
        if status not in Task.VALID_STATUSES:
            raise TaskError(f"Invalid status '{status}'. Must be one of {Task.VALID_STATUSES}.")

        
        if deadline:
            try:
                datetime.strptime(deadline, "%Y-%m-%d")
            except ValueError:
                raise TaskError("Deadline must be a valid date in YYYY-MM-DD format.")

        self.short_id = str(uuid.uuid4())[:6]  # 6 کاراکتر اول UUID به عنوان شناسه کوتاه
        self.title = title
        self.description = description
        self.status = status
        self.deadline = deadline

    def __repr__(self):
        return f"<Task id={self.id} title={self.title} status={self.status}>"
