import tkinter as tk
from tkinter import messagebox, simpledialog, colorchooser
import json, datetime, os, random


TASK_FILE = "tasks.json"
tasks = []
dark_mode = False

QUOTES = [
    "Push yourself, because no one else is going to do it for you.",
    "Success is what comes after you stop making excuses.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
]

def save_tasks():
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
    backup_tasks()

def load_tasks():
    global tasks
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            tasks = json.load(file)

def backup_tasks():
    backup_file = f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(backup_file, "w") as f:
        json.dump(tasks, f, indent=4)

def refresh_task_list(filtered=None):
    task_listbox.delete(0, tk.END)
    data = filtered if filtered else tasks
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

        with open("task_note.txt", "a") as f:
            f.write(f"🆕 Task Added: {new_task['task']} | Due: {new_task['due']} | Priority: {new_task['priority']}\n")
    else:
        messagebox.showwarning("Empty Task", "Please enter a task name.")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        task = tasks.pop(index)
        save_tasks()
        refresh_task_list()
        messagebox.showinfo("Task Deleted", f"Deleted: {task['task']}")
    else:
        messagebox.showwarning("No Selection", "Please select a task to delete.")

def mark_done():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        current_status = tasks[index]["status"]
        tasks[index]["status"] = "Done" if current_status == "Pending" else "Pending"
        save_tasks()
        refresh_task_list()
    else:
        messagebox.showwarning("No Selection", "Please select a task.")

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
            current["due"] = new_due if new_due else current["due"]
            current["priority"] = new_priority if new_priority else current["priority"]
            save_tasks()
            refresh_task_list()
    else:
        messagebox.showwarning("No Selection", "Please select a task to edit.")

def clear_all():
    confirm = messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?")
    if confirm:
        tasks.clear()
        save_tasks()
        refresh_task_list()

def search_tasks():
    query = search_entry.get().strip().lower()
    if query:
        filtered = [t for t in tasks if query in t['task'].lower()]
        refresh_task_list(filtered)
    else:
        refresh_task_list()

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    bg, fg = ("#222", "#fff") if dark_mode else ("#fff", "#000")
    root.config(bg=bg)
    for widget in root.winfo_children():
        try:
            widget.config(bg=bg, fg=fg, insertbackground=fg)
        except:
            pass
    refresh_task_list()

def update_analytics():
    total = len(tasks)
    done = sum(1 for t in tasks if t["status"] == "Done")
    pending = total - done
    analytics_label.config(text=f"📊 Total: {total} | ✔️ Done: {done} | ⏳ Pending: {pending}")

def open_text_editor():
    editor = tk.Toplevel(root)
    editor.title("📝 Task Notes")
    editor.geometry("500x550")

    text_area = tk.Text(editor, wrap="word", font=("Arial", 11))
    text_area.pack(expand=True, fill="both", padx=5, pady=5)

    if os.path.exists("task_note.txt"):
        with open("task_note.txt", "r") as f:
            content = f.read()
            text_area.insert(tk.END, content)

    def save_note():
        content = text_area.get("1.0", tk.END).strip()
        with open("task_note.txt", "w") as f:
            f.write(content)
        messagebox.showinfo("Saved", "Notes saved to task_note.txt")

    def load_note():
        if os.path.exists("task_note.txt"):
            with open("task_note.txt", "r") as f:
                text_area.delete("1.0", tk.END)
                text_area.insert(tk.END, f.read())
            messagebox.showinfo("Loaded", "Note loaded from task_note.txt")
        else:
            messagebox.showwarning("Not Found", "No saved notes found.")

    def clear_note():
        text_area.delete("1.0", tk.END)

    def insert_timestamp():
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        text_area.insert(tk.INSERT, f"[{now}] ")

    def insert_summary():
        total = len(tasks)
        done = sum(1 for t in tasks if t["status"] == "Done")
        pending = total - done
        summary = f"\n--- Task Summary ---\nTotal: {total}\n✔️ Done: {done}\n⏳ Pending: {pending}\n"
        text_area.insert(tk.END, summary)

    def export_note():
        filename = simpledialog.askstring("Export File", "Enter file name (e.g., MyNotes.txt):")
        if filename:
            with open(filename, "w") as f:
                f.write(text_area.get("1.0", tk.END).strip())
            messagebox.showinfo("Exported", f"Notes exported to {filename}")

    def auto_save():
        content = text_area.get("1.0", tk.END).strip()
        with open("task_note.txt", "w") as f:
            f.write(content)
        editor.after(60000, auto_save)

    word_count_label = tk.Label(editor, text="Words: 0", font=("Arial", 9))
    word_count_label.pack(side="bottom", pady=3)

    def update_word_count(event=None):
        text = text_area.get("1.0", tk.END)
        words = len(text.split())
        word_count_label.config(text=f"Words: {words}")

    text_area.bind("<KeyRelease>", update_word_count)

    btn_frame = tk.Frame(editor)
    btn_frame.pack(pady=6)

    tk.Button(btn_frame, text="💾 Save", command=save_note, width=12).grid(row=0, column=0, padx=4)
    tk.Button(btn_frame, text="🧾 Load", command=load_note, width=12).grid(row=0, column=1, padx=4)
    tk.Button(btn_frame, text="🧹 Clear", command=clear_note, width=12).grid(row=0, column=2, padx=4)
    tk.Button(btn_frame, text="⏰ Time", command=insert_timestamp, width=12).grid(row=1, column=0, padx=4, pady=5)
    tk.Button(btn_frame, text="📊 Summary", command=insert_summary, width=12).grid(row=1, column=1, padx=4)
    tk.Button(btn_frame, text="📤 Export", command=export_note, width=12).grid(row=1, column=2, padx=4)

    auto_save()

def open_paint():
    paint = tk.Toplevel(root)
    paint.title("🎨 SketchPad")
    paint.geometry("600x550")

    current_color = "black"
    brush_size = tk.IntVar(value=3)
    erasing = tk.BooleanVar(value=False)
    drawn_items = []

    canvas = tk.Canvas(paint, bg="white")
    canvas.pack(fill="both", expand=True)

    def draw(event):
        size = brush_size.get()
        color = "white" if erasing.get() else current_color
        item = canvas.create_oval(
            event.x - size, event.y - size,
            event.x + size, event.y + size,
            fill=color, outline=color
        )
        drawn_items.append(item)

    def choose_color():
        nonlocal current_color
        color = colorchooser.askcolor()[1]
        if color:
            current_color = color
            erasing.set(False)
            eraser_btn.config(text="🩹 Eraser", bg="#d0f0c0")

    def toggle_eraser():
        erasing.set(not erasing.get())
        eraser_btn.config(
            text="✏️ Pencil" if erasing.get() else "🩹 Eraser",
            bg="#fbb" if erasing.get() else "#d0f0c0"
        )

    def undo_last():
        if drawn_items:
            canvas.delete(drawn_items.pop())

    def clear_canvas():
        canvas.delete("all")
        drawn_items.clear()

    def set_bg_color():
        bg_color = colorchooser.askcolor()[1]
        if bg_color:
            canvas.config(bg=bg_color)

    canvas.bind("<B1-Motion>", draw)

    controls = tk.Frame(paint)
    controls.pack(pady=5)

    tk.Label(controls, text="Brush Size:").grid(row=0, column=0, padx=5)
    tk.Scale(controls, from_=1, to=20, orient="horizontal", variable=brush_size).grid(row=0, column=1, padx=5)

    tk.Button(controls, text="🎨 Color", command=choose_color).grid(row=0, column=2, padx=5)
    eraser_btn = tk.Button(controls, text="🩹 Eraser", bg="#d0f0c0", command=toggle_eraser)
    eraser_btn.grid(row=0, column=3, padx=5)
    tk.Button(controls, text="↩️ Undo", command=undo_last).grid(row=0, column=4, padx=5)
    tk.Button(controls, text="🧹 Clear", command=clear_canvas).grid(row=0, column=5, padx=5)
    tk.Button(controls, text="🖼️ Background", command=set_bg_color).grid(row=0, column=6, padx=5)

def show_today_reminders():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    today_tasks = [t for t in tasks if t.get("due") == today and t["status"] != "Done"]
    if today_tasks:
        task_lines = "\n".join([f"- {t['task']} (Priority: {t.get('priority')})" for t in today_tasks])
        messagebox.showinfo("🗓️ Today's Tasks", f"Tasks due today:\n\n{task_lines}")

def open_calendar_view():
    cal_win = tk.Toplevel(root)
    cal_win.title("📅 Calendar View")
    cal_win.geometry("450x400")

    calendar_box = tk.Text(cal_win, font=("Courier New", 10), wrap="word")
    calendar_box.pack(expand=True, fill="both", padx=10, pady=10)

    grouped = {}
    for task in tasks:
        due = task.get("due", "No Due Date")
        grouped.setdefault(due, []).append(task)

    for due, group in sorted(grouped.items()):
        calendar_box.insert(tk.END, f"\n📆 {due}\n" + "-"*40 + "\n")
        for t in group:
            status = "✔️" if t["status"] == "Done" else "⏳"
            line = f"{status} [{t.get('priority', 'Medium')}] {t['task']}\n"
            calendar_box.insert(tk.END, line)

def show_motivational_quote():
    quote = random.choice(QUOTES)
    messagebox.showinfo("💡 Motivation", quote)

# GUI Setup
root = tk.Tk()
root.title("📝 Advanced To-Do List")
root.geometry("650x720")
root.resizable(False, False)
root.config(bg="#ffffff")

task_entry = tk.Entry(root, width=50, font=("Arial", 12))
task_entry.pack(pady=10)

search_entry = tk.Entry(root, width=30, font=("Arial", 10))
search_entry.insert(0, "Search tasks...")
search_entry.pack(pady=5)

btn_frame = tk.Frame(root, bg="#ffffff")
btn_frame.pack(pady=10)

btns = [
    ("Add Task", add_task),
    ("Edit Task", edit_task),
    ("Mark Done", mark_done),
    ("Delete Task", delete_task),
    ("Clear All", clear_all),
    ("Search", search_tasks),
    ("🌓 Toggle Theme", toggle_theme),
    ("📝 Notes", open_text_editor),
    ("🎨 SketchPad", open_paint),
    ("📅 Calendar", open_calendar_view),
]

for i, (text, cmd) in enumerate(btns):
    tk.Button(btn_frame, text=text, command=cmd, width=18, font=("Arial", 9)).grid(row=i//3, column=i%3, padx=6, pady=5)

task_listbox = tk.Listbox(root, width=90, height=16, font=("Consolas", 10))
task_listbox.pack(pady=15)

analytics_label = tk.Label(root, text="📊 Stats: Loading...", bg="#ffffff", font=("Arial", 11))
analytics_label.pack(pady=8)

load_tasks()
refresh_task_list()
show_motivational_quote()
show_today_reminders()
root.mainloop()
