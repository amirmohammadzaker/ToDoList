"""
Main entry point for the Project and Task Manager CLI.

Provides a command-line interface for creating and managing projects and tasks.
Users can create projects, add tasks, edit tasks, update statuses, and delete projects/tasks.
"""

from interface.cli import (
    create_project,
    show_projects,
    add_task_to_project,
    list_tasks_of_project,
    edit_task_in_project,
    update_task_status,
    delete_task_from_project,
    delete_project,
    edit_project,
)


def main() -> None:
    """
    Display the main menu and handle user input for project and task management.

    The menu allows users to:
        1. Create a new project
        2. Show all projects
        3. Add a task to a project
        4. Show tasks of a project
        5. Edit a task
        6. Update task status
        7. Delete a task
        8. Edit a project
        9. Delete a project
        10. Exit the program

    Loops until the user chooses to exit.
    """
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
            create_project()
        elif choice == "2":
            show_projects()
        elif choice == "3":
            add_task_to_project()
        elif choice == "4":
            list_tasks_of_project()
        elif choice == "5":
            edit_task_in_project()
        elif choice == "6":
            update_task_status()
        elif choice == "7":
            delete_task_from_project()
        elif choice == "8":
            edit_project()
        elif choice == "9":
            delete_project()
        elif choice == "10":
            print("👋 Exiting the program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
