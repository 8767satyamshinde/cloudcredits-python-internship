import tkinter as tk
from math import sqrt, sin, cos, tan, log, radians
from reportlab.pdfgen import canvas
from tkinter import messagebox, Toplevel

# To store calculation history
history = []

# Function to show history in a new popup window
def show_history():
    if not history:
        messagebox.showinfo("History", "No history available.")
        return

    hist_window = Toplevel(root)
    hist_window.title("Calculation History")
    hist_window.geometry("400x300")
    hist_window.config(bg="#f9f9f9")

    hist_text = tk.Text(hist_window, font=("Arial", 12), wrap="word")
    hist_text.pack(expand=True, fill="both", padx=10, pady=10)

    for item in history:
        hist_text.insert(tk.END, item + "\n")

    hist_text.config(state='disabled')

# PDF download function
def download_pdf():
    if not history:
        messagebox.showinfo("No History", "No calculations to download.")
        return
    c = canvas.Canvas("Calculator_History.pdf")
    c.setFont("Helvetica", 14)
    c.drawString(100, 800, "Calculator History:")
    y = 770
    for item in history:
        c.drawString(100, y, item)
        y -= 20
        if y < 50:
            c.showPage()
            y = 800
    c.save()
    messagebox.showinfo("PDF Downloaded", "Calculator_History.pdf saved successfully!")

# Calculator click handler
def click(event):
    text = event.widget.cget("text")
    current = entry.get()

    try:
        if text == "=":
            result = eval(current)
            history.append(f"{current} = {result}")
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
                    result = sqrt(value)
                elif text == "sin":
                    result = sin(radians(value))
                elif text == "cos":
                    result = cos(radians(value))
                elif text == "tan":
                    result = tan(radians(value))
                elif text == "log":
                    if value > 0:
                        result = log(value)
                    else:
                        entry.insert(tk.END, "Invalid (log)")
                        return
                history.append(f"{text}({value}) = {result}")
                entry.insert(tk.END, result)
        else:
            entry.insert(tk.END, text)

    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# GUI Setup
root = tk.Tk()
root.title("Scientific Calculator - Cloudcredits Internship")
root.geometry("600x800")
root.config(bg="#e6f2ff")

# Layout configuration
for i in range(8):
    root.grid_rowconfigure(i, weight=1)
for j in range(5):
    root.grid_columnconfigure(j, weight=1)

# Entry box
entry = tk.Entry(root, font=("Arial", 24), bd=5, relief=tk.RIDGE, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=10, ipady=10)

# Buttons layout
buttons = [
    ["7", "8", "9", "/", "√"],
    ["4", "5", "6", "*", "sin"],
    ["1", "2", "3", "-", "cos"],
    ["0", ".", "=", "+", "tan"],
    ["C", "log", "%", "**", ""]
]

# Create calculator buttons
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

# PDF Download Button
pdf_btn = tk.Button(
    root, text="Download PDF", font=("Arial", 18),
    bg="#4CAF50", fg="white", relief=tk.RIDGE, bd=2,
    command=download_pdf
)
pdf_btn.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

# History Button
hist_btn = tk.Button(
    root, text="Show History", font=("Arial", 18),
    bg="#2196F3", fg="white", relief=tk.RIDGE, bd=2,
    command=show_history
)
hist_btn.grid(row=6, column=2, columnspan=3, sticky="nsew", padx=10, pady=10)

root.mainloop()
