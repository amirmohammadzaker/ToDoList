import warnings
from typing import Optional
from services.project_service import ProjectService
from services.task_service import TaskService


class TaskCLI:
    """
    Deprecated CLI interface for managing projects and tasks.

    ⚠️ This CLI is deprecated and will be removed in a future version.
    Please use the FastAPI API endpoints instead.

    Attributes:
        project_service: ProjectService instance.
        task_service: TaskService instance.
    """

    def __init__(self, project_service: ProjectService, task_service: TaskService) -> None:
        """
        Initialize the CLI with injected service dependencies.

        Args:
            project_service: Instance of ProjectService.
            task_service: Instance of TaskService.
        """
        print(
            "⚠️ CLI interface is deprecated and will be removed in a future version. "
            "Please use the FastAPI API endpoints instead."
        )
        self.project_service = project_service
        self.task_service = task_service

    # ====================== Project Commands ======================

    def create_project(self) -> None:
        """Create a new project (Deprecated CLI)."""
        name: str = input("Project name: ").strip()
        description: Optional[str] = input("Project description (optional): ").strip() or None
        try:
            project = self.project_service.create_project(name, description)
            print(f"✅ Project '{project.name}' created successfully.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def list_projects(self) -> None:
        """List all projects (Deprecated CLI)."""
        try:
            projects = self.project_service.list_projects()
            if not projects:
                print("⚠️ No projects found.")
                return

            for p in projects:
                print(f"ID: {p.id}\nName: {p.name}\nDescription: {p.description}\n")
        except Exception as e:
            print(f"❌ Error: {e}")

    def edit_project(self) -> None:
        """Edit a project (Deprecated CLI)."""
        project_id: str = input("Project ID: ").strip()
        new_name: Optional[str] = input("New project name (leave blank to skip): ").strip() or None
        new_description: Optional[str] = input("New description (leave blank to skip): ").strip() or None

        try:
            self.project_service.edit_project(
                project_id=project_id,
                new_name=new_name,
                new_description=new_description
            )
            print("✅ Project updated successfully.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def delete_project(self) -> None:
        """Delete a project (Deprecated CLI)."""
        project_id: str = input("Project ID: ").strip()
        try:
            self.project_service.delete_project(project_id)
            print("✅ Project deleted successfully.")
        except Exception as e:
            print(f"❌ Error: {e}")

    # ====================== Task Commands ======================

    def add_task(self) -> None:
        """Add a new task to a project (Deprecated CLI)."""
        project_id: str = input("Project ID: ").strip()
        title: str = input("Task title: ").strip()
        description: Optional[str] = input("Task description (optional): ").strip() or None
        deadline: Optional[str] = input("Deadline (YYYY-MM-DD, optional): ").strip() or None

        try:
            task = self.task_service.create_task(
                project_id=project_id,
                title=title,
                description=description,
                deadline=deadline
            )
            print(f"✅ Task '{task.title}' created successfully.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def list_tasks(self) -> None:
        """List all tasks for a project (Deprecated CLI)."""
        project_id: str = input("Project ID: ").strip()
        try:
            tasks = self.task_service.list_tasks(project_id)
            if not tasks:
                print("⚠️ No tasks found for this project.")
                return

            for t in tasks:
                print(
                    f"ID: {t.id}\n"
                    f"Title: {t.title}\n"
                    f"Description: {t.description}\n"
                    f"Status: {t.status}\n"
                    f"Deadline: {t.deadline}\n"
                )

        except Exception as e:
            print(f"❌ Error: {e}")

    def edit_task(self) -> None:
        """Edit a task (Deprecated CLI)."""
        task_id: str = input("Task ID: ").strip()
        title: Optional[str] = input("New title (leave blank to skip): ").strip() or None
        description: Optional[str] = input("New description (leave blank to skip): ").strip() or None
        status: Optional[str] = input("New status (todo/doing/done, leave blank to skip): ").strip() or None
        deadline: Optional[str] = input("New deadline (YYYY-MM-DD, leave blank to skip): ").strip() or None

        try:
            self.task_service.update_task(
                task_id=task_id,
                title=title,
                description=description,
                status=status,
                deadline=deadline
            )
            print("✅ Task updated successfully.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def update_task_status(self) -> None:
        """Update task status (Deprecated CLI)."""
        task_id: str = input("Task ID: ").strip()
        new_status: str = input("New status (todo/doing/done): ").strip()
        try:
            self.task_service.update_status(task_id=task_id, new_status=new_status)
            print("✅ Task status updated successfully.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def delete_task(self) -> None:
        """Delete a task (Deprecated CLI)."""
        task_id: str = input("Task ID: ").strip()
        try:
            self.task_service.delete_task(task_id)
            print("🗑️ Task deleted successfully.")
        except Exception as e:
            print(f"❌ Error: {e}")
