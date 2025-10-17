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
        
        self.id = str(uuid.uuid4())  
        self.name = name
        self.description = description
        self.tasks = []  
        
        Project._all_projects.append(self)
    
    @classmethod
    def get_all_projects(cls):
        return cls._all_projects
    
    def __repr__(self):
        return f"<Project id={self.id} name={self.name} tasks={len(self.tasks)}>"
