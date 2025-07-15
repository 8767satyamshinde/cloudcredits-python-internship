Here's your finalized **`README.md`** file for the **Advanced To-Do List Desktop App** built with **Python and Tkinter**.

---

```markdown
# 📝 Advanced To-Do List Desktop App (Tkinter + Python)

This is a feature-rich **To-Do List Desktop Application** developed using **Python and Tkinter GUI**.  
It helps users efficiently manage daily tasks by allowing them to add, edit, complete, search, and organize their work with due dates, priorities, analytics, and more.

---

## 🚀 Features

- ➕ **Add New Task**
- ✏️ **Edit Task Details** (Name, Due Date, Priority)
- ✔️ **Mark as Done**
- 🗑️ **Delete Task**
- 🔄 **Clear All Tasks**
- 🔍 **Search Tasks by Name**
- 📁 **Auto Save & Load Tasks** (`tasks.json`)
- ⏰ **Set Due Date for Each Task**
- 🧠 **Set Task Priority** (Low / Medium / High)
- 📊 **Task Analytics** (Total / Done / Pending)
- 🌓 **Toggle Between Light & Dark Mode**
- ✅ **Simple GUI** built using Tkinter

---

## 📁 File Structure

```

ToDo\_Desktop\_App/
├── todo.py           # Main Python application
├── tasks.json        # Local storage of tasks (auto-created)
├── README.md         # Documentation file

````

---

## 💻 How to Run the App

### 1. Requirements
- ✅ Python 3.8 to 3.11  
- ❌ Python 3.13 not recommended (Tkinter GUI issues)

### 2. Steps to Run

Open terminal or command prompt and run:

```bash
python todo.py
````

Make sure you're in the folder where `todo.py` exists.

---

## 🧑‍💻 How to Use the App

### ➕ Add Task

1. Enter task name in the text field.
2. Click **"Add Task"**.
3. You'll be prompted to enter a **due date** and **priority level**.

### ✏️ Edit Task

1. Select a task from the list.
2. Click **"Edit Task"**.
3. Modify task details.

### ✔️ Mark Task as Done

* Select a task → Click **"Mark as Done"**.

### 🗑️ Delete or Clear Tasks

* **Delete Task**: Select a task → Click **"Delete Task"**.
* **Clear All**: Click **"Clear All Tasks"** → Confirm deletion.

### 🔍 Search Tasks

* Enter keywords in the search bar → Click **"Search"**.

### 🌙 Dark Mode

* Click **"Toggle Dark Mode"** to switch between themes.

### 📊 View Analytics

* Total tasks, completed, and pending counts shown at the bottom.

---

## 🧾 Task Storage Format

Tasks are saved in `tasks.json` like this:

```json
[
  {
    "task": "Finish Python Project",
    "status": "Pending",
    "created": "2025-07-15 10:30",
    "due": "2025-07-18",
    "priority": "High"
  }
]
```

This file is automatically created and updated in the same folder.

---

## 📌 Optional Improvements

You can enhance this project by adding:

* 🔔 Task reminders using `threading` or `apscheduler`
* ☁️ Login system and cloud sync with Flask + Firebase/MongoDB
* 📱 Mobile version using Kivy or React Native

---

## 🙋‍♂️ Developer

**Satyam Shinde**
M.Tech Computer Engineering (AI), Pimpri Chinchwad University
Email: [shindesatyam72@gmail.com](mailto:shindesatyam72@gmail.com)
GitHub: *your GitHub link*
LinkedIn: *your LinkedIn link*

---

## 📜 License

This project is open for educational and personal use. Attribution is appreciated!

```

---

Let me know if you'd like:
- A `.md` file download
- Help uploading this to GitHub with your project

Or if you want to add your **GitHub/LinkedIn links** directly into the file!
```
