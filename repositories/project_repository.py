from typing import List, Optional
from sqlalchemy.orm import Session
from models.project import Project as ProjectModel


class ProjectRepository:
    """
    Repository class for managing Project database operations.
    Provides CRUD operations such as create, read, update, and delete.
    """

    def __init__(self, db_session: Session) -> None:
        """
        Initialize the ProjectRepository.

        Args:
            db_session: SQLAlchemy database session.
        """
        self.db_session = db_session

    def create_project(self, project: ProjectModel) -> ProjectModel:
        """
        Add a new project to the database.

        Args:
            project: Project entity to be added.

        Returns:
            The created Project instance.
        """
        self.db_session.add(project)
        self.db_session.commit()
        self.db_session.refresh(project)
        return project

    def get_project_by_id(self, project_id: str) -> Optional[ProjectModel]:
        """
        Retrieve a project by its ID.

        Args:
            project_id: The UUID or identifier of the project.

        Returns:
            The matching Project instance, or None if not found.
        """
        return (
            self.db_session.query(ProjectModel)
            .filter(ProjectModel.id == project_id)
            .first()
        )

    def list_projects(self) -> List[ProjectModel]:
        """
        Retrieve all projects in the database.

        Returns:
            A list of all Project instances.
        """
        return self.db_session.query(ProjectModel).all()

    def update_project(self, project: ProjectModel) -> ProjectModel:
        """
        Update an existing project.

        Args:
            project: The Project instance with updated fields.

        Returns:
            The updated Project instance.
        """
        self.db_session.commit()
        self.db_session.refresh(project)
        return project

    def delete_project(self, project: ProjectModel) -> None:
        """
        Delete a project from the database.

        Args:
            project: The Project instance to remove.
        """
        self.db_session.delete(project)
        self.db_session.commit()
