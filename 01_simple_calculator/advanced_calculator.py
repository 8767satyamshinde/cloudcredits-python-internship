import tkinter as tk
from tkinter import messagebox, Toplevel, PhotoImage, filedialog
from math import sqrt, sin, cos, tan, log, radians
from reportlab.pdfgen import canvas
from datetime import datetime
import os
import webbrowser

# === Store History ===
history = []

# === Main Window ===
root = tk.Tk()
root.title("Scientific Calculator - Cloudcredits Internship")

# === Responsive Scaling ===
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
app_width = int(screen_width * 0.35)
app_height = int(screen_height * 0.8)
root.geometry(f"{app_width}x{app_height}")
root.minsize(500, 600)
root.config(bg="#e6f2ff")

# === Dynamic Font Sizes ===
FONT_SIZE = int(app_width * 0.025)
BUTTON_FONT = ("Arial", FONT_SIZE)
ENTRY_FONT = ("Arial", FONT_SIZE + 4)

# === Show History Function ===
def show_history():
    if not history:
        messagebox.showinfo("History", "No history available.")
        return

    hist_window = Toplevel(root)
    hist_window.title("Calculation History")
    hist_window.geometry(f"{app_width}x{app_height}")
    hist_window.config(bg="#f9f9f9")

    hist_text = tk.Text(hist_window, font=BUTTON_FONT, wrap="word", bg="white", fg="black", relief=tk.SUNKEN, bd=4)
    hist_text.pack(expand=True, fill="both", padx=20, pady=(20, 10))
    for item in history:
        hist_text.insert(tk.END, item + "\n")
    hist_text.config(state='disabled')

    def generate_pdf(path):
        c = canvas.Canvas(path)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, 800, "Calculator History")
        c.setFont("Helvetica", 12)
        c.drawString(100, 780, "Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        y = 750
        for item in history:
            c.drawString(100, y, item)
            y -= 20
            if y < 50:
                c.showPage()
                y = 800
        c.save()

    def quick_save_pdf():
        default_path = os.path.join(os.getcwd(), "calculator_history.pdf")
        try:
            generate_pdf(default_path)
            messagebox.showinfo("Saved", f"PDF saved at:\n{default_path}")
            webbrowser.open_new(default_path)
        except Exception as e:
            messagebox.showerror("Error", f"Quick Save Failed:\n{e}")

    def save_as_pdf():
        filepath = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                filetypes=[("PDF files", "*.pdf")],
                                                title="Save History As PDF")
        if filepath:
            try:
                generate_pdf(filepath)
                messagebox.showinfo("Saved", f"PDF saved at:\n{filepath}")
                webbrowser.open_new(filepath)
            except Exception as e:
                messagebox.showerror("Error", f"Save As Failed:\n{e}")

    button_frame = tk.Frame(hist_window, bg="#f9f9f9")
    button_frame.pack(pady=(5, 20))

    save_btn = tk.Button(button_frame, text="Save", font=BUTTON_FONT, bg="#4CAF50", fg="white",
                         padx=15, pady=5, command=quick_save_pdf)
    saveas_btn = tk.Button(button_frame, text="Save As", font=BUTTON_FONT, bg="#2196F3", fg="white",
                           padx=15, pady=5, command=save_as_pdf)

    save_btn.pack(side=tk.LEFT, padx=15)
    saveas_btn.pack(side=tk.LEFT, padx=15)

# === Click Function ===
def click(event):
    text = event.widget.cget("text")
    current = entry.get()

    try:
        if text == "=":
            expression = current.replace("%", "/100")
            result = eval(expression)
            result = round(result, 4)
            if not history or history[-1] != f"{current} = {result}":
                history.append(f"{current} = {result}")
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
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
                        result = log(value)
                    else:
                        entry.insert(tk.END, "Invalid (log)")
                        return
                result = round(result, 4)
                history.append(f"{text}({value}) = {result}")
                entry.insert(tk.END, result)
        else:
            entry.insert(tk.END, text)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# === Keyboard Support ===
def on_key(event):
    key = event.char
    if key in '0123456789.+-*/%':
        entry.insert(tk.END, key)
    elif key == '\r':  # Enter key
        click(type('Event', (object,), {'widget': type('W', (), {'cget': lambda s: '='})()})())
    elif key == '\x08':  # Backspace
        entry.delete(len(entry.get()) - 1, tk.END)

root.bind("<Key>", on_key)

# === Set Icon ===
try:
    root.iconbitmap("calculator.ico")
except:
    pass

# === Logo ===
try:
    logo = PhotoImage(file="logo.png")
    tk.Label(root, image=logo, bg="#e6f2ff").grid(row=0, column=0, columnspan=5, pady=(10, 0))
except:
    pass

# === Entry Widget ===
entry = tk.Entry(root, font=ENTRY_FONT, bd=5, relief=tk.RIDGE, justify=tk.RIGHT)
entry.grid(row=1, column=0, columnspan=5, sticky="nsew", padx=10, pady=10, ipady=10)

# === Grid Weighting ===
for i in range(9):
    root.grid_rowconfigure(i, weight=1)
for j in range(5):
    root.grid_columnconfigure(j, weight=1)

# === Buttons ===
buttons = [
    ["7", "8", "9", "/", "√"],
    ["4", "5", "6", "*", "sin"],
    ["1", "2", "3", "-", "cos"],
    ["0", ".", "=", "+", "tan"],
    ["C", "log", "%", "**", "⌫"]
]

for i, row in enumerate(buttons, start=2):
    for j, val in enumerate(row):
        if val:
            btn = tk.Button(root, text=val, font=BUTTON_FONT, bg="#ffffff", fg="#333333", relief=tk.RIDGE, bd=2)
            btn.grid(row=i, column=j, sticky="nsew", padx=3, pady=3)
            btn.bind("<Button-1>", click)

# === History Button ===
tk.Button(root, text="Show History", font=BUTTON_FONT, bg="#2196F3", fg="white",
          relief=tk.RIDGE, bd=2, command=show_history).grid(row=7, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

# === Start App ===
root.mainloop()
