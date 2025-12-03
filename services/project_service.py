from models.project import Project, ProjectError
from models.task import Task, TaskError
import os
from typing import List, Optional

MAX_NUMBER_OF_PROJECT = int(os.getenv("MAX_NUMBER_OF_PROJECT", 5))
MAX_NUMBER_OF_TASK = int(os.getenv("MAX_NUMBER_OF_TASK", 10))

class ProjectService:
    def __init__(self):
        self.projects: List[Project] = []

    def create_project(self, name: str, description: str) -> Project:
        if len(self.projects) >= MAX_NUMBER_OF_PROJECT:
            raise ProjectError(f"Cannot create more than {MAX_NUMBER_OF_PROJECT} projects.")
        if any(p.name == name for p in self.projects):
            raise ProjectError(f"A project with the name '{name}' already exists.")
        project = Project(name, description)
        self.projects.append(project)
        return project

    def get_project_by_id(self, project_id: str) -> Project:
        for project in self.projects:
            if project.id == project_id:
                return project
        raise ProjectError(f"Project with ID '{project_id}' not found.")

    def list_projects(self) -> List[Project]:
        return self.projects

    def edit_project(self, project_id: str, new_name: Optional[str], new_description: Optional[str]):
        project = self.get_project_by_id(project_id)
        if new_name:
            project.name = new_name
        if new_description:
            project.description = new_description

    def delete_project(self, project_id: str):
        project = self.get_project_by_id(project_id)
        self.projects.remove(project)
