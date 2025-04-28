import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor
from screens.stocks_screen import create_stocks_screen

def create_add_item_screen(app, current_mode: str, barcode=None):
    app.show_frame(app.frame_add_item)
    app.bg_color = "#E5E5E5"
    app.fg_color = "#000000"

    def go_back():
        print("Back button pressed!")
        app.show_frame(app.frame_stocks)
        for widget in app.frame_add_item.winfo_children():
            widget.destroy()

    def choose_fg_color():
        color = askcolor()[1]
        if color:
            print(f"Selected Foreground Color: {color}")
            no_action_button.config(fg=color)
            app.fg_color = color

    def choose_bg_color():
        color = askcolor()[1]
        if color:
            print(f"Selected Background Color: {color}")
            no_action_button.config(bg=color)
            app.bg_color = color

    def check_upload_data(data):
        is_error = False
        for key, value in data.items():
            if value in (None, "", []):
                if key == "cat":
                    app.category_error_label.grid(row=0, column=2, padx=10, pady=5)
                if key == "subcat":
                    app.subcategory_error_label.grid(row=1, column=2, padx=10, pady=5)
                if key == "barcode":
                    app.barcode_error_empty_label.grid(row=2, column=2, padx=10, pady=5)
                if key == "name":
                    app.name_error_label.grid(row=3, column=2, padx=10, pady=5)
                if key == "price":
                    app.price_error_label.grid(row=4, column=2, padx=10, pady=5)
                if key == "stock":
                    app.stock_error_label.grid(row=5, column=2, padx=10, pady=5)
                if key == "notes":
                    continue
                print(f"Error: '{key}' is empty.")
                is_error = True
        return not is_error

    def check_barcode_exists(barcode):
        value = app.db.get_barcode(barcode)
        return bool(value)

    def add_item():
        app.category_error_label.grid_forget()
        app.subcategory_error_label.grid_forget()
        app.barcode_error_empty_label.grid_forget()
        app.name_error_label.grid_forget()
        app.price_error_label.grid_forget()
        app.stock_error_label.grid_forget()
        app.barcode_error_exists_label.grid_forget()

        upload_data = {
            'cat': app.category_combobox.get(),
            'subcat': app.subcategory_combobox.get(),
            'barcode': app.barcode_entry.get(),
            'name': app.name_entry.get(),
            'price': app.price_entry.get(),
            'stock': app.stock_entry.get(),
            'notes': app.notes_entry.get(),
            'no-stock': app.no_stock_var.get(),
            'bg_color': app.bg_color,
            'fg_color': app.fg_color
        }
        print(current_mode)
        if current_mode == "Add":
            if check_upload_data(upload_data):
                print("Can Continue to add data it's not empty.")
                if check_barcode_exists(upload_data['barcode']):
                    app.barcode_error_exists_label.grid(row=2, column=2, padx=10, pady=5)
                    print("barcode exists")
                else:
                    print(upload_data)
                    app.db.insert_new_menu_item(upload_data)
                    for widget in app.frame_stocks.winfo_children():
                        widget.destroy()
                    for widget in app.frame_add_item.winfo_children():
                        widget.destroy()
                    create_stocks_screen(app)
                    app.show_frame(app.frame_stocks)
            else:
                print("It's empty")
        else:
            app.db.update_menu_item(upload_data)
            for widget in app.frame_stocks.winfo_children():
                widget.destroy()
            for widget in app.frame_add_item.winfo_children():
                widget.destroy()
            create_stocks_screen(app)
            app.show_frame(app.frame_stocks)

    def update_subcategories(event=None):
        selected_name = app.category_combobox.get()
        category_id = app.category_dict.get(selected_name)
        if category_id is not None:
            subcat_data = app.db.get_subcat_from_cat(category_id)
            subcategories = [row[0] for row in subcat_data]
            app.subcategory_combobox["values"] = subcategories
            app.subcategory_combobox.set("")

    def update_no_action_button(*args):
        no_action_button.config(text=app.name_var.get())

    app.frame = tk.Frame(app.frame_add_item)
    app.frame.pack(fill="both", expand=True, padx=10, pady=10)

    top_frame = tk.Frame(app.frame)
    top_frame.pack(fill="x", pady=10)

    back_button = tk.Button(top_frame, text="Back", command=go_back)
    back_button.pack(side="left")

    title_text = "Add Item" if current_mode == "Add" else "Edit Item"
    label_add_item = tk.Label(top_frame, text=title_text, font=("Arial", 18))
    label_add_item.pack(side="left", padx=50)

    form_frame = tk.Frame(app.frame)
    form_frame.pack(fill="both", expand=True, pady=20)

    category_list = app.db.get_categories()
    app.category_dict = {row[1]: row[0] for row in category_list}
    only_name_category = [name[1] for name in category_list]

    label_category = tk.Label(form_frame, text="Category:")
    label_category.grid(row=0, column=0, sticky="w", pady=5)
    app.category_combobox = ttk.Combobox(form_frame, values=only_name_category, state="readonly")
    app.category_combobox.grid(row=0, column=1, padx=10, pady=5)
    app.category_combobox.bind("<<ComboboxSelected>>", update_subcategories)

    app.category_error_label = tk.Label(form_frame, text="Category cannot be empty!", foreground='red')

    label_subcategory = tk.Label(form_frame, text="Subcategory:")
    label_subcategory.grid(row=1, column=0, sticky="w", pady=5)
    app.subcategory_combobox = ttk.Combobox(form_frame, values=["Choose a category"])
    app.subcategory_combobox.grid(row=1, column=1, padx=10, pady=5)

    app.subcategory_error_label = tk.Label(form_frame, text="Subcategory cannot be empty!", foreground='red')

    label_barcode = tk.Label(form_frame, text="Barcode:")
    label_barcode.grid(row=2, column=0, sticky="w", pady=5)
    app.barcode_entry = ttk.Entry(form_frame)
    app.barcode_entry.grid(row=2, column=1, padx=10, pady=5)

    app.barcode_error_empty_label = tk.Label(form_frame, text="Barcode cannot be empty!", foreground='red')
    app.barcode_error_exists_label = tk.Label(form_frame, text="Barcode already exists!", foreground='orange')

    app.name_var = tk.StringVar()
    label_name = tk.Label(form_frame, text="Name:")
    label_name.grid(row=3, column=0, sticky="w", pady=5)
    app.name_entry = ttk.Entry(form_frame, textvariable=app.name_var)
    app.name_entry.grid(row=3, column=1, padx=10, pady=5)
    app.name_var.trace_add("write", update_no_action_button)

    app.name_error_label = tk.Label(form_frame, text="Name cannot be empty!", foreground='red')

    label_price = tk.Label(form_frame, text="Price:")
    label_price.grid(row=4, column=0, sticky="w", pady=5)
    app.price_entry = ttk.Entry(form_frame)
    app.price_entry.grid(row=4, column=1, padx=10, pady=5)

    app.price_error_label = tk.Label(form_frame, text="Price cannot be empty!", foreground='red')

    label_stock = tk.Label(form_frame, text="Stock:")
    label_stock.grid(row=5, column=0, sticky="w", pady=5)
    app.stock_entry = ttk.Entry(form_frame)
    app.stock_entry.grid(row=5, column=1, padx=10, pady=5)

    app.stock_error_label = tk.Label(form_frame, text="Stock cannot be empty!", foreground='red')

    label_notes = tk.Label(form_frame, text="Notes:")
    label_notes.grid(row=6, column=0, sticky="w", pady=5)
    app.notes_entry = ttk.Entry(form_frame)
    app.notes_entry.grid(row=6, column=1, padx=10, pady=5)

    app.no_stock_var = tk.BooleanVar()
    app.no_stock_checkbox = tk.Checkbutton(form_frame, text="No Stock", variable=app.no_stock_var)
    app.no_stock_checkbox.grid(row=7, column=0, columnspan=2, pady=10)

    label_fg_color = tk.Label(form_frame, text="Foreground Color:")
    label_fg_color.grid(row=8, column=0, sticky="w", pady=5)
    app.foreground_button = tk.Button(form_frame, text="Pick Color", command=choose_fg_color)
    app.foreground_button.grid(row=8, column=1, padx=10, pady=5)

    label_bg_color = tk.Label(form_frame, text="Background Color:")
    label_bg_color.grid(row=9, column=0, sticky="w", pady=5)
    app.background_button = tk.Button(form_frame, text="Pick Color", command=choose_bg_color)
    app.background_button.grid(row=9, column=1, padx=10, pady=5)

    no_action_button = tk.Button(form_frame, text="Add Name", padx=10, pady=10, borderwidth=0, relief="solid", width=10, height=2, background=app.bg_color, foreground=app.fg_color, font=("Arial", 18))
    no_action_button.grid(row=10, column=0, columnspan=5, pady=20)

    add_button = tk.Button(app.frame, text="Save", command=add_item)
    add_button.pack(pady=10)

    if current_mode == "Edit":
        print("Edit mode")
        print(barcode)
        edit_item_data = app.db.get_specific_menu_item(barcode)
        app.category_combobox.set(edit_item_data[1])
        app.subcategory_combobox.set(edit_item_data[2])
        app.name_var.set(edit_item_data[3])
        app.price_entry.insert(0, edit_item_data[4])
        app.stock_entry.insert(0, edit_item_data[5])
        app.notes_entry.insert(0, edit_item_data[10])
        app.barcode_entry.insert(0, barcode)
        no_action_button.config(bg=edit_item_data[11], fg=edit_item_data[12])
        app.no_stock_var.set(edit_item_data[7] == "True")
    elif current_mode == "Add":
        print("add mode")