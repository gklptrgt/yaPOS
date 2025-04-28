import tkinter as tk
from typing import Literal

class MenuButton(tk.Button):
    def __init__(self, master, text, command, state="normal", big=None, bg="#bfbfbf", **kwargs):
        super().__init__(master, text=text, command=command, **kwargs)
        self.config(font=("Impact", 20), bg=bg, relief="groove")

        if big:
            self.config(font=("Impact", 50), width=15, height=2)

    def change_state(self, state: Literal["disabled", "normal"]):
        self.config(state=state)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    
    def hello_world():
        custom_button

    custom_button = MenuButton(root, "Settings", hello_world, big=True)
    custom_button.pack()

    root.mainloop()
