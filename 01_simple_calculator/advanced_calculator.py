import tkinter as tk
from tkinter import messagebox, Toplevel, Scrollbar, StringVar, filedialog
from math import sqrt, sin, cos, tan, log10, radians, factorial
from datetime import datetime
import os

# === History Management ===
HISTORY_FILE = "history.txt"

if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r") as f:
        history = [line.strip() for line in f.readlines()]
else:
    history = []

def save_history_entry(entry):
    with open(HISTORY_FILE, "a") as f:
        f.write(entry + "\n")

memory_value = 0
dark_mode = False

# === Main Window ===
root = tk.Tk()
root.title("Scientific Calculator - Cloudcredits Internship")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
app_width = int(screen_width * 0.35)
app_height = int(screen_height * 0.8)
root.geometry(f"{app_width}x{app_height}")
root.minsize(500, 600)

FONT_SIZE = int(app_width * 0.025)
BUTTON_FONT = ("Arial", FONT_SIZE)
ENTRY_FONT = ("Arial", FONT_SIZE + 4)

# === Click Function ===
def click(event):
    global memory_value
    text = event.widget.cget("text")
    current = entry.get()

    try:
        if text == "=":
            expression = current.replace("%", "/100")
            result = eval(expression)
            result = round(result, 4)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
            full_expr = f"{current} = {result}"
            if not history or history[-1] != full_expr:
                history.append(full_expr)
                save_history_entry(full_expr)

        elif text == "C":
            entry.delete(0, tk.END)

        elif text == "⌫":
            entry.delete(len(current) - 1, tk.END)

        elif text in ["√", "sin", "cos", "tan", "log"]:
            if current == "":
                entry.insert(tk.END, "Enter number first")
            else:
                value = float(current)
                entry.delete(0, tk.END)
                if text == "√":
                    result = sqrt(value)
                elif text == "sin":
                    result = sin(radians(value))
                elif text == "cos":
                    result = cos(radians(value))
                elif text == "tan":
                    result = tan(radians(value))
                elif text == "log":
                    if value > 0:
                        result = log10(value)
                    else:
                        entry.insert(tk.END, "Invalid (log)")
                        return
                result = round(result, 4)
                full_expr = f"{text}({value}) = {result}"
                history.append(full_expr)
                save_history_entry(full_expr)
                entry.insert(tk.END, result)

        elif text == "x!":
            if current == "":
                entry.insert(tk.END, "Enter number first")
            else:
                value = float(current)
                if value < 0 or not value.is_integer():
                    entry.delete(0, tk.END)
                    entry.insert(tk.END, "Invalid (x!)")
                else:
                    result = factorial(int(value))
                    entry.delete(0, tk.END)
                    full_expr = f"{int(value)}! = {result}"
                    history.append(full_expr)
                    save_history_entry(full_expr)
                    entry.insert(tk.END, result)

        elif text == "M+":
            if current != "":
                memory_value += float(current)
                messagebox.showinfo("Memory", f"Added to memory: {memory_value}")

        elif text == "M-":
            if current != "":
                memory_value -= float(current)
                messagebox.showinfo("Memory", f"Subtracted from memory: {memory_value}")

        elif text == "MR":
            entry.insert(tk.END, str(memory_value))

        elif text == "MC":
            memory_value = 0
            messagebox.showinfo("Memory", "Memory cleared.")

        elif text == "Copy":
            root.clipboard_clear()
            root.clipboard_append(entry.get())
            messagebox.showinfo("Copied", "Result copied to clipboard!")

        else:
            entry.insert(tk.END, text)

    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# === Unit Converter ===
def open_unit_converter():
    conv_win = Toplevel(root)
    conv_win.title("Unit Converter")
    conv_win.geometry("400x400")

    conversions = {
        "Length": {"m to km": 0.001, "km to m": 1000, "cm to m": 0.01, "m to cm": 100},
        "Weight": {"kg to g": 1000, "g to kg": 0.001, "pound to kg": 0.4536, "kg to pound": 2.2046},
        "Temperature": {"C to F": "CtoF", "F to C": "FtoC"}
    }

    category_var = StringVar()
    category_var.set("Length")
    unit_var = StringVar()
    unit_var.set("m to km")

    def update_units(*args):
        options = list(conversions[category_var.get()].keys())
        unit_var.set(options[0])
        menu = unit_menu["menu"]
        menu.delete(0, "end")
        for opt in options:
            menu.add_command(label=opt, command=lambda value=opt: unit_var.set(value))

    def convert():
        try:
            value = float(input_val.get())
            conv_type = conversions[category_var.get()][unit_var.get()]
            if conv_type == "CtoF":
                result = value * 9/5 + 32
            elif conv_type == "FtoC":
                result = (value - 32) * 5/9
            else:
                result = value * conv_type
            result_lbl.config(text=f"Result: {round(result, 4)}")
        except:
            result_lbl.config(text="Error")

    tk.Label(conv_win, text="Category").pack(pady=5)
    tk.OptionMenu(conv_win, category_var, *conversions.keys(), command=update_units).pack(pady=5)
    tk.Label(conv_win, text="Conversion Type").pack(pady=5)
    unit_menu = tk.OptionMenu(conv_win, unit_var, *conversions["Length"].keys())
    unit_menu.pack(pady=5)

    tk.Label(conv_win, text="Enter Value").pack(pady=5)
    input_val = tk.Entry(conv_win)
    input_val.pack(pady=5)
    tk.Button(conv_win, text="Convert", command=convert).pack(pady=10)
    result_lbl = tk.Label(conv_win, text="")
    result_lbl.pack(pady=5)

# === Show History with Save, Save As, Clear ===
def show_history():
    hist_win = Toplevel(root)
    hist_win.title("Calculation History")
    hist_win.geometry("500x500")

    scroll = Scrollbar(hist_win)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    text_area = tk.Text(hist_win, yscrollcommand=scroll.set)
    text_area.pack(expand=True, fill=tk.BOTH)
    scroll.config(command=text_area.yview)

    for h in history:
        text_area.insert(tk.END, h + "\n")

    def clear_hist():
        global history
        history.clear()
        with open(HISTORY_FILE, "w") as f:
            f.write("")
        text_area.delete(1.0, tk.END)
        messagebox.showinfo("History", "History cleared.")

    def save_hist():
        with open(HISTORY_FILE, "w") as f:
            f.write(text_area.get("1.0", tk.END).strip())
        messagebox.showinfo("Saved", f"History saved to {HISTORY_FILE}")

    def save_as_hist():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                f.write(text_area.get("1.0", tk.END).strip())
            messagebox.showinfo("Saved", f"History saved as {file_path}")

    btn_frame = tk.Frame(hist_win)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Clear History", command=clear_hist, bg="#f44336", fg="white", padx=10).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Save History", command=save_hist, bg="#4CAF50", fg="white", padx=10).grid(row=0, column=1, padx=5)
    tk.Button(btn_frame, text="Save As...", command=save_as_hist, bg="#2196F3", fg="white", padx=10).grid(row=0, column=2, padx=5)

# === Dark Mode ===
def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    bg_color = "#121212" if dark_mode else "#e6f2ff"
    fg_color = "white" if dark_mode else "#333333"
    entry.config(bg=bg_color, fg=fg_color, insertbackground=fg_color)
    root.config(bg=bg_color)
    for child in root.winfo_children():
        if isinstance(child, tk.Button):
            child.config(bg="#333333" if dark_mode else "#ffffff", fg=fg_color)

# === Keyboard Support ===
def on_key(event):
    key = event.char
    if key in '0123456789.+-*/%':
        entry.insert(tk.END, key)
    elif key == '\r':
        click(type('Event', (object,), {'widget': type('W', (), {'cget': lambda s: '='})()})())
    elif key == '\x08':
        entry.delete(len(entry.get()) - 1, tk.END)

root.bind("<Key>", on_key)

# === Entry ===
entry = tk.Entry(root, font=ENTRY_FONT, bd=5, relief=tk.RIDGE, justify=tk.RIGHT, bg="#e6f2ff", fg="#333333")
entry.grid(row=1, column=0, columnspan=5, sticky="nsew", padx=10, pady=10, ipady=10)
entry.focus_set()

time_label = tk.Label(root, text=datetime.now().strftime("\U0001F552 %Y-%m-%d %H:%M:%S"),
                      font=("Arial", int(FONT_SIZE * 0.8)), bg="#e6f2ff", fg="gray")
time_label.grid(row=2, column=0, columnspan=5)

# === Layout ===
for i in range(11):
    root.grid_rowconfigure(i, weight=1)
for j in range(5):
    root.grid_columnconfigure(j, weight=1)

buttons = [
    ["7", "8", "9", "/", "√"],
    ["4", "5", "6", "*", "sin"],
    ["1", "2", "3", "-", "cos"],
    ["0", ".", "=", "+", "tan"],
    ["C", "log", "%", "**", "⌫"],
    ["M+", "M-", "MR", "MC", "x!"],
    ["Copy"]
]

for i, row in enumerate(buttons, start=3):
    for j, val in enumerate(row):
        btn = tk.Button(root, text=val, font=BUTTON_FONT, bg="#ffffff", fg="#333333", relief=tk.RIDGE, bd=2)
        btn.grid(row=i, column=j, sticky="nsew", padx=3, pady=3)
        btn.bind("<Button-1>", click)

# === Bottom Buttons ===
tk.Button(root, text="Show History", font=BUTTON_FONT, bg="#2196F3", fg="white", command=show_history).grid(row=9, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
tk.Button(root, text="Dark Mode", font=BUTTON_FONT, bg="#444444", fg="white", command=toggle_dark_mode).grid(row=9, column=2, columnspan=2, sticky="nsew", padx=10, pady=10)
tk.Button(root, text="Unit Converter", font=BUTTON_FONT, bg="#9C27B0", fg="white", command=open_unit_converter).grid(row=9, column=4, sticky="nsew", padx=10, pady=10)

# === Start App ===
root.mainloop()
