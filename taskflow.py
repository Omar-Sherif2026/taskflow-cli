PENDING = "Pending"
DONE = "Done"

task_list = []


def ask_text(message):
    """Keep asking until the user types something that is not blank."""
    while True:
        text = input(message).strip()
        if text:
            return text
        print("Error: input cannot be empty. Try again.")


def locate(title):
    """Return the position of a task in the list, or -1 if it is missing."""
    for position in range(len(task_list)):
        if task_list[position]["name"].lower() == title.lower():
            return position
    return -1


def add_task():
    title = ask_text("New task name: ")
    if locate(title) != -1:
        print(f"'{title}' is already in your list.")
        return
    task_list.append({"name": title, "status": PENDING})
    print(f"Added '{title}' (Pending).")


def show_tasks():
    if len(task_list) == 0:
        print("Your list is empty. Add a task first.")
        return
    print("\nNo.  Task                          Status")
    print("-" * 46)
    number = 1
    for task in task_list:
        print(f"{number:<4} {task['name']:<30}{task['status']}")
        number += 1


def search_task():
    title = ask_text("Search for: ")
    position = locate(title)
    if position == -1:
        print("Task not found.")
    else:
        found = task_list[position]
        print(f"Found -> {found['name']} | {found['status']}")


def mark_task_done():
    title = ask_text("Which task is finished? ")
    position = locate(title)
    if position == -1:
        print("Task not found.")
    elif task_list[position]["status"] == DONE:
        print("That task is already marked as Done.")
    else:
        task_list[position]["status"] = DONE
        print(f"Great job! '{task_list[position]['name']}' is now Done.")


def remove_task():
    title = ask_text("Task to delete: ")
    position = locate(title)
    if position == -1:
        print("Task not found.")
    else:
        removed = task_list.pop(position)
        print(f"Deleted '{removed['name']}'.")


def print_menu():
    print("\n===== TASKFLOW =====")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Search Task")
    print("4. Mark Task as Done")
    print("5. Remove Task")
    print("6. Exit")


def read_choice():
    """Return a valid menu number (1-6) or None if the input is bad."""
    raw = input("Choose an option: ")
    try:
        number = int(raw)
    except ValueError:
        print("Please enter a number, not text.")
        return None
    if number < 1 or number > 6:
        print("Option must be between 1 and 6.")
        return None
    return number


def run():
    running = True
    while running:
        print_menu()
        choice = read_choice()

        if choice is None:
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
        else:
            print("Goodbye!")
            running = False


run()
