tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Save Tasks")
    print("5. Load Tasks")
    print("6. Clear All Tasks")
    print("7. Exit")

def show_tasks():
    if not tasks:
        print("No tasks added yet.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print("✅ Task added!")
    else:
        print("⚠️ Empty task not allowed.")

def remove_task():
    show_tasks()
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"🗑️ Removed: {removed}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Enter a valid number.")

def save_tasks():
    try:
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
        print("💾 Tasks saved to tasks.txt")
    except Exception as e:
        print(f"⚠️ Error saving tasks: {e}")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            loaded_tasks = [line.strip() for line in file]
        tasks.clear()
        tasks.extend(loaded_tasks)
        print("📂 Tasks loaded from tasks.txt")
    except FileNotFoundError:
        print("⚠️ No saved tasks found.")

def clear_all_tasks():
    confirm = input("Are you sure you want to delete all tasks? (yes/no): ").lower()
    if confirm == "yes":
        tasks.clear()
        print("🧹 All tasks cleared.")
    else:
        print("Cancelled.")

# Main loop
load_tasks()

while True:
    show_menu()
    choice = input("Choose an option (1–7): ")

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
        clear_all_tasks()
    elif choice == "7":
        print("👋 Exiting To-Do App. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Try again.")
