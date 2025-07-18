import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import datetime
import os

TASK_FILE = "tasks.json"
tasks = []
dark_mode = False

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

def refresh_task_list(filtered=None):
    task_listbox.delete(0, tk.END)
    data = filtered if filtered is not None else tasks
    for i, task in enumerate(data):
        status = "✔️" if task["status"] == "Done" else "⏳"
        priority = f"[{task.get('priority', 'Medium')}]"
        due = f"(Due: {task.get('due', 'N/A')})"
        display = f"{i+1}. {status} {priority} {task['task']} {due}"
        task_listbox.insert(tk.END, display)
    update_analytics()

def add_task():
    task_text = task_entry.get().strip()
    if task_text:
        due_date = simpledialog.askstring("Due Date", "Enter due date (YYYY-MM-DD):")
        priority = simpledialog.askstring("Priority", "Enter priority (Low/Medium/High):")
        new_task = {
            "task": task_text,
            "status": "Pending",
            "created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "due": due_date if due_date else "N/A",
            "priority": priority if priority else "Medium"
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

def edit_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        current = tasks[index]
        new_text = simpledialog.askstring("Edit Task", "Edit task name:", initialvalue=current["task"])
        new_due = simpledialog.askstring("Edit Due Date", "Edit due date (YYYY-MM-DD):", initialvalue=current.get("due", ""))
        new_priority = simpledialog.askstring("Edit Priority", "Edit priority (Low/Medium/High):", initialvalue=current.get("priority", "Medium"))
        if new_text:
            current["task"] = new_text
            current["due"] = new_due if new_due else current.get("due", "")
            current["priority"] = new_priority if new_priority else current.get("priority", "Medium")
            save_tasks()
            refresh_task_list()
    else:
        messagebox.showwarning("Select Task", "No task selected.")

def clear_all():
    confirm = messagebox.askyesno("Confirm", "Delete all tasks?")
    if confirm:
        tasks.clear()
        save_tasks()
        refresh_task_list()

def search_tasks():
    query = search_entry.get().strip().lower()
    if query:
        filtered = [task for task in tasks if query in task['task'].lower()]
        refresh_task_list(filtered)
    else:
        refresh_task_list()

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    bg = "#2e2e2e" if dark_mode else "#ffffff"
    fg = "#ffffff" if dark_mode else "#000000"
    root.config(bg=bg)
    for widget in root.winfo_children():
        try:
            widget.config(bg=bg, fg=fg)
        except:
            pass
    refresh_task_list()

def update_analytics():
    total = len(tasks)
    done = len([t for t in tasks if t["status"] == "Done"])
    pending = total - done
    analytics_label.config(text=f"📊 Total: {total} | ✔️ Done: {done} | ⏳ Pending: {pending}")

def open_text_editor():
    editor = tk.Toplevel(root)
    editor.title("📝 Task Note Editor")
    editor.geometry("400x400")
    text_area = tk.Text(editor, wrap="word")
    text_area.pack(expand=True, fill="both")
    def save_note():
        content = text_area.get("1.0", tk.END).strip()
        with open("task_note.txt", "w") as f:
            f.write(content)
        messagebox.showinfo("Saved", "Task note saved to task_note.txt")
    tk.Button(editor, text="Save Note", command=save_note).pack(pady=5)

def open_paint():
    paint = tk.Toplevel(root)
    paint.title("🎨 SketchPad")
    paint.geometry("400x400")
    canvas = tk.Canvas(paint, bg="white")
    canvas.pack(fill="both", expand=True)
    def paint_draw(event):
        x, y = event.x, event.y
        canvas.create_oval(x-2, y-2, x+2, y+2, fill="black", outline="black")
    canvas.bind("<B1-Motion>", paint_draw)
    def clear_canvas():
        canvas.delete("all")
    tk.Button(paint, text="Clear Canvas", command=clear_canvas).pack(pady=5)

# ---------------- GUI Layout ----------------
root = tk.Tk()
root.title("📝 Advanced To-Do List App")
root.geometry("620x680")
root.config(bg="#ffffff")

# --- Top Input ---
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=5)

search_entry = tk.Entry(root, width=30)
search_entry.pack(pady=3)
search_entry.insert(0, "Search tasks...")

# --- Button Grid Frame ---
btn_frame = tk.Frame(root, bg="#ffffff")
btn_frame.pack(pady=8)

btns = [
    ("Add Task", add_task),
    ("Edit Task", edit_task),
    ("Mark as Done", mark_done),
    ("Delete Task", delete_task),
    ("Clear All", clear_all),
    ("Search", search_tasks),
    ("Toggle Dark Mode", toggle_theme),
    ("Task Note 📝", open_text_editor),
    ("SketchPad 🎨", open_paint),
]

for i, (text, cmd) in enumerate(btns):
    tk.Button(btn_frame, text=text, command=cmd, width=20).grid(row=i//3, column=i%3, padx=5, pady=3)

# --- Task List ---
task_listbox = tk.Listbox(root, width=85, height=15)
task_listbox.pack(pady=10)

# --- Analytics ---
analytics_label = tk.Label(root, text="📊 Analytics will show here", font=("Arial", 10), bg="#ffffff")
analytics_label.pack(pady=10)

# --- Load & Run ---
load_tasks()
refresh_task_list()
root.mainloop()
