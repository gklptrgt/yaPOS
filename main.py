# Pareto Principle, roughly 20% of the workforce is responsible for accomplishing 80% of the work.
# Work Hours: 6
# Version: 0.0.1
# Ctrl+F check TODO

import tkinter as tk
import psutil
import os
from database import MenuDatabase

class POSApp:
    def __init__(self, root):
        self.db = MenuDatabase()

        self.root = root
        
        self.root_width = 1366
        self.root_height = 768
        self.root.title("POS System")

        # Create the frames for each screen
        self.frame_login = tk.Frame(root)
        self.frame_menu = tk.Frame(root)
        self.frame_checkout = tk.Frame(root)
        self.frame_settings = tk.Frame(root)

        # Pack layout for all frames, stacking them vertically or horizontally
        self.frame_login.pack(fill="both", expand=True)
        self.frame_menu.pack(fill="both", expand=True)
        self.frame_checkout.pack(fill="both", expand=True)
        self.frame_settings.pack(fill="both", expand=True)

        # Initialize all frames with content
        self.create_login_screen()
        self.create_menu_screen()
        self.create_checkout_screen()
        self.create_settings_screen()

        # Start on the login screen
        self.show_frame(self.frame_login)



    def update_memory_usage(self):
        try:
            mem = psutil.Process(os.getpid()).memory_info().rss / (1024 ** 2)
            self.memory_label.config(text=f"Memory used: {mem:.2f} MB")
        except Exception as e:
            self.memory_label.config(text=f"Error: {e}")
        self.root.after(10000, self.update_memory_usage)  # run again after 1 second

        print("here",mem)


    def show_frame(self, frame):
        # Hide all frames
        self.frame_login.pack_forget()
        self.frame_menu.pack_forget()
        self.frame_checkout.pack_forget()
        self.frame_settings.pack_forget()
        
        # Show the selected frame
        frame.pack(fill="both", expand=True)

    def _from_rgb(self, rgb):
        """translates an rgb tuple of int to a tkinter friendly color code
        """
        r, g, b = rgb
        return f'#{r:02x}{g:02x}{b:02x}'

    def reset_window(self):
        # Destroy all widgets inside the root window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Re-initialize your frames or widgets
        self.create_login_screen()
        self.create_menu_screen()
        self.create_checkout_screen()

        # Show the login frame after reset
        self.show_frame(self.frame_login)

    def create_login_screen(self):
        """Create the login screen."""
        label = tk.Label(self.frame_login, text="Welcome to the POS System! Please Login.")
        label.pack(pady=20)

        username_label = tk.Label(self.frame_login, text="Username:")
        username_label.pack(padx=10, pady=5)
        username_entry = tk.Entry(self.frame_login)
        username_entry.pack(padx=10, pady=5)

        password_label = tk.Label(self.frame_login, text="Password:")
        password_label.pack(padx=10, pady=5)
        password_entry = tk.Entry(self.frame_login, show="*")
        password_entry.pack(padx=10, pady=5)

        login_button = tk.Button(self.frame_login, text="Login", command=lambda: self.show_frame(self.frame_menu))
        login_button.pack(pady=20)

    def create_menu_screen(self):
        """Create the inventory screen."""

        label = tk.Label(self.frame_menu, text="Menu Screen", font=('Arial', 18))
        label.pack(pady=20)

        # Button to go Checkout
        sale_button = tk.Button(self.frame_menu, text="Start Sale", command=lambda: self.show_frame(self.frame_checkout))
        sale_button.pack(pady=10)

        # Button to go Settings screen
        settings_button = tk.Button(self.frame_menu, text="Settings", command=lambda: self.show_frame(self.frame_settings))
        settings_button.pack(pady=10)

        # Button to go back to login screen
        back_button = tk.Button(self.frame_menu, text="Logout", command=lambda: self.show_frame(self.frame_login))
        back_button.pack(pady=10)

    def create_settings_screen(self):
        """Create the settings screen"""
        # product_label = tk.Label(self.frame_settings, text="Settings")
        # product_label.pack(pady=10)

        def show_frame(frame):
            frame.tkraise()

            # Update button styles
            for name, btn in tab_buttons.items():
                if name == frame:
                    # Selected Color
                    btn.config(relief="sunken", bd=3, bg="lightblue")
                else:
                    # Default color
                    btn.config(relief="raised", bd=1, bg="lightgrey")

        # Configure grid
        self.frame_settings.grid_columnconfigure(0, weight=1)   # Left side (10%)
        self.frame_settings.grid_columnconfigure(1, weight=9)   # Right side (90%)
        self.frame_settings.grid_rowconfigure(0, weight=1)

        # Left menu frame
        left_frame = tk.Frame(self.frame_settings, bg="lightgray")
        left_frame.grid(row=0, column=0, sticky="nsew")

        # Right content frame
        right_frame = tk.Frame(self.frame_settings)
        right_frame.grid(row=0, column=1, sticky="nsew")

        # Create multiple content frames

        shop_page = tk.Frame(right_frame, bg='green')
        shop_page.grid(row=0, column=0, sticky="nsew")
        label = tk.Label(shop_page, text=f"TAB: SHOP", font=("Arial", 24))
        label.pack(expand=True)
        
        cat_page = tk.Frame(right_frame, bg='blue')
        cat_page.grid(row=0, column=0, sticky="nsew")
        label = tk.Label(cat_page, text=f"TAB: CATEGORY", font=("Arial", 24))
        label.pack(expand=True)


        exchange_page = tk.Frame(right_frame)
        exchange_page.grid(row=0, column=0, sticky="nsew")
        label = tk.Label(exchange_page, text=f"Exchange Rates", font=("Arial", 24))
        label.pack(expand=True)
        

        # Buttons on the left to switch pages
        tab_buttons = {}
        
        btn_shop = tk.Button(left_frame, height=2, text=f"Shop Settings", command= lambda: show_frame(shop_page))
        btn_shop.pack(fill='x', padx=5, pady=5)
        tab_buttons[shop_page] = btn_shop 

        btn_cat = tk.Button(left_frame, height=2, text="Category Editing", command=lambda: show_frame(cat_page))
        btn_cat.pack(fill='x', padx=5, pady=5)
        tab_buttons[cat_page] = btn_cat

        btn_exc = tk.Button(left_frame, height=2, text="Exchance Rates", command=lambda: show_frame(exchange_page))
        btn_exc.pack(fill='x', padx=5, pady=5)
        tab_buttons[exchange_page] = btn_exc

        # Raise the first page (shop) initially
        show_frame(shop_page)

        ### Categories Window ###



        ### Exhange Rates Window ###
        self.euro_var = tk.StringVar()
        self.dollar_var = tk.StringVar()
        self.sterlin_var = tk.StringVar()

        euro, dollar, sterlin = self.db.get_exchange()

        if euro and dollar and sterlin:
            self.euro_var.set(str(euro))
            self.dollar_var.set(str(dollar))
            self.sterlin_var.set(str(sterlin))

        else:
            self.euro_var.set("1")
            self.dollar_var.set("1")
            self.sterlin_var.set("1")


        row1 = tk.Frame(exchange_page)
        row1.pack(fill='x', pady=5)
        label1 = tk.Label(row1, text="Dollar $", width=12, anchor='e')
        label1.pack(side='left')
        dollar_entry = tk.Entry(row1, state="disabled", textvariable=self.dollar_var)
        dollar_entry.pack(side='left', fill='x', expand=True)

        row2 = tk.Frame(exchange_page)
        row2.pack(fill='x', pady=5)
        label2 = tk.Label(row2, text="Euro €", width=12, anchor='e')
        label2.pack(side='left')
        euro_entry = tk.Entry(row2,state="disabled",textvariable=self.euro_var)
        euro_entry.pack(side='left', fill='x', expand=True)

        row3 = tk.Frame(exchange_page)
        row3.pack(fill='x', pady=5)
        label3 = tk.Label(row3, text="Sterlin £", width=12, anchor='e')
        label3.pack(side='left')
        sterlin_entry = tk.Entry(row3,state="disabled",textvariable=self.sterlin_var)
        sterlin_entry.pack(side='left', fill='x', expand=True)

        buttons_frame = tk.Frame(exchange_page)
        buttons_frame.pack(pady=20)

        edit_button = tk.Button(buttons_frame, text="Edit", command=lambda: edit_exchange())
        edit_button.pack(side='left', padx=10)

        save_button = tk.Button(buttons_frame, text="Save", state="disabled",command=lambda: save_exchange())
        save_button.pack(side='left', padx=10)

        def edit_exchange():
            # Editing the Exchange Rates

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

            euro = float(self.euro_var.get())
            dollar = float(self.dollar_var.get())
            sterlin = float(self.sterlin_var.get())
            self.db.update_exchange(euro=euro,dollar=dollar,sterlin=sterlin)

        ### END - Exhange Rates Window ###



    def create_checkout_screen(self):
        """Create the sales (transaction) screen."""

        # TODO Fix frame names, there is mix happened.
        # TODO Check figma and continue the layout system.
        # TODO Checkout screen has to have table mode and express mode. easy wy to do it, if table_id given with checkout screen then, table mode
        # if not means given for express mode. in this mean it should disable some parts.
        # TODO also when kapat is active, menu buttons should be disabled. So we dont need menu items.

        # Left section (75% width)
        self.left_frame = tk.Frame(self.frame_checkout, bg="lavenderblush2")  # Set background color
        self.left_frame.place(relwidth=0.75, relheight=1.0, relx=0, rely=0)  # 75% width, full height

        # Right section (25% width)
        self.right_frame = tk.Frame(self.frame_checkout, bg="ivory2")  # Set background color
        self.right_frame.place(relwidth=0.25, relheight=1.0, relx=0.75, rely=0)  # 25% width, full height

                # Configure the grid inside shops_selection_frame
        # 5% for the first and second rows, then 20% for the left, 80% for the right section
        self.left_frame.grid_rowconfigure(0, weight=1)  # 5% height for top section
        self.left_frame.grid_rowconfigure(1, weight=1)  # 5% height for next section
        self.left_frame.grid_rowconfigure(2, weight=19)  # 90% height for the main section
        
        self.left_frame.grid_columnconfigure(0, weight=1)  # Left section (20% width)
        self.left_frame.grid_columnconfigure(1, weight=4)  # Right section (80% width)
        # Top section - 5% height (e.g., title or header)
        top_section = tk.Frame(self.left_frame, bg="lightblue")
        top_section.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # Second section - 5% height (e.g., another header or separator)
        self.second_section = tk.Frame(self.left_frame, bg="lightgreen")
        self.second_section.grid(row=1, column=0, columnspan=2, sticky="nsew")

        # Main section - 90% height (Split into left 20% and right 80%)
        # Left side (20% width)
        self.cat_section = tk.Frame(self.left_frame, bg="gray")
        self.cat_section.grid(row=2, column=0, sticky="nsew")

        # Right side (80% width)
        right_section = tk.Frame(self.left_frame, bg="lightyellow")  # Right section for buttons
        right_section.grid(row=2, column=1, sticky="nsew")


        self.memory_label = tk.Label(top_section, text="Memory used: -- MB", font=("Helvetica", 16))
        self.memory_label.pack()




        self.generate_shop_buttons() # Generate Shop buttons [Kale Cafe, Hediyelik, Personel]
        # self.create_shops_buttons()

    def generate_shop_buttons(self):

        # TODO Take data from sql
        shops = ["Kale Cafe", "Hediyelik","personel"] 
        # shops = []
        if shops:
            self.selected_shop_button = None  # Variable to store the currently selected button

            for i, shop in enumerate(shops):
                shop_button = tk.Button(self.second_section, text=shop, padx=5, pady=5, borderwidth=0, relief="solid",font=("Arial", 20))
                shop_button.config(command=lambda button=shop_button, index=shop: on_button_click(button, index))

                if i == 0:
                    shop_button.config(bg="blue")  # First button selected
                    self.selected_shop_button = shop_button
                    print("Program Initlized selected first item in the shop list:", shop) 
                    self.generate_category_buttons(shop)

                shop_button.grid(row=0, column=i, padx=0, pady=0, sticky="nsew")

            for col in range(len(shops)):
                self.second_section.grid_columnconfigure(col, weight=1)        
            self.second_section.grid_rowconfigure(0, weight=1)
        else:
            # E001 - User did not add shops 
            error_label_1 = tk.Label(self.second_section, text="Please add Category from settings!\nE001",font=("Arial", 20), bg='red',fg='white')
            error_label_1.pack(fill="both", expand=True)
    
        def on_button_click(button, index):
            """Handle button click event to mark the selected button."""
            # If there's a previously selected button, reset its appearance
            if self.selected_shop_button:
                self.selected_shop_button.config(bg="gray")  # Default background color

            # Set the clicked button as selected
            button.config(bg="blue")  # Change color to indicate it's selected
            self.selected_shop_button = button  # Update the selected button reference
            print("Selected button", index)
            self.generate_category_buttons(index)

    def generate_category_buttons(self, shop):
        print("Getting this shop data--->", shop)
        
        # Clear old data.
        for widget in self.cat_section.winfo_children():
            widget.destroy()
        
        # Get Category for that shop from SQL
        
        dumb_cat = {'Kale Cafe':[('Soguk Icecekler',(0,0,255),(255,255,255)), ('Sicak Icecekler',(255,0,0),(255,255,255)),('Alkollu Icecekler',(125,125,0),(255,255,255)),('Yiyecekler',(123,34,232),(1,1,1)),('Salatalar',(100,44,9),(1,1,1)),('Ice Cream',(10,20,100),(1,1,1)),('Tatlilar',(23,234,11),(1,1,1)),('Snacks',(222,111,222),(1,1,1))],
                    'Hediyelik':[('Hediyelik',(0,0,255),(255,255,255)),('Canta ve Cuzdan',(0,0,255),(255,255,255)),('Kulluk',(0,0,255),(255,255,255)),('Tabak',(0,0,255),(255,255,255)),('Bardak',(0,0,255),(255,255,255)),('Mumluk',(0,0,255),(255,255,255)),('Maketler (Mucahit Kaya)',(0,0,255),(255,255,255)),('Kilim (Carpet)',(222,111,222),(1,1,1))]}
        
        target_data = dumb_cat.get(shop, [])
        self.selected_cat_button = None
        if target_data:
            for i, cat in enumerate(target_data):
                name = cat[0]
                bg = self._from_rgb(cat[1])
                fg = self._from_rgb(cat[2])
                cat_button = tk.Button(self.cat_section, text=name, padx=5, pady=5, borderwidth=0, relief="solid", width=7, background=bg,foreground=fg,font=("Arial", 20))
                cat_button.config(command=lambda button=cat_button, index=name: on_button_click(button, index))

                if i == 0:
                    cat_button.config(border=3)  # First button selected
                    self.selected_cat_button = cat_button
                    print("Program Initlized selected first category", cat) 
                    # self.generate_category_buttons(shop)

                cat_button.grid(row=i, column=0, padx=0, pady=0, sticky="nsew")

            for row in range(len(target_data)):
                self.cat_section.grid_rowconfigure(row, weight=1)        
            self.cat_section.grid_columnconfigure(0, weight=1)
        else:
            # E002 - No Sub category added for current selected category
            info_label = tk.Label(self.cat_section, text="No Category found please add from settings!\nE002", width=15, background='red', foreground='white')
            info_label.grid(row=0, column=0, sticky="nsew")

        def on_button_click(button, index):
            """Handle button click event to mark the selected button."""
            # If there's a previously selected button, reset its appearance
            if self.selected_cat_button:
                self.selected_cat_button.config(border=0)
            # Set the clicked button as selected
            button.config(border=3)  # Change color to indicate it's selected
            self.selected_cat_button = button  # Update the selected button reference
            print("Selected category", index)


# Create the main Tkinter window
root = tk.Tk()
root.geometry("1366x768")
app = POSApp(root)

app.update_memory_usage()
# Start the main event loop
root.mainloop()
