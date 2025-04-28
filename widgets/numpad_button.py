import tkinter as tk
from typing import Literal

class NumpadButton(tk.Button):
    def __init__(self, master, text, command, state="normal", bg="#bfbfbf", **kwargs):
        super().__init__(master, text=text, command=command, width=5, **kwargs)
        self.config(font=("Impact", 25), bg=bg, relief="groove")

    def change_state(self, state: Literal["disabled", "normal"]):
        self.config(state=state)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    
    def hello_world():
        custom_button

    custom_button = NumpadButton(root, "0", hello_world)
    custom_button.pack()

    root.mainloop()
