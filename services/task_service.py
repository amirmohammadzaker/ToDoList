from models.task import Task, TaskError
from services.project_service import ProjectService
from typing import Optional, List

MAX_NUMBER_OF_TASK = 10

class TaskService:
    def __init__(self, project_service: ProjectService):
        self.project_service = project_service

    def create_task(self, project_id: str, title: str, description: str, deadline: Optional[str] = None) -> Task:
        project = self.project_service.get_project_by_id(project_id)
        if len(project.tasks) >= MAX_NUMBER_OF_TASK:
            raise TaskError(f"Cannot add more than {MAX_NUMBER_OF_TASK} tasks to project '{project.name}'.")
        task = Task(title, description, deadline=deadline)
        project.tasks.append(task)
        return task

    def list_tasks(self, project_id: str) -> List[Task]:
        project = self.project_service.get_project_by_id(project_id)
        return project.tasks

    def edit_task(self, project_id: str, task_id: str, title: Optional[str] = None, description: Optional[str] = None,
                  status: Optional[str] = None, deadline: Optional[str] = None):
        project = self.project_service.get_project_by_id(project_id)
        for task in project.tasks:
            if task.id == task_id:
                if title: task.title = title
                if description: task.description = description
                if status:
                    if status not in Task.VALID_STATUSES:
                        raise TaskError(f"Invalid status '{status}'. Must be one of {Task.VALID_STATUSES}.")
                    task.status = status
                if deadline: task.deadline = deadline
                return
        raise TaskError(f"Task with ID '{task_id}' not found in project '{project.name}'.")

    def update_status(self, project_id: str, task_id: str, new_status: str):
        self.edit_task(project_id, task_id, status=new_status)

    def delete_task(self, project_id: str, task_id: str):
        project = self.project_service.get_project_by_id(project_id)
        for task in project.tasks:
            if task.id == task_id:
                project.tasks.remove(task)
                return
        raise TaskError(f"Task with ID '{task_id}' not found in project '{project.name}'.")
