import schedule
import time
from services.task_service import TaskService
from repositories.task_repository import TaskRepository
from repositories.project_repository import ProjectRepository
from db.session import SessionLocal
from datetime import datetime

# نمونه‌سازی Repository و Service
db_session = SessionLocal()
project_repo = ProjectRepository(db_session)
task_repo = TaskRepository(db_session)
task_service = TaskService(task_repo, project_repo)

def close_overdue_tasks():
    tasks = task_repo.list_all_overdue(datetime.now())  # فرض: تابعی در repo که تسک‌های منقضی را برمی‌گرداند
    for task in tasks:
        task.status = "done"
        task_repo.update(task)
    print(f"✅ {len(tasks)} overdue tasks updated at {datetime.now()}")

# زمان‌بندی
schedule.every().day.at("02:00").do(close_overdue_tasks)  # هر روز ساعت ۲ صبح
schedule.every(15).minutes.do(close_overdue_tasks)        # هر ۱۵ دقیقه هم بررسی شود

print("⏱ Scheduler started")
while True:
    schedule.run_pending()
    time.sleep(900)  # هر ۱۵ دقیقه بررسی می‌کند
