import tkinter as tk
from database import MenuDatabase
from screens.login_screen import create_login_screen
from screens.menu_screen import create_menu_screen
from screens.checkout_screen import create_checkout_screen
from screens.settings_screen import create_settings_screen
from screens.stocks_screen import create_stocks_screen
from screens.add_item_screen import create_add_item_screen

class POSApp:
    def __init__(self, root):
        self.db = MenuDatabase()
        self.root = root
        self.root_width = 1366
        self.root_height = 768
        self.root.title("POS System")

        # Create frames for each screen
        self.frame_login = tk.Frame(root)
        self.frame_menu = tk.Frame(root)
        self.frame_checkout = tk.Frame(root)
        self.frame_settings = tk.Frame(root)
        self.frame_stocks = tk.Frame(root)
        self.frame_add_item = tk.Frame(root)

        # Pack layout for all frames
        self.frame_login.pack(fill="both", expand=True)
        self.frame_menu.pack(fill="both", expand=True)
        self.frame_checkout.pack(fill="both", expand=True)
        self.frame_settings.pack(fill="both", expand=True)
        self.frame_stocks.pack(fill="both", expand=True)
        self.frame_add_item.pack(fill="both", expand=True)

        # Initialize all frames with content
        create_login_screen(self)
        create_menu_screen(self)
        create_checkout_screen(self)
        create_settings_screen(self)
        create_stocks_screen(self)

        # Start on the login screen
        self.show_frame(self.frame_login)

    def show_frame(self, frame_to_show):
        frames = (self.frame_login, self.frame_menu, self.frame_checkout, self.frame_settings, self.frame_stocks, self.frame_add_item)
        for frame in frames:
            frame.pack_forget()
        frame_to_show.pack(fill="both", expand=True)

    def _from_rgb(self, rgb):
        r, g, b = rgb
        return f'#{r:02x}{g:02x}{b:02x}'

    def show_add_item_screen(self, current_mode, barcode=None):
        create_add_item_screen(self, current_mode, barcode)