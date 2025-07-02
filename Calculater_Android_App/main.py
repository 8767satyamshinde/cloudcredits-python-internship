from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from math import sqrt, sin, cos, tan, log10, radians, factorial
from datetime import datetime
import os

# === History Management (Console-based) ===
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

# === KV Layout ===
KV = """
<CalcLayout>:
    orientation: 'vertical'
    padding: 10
    spacing: 10

    TextInput:
        id: input_field
        text: ""
        font_size: 32
        size_hint_y: 0.2
        multiline: False
        readonly: True

    GridLayout:
        cols: 4
        spacing: 5
        size_hint_y: 0.7

        Button:
            text: "7"
            on_press: root.add("7")
        Button:
            text: "8"
            on_press: root.add("8")
        Button:
            text: "9"
            on_press: root.add("9")
        Button:
            text: "/"
            on_press: root.add("/")

        Button:
            text: "4"
            on_press: root.add("4")
        Button:
            text: "5"
            on_press: root.add("5")
        Button:
            text: "6"
            on_press: root.add("6")
        Button:
            text: "*"
            on_press: root.add("*")

        Button:
            text: "1"
            on_press: root.add("1")
        Button:
            text: "2"
            on_press: root.add("2")
        Button:
            text: "3"
            on_press: root.add("3")
        Button:
            text: "-"
            on_press: root.add("-")

        Button:
            text: "0"
            on_press: root.add("0")
        Button:
            text: "."
            on_press: root.add(".")
        Button:
            text: "="
            on_press: root.calculate()
        Button:
            text: "+"
            on_press: root.add("+")

        Button:
            text: "sqrt"
            on_press: root.calculate_func("sqrt")
        Button:
            text: "sin"
            on_press: root.calculate_func("sin")
        Button:
            text: "cos"
            on_press: root.calculate_func("cos")
        Button:
            text: "tan"
            on_press: root.calculate_func("tan")

        Button:
            text: "log"
            on_press: root.calculate_func("log")
        Button:
            text: "fact"
            on_press: root.calculate_func("fact")
        Button:
            text: "C"
            on_press: root.clear()
        Button:
            text: "Del"
            on_press: root.delete_last()
"""

class CalcLayout(BoxLayout):
    def add(self, value):
        self.ids.input_field.text += value

    def clear(self):
        self.ids.input_field.text = ""

    def delete_last(self):
        self.ids.input_field.text = self.ids.input_field.text[:-1]

    def calculate(self):
        try:
            expr = self.ids.input_field.text
            result = str(eval(expr))
            self.ids.input_field.text = result
            history.append(f"{expr} = {result}")
            save_history()
        except Exception:
            self.ids.input_field.text = "Error"

    def calculate_func(self, func):
        try:
            value = float(self.ids.input_field.text)
            result = {
                "sqrt": sqrt(value),
                "sin": sin(radians(value)),
                "cos": cos(radians(value)),
                "tan": tan(radians(value)),
                "log": log10(value),
                "fact": factorial(int(value))
            }.get(func, value)

            self.ids.input_field.text = str(result)
            history.append(f"{func}({value}) = {result}")
            save_history()
        except Exception:
            self.ids.input_field.text = "Error"

class CalculatorApp(App):
    def build(self):
        Builder.load_string(KV)
        return CalcLayout()

if __name__ == "__main__":
    CalculatorApp().run()
