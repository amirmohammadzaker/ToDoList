from typing import ClassVar, List
import uuid

MAX_NUMBER_OF_PROJECT = 5  # حداکثر تعداد پروژه‌ها

class ProjectError(Exception):
    pass

class Project:
    _all_projects: ClassVar[List["Project"]] = []

    def __init__(self, name: str, description: str):
        if len(Project._all_projects) >= MAX_NUMBER_OF_PROJECT:
            raise ProjectError(f"Cannot create more than {MAX_NUMBER_OF_PROJECT} projects.")
        
        if len(description.split()) < 30 or len(description) < 150:
            raise ProjectError("Project description must be at least 30 words and 150 characters.")
        
        if any(p.name == name for p in Project._all_projects):
            raise ProjectError(f"A project with the name '{name}' already exists.")
        
        self.id = str(uuid.uuid4())  
        self.name = name
        self.description = description
        self.tasks = []  
        
        Project._all_projects.append(self)
    
    @classmethod
    def get_all_projects(cls):
        return cls._all_projects
    
    def update_name(self, new_name: str):
        if any(p.name == new_name and p is not self for p in Project._all_projects):
            raise ProjectError(f"A project with the name '{new_name}' already exists.")
        self.name = new_name
    
    def update_description(self, new_description: str):
        if len(new_description.split()) < 30 or len(new_description) < 150:
            raise ProjectError("Project description must be at least 30 words and 150 characters.")
        self.description = new_description
    
    def __repr__(self):
        return f"<Project id={self.id} name={self.name} tasks={len(self.tasks)}>"
