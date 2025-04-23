from tkinter import colorchooser
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Simple Centered UI")
root.geometry("400x300")

def pick_color():
    color_code = colorchooser.askcolor(title="Choose a color")
    print("Selected color:", color_code[0])

import os

def open_keyboard():
    os.system("osk")

color_button = ttk.Button(root, text="Pick Color", command=open_keyboard)
color_button.pack(pady=10)


# Run the application
root.mainloop()
