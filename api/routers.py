from fastapi import APIRouter
from .controllers import projects_controller, tasks_controller

api_router: APIRouter = APIRouter(prefix="/api/v1")
"""
Main API router that includes all sub-routers for the application.
"""

# Register Project Router
api_router.include_router(
    projects_controller.router,
    prefix="/projects",
    tags=["Projects"]
)

# Register Task Router
api_router.include_router(
    tasks_controller.router,
    prefix="/tasks",
    tags=["Tasks"]
)
