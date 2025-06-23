Sure, Satyam! Here's a **`README.md` file** you can include in your calculator project folder. This file explains what your project is, how to run it, and how the history saving feature works.

---

## 📄 `README.md` (Place this in the same folder as your `.py` file)

````markdown
# 🔢 Scientific Calculator - Cloudcredits Internship Project

This is a **Tkinter-based Scientific Calculator** developed as part of the **Cloudcredits Internship** by Satyam Shinde.

It includes support for:
- Basic arithmetic operations
- Scientific functions (√, sin, cos, tan, log)
- Memory operations (M+, M-, MR, MC)
- Trigonometric angle handling (in degrees)
- Unit converter (Length, Weight, Temperature)
- Dark mode toggle
- Real-time clock display
- Calculation history saved **across sessions** using a `.txt` file

---

## 📦 Features

- **User-Friendly GUI:** Built with Tkinter, supporting keyboard input and mouse clicks.
- **Memory Functions:** Save and retrieve numbers using M+/M-/MR/MC.
- **Copy Function:** Easily copy result to clipboard.
- **History Log:** 
  - Saved in `history.txt` file
  - Displayed using "Show History"
  - Automatically restored when reopening the app
  - Clear history button available
- **Dark Mode:** Switch between light and dark themes.
- **Unit Converter:** Convert between various units directly within the app.

---

## ▶️ How to Run

1. Install Python (version 3.x recommended).
2. Make sure `tkinter` is available (comes by default with Python on most systems).
3. Save the main calculator script as `calculator.py`.
4. Open terminal or command prompt.
5. Navigate to the folder where `calculator.py` is saved.
6. Run the app with:
   ```bash
   python calculator.py
````

---

## 🧠 History Persistence

* All calculations are stored in `history.txt`.
* This file is automatically created/updated every time you perform a new calculation.
* When you relaunch the app, it loads the existing history so you can continue where you left off.
* You can clear the history anytime using the **"Clear History"** button in the History window.

---

## 📁 Project Structure

```
project-folder/
│
├── calculator.py        # Main Python file
├── history.txt          # Stores all past calculations (auto-created)
└── README.md            # This file (project description)
```

---

## 👨‍💻 Developer

**Satyam Shinde**
M.Tech Computer Engineering (AI)
Cloudcredits Internship Project

```


