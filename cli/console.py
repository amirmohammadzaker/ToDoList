# app/cli/console.py

class TaskCLI:
    def __init__(self, project_service, task_service):
        """
        Dependency Injection: سرویس‌ها از بیرون به CLI داده می‌شوند.
        """
        self.project_service = project_service
        self.task_service = task_service

    # ====================== Project Commands ======================
    def create_project(self):
        name = input("Project name: ").strip()
        description = input("Project description (optional): ").strip()
        try:
            project = self.project_service.create_project(name, description)
            print(f"✅ Project '{project.name}' created successfully.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def list_projects(self):
        try:
            projects = self.project_service.list_projects()
            if not projects:
                print("⚠️ No projects found.")
                return
            for project in projects:
                print(f"ID: {project.id}\nName: {project.name}\nDescription: {project.description}\n")
        except Exception as e:
            print(f"❌ Error: {e}")

    def edit_project(self):
        project_id = input("Project ID: ").strip()
        new_name = input("New project name (leave blank to skip): ").strip() or None
        new_description = input("New description (leave blank to skip): ").strip() or None
        try:
            self.project_service.edit_project(project_id, new_name, new_description)
            print("✅ Project updated successfully.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def delete_project(self):
        project_id = input("Project ID: ").strip()
        try:
            self.project_service.delete_project(project_id)
            print("✅ Project deleted successfully.")
        except Exception as e:
            print(f"❌ Error: {e}")

    # ====================== Task Commands ======================
    def add_task(self):
        project_id = input("Project ID: ").strip()
        title = input("Task title: ").strip()
        description = input("Task description (optional): ").strip()
        deadline = input("Deadline (YYYY-MM-DD, optional): ").strip() or None
        try:
            task = self.task_service.create_task(project_id, title, description, deadline)
            print(f"✅ Task '{task.title}' added to project {project_id}.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def list_tasks(self):
        project_id = input("Project ID: ").strip()
        try:
            tasks = self.task_service.list_tasks(project_id)
            if not tasks:
                print("⚠️ No tasks found.")
                return
            for task in tasks:
                deadline = task.deadline if task.deadline else "None"
                print(f"ID: {task.id}\nTitle: {task.title}\nDescription: {task.description}\nStatus: {task.status}\nDeadline: {deadline}\n")
        except Exception as e:
            print(f"❌ Error: {e}")

    def edit_task(self):
        project_id = input("Project ID: ").strip()
        task_id = input("Task ID: ").strip()
        title = input("New title (leave blank to skip): ").strip() or None
        description = input("New description (leave blank to skip): ").strip() or None
        status = input("New status (todo/doing/done, leave blank to skip): ").strip() or None
        deadline = input("New deadline (YYYY-MM-DD, leave blank to skip): ").strip() or None
        try:
            self.task_service.edit_task(project_id, task_id, title, description, status, deadline)
            print("✅ Task updated successfully.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def update_task_status(self):
        project_id = input("Project ID: ").strip()
        task_id = input("Task ID: ").strip()
        new_status = input("New status (todo/doing/done): ").strip()
        try:
            self.task_service.update_status(project_id, task_id, new_status)
            print("✅ Task status updated.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def delete_task(self):
        project_id = input("Project ID: ").strip()
        task_id = input("Task ID: ").strip()
        try:
            self.task_service.delete_task(project_id, task_id)
            print("✅ Task deleted successfully.")
        except Exception as e:
            print(f"❌ Error: {e}")
