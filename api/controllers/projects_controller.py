# TODOLIST/api/controllers/project_controller.py
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from services.project_service import ProjectService
from ..controller_schemas.requests.projects_request_schema import ProjectCreateRequest, ProjectUpdateRequest
from ..controller_schemas.responses.projects_response_schema import ProjectResponse
from models.project import ProjectError

router = APIRouter()

# Dependency injection for ProjectService
def get_project_service():
    return ProjectService()  # خود Service SessionLocal را مدیریت می‌کند

# ===========================
# Routes
# ===========================

@router.get("/", response_model=List[ProjectResponse], summary="List all projects")
def list_projects(project_service: ProjectService = Depends(get_project_service)):
    return project_service.list_projects()


@router.post("/", response_model=ProjectResponse, summary="Create a new project")
def create_project(payload: ProjectCreateRequest, project_service: ProjectService = Depends(get_project_service)):
    try:
        return project_service.create_project(name=payload.name, description=payload.description)
    except ProjectError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{project_id}", response_model=ProjectResponse, summary="Update a project")
def update_project(
    project_id: str,
    payload: ProjectUpdateRequest,
    project_service: ProjectService = Depends(get_project_service)
):
    try:
        return project_service.edit_project(
            project_id=project_id,
            new_name=payload.name,
            new_description=payload.description
        )
    except ProjectError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{project_id}", summary="Delete a project")
def delete_project(project_id: str, project_service: ProjectService = Depends(get_project_service)):
    try:
        project_service.delete_project(project_id)
        return {"detail": "Project deleted successfully."}
    except ProjectError as e:
        raise HTTPException(status_code=404, detail=str(e))
