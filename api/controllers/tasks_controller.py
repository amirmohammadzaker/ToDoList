from fastapi import APIRouter, HTTPException, Depends
from typing import List, Generator
from services.task_service import TaskService
from ..controller_schemas.requests.tasks_request_schema import (
    TaskCreateRequest,
    TaskUpdateRequest,
    TaskStatusUpdateRequest
)
from ..controller_schemas.responses.tasks_response_schema import TaskResponse
from exceptions.service_exceptions import TaskLimitReachedError
from repositories.project_repository import ProjectRepository
from repositories.task_repository import TaskRepository
from db.session import SessionLocal

router: APIRouter = APIRouter()
"""
Router for handling task-related API endpoints.
"""

def get_task_service() -> Generator[TaskService, None, None]:
    """
    Dependency injection for TaskService.

    Yields:
        An instance of TaskService with repositories initialized.
    """
    db = SessionLocal()
    project_repo = ProjectRepository(db)
    task_repo = TaskRepository(db)
    yield TaskService(task_repo=task_repo, project_repo=project_repo)


# ===========================
# Routes
# ===========================

@router.get("/project/{project_id}", response_model=List[TaskResponse], summary="List all tasks for a project")
def list_tasks(
    project_id: str,
    task_service: TaskService = Depends(get_task_service)
) -> List[TaskResponse]:
    """
    Retrieve all tasks for a specific project.

    Args:
        project_id: ID of the project.
        task_service: TaskService instance (injected dependency).

    Returns:
        List of TaskResponse objects.

    Raises:
        HTTPException: If tasks cannot be retrieved.
    """
    try:
        return task_service.list_tasks(project_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/project/{project_id}", response_model=TaskResponse, summary="Create a new task for a project")
def create_task(
    project_id: str,
    payload: TaskCreateRequest,
    task_service: TaskService = Depends(get_task_service)
) -> TaskResponse:
    """
    Create a new task for a specific project.

    Args:
        project_id: ID of the project.
        payload: TaskCreateRequest containing title, optional description, and optional deadline.
        task_service: TaskService instance (injected dependency).

    Returns:
        The created task as TaskResponse.

    Raises:
        HTTPException: If task limit is exceeded or creation fails.
    """
    try:
        return task_service.create_task(
            project_id=project_id,
            title=payload.title,
            description=payload.description,
            deadline=payload.deadline
        )
    except TaskLimitReachedError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/{task_id}", response_model=TaskResponse, summary="Update a task")
def update_task(
    task_id: str,
    payload: TaskUpdateRequest,
    task_service: TaskService = Depends(get_task_service)
) -> TaskResponse:
    """
    Update a task's details.

    Args:
        task_id: ID of the task to update.
        payload: TaskUpdateRequest containing new title, description, status, and/or deadline.
        task_service: TaskService instance (injected dependency).

    Returns:
        The updated task as TaskResponse.

    Raises:
        HTTPException: If the task cannot be updated.
    """
    try:
        return task_service.update_task(
            task_id=task_id,
            title=payload.title,
            description=payload.description,
            status=payload.status,
            deadline=payload.deadline
        )
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.patch("/{task_id}/status", response_model=TaskResponse, summary="Update task status")
def update_task_status(
    task_id: str,
    payload: TaskStatusUpdateRequest,
    task_service: TaskService = Depends(get_task_service)
) -> TaskResponse:
    """
    Update only the status of a task.

    Args:
        task_id: ID of the task.
        payload: TaskStatusUpdateRequest containing the new status.
        task_service: TaskService instance (injected dependency).

    Returns:
        The updated task as TaskResponse.

    Raises:
        HTTPException: If the task status cannot be updated.
    """
    try:
        return task_service.update_status(task_id=task_id, new_status=payload.status)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{task_id}", summary="Delete a task")
def delete_task(
    task_id: str,
    task_service: TaskService = Depends(get_task_service)
) -> dict:
    """
    Delete a task by its ID.

    Args:
        task_id: ID of the task to delete.
        task_service: TaskService instance (injected dependency).

    Returns:
        A success message.

    Raises:
        HTTPException: If the task cannot be deleted.
    """
    try:
        task_service.delete_task(task_id)
        return {"detail": "Task deleted successfully."}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
