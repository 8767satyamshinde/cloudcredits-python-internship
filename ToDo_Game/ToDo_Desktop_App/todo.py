tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Save Tasks")
    print("5. Load Tasks")
    print("6. Exit")

def show_tasks():
    if not tasks:
        print("No tasks added yet.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def remove_task():
    show_tasks()
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks saved to tasks.txt")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
        print("Tasks loaded from tasks.txt")
    except FileNotFoundError:
        print("No saved tasks found.")

# Main loop
load_tasks()
while True:
    show_menu()
    choice = input("Choose an option (1–6): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        save_tasks()
    elif choice == "5":
        load_tasks()
    elif choice == "6":
        print("Exiting To-Do App. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
