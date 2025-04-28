import tkinter as tk
from screens.pos_app import POSApp

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1366x768")
    app = POSApp(root)
    root.mainloop()