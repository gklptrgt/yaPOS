import tkinter as tk
from widgets.menu_button import MenuButton

def create_menu_screen(app):
    top_frame = tk.Frame(app.frame_menu)
    top_frame.pack(side=tk.TOP)

    # Title at top-center
    title_label = tk.Label(top_frame, text="yaPOS", font=("Impact", 100, "bold"))
    title_label.pack()

    # Admin label under the title
    admin_label = tk.Label(top_frame, text="yet another point-of-sale", font=("Arial", 22))
    admin_label.pack()

    # Admin label under the title
    admin_label = tk.Label(app.frame_menu, text="Admin", font=("Impact", 22))
    admin_label.pack()


    # Center frame for buttons
    button_frame = tk.Frame(app.frame_menu)
    button_frame.pack()

    menu_btn = MenuButton(button_frame, text="Tables", command=None, big=True, bg="#69beec")
    menu_btn.grid(row=0, column=0, padx=10, pady=10)

    menu_btn = MenuButton(button_frame, text="Express", command=lambda: app.show_frame(app.frame_checkout), big=True, bg="#ebee77") # should enter to checkout with express mode
    menu_btn.grid(row=0, column=1, padx=10, pady=10)

    menu_btn = MenuButton(button_frame, text="Stocks", command=lambda: app.show_frame(app.frame_stocks), big=True, bg="#84e9b4")
    menu_btn.grid(row=0, column=2, padx=10, pady=10)

    menu_btn = MenuButton(button_frame, text="Reports", command=None, big=True, bg="#eda0b4")
    menu_btn.grid(row=1, column=0, padx=10, pady=10)

    menu_btn = MenuButton(button_frame, text="Settings", command=lambda: app.show_frame(app.frame_settings), big=True, bg="#a9d2d5")
    menu_btn.grid(row=1, column=1, padx=10, pady=10)

    menu_btn = MenuButton(button_frame, text="Help", command=None, big=True, bg="#f0b07b")
    menu_btn.grid(row=1, column=2, padx=10, pady=10)

    menu_btn = MenuButton(button_frame, text="Logout", command=lambda: app.show_frame(app.frame_login), big=True, bg="#edbbe5") #logout function
    menu_btn.grid(row=2, column=1, padx=10, pady=10)