Here is a complete and updated **`README.md`** file for your advanced To-Do List application with added features like **SketchPad**, **Text Editor**, **Calendar**, **Motivational Quotes**, and **Statistics**:

---

### 📘 `README.md`

```markdown
# 📝 Advanced To-Do List Application (with SketchPad & Notes)

This is a powerful Python-based desktop To-Do List app using **Tkinter GUI**. It allows users to manage tasks efficiently with enhanced features like:
- 🎨 SketchPad Drawing Tool
- 📝 Rich Text Notes Editor
- 📅 Calendar View of Tasks
- 💡 Motivational Quotes
- 📊 Task Analytics (Done/Pending)
- 🌙 Light/Dark Mode Toggle

---

## ✅ Features

### 📋 Task Management
- Add new tasks with **priority** and **due date**
- Mark tasks as **Done** or **Pending**
- Edit existing tasks
- Delete individual or all tasks
- Search tasks by keyword
- Automatically **backup** tasks on every change

### 📝 Notes Editor
- Open rich text editor with full features
- Save/load notes from `task_note.txt`
- Insert current **timestamp**
- View **task summary** inside notes
- Auto-save notes every 60 seconds
- Export notes to custom `.txt` file
- Word count label at the bottom

### 🎨 SketchPad Drawing Tool *(Updated)*
- Draw freehand sketches using the mouse
- Choose **brush size** using a slider
- Select any **brush color**
- Use **eraser tool**
- Undo last stroke
- Change entire **canvas background color**
- Clear all drawings

### 📅 Calendar View
- See all tasks grouped by their **due date**

### 💡 Motivation
- Shows random motivational quote on every launch

### 🌙 Light/Dark Theme
- Toggle between light and dark mode

---

## 🗃️ File Structure

```

📁 Project Directory
├── tasks.json              # Main task storage (auto-created)
├── task\_note.txt           # Notes editor save file
├── backup\_\*.json           # Auto-backup file created on each save
├── main.py                 # Main Python code
└── README.md               # Project readme (you’re reading it)

````

---

## 💻 Requirements

- Python 3.x
- Tkinter (comes with standard Python)
- `json`, `os`, `datetime`, `random`, `colorchooser`

Install if missing:
```bash
pip install tk
````

---

## 🚀 How to Run

1. Save the provided code as `main.py`
2. Open terminal in the same directory
3. Run the app using:

```bash
python main.py
```

---

## 🙌 Credits

Developed by: **Satyam Shinde**
Language: **Python (Tkinter GUI)**
Project Type: **Desktop Application**

```

---

Let me know if you also want a separate PDF version, GitHub setup instructions, or badges added for a repository.
```
