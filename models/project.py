from typing import ClassVar, List
import uuid
from task import Task, TaskError 
MAX_NUMBER_OF_PROJECT = 5   # حداکثر پروژه‌ها
MAX_NUMBER_OF_TASK = 10     # حداکثر تسک‌ها در هر پروژه

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

    def add_task(self, task):
        if len(self.tasks) >= MAX_NUMBER_OF_TASK:
            raise ProjectError(f"Cannot add more than {MAX_NUMBER_OF_TASK} tasks to project '{self.name}'.")
        self.tasks.append(task)
        return f"✅ Task '{task.title}' added successfully to project '{self.name}'."

    def update_task_status(self, task_id: str, new_status: str):
        VALID_STATUSES = {"todo", "doing", "done"}
        if new_status not in VALID_STATUSES:
            raise TaskError(f"Invalid status '{new_status}'. Must be one of {VALID_STATUSES}.")
        
        for task in self.tasks:
            if task.id == task_id:
                task.status = new_status
                return f"✅ Status of task '{task.title}' updated to '{new_status}'."
        
        raise TaskError(f"Task with id '{task_id}' not found in project '{self.name}'.")
    
    # ویرایش تسک
    def edit_task(self, task_id: str, title: str = None, description: str = None, 
                status: str = None, deadline: str = None):
        from task import TaskError  # اگر TaskError جداست

        # پیدا کردن تسک با id
        for task in self.tasks:
            if task.id == task_id:
                # تغییر عنوان
                if title is not None:
                    if len(title.split()) > 30:
                        raise TaskError("Task title cannot exceed 30 words.")
                    task.title = title

                # تغییر توضیح
                if description is not None:
                    if len(description.split()) > 150:
                        raise TaskError("Task description cannot exceed 150 words.")
                    task.description = description

                # تغییر وضعیت
                if status is not None:
                    if status not in Task.VALID_STATUSES:
                        raise TaskError(f"Invalid status '{status}'. Must be one of {Task.VALID_STATUSES}.")
                    task.status = status

                # تغییر ددلاین
                if deadline is not None:
                    try:
                        from datetime import datetime
                        datetime.strptime(deadline, "%Y-%m-%d")
                    except ValueError:
                        raise TaskError("Deadline must be a valid date in YYYY-MM-DD format.")
                    task.deadline = deadline

                return f"✅ Task '{task.title}' updated successfully."

        raise TaskError(f"Task with id '{task_id}' not found in project '{self.name}'.")
        
    

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

    def delete_project(self):
        try:
            self.tasks.clear()
            Project._all_projects.remove(self)
            return f"✅ Project '{self.name}' and its tasks were successfully deleted."
        except ValueError:
            return f"❌ Error: Project '{self.name}' was not found."
        
    def __repr__(self):
        return f"<Project id={self.id} name={self.name} tasks={len(self.tasks)}>"
