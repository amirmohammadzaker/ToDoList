from typing import List, Optional
import os

from models.project import Project, ProjectError
from repositories.project_repository import ProjectRepository
from db.session import SessionLocal

MAX_NUMBER_OF_PROJECT = int(os.getenv("MAX_NUMBER_OF_PROJECT", 5))


class ProjectService:
    """
    Service layer for managing projects.
    Uses ProjectRepository for all database operations.
    """

    def __init__(self, db_session=None):
        # Use provided session or create a new one
        self.db_session = db_session or SessionLocal()
        self.project_repo = ProjectRepository(self.db_session)

    def create_project(self, name: str, description: str) -> Project:
        """
        Create a new project.

        Raises:
            ProjectError: if project limit exceeded or name already exists.
        """
        projects = self.project_repo.list_projects()
        if len(projects) >= MAX_NUMBER_OF_PROJECT:
            raise ProjectError(f"Cannot create more than {MAX_NUMBER_OF_PROJECT} projects.")

        if any(p.name == name for p in projects):
            raise ProjectError(f"A project with the name '{name}' already exists.")

        project = Project(name=name, description=description)
        return self.project_repo.create_project(project)

    def get_project_by_id(self, project_id: str) -> Project:
        """
        Get a project by its ID.

        Raises:
            ProjectError: if project not found.
        """
        project = self.project_repo.get_project_by_id(project_id)
        if not project:
            raise ProjectError(f"Project with ID '{project_id}' not found.")
        return project

    def list_projects(self) -> List[Project]:
        """
        Return all projects.
        """
        return self.project_repo.list_projects()

    def edit_project(
        self,
        project_id: str,
        new_name: Optional[str] = None,
        new_description: Optional[str] = None,
    ) -> Project:
        """
        Update a project's name and/or description.

        Raises:
            ProjectError: if project not found.
        """
        project = self.get_project_by_id(project_id)

        if new_name:
            # Check for duplicate name
            all_projects = self.project_repo.list_projects()
            if any(p.name == new_name and p.id != project_id for p in all_projects):
                raise ProjectError(f"A project with the name '{new_name}' already exists.")
            project.name = new_name

        if new_description:
            project.description = new_description

        return self.project_repo.update_project(project)

    def delete_project(self, project_id: str) -> None:
        """
        Delete a project by ID.

        Raises:
            ProjectError: if project not found.
        """
        project = self.get_project_by_id(project_id)
        self.project_repo.delete_project(project)
