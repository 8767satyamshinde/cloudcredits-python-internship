# --- Full 400-Line Project Code Below ---
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
    name = f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(name, "w") as f:
        json.dump(tasks, f, indent=4)

def refresh_task_list(filtered=None):
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(filtered if filtered else tasks):
        status = "✔️" if task["status"] == "Done" else "⏳"
        text = f"{i+1}. {status} [{task.get('priority','Medium')}] {task['task']} (Due: {task.get('due','N/A')})"
        task_listbox.insert(tk.END, text)
    update_analytics()

def add_task():
    task_text = task_entry.get().strip()
    if task_text:
        due = simpledialog.askstring("Due Date", "Enter due date (YYYY-MM-DD):")
        priority = simpledialog.askstring("Priority", "Enter priority (Low/Medium/High):")
        task = {
            "task": task_text, "status": "Pending",
            "created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "due": due or "N/A", "priority": priority or "Medium"
        }
        tasks.append(task)
        save_tasks(); refresh_task_list(); task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Please enter a task name.")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task = tasks.pop(selected[0])
        save_tasks(); refresh_task_list()
        messagebox.showinfo("Deleted", f"Deleted: {task['task']}")

def mark_done():
    selected = task_listbox.curselection()
    if selected:
        i = selected[0]
        tasks[i]["status"] = "Done" if tasks[i]["status"] == "Pending" else "Pending"
        save_tasks(); refresh_task_list()

def edit_task():
    selected = task_listbox.curselection()
    if selected:
        i = selected[0]
        t = tasks[i]
        new = simpledialog.askstring("Edit Task", "Edit name:", initialvalue=t["task"])
        due = simpledialog.askstring("Edit Due", "Due (YYYY-MM-DD):", initialvalue=t.get("due"))
        prio = simpledialog.askstring("Edit Priority", "Low/Medium/High:", initialvalue=t.get("priority"))
        if new: t.update({"task": new, "due": due or t["due"], "priority": prio or t["priority"]})
        save_tasks(); refresh_task_list()

def clear_all():
    if messagebox.askyesno("Clear All", "Delete all tasks?"):
        tasks.clear(); save_tasks(); refresh_task_list()

def search_tasks():
    query = search_entry.get().strip().lower()
    refresh_task_list([t for t in tasks if query in t['task'].lower()] if query else None)

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    bg, fg = ("#222", "#fff") if dark_mode else ("#fff", "#000")
    root.config(bg=bg)
    for widget in root.winfo_children():
        try: widget.config(bg=bg, fg=fg, insertbackground=fg)
        except: pass
    refresh_task_list()

def update_analytics():
    total = len(tasks)
    done = sum(1 for t in tasks if t["status"] == "Done")
    analytics_label.config(text=f"📊 Total: {total} | ✔️ Done: {done} | ⏳ Pending: {total - done}")

def open_text_editor():
    ed = tk.Toplevel(root); ed.title("📝 Notes"); ed.geometry("500x550")
    txt = tk.Text(ed, wrap="word", font=("Arial", 11)); txt.pack(expand=True, fill="both")
    if os.path.exists("task_note.txt"):
        with open("task_note.txt", "r") as f: txt.insert(tk.END, f.read())
    def auto_save(): open("task_note.txt", "w").write(txt.get("1.0", tk.END).strip()); ed.after(60000, auto_save)
    def update_wc(e=None): wc.config(text=f"Words: {len(txt.get('1.0', tk.END).split())}")
    wc = tk.Label(ed, text="Words: 0", font=("Arial", 9)); wc.pack(side="bottom", pady=3)
    txt.bind("<KeyRelease>", update_wc); update_wc()

    btn = tk.Frame(ed); btn.pack()
    for i, (t, cmd) in enumerate([
        ("💾 Save", lambda: open("task_note.txt", "w").write(txt.get("1.0", tk.END).strip())),
        ("📤 Export", lambda: open(simpledialog.askstring("Export File", "Filename:"), "w").write(txt.get("1.0", tk.END))),
        ("📊 Summary", lambda: txt.insert(tk.END, f"\n--- Task Summary ---\nTotal: {len(tasks)}\n✔️ Done: {sum(1 for t in tasks if t['status']=='Done')}\n⏳ Pending: {len(tasks)-sum(1 for t in tasks if t['status']=='Done')}\n")),
        ("⏰ Time", lambda: txt.insert(tk.INSERT, f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ")),
        ("🧹 Clear", lambda: txt.delete("1.0", tk.END))
    ]): tk.Button(btn, text=t, command=cmd, width=15).grid(row=i//3, column=i%3, padx=4, pady=3)
    auto_save()

def open_paint():
    paint = tk.Toplevel(root); paint.title("🎨 Paint"); paint.geometry("600x550")
    current_color, erasing, drawn = "black", tk.BooleanVar(), []
    canvas = tk.Canvas(paint, bg="white"); canvas.pack(fill="both", expand=True)
    def draw(e):
        c = "white" if erasing.get() else current_color
        item = canvas.create_oval(e.x-3, e.y-3, e.x+3, e.y+3, fill=c, outline=c)
        drawn.append(item)
    def choose(): nonlocal current_color; current_color = colorchooser.askcolor()[1] or current_color
    def erase(): erasing.set(not erasing.get())
    def undo(): canvas.delete(drawn.pop()) if drawn else None
    def clear(): canvas.delete("all"); drawn.clear()
    def bg_color(): canvas.config(bg=colorchooser.askcolor()[1])
    canvas.bind("<B1-Motion>", draw)
    ctrl = tk.Frame(paint); ctrl.pack()
    for i, (t, f) in enumerate([
        ("🎨 Color", choose), ("✏️ Erase", erase), ("↩️ Undo", undo),
        ("🧹 Clear", clear), ("🖼️ Background", bg_color)
    ]): tk.Button(ctrl, text=t, command=f).grid(row=0, column=i, padx=5)

def open_calendar_view():
    win = tk.Toplevel(root); win.title("📅 Calendar"); win.geometry("450x400")
    box = tk.Text(win, font=("Courier", 10)); box.pack(expand=True, fill="both")
    groups = {}
    for t in tasks: groups.setdefault(t.get("due", "N/A"), []).append(t)
    for d, g in sorted(groups.items()):
        box.insert(tk.END, f"\n📆 {d}\n" + "-"*40 + "\n")
        for t in g: box.insert(tk.END, f"{'✔️' if t['status']=='Done' else '⏳'} [{t['priority']}] {t['task']}\n")

def show_today_reminders():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    due = [t for t in tasks if t.get("due") == today and t["status"] != "Done"]
    if due: messagebox.showinfo("🗓️ Today's Tasks", "\n".join(f"- {t['task']} (Priority: {t['priority']})" for t in due))

def show_motivational_quote():
    messagebox.showinfo("💡 Motivation", random.choice(QUOTES))

# --- New Features ---
def set_reminder():
    sel = task_listbox.curselection()
    if sel:
        i, task = sel[0], tasks[sel[0]]
        time_str = simpledialog.askstring("Reminder Time", "HH:MM (24hr):")
        if time_str:
            def check(): 
                if datetime.datetime.now().strftime("%H:%M") == time_str:
                    messagebox.showinfo("⏰ Reminder", f"{task['task']}")
                else: root.after(60000, check)
            check()

def duplicate_task():
    sel = task_listbox.curselection()
    if sel:
        t = tasks[sel[0]].copy()
        t["created"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        tasks.append(t); save_tasks(); refresh_task_list()

def sort_tasks():
    op = simpledialog.askstring("Sort", "Sort by: date or priority").lower()
    if op == "date":
        tasks.sort(key=lambda x: x.get("due", "9999-99-99"))
    elif op == "priority":
        order = {"High": 1, "Medium": 2, "Low": 3}
        tasks.sort(key=lambda x: order.get(x.get("priority", "Medium"), 2))
    refresh_task_list()

def export_tasks():
    name = simpledialog.askstring("Filename", "Export as:")
    if name:
        with open(name, "w") as f:
            for t in tasks:
                f.write(f"{t['task']} | {t['status']} | Due: {t['due']} | Priority: {t['priority']}\n")
        messagebox.showinfo("Exported", f"Saved to {name}")

# --- GUI ---
root = tk.Tk()
root.title("📝 Advanced To-Do List"); root.geometry("680x720"); root.resizable(False, False)

task_entry = tk.Entry(root, width=50, font=("Arial", 12)); task_entry.pack(pady=10)
search_entry = tk.Entry(root, width=30, font=("Arial", 10)); search_entry.insert(0, "Search tasks..."); search_entry.pack()
btn_frame = tk.Frame(root); btn_frame.pack(pady=10)

buttons = [
    ("Add Task", add_task), ("Edit Task", edit_task), ("Mark Done", mark_done),
    ("Delete Task", delete_task), ("Clear All", clear_all), ("Search", search_tasks),
    ("🌓 Toggle Theme", toggle_theme), ("📝 Notes", open_text_editor),
    ("🎨 SketchPad", open_paint), ("📅 Calendar", open_calendar_view),
    ("⏰ Reminder", set_reminder), ("📋 Duplicate", duplicate_task),
    ("🔃 Sort", sort_tasks), ("📤 Export", export_tasks)
]
for i, (text, cmd) in enumerate(buttons):
    tk.Button(btn_frame, text=text, command=cmd, width=18).grid(row=i//3, column=i%3, padx=6, pady=4)

task_listbox = tk.Listbox(root, width=90, height=18, font=("Consolas", 10))
task_listbox.pack(pady=10)
analytics_label = tk.Label(root, text="📊 Stats: Loading...", font=("Arial", 11)); analytics_label.pack(pady=6)

load_tasks(); refresh_task_list(); show_motivational_quote(); show_today_reminders()
root.mainloop()
