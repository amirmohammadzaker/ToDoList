from cli.console import TaskCLI
from services.project_service import ProjectService
from services.task_service import TaskService

def main() -> None:
    # نمونه‌سازی Serviceها
    project_service = ProjectService()
    task_service = TaskService(project_service)
    # نمونه‌سازی CLI
    cli = TaskCLI(project_service, task_service)

    print("📋 Welcome to the Project and Task Manager")

    while True:
        print("1. Create a new project")
        print("2. Show all projects")
        print("3. Add a task to a project")
        print("4. Show tasks of a project")
        print("5. Edit a task")
        print("6. Update task status")
        print("7. Delete a task")
        print("8. Edit a project")
        print("9. Delete a project")
        print("10. Exit")

        choice: str = input("Your choice: ").strip()

        if choice == "1":
            cli.create_project()
        elif choice == "2":
            cli.list_projects()
        elif choice == "3":
            cli.add_task()
        elif choice == "4":
            cli.list_tasks()
        elif choice == "5":
            cli.edit_task()
        elif choice == "6":
            cli.update_task_status()
        elif choice == "7":
            cli.delete_task()
        elif choice == "8":
            cli.edit_project()
        elif choice == "9":
            cli.delete_project()
        elif choice == "10":
            print("👋 Exiting the program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
