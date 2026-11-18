from task_manager import TaskManager


def show_menu():
    print("\n=== Student Task Manager ===")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def handle_add(manager):
    title = input("Task title: ")
    try:
        task = manager.add_task(title)
        print(f"Added task #{task['id']}")
    except ValueError as error:
        print(f"Error: {error}")


def handle_show(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        mark = "x" if task["completed"] else " "
        print(f"[{mark}] {task['id']}. {task['title']}")


def handle_complete(manager):
    task_id = int(input("Task ID to complete: "))
    if manager.complete_task(task_id):
        print("Task marked as completed.")
    else:
        print("Task not found.")


def handle_delete(manager):
    raw = input("Task ID to delete: ").strip()
    if not raw.isdigit():
        print("Error: ID must be a positive number.")
        return
    try:
        manager.delete_task(int(raw))
        print(f"Task {raw} deleted.")
    except ValueError as error:
        print(f"Error: {error}")

def main():
    manager = TaskManager("tasks.json")
    actions = {
        "1": handle_add,
        "2": handle_show,
        "3": handle_complete,
        "4": handle_delete,
    }
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action(manager)
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()