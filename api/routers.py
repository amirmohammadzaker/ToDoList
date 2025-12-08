# TODOLIST/api/routers.py
from fastapi import APIRouter
from .controllers import project_controller, task_controller

api_router = APIRouter(prefix="/api/v1")

# Register Project Router
api_router.include_router(
    project_controller.router,
    prefix="/projects",
    tags=["Projects"]
)

# Register Task Router
api_router.include_router(
    task_controller.router,
    prefix="/tasks",
    tags=["Tasks"]
)
