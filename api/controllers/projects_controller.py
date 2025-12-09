from fastapi import APIRouter, HTTPException, Depends
from typing import List, Generator
from services.project_service import ProjectService
from ..controller_schemas.requests.projects_request_schema import ProjectCreateRequest, ProjectUpdateRequest
from ..controller_schemas.responses.projects_response_schema import ProjectResponse
from models.project import ProjectError

router: APIRouter = APIRouter()
"""
Router for handling project-related API endpoints.
"""

def get_project_service() -> Generator[ProjectService, None, None]:
    """
    Dependency injection for ProjectService.

    Yields:
        An instance of ProjectService.
    """
    yield ProjectService()


# ===========================
# Routes
# ===========================

@router.get("/", response_model=List[ProjectResponse], summary="List all projects")
def list_projects(project_service: ProjectService = Depends(get_project_service)) -> List[ProjectResponse]:
    """
    Retrieve all projects.

    Args:
        project_service: ProjectService instance (injected dependency).

    Returns:
        List of projects.
    """
    return project_service.list_projects()


@router.post("/", response_model=ProjectResponse, summary="Create a new project")
def create_project(
    payload: ProjectCreateRequest,
    project_service: ProjectService = Depends(get_project_service)
) -> ProjectResponse:
    """
    Create a new project.

    Args:
        payload: ProjectCreateRequest containing name and optional description.
        project_service: ProjectService instance (injected dependency).

    Returns:
        The created project.

    Raises:
        HTTPException: If a project with the same name exists or max limit is reached.
    """
    try:
        return project_service.create_project(name=payload.name, description=payload.description)
    except ProjectError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{project_id}", response_model=ProjectResponse, summary="Update a project")
def update_project(
    project_id: str,
    payload: ProjectUpdateRequest,
    project_service: ProjectService = Depends(get_project_service)
) -> ProjectResponse:
    """
    Update a project's name and/or description.

    Args:
        project_id: ID of the project to update.
        payload: ProjectUpdateRequest containing new name and/or description.
        project_service: ProjectService instance (injected dependency).

    Returns:
        The updated project.

    Raises:
        HTTPException: If the project is not found.
    """
    try:
        return project_service.edit_project(
            project_id=project_id,
            new_name=payload.name,
            new_description=payload.description
        )
    except ProjectError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{project_id}", summary="Delete a project")
def delete_project(
    project_id: str,
    project_service: ProjectService = Depends(get_project_service)
) -> dict:
    """
    Delete a project by ID.

    Args:
        project_id: The ID of the project to delete.
        project_service: ProjectService instance (injected dependency).

    Returns:
        A success message.

    Raises:
        HTTPException: If the project is not found.
    """
    try:
        project_service.delete_project(project_id)
        return {"detail": "Project deleted successfully."}
    except ProjectError as e:
        raise HTTPException(status_code=404, detail=str(e))
