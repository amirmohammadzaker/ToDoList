# services/task_service.py

import os
from typing import Optional, List

from repositories.task_repository import TaskRepository
from repositories.project_repository import ProjectRepository

from exceptions.service_exceptions import TaskLimitReachedError
from models.task import Task

MAX_NUMBER_OF_TASK = int(os.getenv("MAX_NUMBER_OF_TASK", 10))


class TaskService:
    """Application layer: Implements business logic for Tasks."""

    def __init__(self, task_repo: TaskRepository, project_repo: ProjectRepository):
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

        # 1. Ensure project exists
        project = self.project_repo.get_by_id(project_id)

        # 2. Ensure task limit per project is not exceeded
        count = self.task_repo.count_tasks_for_project(project_id)
        if count >= MAX_NUMBER_OF_TASK:
            raise TaskLimitReachedError(
                f"Cannot create more than {MAX_NUMBER_OF_TASK} tasks in this project."
            )

        # 3. Create task entity
        task = Task(
            title=title,
            description=description,
            deadline=deadline,
            project_id=project_id
        )

        # 4. Save
        return self.task_repo.add(task)

    # -----------------------------
    # READ
    # -----------------------------
    def get_task(self, task_id: str) -> Task:
        return self.task_repo.get_by_id(task_id)

    def list_tasks(self, project_id: str) -> List[Task]:
        return self.task_repo.list_all(project_id)

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

        task = self.task_repo.get_by_id(task_id)

        if title is not None:
            task.title = title

        if description is not None:
            task.description = description

        if status is not None:
            task.status = status

        if deadline is not None:
            task.deadline = deadline

        return self.task_repo.update(task)

    # -----------------------------
    # DELETE
    # -----------------------------
    def delete_task(self, task_id: str):
        task = self.task_repo.get_by_id(task_id)
        self.task_repo.delete(task)
