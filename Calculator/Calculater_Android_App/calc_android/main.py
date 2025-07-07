from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput as InputBox
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.utils import platform
from kivy.metrics import dp, sp
from datetime import datetime
from math import sqrt, sin, cos, tan, log10, radians, factorial
import os

# Vibration for Android
if platform == 'android':
    from plyer import vibrator

# Desktop: fix window size
if platform != 'android':
    Window.size = (360, 640)

# History file setup
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

def clear_history():
    history.clear()
    save_history()

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class CalculatorLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dark_mode = False
        self.history_visible = True

        self.main_layout = BoxLayout(orientation='vertical', spacing=dp(4), size_hint=(1, 1))
        self.add_widget(self.main_layout)

        # === Display Area ===
        self.result = TextInput(
            font_size=sp(22),
            size_hint=(1, None),
            height=dp(50),
            multiline=False,
            halign="right",
            padding=(dp(10), dp(10)),
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1)
        )
        self.main_layout.add_widget(self.result)

        scroll = ScrollView(size_hint=(1, None), size=(Window.width, dp(100)))
        self.history_display = TextInput(
            font_size=sp(16),
            readonly=True,
            size_hint_y=None,
            height=dp(100),
            background_color=(0.95, 0.95, 0.95, 1),
            foreground_color=(0, 0, 0, 1)
        )
        scroll.add_widget(self.history_display)
        self.main_layout.add_widget(scroll)
        self.update_history_display()

        self.click_sound = SoundLoader.load("click.wav")
        self.history_button_ref = None

        # Buttons layout
        self.button_labels = [
            '7', '8', '9', '/', 'sqrt',
            '4', '5', '6', '*', 'sin',
            '1', '2', '3', '-', 'cos',
            '0', '.', '=', '+', 'tan',
            '(', ')', 'C', 'Del', 'log',
            'fact', 'History', 'Clear History', 'Save As', 'Theme'
        ]
        self.build_button_grid()

    def build_button_grid(self):
        self.button_grid = GridLayout(
            cols=5,
            spacing=dp(4),
            padding=dp(4),
            size_hint=(1, 1)
        )
        for label in self.button_labels:
            btn = Button(
                text=label,
                font_size=sp(18),
                size_hint=(1, None),
                height=dp(60),
                background_normal='',
                background_color=self.get_button_color(label),
                color=(1, 1, 1, 1)
            )
            if label == "History":
                self.history_button_ref = btn
            btn.bind(on_press=self.on_button_press)
            self.button_grid.add_widget(btn)
        self.main_layout.add_widget(self.button_grid)

    def get_button_color(self, label):
        if label in ['=', 'C', 'Del', 'History', 'Clear History', 'Save As', 'Theme']:
            return (0.1, 0.5, 0.6, 1)
        elif label in ['sqrt', 'sin', 'cos', 'tan', 'log', 'fact']:
            return (0.5, 0.2, 0.6, 1)
        else:
            return (0.2, 0.2, 0.2, 1)

    def update_history_display(self):
        self.history_display.text = load_history()

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        bg = (0.1, 0.1, 0.1, 1) if self.dark_mode else (1, 1, 1, 1)
        fg = (1, 1, 1, 1) if self.dark_mode else (0, 0, 0, 1)
        self.result.background_color = bg
        self.result.foreground_color = fg
        self.history_display.background_color = bg
        self.history_display.foreground_color = fg

        for child in self.button_grid.children:
            child.background_color = (0.2, 0.2, 0.2, 1) if self.dark_mode else self.get_button_color(child.text)
            child.color = fg

    def show_popup(self, message):
        popup = Popup(title='Info', content=Label(text=message),
                      size_hint=(None, None), size=(dp(300), dp(150)))
        popup.open()

    def show_save_as_popup(self):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        input_box = InputBox(hint_text="Enter filename (with .txt)", multiline=False)
        confirm_btn = Button(text="Save", size_hint=(1, 0.3))
        content.add_widget(input_box)
        content.add_widget(confirm_btn)
        popup = Popup(title='Save History As', content=content,
                      size_hint=(None, None), size=(dp(350), dp(180)))

        def save_file(instance):
            filename = input_box.text.strip()
            if filename:
                try:
                    with open(filename, "w") as f:
                        f.write('\n'.join(history))
                    popup.dismiss()
                    self.show_popup(f"History saved as '{filename}'")
                except:
                    self.show_popup("Failed to save file.")
            else:
                self.show_popup("Filename cannot be empty.")

        confirm_btn.bind(on_press=save_file)
        popup.open()

    def play_feedback(self):
        if platform == 'android':
            vibrator.vibrate(0.03)
        if self.click_sound:
            self.click_sound.play()

    def on_button_press(self, instance):
        self.play_feedback()
        text = instance.text

        if text == "Theme":
            self.toggle_theme()
        elif text == "Clear History":
            clear_history()
            self.update_history_display()
            self.show_popup("History cleared.")
        elif text == "Save As":
            self.show_save_as_popup()
        elif text == "=":
            try:
                expr = self.result.text
                answer = str(eval(expr))
                entry = f"{timestamp()} | {expr} = {answer}"
                history.append(entry)
                save_history()
                self.result.text = answer
                self.update_history_display()
            except:
                self.result.text = "Error"
        elif text == "C":
            self.result.text = ""
        elif text == "Del":
            self.result.text = self.result.text[:-1]
        elif text == "History":
            self.history_visible = not self.history_visible
            self.history_display.opacity = 1 if self.history_visible else 0
            self.history_display.disabled = not self.history_visible
            self.history_button_ref.text = "Hide History" if self.history_visible else "Show History"
        elif text in ["sqrt", "sin", "cos", "tan", "log", "fact"]:
            try:
                value = float(self.result.text)
                if text == "sqrt":
                    result = sqrt(value)
                elif text == "sin":
                    result = sin(radians(value))
                elif text == "cos":
                    result = cos(radians(value))
                elif text == "tan":
                    result = tan(radians(value))
                elif text == "log":
                    result = log10(value)
                elif text == "fact":
                    result = factorial(int(value))
                entry = f"{timestamp()} | {text}({value}) = {result}"
                history.append(entry)
                save_history()
                self.result.text = str(result)
                self.update_history_display()
            except:
                self.result.text = "Error"
        else:
            self.result.text += text

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

if __name__ == '__main__':
    CalculatorApp().run()
