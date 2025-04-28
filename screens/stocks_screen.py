import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

def create_stocks_screen(app):
    def treeview_sort_column(treeview, col, reverse):
        data = [(treeview.set(k, col), k) for k in treeview.get_children("")]
        try:
            data.sort(key=lambda t: float(t[0]), reverse=reverse)
        except ValueError:
            data.sort(key=lambda t: t[0], reverse=reverse)
        for index, (val, k) in enumerate(data):
            treeview.move(k, "", index)
        if reverse:
            treeview.heading(col, text=f"{col} ↓", command=lambda: treeview_sort_column(treeview, col, False))
        else:
            treeview.heading(col, text=f"{col} ↑", command=lambda: treeview_sort_column(treeview, col, True))
        for other_col in treeview["columns"]:
            if other_col != col:
                treeview.heading(other_col, text=other_col, command=lambda _col=other_col: treeview_sort_column(treeview, _col, False))

    def show_selected():
        selected_item = tree.focus()
        if selected_item:
            values = tree.item(selected_item, "values")
            print("Selected Row:", values)

    def add_item():
        print("add pressed")
        app.show_add_item_screen(current_mode="Add")  # Delegate to POSApp

    def edit_item():
        values = None
        selected_item = tree.focus()
        if selected_item:
            values = tree.item(selected_item, "values")
            print("Selected Row:", values)
        if values:
            app.show_add_item_screen(current_mode="Edit", barcode=values[0])  # Delegate to POSApp
            print("Edit pressed")
        else:
            print("Not selected item")

    app.frame_stocks.grid_rowconfigure(1, weight=9)
    app.frame_stocks.grid_rowconfigure(0, weight=1)
    app.frame_stocks.grid_columnconfigure(0, weight=1)

    top_frame = tk.Frame(app.frame_stocks)
    top_frame.grid(row=0, column=0, sticky="nsew")
    top_frame.grid_columnconfigure(0, weight=1)
    top_frame.grid_columnconfigure(1, weight=1)
    top_frame.grid_columnconfigure(2, weight=1)

    back_btn = tk.Button(top_frame, text="Back", command=lambda: app.show_frame(app.frame_menu))
    back_btn.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    total_label = tk.Label(top_frame, text="Total Items: 100", font=("Arial", 12, "bold"))
    total_label.grid(row=0, column=1)

    right_buttons = tk.Frame(top_frame)
    right_buttons.grid(row=0, column=2, sticky="e", padx=10)
    tk.Button(right_buttons, text="Add", command=add_item).pack(side="left", padx=5)
    tk.Button(right_buttons, text="Edit", command=edit_item).pack(side="left")

    bottom_frame = tk.Frame(app.frame_stocks)
    bottom_frame.grid(row=1, column=0, sticky="nsew")

    tree_scroll_y = tk.Scrollbar(bottom_frame, orient="vertical")
    tree_scroll_y.pack(side="right", fill="y")

    tree_scroll_x = tk.Scrollbar(bottom_frame, orient="horizontal")
    tree_scroll_x.pack(side="bottom", fill="x")

    stock_items = app.db.get_menu_items()
    tree = ttk.Treeview(
        bottom_frame,
        columns=("Barcode", "Category", "Subcategory", "Name", "Price", "Stock", "Total Sold", "No-Stock", "Last Added", "First Added", "Notes"),
        show="headings",
        yscrollcommand=tree_scroll_y.set,
        xscrollcommand=tree_scroll_x.set
    )

    tree.heading("Barcode", text="Barcode")
    tree.heading("Category", text="Category")
    tree.heading("Subcategory", text="Subcategory")
    tree.heading("Name", text="Name")
    tree.heading("Price", text="Price")
    tree.heading("Stock", text="Stock")
    tree.heading("Total Sold", text="Total Sold")
    tree.heading("No-Stock", text="No-Stock")
    tree.heading("Last Added", text="Last Added")
    tree.heading("First Added", text="First Added")
    tree.heading("Notes", text="Notes")

    tree_scroll_y.config(command=tree.yview)
    tree_scroll_x.config(command=tree.xview)

    tree.pack(fill="both", expand=True)

    for row in stock_items:
        tree.insert("", tk.END, values=row)

    style = ttk.Style()
    font_name = style.lookup("Treeview", "font")
    font = tkFont.nametofont(font_name if font_name else "TkDefaultFont")

    for col in tree["columns"]:
        max_width = font.measure(col)
        for item in tree.get_children():
            text = str(tree.set(item, col))
            max_width = max(max_width, font.measure(text))
        tree.column(col, width=max_width + 20)

    for col in tree["columns"]:
        tree.heading(col, text=col, command=lambda _col=col: treeview_sort_column(tree, _col, False))

    treeview_sort_column(tree, "Last Added", False)