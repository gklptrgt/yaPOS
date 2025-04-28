import tkinter as tk

def create_checkout_screen(app):
    app.left_frame = tk.Frame(app.frame_checkout, bg="lavenderblush2")
    app.left_frame.place(relwidth=0.75, relheight=1.0, relx=0, rely=0)

    app.right_frame = tk.Frame(app.frame_checkout, bg="ivory2")
    app.right_frame.place(relwidth=0.25, relheight=1.0, relx=0.75, rely=0)

    app.left_frame.grid_rowconfigure(0, weight=1)
    app.left_frame.grid_rowconfigure(1, weight=1)
    app.left_frame.grid_rowconfigure(2, weight=19)
    app.left_frame.grid_columnconfigure(0, weight=1)
    app.left_frame.grid_columnconfigure(1, weight=4)

    top_section = tk.Frame(app.left_frame, bg="lightblue")
    top_section.grid(row=0, column=0, columnspan=2, sticky="nsew")

    app.second_section = tk.Frame(app.left_frame, bg="lightgreen")
    app.second_section.grid(row=1, column=0, columnspan=2, sticky="nsew")

    app.cat_section = tk.Frame(app.left_frame, bg="gray")
    app.cat_section.grid(row=2, column=0, sticky="nsew")

    right_section = tk.Frame(app.left_frame, bg="lightyellow")
    right_section.grid(row=2, column=1, sticky="nsew")

    generate_shop_buttons(app)

def generate_shop_buttons(app):
    shops = ["Kale Cafe", "Hediyelik", "personel"]
    if shops:
        app.selected_shop_button = None
        for i, shop in enumerate(shops):
            shop_button = tk.Button(app.second_section, text=shop, padx=5, pady=5, borderwidth=0, relief="solid", font=("Arial", 20))
            shop_button.config(command=lambda button=shop_button, index=shop: on_button_click(app, button, index))
            if i == 0:
                shop_button.config(bg="blue")
                app.selected_shop_button = shop_button
                print("Program Initialized selected first item in the shop list:", shop)
                generate_category_buttons(app, shop)
            shop_button.grid(row=0, column=i, padx=0, pady=0, sticky="nsew")
        for col in range(len(shops)):
            app.second_section.grid_columnconfigure(col, weight=1)
        app.second_section.grid_rowconfigure(0, weight=1)
    else:
        error_label_1 = tk.Label(app.second_section, text="Please add Category from settings!\nE001", font=("Arial", 20), bg='red', fg='white')
        error_label_1.pack(fill="both", expand=True)

def on_button_click(app, button, index):
    if app.selected_shop_button:
        app.selected_shop_button.config(bg="gray")
    button.config(bg="blue")
    app.selected_shop_button = button
    print("Selected button", index)
    generate_category_buttons(app, index)

def generate_category_buttons(app, shop):
    for widget in app.cat_section.winfo_children():
        widget.destroy()
    dumb_cat = {
        'Kale Cafe': [('Soguk Icecekler', (0, 0, 255), (255, 255, 255)), ('Sicak Icecekler', (255, 0, 0), (255, 255, 255)), ('Alkollu Icecekler', (125, 125, 0), (255, 255, 255)), ('Yiyecekler', (123, 34, 232), (1, 1, 1)), ('Salatalar', (100, 44, 9), (1, 1, 1)), ('Ice Cream', (10, 20, 100), (1, 1, 1)), ('Tatlilar', (23, 234, 11), (1, 1, 1)), ('Snacks', (222, 111, 222), (1, 1, 1))],
        'Hediyelik': [('Hediyelik', (0, 0, 255), (255, 255, 255)), ('Canta ve Cuzdan', (0, 0, 255), (255, 255, 255)), ('Kulluk', (0, 0, 255), (255, 255, 255)), ('Tabak', (0, 0, 255), (255, 255, 255)), ('Bardak', (0, 0, 255), (255, 255, 255))]
    }
    target_data = dumb_cat.get(shop, [])
    app.selected_cat_button = None
    if target_data:
        for i, cat in enumerate(target_data):
            name = cat[0]
            bg = app._from_rgb(cat[1])
            fg = app._from_rgb(cat[2])
            cat_button = tk.Button(app.cat_section, text=name, padx=5, pady=5, borderwidth=0, relief="solid", width=7, background=bg, foreground=fg, font=("Arial", 20))
            cat_button.config(command=lambda button=cat_button, index=name: on_cat_button_click(app, button, index))
            if i == 0:
                cat_button.config(border=3)
                app.selected_cat_button = cat_button
                print("Program Initialized selected first category", cat)
            cat_button.grid(row=i, column=0, padx=0, pady=0, sticky="nsew")
        for row in range(len(target_data)):
            app.cat_section.grid_rowconfigure(row, weight=1)
        app.cat_section.grid_columnconfigure(0, weight=1)
    else:
        info_label = tk.Label(app.cat_section, text="No Category found please add from settings!\nE002", width=15, background='red', foreground='white')
        info_label.grid(row=0, column=0, sticky="nsew")

def on_cat_button_click(app, button, index):
    if app.selected_cat_button:
        app.selected_cat_button.config(border=0)
    button.config(border=3)
    app.selected_cat_button = button
    print("Selected category", index)