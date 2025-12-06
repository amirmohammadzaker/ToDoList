# app/repositories/project_repository.py
from typing import List, Optional
from sqlalchemy.orm import Session
from models.project import Project as ProjectModel

class ProjectRepository:
    """Repository for Project entity, handles database CRUD operations."""

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_project(self, project: ProjectModel) -> ProjectModel:
        """Add a new project to the database."""
        self.db_session.add(project)
        self.db_session.commit()
        self.db_session.refresh(project)
        return project

    def get_project_by_id(self, project_id: str) -> Optional[ProjectModel]:
        """Retrieve a project by its ID."""
        return self.db_session.query(ProjectModel).filter(ProjectModel.id == project_id).first()

    def list_projects(self) -> List[ProjectModel]:
        """Retrieve all projects."""
        return self.db_session.query(ProjectModel).all()


    def update_project(self, project: ProjectModel) -> ProjectModel:
        """Update a project in the database."""
        self.db_session.commit()
        self.db_session.refresh(project)
        return project

    def delete_project(self, project: ProjectModel) -> None:
        """Delete a project from the database."""
        self.db_session.delete(project)
        self.db_session.commit()
