# advance calulater using tkinter
import tkinter as tk
from math import sqrt

def click(event):
    text = event.widget.cget("text")
    current = entry.get()

    if text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "√":
        try:
            value = float(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, sqrt(value))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Advanced Calculator - Cloudcredits Internship")
root.geometry("320x450")
root.resizable(False, False)
root.config(bg="#f0f0f0")

entry = tk.Entry(root, font=("Arial", 20), borderwidth=3, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, padx=10, pady=15, ipady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "√", "%", "**"]
]

for row_values in buttons:
    row_frame = tk.Frame(root, bg="#f0f0f0")
    row_frame.pack(expand=True, fill="both")
    for val in row_values:
        btn = tk.Button(
            row_frame, text=val, font=("Arial", 16),
            bg="#ffffff", fg="#333333", width=6, height=2,
            relief=tk.GROOVE, borderwidth=1
        )
        btn.pack(side=tk.LEFT, expand=True, fill="both", padx=2, pady=2)
        btn.bind("<Button-1>", click)

root.mainloop()