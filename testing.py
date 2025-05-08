import tkinter as tk
from tkinter import ttk
from widgets.numpad_button import NumpadButton
class NumpadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Numpad Example")
        self.root.geometry("700x500")

        self.code = ""  # Store entered digits

        # ===== Top Frame for Title and Subtitle =====
        top_frame = tk.Frame(root)
        top_frame.pack(side=tk.TOP, pady=20)

        # Title at top-center
        title_label = tk.Label(top_frame, text="yaPOS", font=("Impact", 100, "bold"))
        title_label.pack()

        # Admin label under the title
        admin_label = tk.Label(top_frame, text="yet another point-of-sale", font=("Arial", 22))
        admin_label.pack()

        # ===== Main Middle Frame =====
        middle_frame = tk.Frame(root)
        middle_frame.pack(expand=True,fill="both")

        # Right Frame for Numpad
        right_frame = tk.Frame(middle_frame)
        right_frame.pack(side="right",fill="both", expand=True, padx=50)

        # Label above numpad (hidden initially)
        self.password_label = tk.Label(right_frame, text="", font=("Impact", 100))
        self.password_label.pack(pady=10)

        # Frame for Numpad buttons
        numpad_frame = tk.Frame(right_frame)
        numpad_frame.pack()

        # Create numpad buttons
        buttons = [
            ('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
            ('0', 3, 1),
        ]

        for (text, row, column) in buttons:
            btn = NumpadButton(numpad_frame, text=text,command=lambda t=text: self.press_number(t))
            btn.grid(row=row, column=column, padx=5, pady=5)

    def press_number(self, num):
        if len(self.code) < 4:
            code += num
            # Show * for each entered number
            self.password_label.config(text="*" * len(code), fg="black")

        if len(code) == 4:
            print("Code entered:", self.code)
            if code == "0000":
                print("Enter")

            else:
                code = ""
                password_label.config(text="XXX",fg="#FF413F")

root = tk.Tk()
app = NumpadApp(root)
root.mainloop()
