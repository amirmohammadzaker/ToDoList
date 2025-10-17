import os
import uuid
from datetime import datetime
from typing import ClassVar, List

from dotenv import load_dotenv
from models.task import Task, TaskError

load_dotenv()

MAX_NUMBER_OF_PROJECT = int(os.getenv("MAX_NUMBER_OF_PROJECT", 5))
MAX_NUMBER_OF_TASK = int(os.getenv("MAX_NUMBER_OF_TASK", 10))


class ProjectError(Exception):
    pass


class Project:
    _all_projects: ClassVar[List["Project"]] = []

    def __init__(self, name: str, description: str):
        if len(Project._all_projects) >= MAX_NUMBER_OF_PROJECT:
            raise ProjectError(f"Cannot create more than {MAX_NUMBER_OF_PROJECT} projects.")

        if len(name.split()) > 30:
            raise ProjectError("Project name must be less than 30 words.")

        if len(description.split()) > 150:
            raise ProjectError("Project description must be less than 150 words.")

        if any(p.name == name for p in Project._all_projects):
            raise ProjectError(f"A project with the name '{name}' already exists.")

        self.id: str = str(uuid.uuid4())[:6]  # First 6 characters of UUID as short ID
        self.name: str = name
        self.description: str = description
        self.tasks: List[Task] = []

        Project._all_projects.append(self)

    def add_task(self, task: Task) -> str:
        if len(self.tasks) >= MAX_NUMBER_OF_TASK:
            raise ProjectError(f"Cannot add more than {MAX_NUMBER_OF_TASK} tasks to project '{self.name}'.")
        self.tasks.append(task)
        return f"✅ Task '{task.title}' added successfully to project '{self.name}'."

    def update_task_status(self, task_id: str, new_status: str) -> str:
        VALID_STATUSES = {"todo", "doing", "done"}
        if new_status not in VALID_STATUSES:
            raise TaskError(f"Invalid status '{new_status}'. Must be one of {VALID_STATUSES}.")

        for task in self.tasks:
            if task.id == task_id:
                task.status = new_status
                return f"✅ Status of task '{task.title}' updated to '{new_status}'."

        raise TaskError(f"Task with id '{task_id}' not found in project '{self.name}'.")

    def edit_task(
        self,
        task_id: str,
        title: str = None,
        description: str = None,
        status: str = None,
        deadline: str = None,
    ) -> str:

        for task in self.tasks:
            if task.id == task_id:
                # Update title
                if title is not None:
                    if len(title.split()) > 30:
                        raise TaskError("Task title cannot exceed 30 words.")
                    task.title = title

                # Update description
                if description is not None:
                    if len(description.split()) > 150:
                        raise TaskError("Task description cannot exceed 150 words.")
                    task.description = description

                # Update status
                if status is not None:
                    if status not in Task.VALID_STATUSES:
                        raise TaskError(f"Invalid status '{status}'. Must be one of {Task.VALID_STATUSES}.")
                    task.status = status

                # Update deadline
                if deadline is not None:
                    try:
                        datetime.strptime(deadline, "%Y-%m-%d")
                    except ValueError:
                        raise TaskError("Deadline must be a valid date in YYYY-MM-DD format.")
                    task.deadline = deadline

                return f"✅ Task '{task.title}' updated successfully."

        raise TaskError(f"Task with id '{task_id}' not found in project '{self.name}'.")

    def delete_task(self, task_id: str) -> str:
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return f"✅ Task '{task.title}' successfully deleted from project '{self.name}'."

        return f"❌ Error: Task with id '{task_id}' not found in project '{self.name}'."

    @classmethod
    def get_all_projects(cls) -> List["Project"]:
        return cls._all_projects

    @classmethod
    def list_projects(cls) -> str:
        if not cls._all_projects:
            return "⚠️ No projects exist."

        output = []
        for project in cls._all_projects:
            output.append(
                f"ID: {project.id}\nName: {project.name}\nDescription: {project.description}\n"
            )
        return "\n".join(output)

    def update_name(self, new_name: str):
        if any(p.name == new_name and p is not self for p in Project._all_projects):
            raise ProjectError(f"A project with the name '{new_name}' already exists.")
        self.name = new_name

    def update_description(self, new_description: str):
        if len(new_description.split()) < 30 or len(new_description) < 150:
            raise ProjectError("Project description must be at least 30 words and 150 characters.")
        self.description = new_description

    def delete_project(self) -> str:
        try:
            self.tasks.clear()
            Project._all_projects.remove(self)
            return f"✅ Project '{self.name}' and its tasks were successfully deleted."
        except ValueError:
            return f"❌ Error: Project '{self.name}' was not found."

    def list_tasks(self) -> str:
        if not self.tasks:
            return f"⚠️ Project '{self.name}' has no tasks."

        output = []
        for task in self.tasks:
            deadline = task.deadline if task.deadline else "None"
            output.append(
                f"ID: {task.id}\n"
                f"Title: {task.title}\n"
                f"Description: {task.description}\n"
                f"Status: {task.status}\n"
                f"Deadline: {deadline}\n"
            )
        return "\n".join(output)

    def __repr__(self) -> str:
        return f"<Project id={self.id} name={self.name} tasks={len(self.tasks)}>"
