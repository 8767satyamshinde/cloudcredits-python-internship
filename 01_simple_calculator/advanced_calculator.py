import tkinter as tk
from math import sqrt, sin, cos, tan, log, radians

def click(event):
    text = event.widget.cget("text")
    current = entry.get()

    try:
        if text == "=":
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)

        elif text == "C":
            entry.delete(0, tk.END)

        elif text in ["√", "sin", "cos", "tan", "log"]:
            if current == "":
                entry.delete(0, tk.END)
                entry.insert(tk.END, "Enter number first")
            else:
                value = float(current)
                entry.delete(0, tk.END)

                if text == "√":
                    entry.insert(tk.END, sqrt(value))
                elif text == "sin":
                    entry.insert(tk.END, sin(radians(value)))
                elif text == "cos":
                    entry.insert(tk.END, cos(radians(value)))
                elif text == "tan":
                    entry.insert(tk.END, tan(radians(value)))
                elif text == "log":
                    if value > 0:
                        entry.insert(tk.END, log(value))
                    else:
                        entry.insert(tk.END, "Invalid (log)")
        else:
            entry.insert(tk.END, text)

    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# GUI Setup
root = tk.Tk()
root.title("Scientific Calculator - Cloudcredits Internship")
root.geometry("600x700")  
root.minsize(400, 500)     
root.config(bg="#e6f2ff")


for i in range(6):  # Total rows
    root.grid_rowconfigure(i, weight=1)
for j in range(5):  # Total columns
    root.grid_columnconfigure(j, weight=1)

# Entry box
entry = tk.Entry(root, font=("Arial", 24), bd=5, relief=tk.RIDGE, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=20, ipady=10)


buttons = [
    ["7", "8", "9", "/", "√"],
    ["4", "5", "6", "*", "sin"],
    ["1", "2", "3", "-", "cos"],
    ["0", ".", "=", "+", "tan"],
    ["C", "log", "%", "**", ""]
]

# Create buttons
for i, row_values in enumerate(buttons, start=1):
    for j, val in enumerate(row_values):
        if val != "":
            btn = tk.Button(
                root, text=val, font=("Arial", 18),
                bg="#ffffff", fg="#333333",
                relief=tk.RIDGE, bd=2
            )
            btn.grid(row=i, column=j, sticky="nsew", padx=3, pady=3)
            btn.bind("<Button-1>", click)

root.mainloop()
