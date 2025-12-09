import schedule
import time
from datetime import datetime
from typing import List

from services.task_service import TaskService
from repositories.task_repository import TaskRepository
from repositories.project_repository import ProjectRepository
from db.session import SessionLocal
from models.task import Task


# Initialize database session and repositories
db_session = SessionLocal()
project_repo = ProjectRepository(db_session)
task_repo = TaskRepository(db_session)
task_service = TaskService(task_repo, project_repo)


def close_overdue_tasks() -> None:
    """
    Mark all overdue tasks as done.

    Uses TaskRepository to fetch all overdue tasks and updates their status.
    """
    tasks: List[Task] = task_repo.list_all_overdue()  # Adjusted repo function to take no parameter
    for task in tasks:
        task.status = "done"
        task_repo.update_task(task)
    print(f"✅ {len(tasks)} overdue tasks updated at {datetime.now()}")


# Schedule tasks
schedule.every().day.at("02:00").do(close_overdue_tasks)  # Daily at 2 AM
schedule.every(15).minutes.do(close_overdue_tasks)        # Every 15 minutes

print("⏱ Scheduler started")
while True:
    schedule.run_pending()
    time.sleep(900)  # Sleep for 15 minutes
