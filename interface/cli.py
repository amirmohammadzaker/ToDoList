from typing import Optional

from models.project import Project, ProjectError
from models.task import Task, TaskError


def create_project() -> None:
    """
    Prompt the user to create a new project by entering a name and optional description.

    Validates input and handles ProjectError if creation fails.
    """
    while True:
        name = input("Project name: ").strip()
        if not name:
            print("❌ Project name is required. Please enter a name.")
            continue
        break

    description = input("Project description (optional): ").strip()

    try:
        project = Project(name, description)
        print(f"✅ Project '{name}' has been created successfully.")
    except ProjectError as e:
        print(f"❌ Error: {e}")


def show_projects() -> None:
    """
    Display a list of all existing projects with their ID, name, and description.
    """
    print(Project.list_projects())


def add_task_to_project() -> None:
    """
    Prompt the user to add a task to an existing project.

    Requests project ID, task title, optional description, and optional deadline.
    Handles TaskError or ProjectError if adding fails.
    """
    project_id = input("Project ID: ").strip()
    project = next((p for p in Project.get_all_projects() if p.id == project_id), None)
    if not project:
        print(f"❌ No project found with ID '{project_id}'.")
        return

    while True:
        title = input("Task title: ").strip()
        if not title:
            print("❌ Task title is required. Please enter a title.")
            continue
        break

    description = input("Task description (optional): ").strip()
    deadline = input("Deadline (YYYY-MM-DD) or leave blank: ").strip() or None

    try:
        task = Task(title, description, deadline=deadline)
        print(project.add_task(task))
    except (TaskError, ProjectError) as e:
        print(f"❌ Error: {e}")


def list_tasks_of_project() -> None:
    """
    Display all tasks of a specific project identified by project ID.

    If project not found, prints an error message.
    """
    project_id = input("Project ID: ").strip()
    project = next((p for p in Project.get_all_projects() if p.id == project_id), None)
    if not project:
        print(f"❌ No project found with ID '{project_id}'.")
        return

    print(project.list_tasks())


def edit_task_in_project() -> None:
    """
    Edit an existing task in a project.

    Prompts for project ID, task ID, and new task details (title, description, status, deadline).
    Handles TaskError if editing fails.
    """
    project_id = input("Project ID: ").strip()
    project = next((p for p in Project.get_all_projects() if p.id == project_id), None)
    if not project:
        print(f"❌ No project found with ID '{project_id}'.")
        return

    task_id = input("Task ID: ").strip()
    title = input("New title (or leave blank): ").strip() or None
    description = input("New description (or leave blank): ").strip() or None
    status = input("New status (todo/doing/done) or leave blank: ").strip() or None
    deadline = input("New deadline (YYYY-MM-DD) or leave blank: ").strip() or None

    try:
        print(project.edit_task(task_id, title, description, status, deadline))
    except TaskError as e:
        print(f"❌ Error: {e}")


def update_task_status() -> None:
    """
    Update the status of a specific task in a project.

    Prompts for project ID, task ID, and new status.
    Handles TaskError if update fails.
    """
    project_id = input("Project ID: ").strip()
    project = next((p for p in Project.get_all_projects() if p.id == project_id), None)
    if not project:
        print(f"❌ No project found with ID '{project_id}'.")
        return

    task_id = input("Task ID: ").strip()
    new_status = input("New status (todo/doing/done): ").strip()

    try:
        print(project.update_task_status(task_id, new_status))
    except TaskError as e:
        print(f"❌ Error: {e}")


def delete_task_from_project() -> None:
    """
    Delete a specific task from a project.

    Prompts for project ID and task ID. Prints success or error message.
    """
    project_id = input("Project ID: ").strip()
    project = next((p for p in Project.get_all_projects() if p.id == project_id), None)
    if not project:
        print(f"❌ No project found with ID '{project_id}'.")
        return

    task_id = input("Task ID: ").strip()
    print(project.delete_task(task_id))


def delete_project() -> None:
    """
    Delete an entire project and all its tasks.

    Prompts for project ID. Prints success or error message.
    """
    project_id = input("Project ID: ").strip()
    project = next((p for p in Project.get_all_projects() if p.id == project_id), None)
    if not project:
        print(f"❌ No project found with ID '{project_id}'.")
        return

    print(project.delete_project())


def edit_project() -> None:
    """
    Edit the name and/or description of a project.

    Prompts for project ID and new name/description. Handles ProjectError if update fails.
    """
    project_id = input("Project ID: ").strip()
    project = next((p for p in Project.get_all_projects() if p.id == project_id), None)
    if not project:
        print(f"❌ Project with ID '{project_id}' not found.")
        return

    new_name = input("New project name (leave empty to skip): ").strip() or None
    new_description = input("New project description (leave empty to skip): ").strip() or None

    try:
        if new_name:
            project.update_name(new_name)
        if new_description:
            project.update_description(new_description)
        print(f"✅ Project '{project.name}' updated successfully.")
    except ProjectError as e:
        print(f"❌ Error: {e}")
