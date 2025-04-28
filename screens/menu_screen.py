import tkinter as tk

def create_menu_screen(app):
    label = tk.Label(app.frame_menu, text="Menu Screen", font=('Arial', 18))
    label.pack(pady=20)

    sale_button = tk.Button(app.frame_menu, text="Start Sale", command=lambda: app.show_frame(app.frame_checkout))
    sale_button.pack(pady=10)

    stock_button = tk.Button(app.frame_menu, text="Stocks", command=lambda: app.show_frame(app.frame_stocks))
    stock_button.pack(pady=10)

    settings_button = tk.Button(app.frame_menu, text="Settings", command=lambda: app.show_frame(app.frame_settings))
    settings_button.pack(pady=10)

    back_button = tk.Button(app.frame_menu, text="Logout", command=lambda: app.show_frame(app.frame_login))
    back_button.pack(pady=10)