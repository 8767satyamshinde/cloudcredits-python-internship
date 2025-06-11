import tkinter as tk
from tkinter import messagebox, Toplevel, PhotoImage, filedialog
from math import sqrt, sin, cos, tan, log, radians
from reportlab.pdfgen import canvas
<<<<<<< HEAD
from tkinter import messagebox, Toplevel

# To store calculation history
history = []

# Function to show history in a new popup window
=======
from datetime import datetime
import os
import webbrowser

# Store calculation history
history = []

# === Show History Function ===
>>>>>>> 9ff0dbb (Update: Improved calculator with history save to PDF)
def show_history():
    if not history:
        messagebox.showinfo("History", "No history available.")
        return

    hist_window = Toplevel(root)
    hist_window.title("Calculation History")
<<<<<<< HEAD
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
=======
    hist_window.geometry("600x800")  # Same size as calculator
    hist_window.config(bg="#f9f9f9")
    hist_window.minsize(500, 400)  # Resizable like calculator

    # === History Text Box ===
    hist_text = tk.Text(hist_window, font=("Arial", 14), wrap="word", bg="white", fg="black", relief=tk.SUNKEN, bd=4)
    hist_text.pack(expand=True, fill="both", padx=20, pady=(20, 10))
    for item in history:
        hist_text.insert(tk.END, item + "\n")
    hist_text.config(state='disabled')

    # === Save PDF Functions ===
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
        filepath = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Save History As PDF"
        )
        if filepath:
            try:
                generate_pdf(filepath)
                messagebox.showinfo("Saved", f"PDF saved at:\n{filepath}")
                webbrowser.open_new(filepath)
            except Exception as e:
                messagebox.showerror("Error", f"Save As Failed:\n{e}")

    # === Button Frame ===
    button_frame = tk.Frame(hist_window, bg="#f9f9f9")
    button_frame.pack(pady=(5, 20))

    save_btn = tk.Button(button_frame, text="Save", font=("Arial", 14), bg="#4CAF50", fg="white",
                         padx=15, pady=5, command=quick_save_pdf)
    saveas_btn = tk.Button(button_frame, text="Save As", font=("Arial", 14), bg="#2196F3", fg="white",
                           padx=15, pady=5, command=save_as_pdf)

    save_btn.pack(side=tk.LEFT, padx=15)
    saveas_btn.pack(side=tk.LEFT, padx=15)

# === Click Handler Function ===
>>>>>>> 9ff0dbb (Update: Improved calculator with history save to PDF)
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

<<<<<<< HEAD
    except Exception as e:
=======
    except Exception:
>>>>>>> 9ff0dbb (Update: Improved calculator with history save to PDF)
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# === GUI Setup ===
root = tk.Tk()
root.title("Scientific Calculator - Cloudcredits Internship")
root.geometry("600x800")
root.config(bg="#e6f2ff")

<<<<<<< HEAD
# Layout configuration
for i in range(8):
=======
# === Set icon ===
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

# === Entry box ===
entry = tk.Entry(root, font=("Arial", 24), bd=5, relief=tk.RIDGE, justify=tk.RIGHT)
entry.grid(row=1, column=0, columnspan=5, sticky="nsew", padx=10, pady=10, ipady=10)

# === Layout config ===
for i in range(9):
>>>>>>> 9ff0dbb (Update: Improved calculator with history save to PDF)
    root.grid_rowconfigure(i, weight=1)
for j in range(5):
    root.grid_columnconfigure(j, weight=1)

<<<<<<< HEAD
# Entry box
entry = tk.Entry(root, font=("Arial", 24), bd=5, relief=tk.RIDGE, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=10, ipady=10)

# Buttons layout
=======
# === Buttons layout ===
>>>>>>> 9ff0dbb (Update: Improved calculator with history save to PDF)
buttons = [
    ["7", "8", "9", "/", "√"],
    ["4", "5", "6", "*", "sin"],
    ["1", "2", "3", "-", "cos"],
    ["0", ".", "=", "+", "tan"],
    ["C", "log", "%", "**", ""]
]

<<<<<<< HEAD
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

=======
for i, row in enumerate(buttons, start=2):
    for j, val in enumerate(row):
        if val:
            btn = tk.Button(root, text=val, font=("Arial", 18), bg="#ffffff", fg="#333333", relief=tk.RIDGE, bd=2)
            btn.grid(row=i, column=j, sticky="nsew", padx=3, pady=3)
            btn.bind("<Button-1>", click)

# === History Button ===
tk.Button(root, text="Show History", font=("Arial", 18), bg="#2196F3", fg="white",
          relief=tk.RIDGE, bd=2, command=show_history).grid(row=7, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

# === Start App ===
>>>>>>> 9ff0dbb (Update: Improved calculator with history save to PDF)
root.mainloop()
