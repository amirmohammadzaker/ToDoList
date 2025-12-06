# exceptions/service_exceptions.py

class TaskLimitReachedError(Exception):
    """Raised when the maximum number of tasks per project is exceeded."""
    pass

class ProjectLimitReachedError(Exception):
    """Raised when the maximum number of projects is exceeded."""
    pass
