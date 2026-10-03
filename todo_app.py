tasks = []


def find_task(name):
    """Return the task dict matching the name (case-insensitive), or None."""
    for task in tasks:
        if task["name"].lower() == name.lower():
            return task
    return None


def get_name(prompt):
    """Ask for a task name and reject empty input."""
    name = input(prompt).strip()
    if name == "":
        print("Task name cannot be empty.")
        return None
    return name


def add_task():
    name = get_name("Enter task name: ")
    if name is None:
        return
    if find_task(name):
        print("This task already exists.")
        return
    tasks.append({"name": name, "status": "Pending"})
    print(f"Task '{name}' added.")


def show_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']} [{task['status']}]")


def search_task():
    name = get_name("Enter task name to search: ")
    if name is None:
        return
    task = find_task(name)
    if task:
        print(f"Found: {task['name']} [{task['status']}]")
    else:
        print("Task not found.")


def mark_task_done():
    name = get_name("Enter task name to mark as done: ")
    if name is None:
        return
    task = find_task(name)
    if task:
        task["status"] = "Done"
        print(f"Task '{task['name']}' marked as Done.")
    else:
        print("Task not found.")


def remove_task():
    name = get_name("Enter task name to remove: ")
    if name is None:
        return
    task = find_task(name)
    if task:
        tasks.remove(task)
        print(f"Task '{task['name']}' removed.")
    else:
        print("Task not found.")


def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Search Task")
    print("4. Mark Task as Done")
    print("5. Remove Task")
    print("6. Exit")


def main():
    while True:
        show_menu()
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            add_task()
        elif choice == 2:
            show_tasks()
        elif choice == 3:
            search_task()
        elif choice == 4:
            mark_task_done()
        elif choice == 5:
            remove_task()
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose a number between 1 and 6.")


main()
