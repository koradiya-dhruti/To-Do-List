FILENAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
    return tasks


# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Add a task
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")


# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


# Remove a task
def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_number = int(input("Enter task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{removed}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting To-Do App. Goodbye!")
            break
        else:
            print("Invalid choice! Please select between 1-4.")


if __name__ == "__main__":
    main()
