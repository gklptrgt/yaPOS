import tkinter as tk
from widgets.menu_button import MenuButton

def create_settings_screen(app):
    def show_frame(frame):
        frame.tkraise()
        for name, btn in tab_buttons.items():
            if name == frame:
                btn.config(bd=1, bg="#ffa962")
            else:
                btn.config(bd=1, bg="#bfbfbf")

    app.frame_settings.grid_columnconfigure(0, weight=1)
    app.frame_settings.grid_columnconfigure(1, weight=9)
    app.frame_settings.grid_rowconfigure(0, weight=1)

    left_frame = tk.Frame(app.frame_settings, bg="lightgray")
    left_frame.grid(row=0, column=0, sticky="nsew")

    right_frame = tk.Frame(app.frame_settings)
    right_frame.grid(row=0, column=1, sticky="nsew")

    shop_page = tk.Frame(right_frame, bg='green')
    shop_page.grid(row=0, column=0, sticky="nsew")
    label = tk.Label(shop_page, text="TAB: SHOP", font=("Arial", 24))
    label.pack(expand=True)

    tables_page = tk.Frame(right_frame, bg='orange')
    tables_page.grid(row=0, column=0, sticky="nsew")
    label = tk.Label(tables_page, text="TAB: Tables", font=("Arial", 24))
    label.pack(expand=True)

    cat_page = tk.Frame(right_frame, bg='blue')
    cat_page.grid(row=0, column=0, sticky="nsew")
    label = tk.Label(cat_page, text="TAB: CATEGORY", font=("Arial", 24))
    label.pack(expand=True)

    subcat_page = tk.Frame(right_frame, bg='hotpink')
    subcat_page.grid(row=0, column=0, sticky="nsew")
    label = tk.Label(subcat_page, text="TAB: SUBCATEGORY", font=("Arial", 24))
    label.pack(expand=True)

    users_page = tk.Frame(right_frame, bg='black')
    users_page.grid(row=0, column=0, sticky="nsew")
    label = tk.Label(users_page, text="TAB: USERS", font=("Arial", 24))
    label.pack(expand=True)

    exchange_page = tk.Frame(right_frame)
    exchange_page.grid(row=0, column=0, sticky="nsew")
    label = tk.Label(exchange_page, text="Exchange Rates", font=("Arial", 24))
    label.pack(expand=True)

    tab_buttons = {}

    settings_label = tk.Label(left_frame, text="Settings", font=("Impact", 50), bg="lightgray")
    settings_label.pack(fill='x', padx=5, pady=5)

    btn_shop = MenuButton(left_frame, text="Shop", command=lambda: show_frame(shop_page))
    btn_shop.pack(fill='x', padx=5, pady=5)
    tab_buttons[shop_page] = btn_shop

    btn_tables = MenuButton(left_frame, text="Tables", command=lambda: show_frame(tables_page))
    btn_tables.pack(fill='x', padx=5, pady=5)
    tab_buttons[tables_page] = btn_tables

    btn_cat = MenuButton(left_frame, text="Categories", command=lambda: show_frame(cat_page))
    btn_cat.pack(fill='x', padx=5, pady=5)
    tab_buttons[cat_page] = btn_cat

    btn_subcat = MenuButton(left_frame, text="Subcategories", command=lambda: show_frame(subcat_page))
    btn_subcat.pack(fill='x', padx=5, pady=5)
    tab_buttons[subcat_page] = btn_subcat

    btn_users = MenuButton(left_frame, text="Users", command=lambda: show_frame(users_page))
    btn_users.pack(fill='x', padx=5, pady=5)
    tab_buttons[users_page] = btn_users
    
    btn_exc = MenuButton(left_frame, text="Exchange Rates", command=lambda: show_frame(exchange_page))
    btn_exc.pack(fill='x', padx=5, pady=5)
    tab_buttons[exchange_page] = btn_exc


    btn_back = MenuButton(left_frame, text="Back", command=lambda: app.show_frame(app.frame_menu), bg="#FFAEB5")
    btn_back.pack(fill='x', padx=5, pady=5)


    app.euro_var = tk.StringVar()
    app.dollar_var = tk.StringVar()
    app.sterlin_var = tk.StringVar()

    euro, dollar, sterlin = app.db.get_exchange()
    if euro and dollar and sterlin:
        app.euro_var.set(str(euro))
        app.dollar_var.set(str(dollar))
        app.sterlin_var.set(str(sterlin))
    else:
        app.euro_var.set("1")
        app.dollar_var.set("1")
        app.sterlin_var.set("1")

    row1 = tk.Frame(exchange_page)
    row1.pack(fill='x', pady=5)
    label1 = tk.Label(row1, text="Dollar $", width=12, anchor='e')
    label1.pack(side='left')
    dollar_entry = tk.Entry(row1, state="disabled", textvariable=app.dollar_var)
    dollar_entry.pack(side='left', fill='x', expand=True)

    row2 = tk.Frame(exchange_page)
    row2.pack(fill='x', pady=5)
    label2 = tk.Label(row2, text="Euro €", width=12, anchor='e')
    label2.pack(side='left')
    euro_entry = tk.Entry(row2, state="disabled", textvariable=app.euro_var)
    euro_entry.pack(side='left', fill='x', expand=True)

    row3 = tk.Frame(exchange_page)
    row3.pack(fill='x', pady=5)
    label3 = tk.Label(row3, text="Sterlin £", width=12, anchor='e')
    label3.pack(side='left')
    sterlin_entry = tk.Entry(row3, state="disabled", textvariable=app.sterlin_var)
    sterlin_entry.pack(side='left', fill='x', expand=True)

    buttons_frame = tk.Frame(exchange_page)
    buttons_frame.pack(pady=20)

    edit_button = tk.Button(buttons_frame, text="Edit", command=lambda: edit_exchange())
    edit_button.pack(side='left', padx=10)

    save_button = tk.Button(buttons_frame, text="Save", state="disabled", command=lambda: save_exchange())
    save_button.pack(side='left', padx=10)

    def edit_exchange():
        for name, btn in tab_buttons.items():
            btn.config(state='disabled')
        dollar_entry.config(state='normal')
        euro_entry.config(state='normal')
        sterlin_entry.config(state='normal')
        save_button.config(state='normal')
        edit_button.config(state="disabled")

    def save_exchange():
        for name, btn in tab_buttons.items():
            btn.config(state='normal')
        dollar_entry.config(state='disabled')
        euro_entry.config(state='disabled')
        sterlin_entry.config(state='disabled')
        save_button.config(state='disabled')
        edit_button.config(state="normal")
        euro = float(app.euro_var.get())
        dollar = float(app.dollar_var.get())
        sterlin = float(app.sterlin_var.get())
        app.db.update_exchange(euro=euro, dollar=dollar, sterlin=sterlin)

    show_frame(shop_page)