# Advanced Calculator with History (Tkinter GUI)

This project is a fully functional GUI-based advanced calculator developed using **Python** and **Tkinter**. It supports basic arithmetic, advanced mathematical functions, and offers a complete calculation history system.

---

## ✅ Features

### 🧮 Basic Calculator Functions

* Addition, Subtraction, Multiplication, Division
* Decimal support
* Use of parentheses for expressions

### 🧠 Advanced Functions

* `sqrt(x)` : Square root
* `sin(x)` : Sine (degrees)
* `cos(x)` : Cosine (degrees)
* `tan(x)` : Tangent (degrees)
* `log(x)` : Base-10 logarithm
* `fact(x)` : Factorial (integer only)

### 📖 History Management

* ✅ **View** Calculation History
* ✅ **Clear** All Previous History
* ✅ **Save** to `history.txt` (default file)
* ✅ **Save As** with custom filename anywhere

---

## 📁 Project Structure

```
cloudcredits-python-internship/
└── 01_simple_calculator/
    ├── advanced_calculator.py         # Main Python script (Tkinter GUI)
    ├── history.txt                     # Auto-generated file to store history
    ├── dist/
    │   ├── advanced_calculator.exe     # Compiled executable
    │   └── advanced_calculator.zip     # Compressed shareable version
    └── README.md                      # Project documentation
```

---

## ▶️ How to Run

### 🔧 Prerequisites

* Python 3.6 or higher installed
* Tkinter (comes pre-installed with Python)

### 🖥 Run the app via terminal:

```bash
python advanced_calculator.py
```

> ✅ On Windows, you can also run the `.exe` directly from the `dist/` folder if you have packaged it using PyInstaller.

---

## 🛠 Build Standalone Executable (Optional)

If you want to distribute this app as an `.exe` file:

1. Install PyInstaller:

```bash
pip install pyinstaller
```

2. Navigate to your project folder:

```bash
cd 01_simple_calculator
```

3. Create executable:

```bash
pyinstaller --onefile --windowed advanced_calculator.py
```

> Output will be in the `dist/` folder.

4. (Optional) Compress for upload:

```bash
# In dist/
right-click advanced_calculator.exe ➔ Send to > Compressed (zipped) folder
```

---

## 📋 How to Use

### 📌 GUI Buttons:

* Type expressions using number & operator buttons
* Use `=` to evaluate
* Use `C` to clear
* Use `Del` to delete last character

### 📚 Menu: History

* **View History**: Opens a new window showing previous calculations
* **Clear History**: Erases all stored calculations
* **Save History**: Saves to `history.txt`
* **Save As**: Saves history to custom-named `.txt` file anywhere

---

## 👨‍💻 Author

* **Name:** Satyam Shinde
* **Internship:** Cloudcredits Python Internship
* **Project:** Advanced Tkinter GUI Calculator with Save/Export History

---

## 📌 License

This project is for educational and internship purposes. Free to modify and use.
