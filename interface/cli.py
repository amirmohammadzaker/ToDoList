# interface/cli.py
from models.project import Project, ProjectError
from models.task import Task, TaskError


def create_project():
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


def show_projects():
    print(Project.list_projects())


def add_task_to_project():
    project_id = input("Project ID: ").strip()
    project = next((p for p in Project.get_all_projects() if p.id == project_id), None)
    if not project:
        print(f"❌ No project found with ID '{project_id}'.")
        return

    title = input("Task title: ").strip()
    description = input("Task description: ").strip()
    deadline = input("Deadline (YYYY-MM-DD) or leave blank: ").strip() or None

    try:
        task = Task(title, description, deadline=deadline)
        print(project.add_task(task))
    except (TaskError, ProjectError) as e:
        print(f"❌ Error: {e}")


def list_tasks_of_project():
    project_id = input("Project ID: ").strip()
    project = next((p for p in Project.get_all_projects() if p.id == project_id), None)
    if not project:
        print(f"❌ No project found with ID '{project_id}'.")
        return

    print(project.list_tasks())


def edit_task_in_project():
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


def update_task_status():
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


def delete_task_from_project():
    project_id = input("Project ID: ").strip()
    project = next((p for p in Project.get_all_projects() if p.id == project_id), None)
    if not project:
        print(f"❌ No project found with ID '{project_id}'.")
        return

    task_id = input("Task ID: ").strip()
    print(project.delete_task(task_id))


def delete_project():
    project_id = input("Project ID: ").strip()
    project = next((p for p in Project.get_all_projects() if p.id == project_id), None)
    if not project:
        print(f"❌ No project found with ID '{project_id}'.")
        return

    print(project.delete_project())

def edit_project():
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
