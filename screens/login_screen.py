import tkinter as tk

def create_login_screen(app):
    label = tk.Label(app.frame_login, text="Welcome to the POS System! Please Login.")
    label.pack(pady=20)

    username_label = tk.Label(app.frame_login, text="Username:")
    username_label.pack(padx=10, pady=5)
    username_entry = tk.Entry(app.frame_login)
    username_entry.pack(padx=10, pady=5)

    password_label = tk.Label(app.frame_login, text="Password:")
    password_label.pack(padx=10, pady=5)
    password_entry = tk.Entry(app.frame_login, show="*")
    password_entry.pack(padx=10, pady=5)

    login_button = tk.Button(app.frame_login, text="Login", command=lambda: app.show_frame(app.frame_menu))
    login_button.pack(pady=20)