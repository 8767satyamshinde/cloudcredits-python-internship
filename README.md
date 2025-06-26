Here is  including:

* ✅ View calculation history
* ✅ Clear history
* ✅ Save history to file
* ✅ Save As (export history with a custom filename)

---

### ✅ **Full Updated Python Code**:

```python
import tkinter as tk
from tkinter import messagebox, Toplevel, Scrollbar, StringVar, filedialog
from math import sqrt, sin, cos, tan, log10, radians, factorial
from datetime import datetime
import os

# === History Management ===
HISTORY_FILE = "history.txt"
history = []

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            return file.read()
    return ""

def save_history():
    with open(HISTORY_FILE, "w") as file:
        file.write('\n'.join(history))

def save_history_as():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")],
                                             title="Save history as")
    if file_path:
        with open(file_path, "w") as file:
            file.write('\n'.join(history))
        messagebox.showinfo("Save As", "History saved successfully!")

def clear_history():
    history.clear()
    save_history()
    messagebox.showinfo("Clear History", "History cleared successfully!")

# === Calculator Functions ===
def add_to_expression(symbol):
    entry_var.set(entry_var.get() + str(symbol))

def clear():
    entry_var.set("")

def delete_last():
    entry_var.set(entry_var.get()[:-1])

def calculate():
    try:
        result = eval(entry_var.get())
        output = f"{entry_var.get()} = {result}"
        history.append(output)
        save_history()
        entry_var.set(str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid expression\n{e}")

def calculate_function(func):
    try:
        expression = entry_var.get()
        value = float(expression)
        if func == "sqrt":
            result = sqrt(value)
        elif func == "sin":
            result = sin(radians(value))
        elif func == "cos":
            result = cos(radians(value))
        elif func == "tan":
            result = tan(radians(value))
        elif func == "log":
            result = log10(value)
        elif func == "fact":
            result = factorial(int(value))
        else:
            result = value
        output = f"{func}({value}) = {result}"
        history.append(output)
        save_history()
        entry_var.set(str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Function error\n{e}")

# === GUI Setup ===
root = tk.Tk()
root.title("Advanced Calculator with History")
root.geometry("400x600")
entry_var = StringVar()

entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief="ridge", justify='right')
entry.pack(fill="both", padx=10, pady=10, ipady=10)

# === Button Frame ===
btn_frame = tk.Frame(root)
btn_frame.pack()

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
    ('(', ')', 'C', 'Del'),
    ('sqrt', 'sin', 'cos', 'tan'),
    ('log', 'fact')
]

for row in buttons:
    row_frame = tk.Frame(btn_frame)
    row_frame.pack(expand=True, fill='both')
    for btn in row:
        action = lambda x=btn: (
            calculate() if x == '=' else
            clear() if x == 'C' else
            delete_last() if x == 'Del' else
            calculate_function(x) if x in ['sqrt', 'sin', 'cos', 'tan', 'log', 'fact'] else
            add_to_expression(x)
        )
        tk.Button(row_frame, text=btn, font=("Arial", 14), height=2, width=6, command=action).pack(side='left', expand=True, fill='both')

# === History Menu ===
def show_history():
    hist_win = Toplevel(root)
    hist_win.title("Calculation History")
    hist_win.geometry("400x300")

    scrollbar = Scrollbar(hist_win)
    scrollbar.pack(side="right", fill="y")

    hist_text = tk.Text(hist_win, wrap="word", yscrollcommand=scrollbar.set)
    hist_text.insert("1.0", load_history())
    hist_text.pack(expand=True, fill="both")
    scrollbar.config(command=hist_text.yview)

    tk.Button(hist_win, text="Clear History", command=clear_history).pack(side="left", padx=10, pady=10)
    tk.Button(hist_win, text="Save History", command=save_history).pack(side="left", padx=10)
    tk.Button(hist_win, text="Save As", command=save_history_as).pack(side="left", padx=10)

menu = tk.Menu(root)
root.config(menu=menu)
history_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="History", menu=history_menu)
history_menu.add_command(label="View History", command=show_history)
history_menu.add_command(label="Clear History", command=clear_history)
history_menu.add_command(label="Save History", command=save_history)
history_menu.add_command(label="Save As...", command=save_history_as)

root.mainloop()
```

---

### 📄 `README.md` (Updated Content for the Project):

````markdown
# Advanced Calculator with History (Tkinter GUI)

This is a Python-based GUI calculator built with Tkinter. It supports:

### ✅ Features:
- Basic arithmetic operations: +, -, *, /
- Advanced math functions:
  - Square root, log10, sin, cos, tan
  - Factorial
- Expression evaluation with parentheses
- **Calculation History**:
  - View history in a separate window
  - Clear history
  - Save to default file (`history.txt`)
  - Save As... (choose custom location/file)

### 💾 Requirements:
- Python 3.x
- Tkinter (standard in Python)

### ▶️ Run the app:
```bash
python calculator.py
````

### 📁 Files:

* `calculator.py` – main GUI calculator script
* `history.txt` – stores saved calculation history

### 🛠 How to Use:

* Click numbers and operators to form expressions
* Press `=` to evaluate
* Use the **History** menu to view, clear, or save history

### 📌 Author:

* Satyam Shinde, Cloudcredits Internship Project

---

```

