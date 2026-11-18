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
    raw = input("Task ID(s) to complete (e.g. 1 or 1,3): ")
    for part in raw.split(","):
        part = part.strip()
        if not part.isdigit():
            print(f"Skipped '{part}': not a valid ID.")
            continue
        try:
            task = manager.complete_task(int(part))
        except ValueError as error:
            print(f"Error: {error}")
            continue
        print(f"Task {part} completed." if task else f"Task {part} not found.")


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