import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import math
from widgets.menu_button import MenuButton
from widgets.checkout_button import CheckoutButton
from database import MenuDatabase
from datetime import datetime

def create_split_layout(root, mode):
    db = MenuDatabase()

    opening_var = tk.StringVar()


    # Configure the root window to expand with resizing
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=80)  # Left side: 80%
    root.grid_columnconfigure(1, weight=20)  # Right side: 20%

    # Left frame (80% width, no border)
    left_frame = tk.Frame(root)
    left_frame.grid(row=0, column=0, sticky="nsew")

    # Right frame (20% width, no border)
    right_frame = tk.Frame(root)
    right_frame.grid(row=0, column=1, sticky="nsew")

    # Configure right frame for 10%/60%/30% vertical split
    right_frame.grid_rowconfigure(0, weight=10)  # Top 10%
    right_frame.grid_rowconfigure(1, weight=60)  # Middle 60%
    right_frame.grid_rowconfigure(2, weight=30)  # Bottom 30%
    right_frame.grid_columnconfigure(0, weight=1)

    # Top sub-frame in right frame (10% height)
    top_right_frame = tk.Frame(right_frame)  # Light pink
    top_right_frame.grid(row=0, column=0, sticky="nsew")

    # Middle sub-frame in right frame (60% height)
    middle_right_frame = tk.Frame(right_frame)  # Medium pink
    middle_right_frame.grid(row=1, column=0, sticky="nsew")

    # Bottom sub-frame in right frame (30% height)
    bottom_right_frame = tk.Frame(right_frame)  # Darker pink
    bottom_right_frame.grid(row=2, column=0, sticky="nsew")

    title_label = tk.Label(top_right_frame, text="Express", font=("Arial", 25, "bold"), bg="#fce1e4")
    title_label.grid(row=0, column=0, columnspan=2, sticky="n")

    # Left-aligned Opening time
    opening_label = tk.Label(top_right_frame, textvariable=opening_var, font=("Arial", 10), bg="#fce1e4")
    opening_label.grid(row=1, column=0, sticky="w")

    # Right-aligned Cashier
    cashier_label = tk.Label(top_right_frame, text="Admin", font=("Arial", 10), bg="#fce1e4")
    cashier_label.grid(row=1, column=1, sticky="e")

    # Stretch columns so labels align to edges
    top_right_frame.grid_columnconfigure(0, weight=1)
    top_right_frame.grid_rowconfigure(0, weight=1)
    top_right_frame.grid_rowconfigure(1, weight=1)

    # Content for middle_right_frame: Treeview with scrollbars
    tree_frame = tk.Frame(middle_right_frame)
    tree_frame.grid(row=0, column=0, sticky="nsew")
    middle_right_frame.grid_rowconfigure(0, weight=1)
    middle_right_frame.grid_columnconfigure(0, weight=1)

    tree = ttk.Treeview(tree_frame, columns=("Saat","Adet", "Isim", "Fiyat", "Toplam Fiyat"), show="headings")
    tree.grid(row=0, column=0, sticky="nsew")

    # Configure Treeview columns
    tree.heading("Adet", text="Adet")
    tree.heading("Saat", text="Saat")
    tree.heading("Isim", text="Isim")
    tree.heading("Fiyat", text="Fiyat")
    tree.heading("Toplam Fiyat", text="Toplam Fiyat")
    tree.column("Adet", width=50, anchor="center")
    tree.column("Saat", width=50, anchor="center")
    tree.column("Isim", width=100, anchor="w")
    tree.column("Fiyat", width=80, anchor="e")
    tree.column("Toplam Fiyat", width=100, anchor="e")

    # Add scrollbars
    vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    vsb.grid(row=0, column=1, sticky="ns")
    hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
    hsb.grid(row=1, column=0, sticky="ew")
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # Make Treeview expand to fill frame
    tree_frame.grid_rowconfigure(0, weight=1)
    tree_frame.grid_columnconfigure(0, weight=1)

    # Content for bottom_right_frame
    bottom_right_content_frame = tk.Frame(bottom_right_frame)
    bottom_right_content_frame.grid(row=0, column=0, sticky="nsew")
    bottom_right_frame.grid_rowconfigure(0, weight=1)
    bottom_right_frame.grid_columnconfigure(0, weight=1)

    # Configure bottom_right_content_frame for labels, button grid, and bottom buttons

    bottom_right_content_frame.grid_rowconfigure(0, weight=1)  # Labels
    bottom_right_content_frame.grid_rowconfigure(1, weight=2)  # Button grid
    bottom_right_content_frame.grid_rowconfigure(2, weight=1)  # Bottom buttons
    
    # Equalisers for the grid
    for j in range(4):
        bottom_right_content_frame.grid_columnconfigure(j, weight=1)


    font_style_1 = ("Calibri",18,"bold")
    # TODO: This is where the calculations will be happened when a item is added.
    ### Exchange Rates Labels ###
    var_total_pounds = tk.StringVar()
    var_total_euro = tk.StringVar()
    var_total_dollar = tk.StringVar()
    var_total_tl = tk.StringVar()

    label_total_pounds = tk.Label(bottom_right_content_frame, textvariable=var_total_pounds, font=font_style_1, bg="#ca87f5")
    label_total_pounds.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    label_total_euro = tk.Label(bottom_right_content_frame, textvariable=var_total_euro, font=font_style_1, bg="#FFCC33")
    label_total_euro.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)

    label_total_dollar = tk.Label(bottom_right_content_frame, textvariable=var_total_dollar,font=font_style_1, bg="#85BB65")
    label_total_dollar.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)

    label_total_tl = tk.Label(bottom_right_content_frame, textvariable=var_total_tl, font=font_style_1, bg="#64baed")
    label_total_tl.grid(row=0, column=3, sticky="nsew", padx=2, pady=2)

    

    main_frame = tk.Frame(left_frame)
    main_frame.grid(row=1, column=0, sticky="nsew")
    # Configure main_frame for 10%/90% horizontal split
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_columnconfigure(0, weight=20)
    main_frame.grid_columnconfigure(1, weight=80)
    


        # Right sub-frame (90% width, no border, no margin)
    right_sub_frame = tk.Frame(main_frame)
    right_sub_frame.grid(row=0, column=1, sticky="nsew")
    # Configure right_sub_frame for top 10% and bottom 90%
    right_sub_frame.grid_rowconfigure(0, weight=1)
    right_sub_frame.grid_rowconfigure(1, weight=999)
    right_sub_frame.grid_columnconfigure(0, weight=1)

    # Top frame in right_sub_frame (10% height)
    top_sub_right_frame = tk.Frame(right_sub_frame)
    top_sub_right_frame.grid(row=0, column=0, sticky="nsew")

    # Bottom frame in right_sub_frame (90% height, new color)
    bottom_sub_right_frame = tk.Frame(right_sub_frame)
    bottom_sub_right_frame.grid(row=1, column=0, sticky="nsew")

    def clear_old_items():
        for widget in bottom_sub_right_frame.winfo_children():
            widget.destroy()


    def generate_menu_items(subcat):
        print("Came here, ",subcat)
        # provide subcat id for that items there.
        # Menu item pressed should add to data table on the right.
        def menu_item_pressed(value):
            no_items = int(multiplier_entry.get())
            clear_numpad()
            # Get spefic item with from database.
            
            item_data = db.get_specific_menu_item(value)
            print(item_data)
            item_barcode = item_data[0]
            item_name = item_data[3]
            item_price = float(item_data[4])
            item_total = no_items * item_price
            time_now = datetime.now().strftime("%H:%M")

            # ADD TO TREE

            # Check db if data exists, in the express if so continue else, create the first new 
            # opening time.
            is_data = db.get_all_express()
            if is_data:
                db.add_item_to_express(item_barcode, item_name, item_price,no_items, item_total, time_now)
            else:
                # Fist item.
                opening_time = datetime.now().strftime("%D %H:%M")
                opening_var.set(f"Açılış: {opening_time}")
                db.add_item_to_express(item_barcode,item_name, item_price,no_items, item_total, time_now, first=True, opening=opening_time)

            tree.insert("", "end", values=(time_now,no_items, item_name, item_price, item_total))#
            update_prices()
            

        # SQL Get Data from here.
        subcat_menu_items = db.get_subcategory_menu_items(subcat)
        num_subcat_menu_items = len(subcat_menu_items)
        # Calculate rows and columns for a roughly square grid

        # cols = math.ceil(math.sqrt(num_subcat_menu_items))
        # rows = math.ceil(num_subcat_menu_items / cols)

        # # Configure grid
        # for i in range(rows):
        #     bottom_sub_right_frame.grid_rowconfigure(i, weight=1)
        # for j in range(cols):
        #     bottom_sub_right_frame.grid_columnconfigure(j, weight=1)

        # Add rectangular buttons in a grid with dynamic font size and text wrapping
        for index, item in enumerate(subcat_menu_items):
            row = index // 7
            col = index % 7

            item_barcode = item[0]
            item_text = item[1]
            item_bg = item[3]
            item_fg = item[4]
            print(item_fg,item_bg)

            btn = CheckoutButton(master=bottom_sub_right_frame, text=item_text, width=10, height=3, command=lambda i=item_barcode: menu_item_pressed(i), bg=item_bg, fg=item_fg)
            btn.grid(row=row, column=col, padx=5, pady=5)


    # 2x3 button grid
    button_grid_frame = tk.Frame(bottom_right_content_frame)
    button_grid_frame.grid(row=1, column=0, columnspan=4, sticky="nsew")

    # Equalisers for grids.
    for i in range(2):
        button_grid_frame.grid_rowconfigure(i, weight=1)
    for j in range(3):
        button_grid_frame.grid_columnconfigure(j, weight=1)

    def iptal_button_pressed():
        # Clear the tree and the express database.
        db.clear_express()
        for row in tree.get_children():
            tree.delete(row)
        update_prices()


    table_change_btn = CheckoutButton(master=button_grid_frame, text="Change Table", width=7, height=1, command=None)
    table_change_btn.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    hesap_yaz_btn = CheckoutButton(master=button_grid_frame, text="Write Receipt", width=7, height=1, command=None)
    hesap_yaz_btn.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)

    btn = CheckoutButton(master=button_grid_frame, text="Iade", width=7, height=1, command=None)
    btn.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)

    btn = CheckoutButton(master=button_grid_frame, text="Iptal", width=7, height=1, command=iptal_button_pressed)
    btn.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

    not1_btn = CheckoutButton(master=button_grid_frame, text="Not Active", width=7, height=1, command=None, state='disabled')
    not1_btn.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)

    not2_btn = CheckoutButton(master=button_grid_frame, text="Not Active", width=7, height=1, command=None, state='disabled')
    not2_btn.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)

    


    # Two bottom buttons (Pay and Close)
    bottom_buttons_frame = tk.Frame(bottom_right_content_frame)
    bottom_buttons_frame.grid(row=2, column=0, columnspan=4, sticky="nsew")
    bottom_buttons_frame.grid_rowconfigure(0, weight=1)
    bottom_buttons_frame.grid_columnconfigure(0, weight=1)
    bottom_buttons_frame.grid_columnconfigure(1, weight=1)
    
    # Pay and Close Buttons (TODO close button will have option as Write Table)
    pay_btn = CheckoutButton(master=bottom_buttons_frame, text="PAY", width=7, height=1, command=None, bg="#8af49b")
    pay_btn.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    close_btn = CheckoutButton(master=bottom_buttons_frame, text="CLOSE", width=7, height=1, command=None, bg="#ef7783")
    close_btn.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)

    ### Left Section ###

    # Configure left frame for top 10% button layout and remaining space
    left_frame.grid_rowconfigure(0, weight=1)  # Top 10% for buttons
    left_frame.grid_rowconfigure(1, weight=999)  # Remaining 90%
    left_frame.grid_columnconfigure(0, weight=1)

    # Top button frame in left frame (10%)
    button_frame = tk.Frame(left_frame)
    button_frame.grid(row=0, column=0, sticky="nsew")

    # Configure button_frame to center buttons horizontally and stick to top
    def generate_subcategories(cat_id):
            # New frame in the main area of left frame (90% height)
            selected_button = {'btn': None}

            def select_category(subcat, title, btn):
                print("Selected SubCategory:", title)
                clear_old_items()
                generate_menu_items(subcat[0])
                if selected_button['btn']:
                    selected_button['btn'].remove_border()
                btn.add_border()
                selected_button['btn'] = btn

                # Call outside function to start for subcategories.
                # generate_subcategories(subcat[0])

            # Left sub-frame (10% width, no border, no margin)
            left_sub_frame = tk.Frame(main_frame)
            left_sub_frame.grid(row=0, column=0, sticky="nsew")

            # Configure left_sub_frame for vertical buttons
            left_sub_frame.grid_columnconfigure(0, weight=1)

            ### FIXME correct db call
            subcategories = db.get_subcat_from_cat(cat_id)
            
            for i in range(len(subcategories)):
                left_sub_frame.grid_rowconfigure(i, weight=1)

            # Add vertical buttons in a loop
            for i, subcat in enumerate(subcategories):
                title = subcat[1]
                bg= subcat[2]
                fg= subcat[3]
                # print(subcat)

                btn = CheckoutButton(master=left_sub_frame, text=title, bg=bg, fg=fg, width=17, height=1,)
            
                # Set command after btn is defined
                btn.config(command=lambda subcat=subcat, b=btn, title=title: select_category(subcat, title, b))

                btn.grid(row=i, column=0, sticky="nsew", padx=5, pady=2)

                if i == 0:
                    print("i==0",subcat)
                    print("Initializing on first sub-category")
                    select_category(subcat, title, btn)  # Auto-select first button
        
                


    
    ### Category Selection ###
    #FIXME database correct callign
    def generate_categories():
        selected_button = {'btn': None}  # Mutable container to hold reference to selected button

        def select_category(cat, btn):
            print("Selected Category:", cat)
            if selected_button['btn']:
                selected_button['btn'].configure(bg="gray",fg="black")
            btn.configure(bg="purple", fg="white")
            selected_button['btn'] = btn

            # Call outside function to start for subcategories.
            generate_subcategories(cat[0])

        categories = db.get_categories()
        button_frame.grid_rowconfigure(0, weight=0)

        for i in range(len(categories)):
            button_frame.grid_columnconfigure(i, weight=1)

        for i, cat in enumerate(categories):
            title = cat[1]
            bg = "gray"

            btn = CheckoutButton(master=button_frame, text=title, bg=bg)
            
            # Set command after btn is defined
            btn.config(command=lambda cat=cat, b=btn: select_category(cat, b))

            btn.grid(row=0, column=i, sticky="nsew")

            if i == 0:
                print("Initializing on first category")
                select_category(title, btn)  # Auto-select first button
                generate_subcategories(cat[0])



    generate_categories()




    def convert_and_round(tl_amount, exchange_rate):
        # Convert TL to EUR
        raw_euro = tl_amount / exchange_rate
        print(raw_euro)

        # Round up to nearest 0.25
        rounded_euro = math.ceil(raw_euro * 4) / 4

        return round(rounded_euro, 2)

    def update_prices():
        if tree.get_children():
            column_values = []
            for row_id in tree.get_children():
                values = tree.item(row_id, 'values')
                column_values.append(values[4])

            total_in_tl = sum(float(p) for p in column_values)
            # Get exchange rates in database.
            euro_rate, dollar_rate, sterlin_rate = db.get_exchange()

            euros = convert_and_round(total_in_tl, euro_rate)
            pounds = convert_and_round(total_in_tl, sterlin_rate)
            dollars = convert_and_round(total_in_tl, dollar_rate)

            var_total_tl.set(f"₺ {total_in_tl}")
            var_total_dollar.set(f"$ {dollars}")
            var_total_euro.set(f"€ {euros}")
            var_total_pounds.set(f"£ {pounds}")
        else:
            var_total_tl.set(f"₺ 0")
            var_total_dollar.set(f"$ 0")
            var_total_euro.set(f"€ 0")
            var_total_pounds.set(f"£ 0")
            opening_var.set("Açılış:")
            
    # Configure top_sub_right_frame for entry and buttons
    top_sub_right_frame.grid_rowconfigure(0, weight=1)
    top_sub_right_frame.grid_columnconfigure(0, weight=0)
    for i in range(1, 12):
        top_sub_right_frame.grid_columnconfigure(i, weight=1)


    def numpad_entrance(value):
        """
        Function: A directional numpad for multiple entries.
        1. When a number pressed it should copy that.
        2. System always waits at 1, when a button is pressed it directly, addopts that.
        - If its mask number than it should be gray, when a number is pressed,
        it should be black again.

        current_value: already existing value inside the entry.
        value: newly pressed number on the numpad.
        color: Turns the number to black to indicate its editing mode.
        """
        current_value = multiplier_entry.get()

        if current_value == "1" and entry.cget("fg")=="gray":
            multiplier_entry.set(f"{value}")

        elif current_value == "0":
            multiplier_entry.set(value)
        else:
            multiplier_entry.set(f"{current_value}{value}")

        entry.configure(fg="black")

    def clear_numpad():
        """
        Function to clear the numpad to "1" and turns color to gray.
        color: Turns to gray to indicate it's not in editing mode.
        """
        multiplier_entry.set("1")
        entry.configure(fg="gray")
    
    multiplier_entry = tk.StringVar()
    
    # Add Entry widget on the left
    entry = tk.Entry(top_sub_right_frame, font=("Impact", 15), width=5,  justify='center', textvariable=multiplier_entry)
    entry.grid(row=0, column=0, sticky="nsew")

    # Add buttons 1-9 in a loop
    for i in range(0, 10):
        btn = tk.Button(top_sub_right_frame, text=str(i),font=("Impact",15 ), bg="#a3c3fc", command=lambda i=i: numpad_entrance(str(i)))
        btn.grid(row=0, column=i+1, sticky="nsew", padx=2, pady=2)

    btn = tk.Button(top_sub_right_frame, text="X",font=("Impact",15 ), bg="#ff7967", command=clear_numpad)
    btn.grid(row=0, column=11, sticky="nsew", padx=2, pady=2)

    
    clear_numpad()

    if mode == "express":
        express_date = db.get_all_express()
        if express_date:
            total_in_tl = 0.0
            for index, data in enumerate(express_date):
                    
                if data[1]:
                    opening_var.set(f"Açılış: {data[1]}")

                item_name = data[2]
                item_price = data[3]
                item_qty = data[4]
                item_total = data[5]
                item_date = data[6]
                total_in_tl += item_total
                tree.insert("", "end", values=(item_date,item_qty, item_name, item_price, item_total))#
            
            update_prices()

        else:
            # Means it's empty.
            var_total_tl.set(f"₺ 0")
            var_total_dollar.set(f"$ 0")
            var_total_euro.set(f"€ 0")
            var_total_pounds.set(f"£ 0")
            opening_var.set("Açılış:")


    # Data Loading from the database, populating the tree.
    # Any item that is loaded from the database will be black color. except deleted ones.
    # Any item added new will be green.
    # Any item that is deleted will be red.

    
# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    root.title("80/20 Frame Layout with Wrapped Button Text")
    root.geometry("1336x768")  # Set initial window size
    create_split_layout(root, mode="express")
    root.mainloop()