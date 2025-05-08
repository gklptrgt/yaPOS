import tkinter as tk
import tkinter.font as tkFont
from typing import Literal


class CheckoutButton(tk.Button):
    def __init__(self, master, text, command=None, state:Literal["disabled", "normal"]="normal",font_size=20,width=10,height=1, bg="#bfbfbf",fg="#000000",**kwargs):
        super().__init__(master, text=text, command=command, **kwargs)
        
        font = tkFont.Font(family="Calibri", size=font_size)
        avg_char_width = font.measure("0")  # Approximate width of a character
        button_width_pixels = avg_char_width * width  # width=10 in characters
        wraplength = int(button_width_pixels * 0.9)
        
        self.config(font=("Calibri", font_size, "bold"),width=width,height=height,fg=fg, bg=bg, relief="groove",wraplength=wraplength, state=state)

    def change_state(self, state: Literal["disabled", "normal"]):
        self.config(state=state)

    def add_border(self):
        self.config(border=6)

    def remove_border(self):
        self.config(border=0)  


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    
    def hello_world():
        custom_button

    custom_button = CheckoutButton(master=root, text="Hello World", command=hello_world, width=11)
    custom_button.pack()

    custom_button.add_border()

    root.mainloop()
