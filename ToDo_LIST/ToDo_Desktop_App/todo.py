import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import datetime
import os

TASK_FILE = "tasks.json"
tasks = []

# --- Data Functions ---

def save_tasks():
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def load_tasks():
    global tasks
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            tasks = json.load(file)
    else:
        tasks = []

# --- GUI Functions ---

def refresh_task_list():
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "✔️" if task["status"] == "Done" else "⏳"
        display = f"{i+1}. {status} {task['task']} ({task['created']})"
        task_listbox.insert(tk.END, display)

def add_task():
    task_text = task_entry.get().strip()
    if task_text:
        new_task = {
            "task": task_text,
            "status": "Pending",
            "created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        tasks.append(new_task)
        save_tasks()
        refresh_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        task = tasks.pop(index)
        save_tasks()
        refresh_task_list()
        messagebox.showinfo("Deleted", f"Deleted: {task['task']}")
    else:
        messagebox.showwarning("Select Task", "No task selected.")

def mark_done():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        if tasks[index]["status"] == "Pending":
            tasks[index]["status"] = "Done"
            save_tasks()
            refresh_task_list()
        else:
            messagebox.showinfo("Already Done", "Task is already marked as done.")
    else:
        messagebox.showwarning("Select Task", "No task selected.")

def clear_all():
    confirm = messagebox.askyesno("Confirm", "Delete all tasks?")
    if confirm:
        tasks.clear()
        save_tasks()
        refresh_task_list()

# --- GUI Setup ---

root = tk.Tk()
root.title("📝 Enhanced To-Do List")
root.geometry("500x400")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()

task_listbox = tk.Listbox(root, width=70, height=12)
task_listbox.pack(pady=10)

done_btn = tk.Button(root, text="Mark as Done", command=mark_done)
done_btn.pack(pady=5)

del_btn = tk.Button(root, text="Delete Task", command=delete_task)
del_btn.pack(pady=5)

clear_btn = tk.Button(root, text="Clear All Tasks", command=clear_all)
clear_btn.pack(pady=5)

# --- Load & Start ---

load_tasks()
refresh_task_list()

root.mainloop()
